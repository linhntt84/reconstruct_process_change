#!/usr/bin/env python3
"""Build a reproducible Ostovar pilot manifest and quantitative evidence.

The script intentionally uses only the Python standard library. It treats the
XES trace order as the trace coordinate system used by the supplied ground
truth. Ground-truth labels are used only for window placement and evaluation;
change-pattern labels are never copied into the evidence JSON.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import statistics
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


DEFAULT_WINDOW_SIZE = 200
GENERATOR_METADATA_KEYS = {"Fran", "Lran", "n", "lowerBranch"}
TECHNICAL_ACTIVITY_PREFIXES = ("DRIFT_",)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def is_technical_activity(value: Any) -> bool:
    return isinstance(value, str) and value.startswith(TECHNICAL_ACTIVITY_PREFIXES)


def read_xes(path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Read a gzipped XES log into compact trace records and audit its schema."""
    traces: list[dict[str, Any]] = []
    event_attribute_keys: Counter[str] = Counter()
    trace_attribute_keys: Counter[str] = Counter()
    lifecycle_values: Counter[str] = Counter()
    activity_values: Counter[str] = Counter()

    with gzip.open(path, "rb") as stream:
        for _, elem in ET.iterparse(stream, events=("end",)):
            if local_name(elem.tag) != "trace":
                continue

            trace_id: str | None = None
            events: list[dict[str, Any]] = []
            for child in elem:
                kind = local_name(child.tag)
                if kind == "event":
                    event: dict[str, Any] = {}
                    for attr in child:
                        key = attr.attrib.get("key")
                        value = attr.attrib.get("value")
                        if key is None:
                            continue
                        event_attribute_keys[key] += 1
                        event[key] = value
                    activity = event.get("concept:name")
                    lifecycle = event.get("lifecycle:transition")
                    if activity is not None and not is_technical_activity(activity):
                        activity_values[str(activity)] += 1
                    if lifecycle is not None:
                        lifecycle_values[str(lifecycle)] += 1
                    events.append(event)
                elif kind in {"string", "date", "int", "float", "boolean"}:
                    key = child.attrib.get("key")
                    value = child.attrib.get("value")
                    if key is not None:
                        trace_attribute_keys[key] += 1
                    if key == "concept:name":
                        trace_id = value

            activities: list[str] = []
            timestamps: list[datetime] = []
            for event in events:
                activity = event.get("concept:name")
                timestamp = event.get("time:timestamp")
                if activity is None or timestamp is None:
                    continue
                if is_technical_activity(activity):
                    continue
                activities.append(str(activity))
                timestamps.append(parse_timestamp(str(timestamp)))

            traces.append(
                {
                    "trace_id": trace_id,
                    "activities": activities,
                    "timestamps": timestamps,
                }
            )
            elem.clear()

    audit = {
        "file": path.name,
        "n_traces": len(traces),
        "n_events": sum(len(trace["activities"]) for trace in traces),
        "event_attribute_keys": dict(sorted(event_attribute_keys.items())),
        "trace_attribute_keys": dict(sorted(trace_attribute_keys.items())),
        "lifecycle_values": dict(sorted(lifecycle_values.items())),
        "n_activities": len(activity_values),
        "activities": sorted(activity_values),
        "generator_metadata_keys_present": sorted(
            GENERATOR_METADATA_KEYS & set(event_attribute_keys)
        ),
        "has_resource": any(
            key in event_attribute_keys
            for key in ("org:resource", "resource", "Resource")
        ),
        "has_start_lifecycle": any(
            value.lower() == "start" for value in lifecycle_values
        ),
    }
    return traces, audit


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def safe_mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def safe_std(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.stdev(values) if len(values) > 1 else 0.0


def summarize_window(traces: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    activity_frequency: Counter[str] = Counter()
    activity_trace_support: Counter[str] = Counter()
    dfg_frequency: Counter[str] = Counter()
    dfg_trace_support: Counter[str] = Counter()
    variant_frequency: Counter[str] = Counter()
    case_durations_hours: list[float] = []
    transition_durations: defaultdict[str, list[float]] = defaultdict(list)

    for trace in traces:
        activities = trace["activities"]
        timestamps = trace["timestamps"]
        activity_frequency.update(activities)
        activity_trace_support.update(set(activities))

        edges = [f"{a} -> {b}" for a, b in zip(activities, activities[1:])]
        dfg_frequency.update(edges)
        dfg_trace_support.update(set(edges))
        variant_frequency[" -> ".join(activities)] += 1

        if len(timestamps) >= 2:
            duration = (timestamps[-1] - timestamps[0]).total_seconds() / 3600
            case_durations_hours.append(duration)
            for edge, start, end in zip(edges, timestamps, timestamps[1:]):
                transition_durations[edge].append((end - start).total_seconds() / 3600)

    n_traces = len(traces)
    activity_probability = {
        key: value / n_traces for key, value in activity_trace_support.items()
    } if n_traces else {}
    dfg_probability = {
        key: value / n_traces for key, value in dfg_trace_support.items()
    } if n_traces else {}

    return {
        "activity_frequency": dict(activity_frequency),
        "activity_probability": activity_probability,
        "directly_follows_frequency": dict(dfg_frequency),
        "directly_follows_probability": dfg_probability,
        "number_of_activities": {"process": float(len(activity_frequency))},
        "number_of_transitions": {"process": float(len(dfg_frequency))},
        "number_of_variants": {"process": float(len(variant_frequency))},
        "variant_frequency": dict(variant_frequency),
        "case_duration_mean": {"process": safe_mean(case_durations_hours)},
        "case_duration_std": {"process": safe_std(case_durations_hours)},
        "transition_time_mean": {
            edge: safe_mean(values) for edge, values in transition_durations.items()
        },
    }


def rounded(value: float, digits: int = 6) -> float:
    result = round(float(value), digits)
    return 0.0 if result == -0.0 else result


def compare_measure(
    before: dict[str, float],
    after: dict[str, float],
    include_relative_delta: bool,
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for entity in sorted(set(before) | set(after)):
        before_value = float(before.get(entity, 0.0))
        after_value = float(after.get(entity, 0.0))
        delta = after_value - before_value
        item: dict[str, Any] = {
            "entity": entity,
            "before": rounded(before_value),
            "after": rounded(after_value),
            "delta": rounded(delta),
        }
        if include_relative_delta:
            item["relative_delta"] = (
                None if before_value == 0.0 else rounded(delta / before_value)
            )
        items.append(item)
    return items


def build_evidence(
    traces: list[dict[str, Any]],
    anchor_trace: int,
    window_size: int,
    anchor_source: str,
) -> dict[str, Any]:
    before_start = max(0, anchor_trace - window_size)
    before_end = anchor_trace
    after_start = anchor_trace
    after_end = min(len(traces), anchor_trace + window_size)
    before = summarize_window(traces[before_start:before_end])
    after = summarize_window(traces[after_start:after_end])

    relative_measures = {
        "activity_frequency",
        "directly_follows_frequency",
    }
    control_flow_names = [
        "activity_frequency",
        "activity_probability",
        "directly_follows_frequency",
        "directly_follows_probability",
        "number_of_activities",
        "number_of_transitions",
        "number_of_variants",
        "variant_frequency",
    ]
    performance_names = [
        "case_duration_mean",
        "case_duration_std",
        "transition_time_mean",
    ]

    def measures(names: list[str]) -> dict[str, list[dict[str, Any]]]:
        return {
            name: compare_measure(
                before[name], after[name], name in relative_measures
            )
            for name in names
        }

    return {
        "window": {
            "coordinate_system": "zero_based_xes_trace_order",
            "anchor_source": anchor_source,
            "anchor_trace": anchor_trace,
            "requested_window_size": window_size,
            "before": {
                "start_inclusive": before_start,
                "end_exclusive": before_end,
                "n_traces": before_end - before_start,
            },
            "after": {
                "start_inclusive": after_start,
                "end_exclusive": after_end,
                "n_traces": after_end - after_start,
            },
        },
        "perspectives": {
            "control_flow": {
                "availability": "available",
                "evidence_level": "E1",
                "measures": measures(control_flow_names),
            },
            "performance": {
                "availability": "partial",
                "evidence_level": "E2",
                "available_measures": performance_names,
                "unavailable_measures": [
                    "service_time_mean",
                    "waiting_time_mean",
                    "sojourn_time_mean",
                ],
                "reason": "Only lifecycle=complete timestamps are present.",
                "measures": measures(performance_names),
            },
            "data": {
                "availability": "unavailable",
                "evidence_level": "E3",
                "reason": "Only generator metadata attributes were observed; they are excluded from business-data evidence.",
                "measures": {},
            },
            "resources": {
                "availability": "unavailable",
                "evidence_level": "E4",
                "reason": "No resource attribute is present in the Ostovar logs.",
                "measures": {},
            },
        },
    }


def make_manifest(
    ground_truth_rows: list[dict[str, str]],
    benchmark_rows: list[dict[str, str]],
    log_dir: Path,
    window_size: int,
) -> list[dict[str, Any]]:
    benchmark_by_key = {
        (row["filename"], row["ground_truth_trace"]): row
        for row in benchmark_rows
    }
    manifest: list[dict[str, Any]] = []
    for row in ground_truth_rows:
        benchmark = benchmark_by_key[(row["filename"], row["ground_truth_trace"])]
        point = int(row["ground_truth_trace"])
        manifest.append(
            {
                "case_id": f"ostovar::{row['filename']}::drift_{row['drift_sequence']}",
                "dataset": "Ostovar",
                "filename": row["filename"],
                "source_path": str((log_dir / row["filename"]).resolve()),
                "level": row["level"],
                "change_pattern": row["change_pattern"],
                "noise_pct": float(row["noise_pct"]),
                "drift_sequence": int(row["drift_sequence"]),
                "drift_nature": row["drift_nature"],
                "ground_truth_trace": point,
                "before_start": max(0, point - window_size),
                "before_end": point,
                "after_start": point,
                "after_end": min(int(benchmark["n_traces"]), point + window_size),
                "n_traces": int(benchmark["n_traces"]),
                "detected_trace": benchmark["detected_trace"],
                "detection_outcome": benchmark["outcome"],
                "annotation_source": "data/annotation/ground_truth.csv",
            }
        )
    return sorted(
        manifest,
        key=lambda item: (
            item["noise_pct"], item["level"], item["change_pattern"],
            item["filename"], item["drift_sequence"],
        ),
    )


def select_pilot(
    manifest: list[dict[str, Any]],
    logs_per_level: int,
    require_detected_trace: bool,
) -> list[dict[str, Any]]:
    """Select deterministic noise-free logs, diversified by level and pattern."""
    by_level: defaultdict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for row in manifest:
        if row["noise_pct"] != 0.0:
            continue
        if require_detected_trace and not row["detected_trace"]:
            continue
        names = by_level[row["level"]][row["change_pattern"]]
        if row["filename"] not in names:
            names.append(row["filename"])

    selected_files: set[str] = set()
    for level in sorted(by_level):
        patterns = sorted(by_level[level])
        candidates = [by_level[level][pattern][0] for pattern in patterns]
        selected_files.update(candidates[:logs_per_level])

    return [row for row in manifest if row["filename"] in selected_files]


def audit_summary(audits: list[dict[str, Any]]) -> dict[str, Any]:
    event_keys: Counter[str] = Counter()
    trace_keys: Counter[str] = Counter()
    lifecycle: Counter[str] = Counter()
    generator_keys: set[str] = set()
    for audit in audits:
        event_keys.update(audit["event_attribute_keys"])
        trace_keys.update(audit["trace_attribute_keys"])
        lifecycle.update(audit["lifecycle_values"])
        generator_keys.update(audit["generator_metadata_keys_present"])
    return {
        "dataset": "Ostovar",
        "files_audited": len(audits),
        "total_traces": sum(audit["n_traces"] for audit in audits),
        "total_events": sum(audit["n_events"] for audit in audits),
        "event_attribute_keys": dict(sorted(event_keys.items())),
        "trace_attribute_keys": dict(sorted(trace_keys.items())),
        "lifecycle_values": dict(sorted(lifecycle.items())),
        "generator_metadata_keys_excluded_from_E3": sorted(generator_keys),
        "perspective_availability": {
            "E1_control_flow": "available",
            "E2_performance": "partial: case duration and transition time only",
            "E3_data": "unavailable: generator metadata is excluded",
            "E4_resources": "unavailable: no resource attribute",
        },
        "files": audits,
    }


MEASURE_METADATA = {
    "activity_frequency": ("event_count", "count"),
    "activity_probability": ("trace_support", "proportion"),
    "directly_follows_frequency": ("edge_occurrence_count", "count"),
    "directly_follows_probability": ("trace_support", "proportion"),
    "number_of_activities": ("distinct_entity_count", "count"),
    "number_of_transitions": ("distinct_entity_count", "count"),
    "number_of_variants": ("distinct_entity_count", "count"),
    "variant_frequency": ("trace_count", "count"),
    "case_duration_mean": ("arithmetic_mean", "hours"),
    "case_duration_std": ("sample_standard_deviation", "hours"),
    "transition_time_mean": ("arithmetic_mean", "hours"),
}


def flatten_master_evidence(payload: dict[str, Any]) -> dict[str, Any]:
    """Convert nested extraction output to stable atomic evidence records."""
    items: list[dict[str, Any]] = []
    perspectives = payload["evidence"]["perspectives"]
    for perspective, perspective_data in perspectives.items():
        for measure, records in perspective_data.get("measures", {}).items():
            value_semantics, unit = MEASURE_METADATA[measure]
            for record in records:
                item = {
                    "evidence_id": f"{perspective}::{measure}::{record['entity']}",
                    "perspective": perspective,
                    "measure": measure,
                    "entity": record["entity"],
                    "value_semantics": value_semantics,
                    "unit": unit,
                    "before": record["before"],
                    "after": record["after"],
                    "delta": record["delta"],
                }
                if "relative_delta" in record:
                    item["relative_delta"] = record["relative_delta"]
                items.append(item)
    items.sort(key=lambda item: item["evidence_id"])
    return {
        "schema_version": "quantitative-process-evidence-0.1",
        "artifact_type": "master_evidence",
        "case": payload["case"],
        "window": payload["evidence"]["window"],
        "perspective_availability": {
            name: {
                "availability": data["availability"],
                "reason": data.get("reason"),
                "available_measures": sorted(data.get("measures", {})),
                "unavailable_measures": data.get("unavailable_measures", []),
            }
            for name, data in perspectives.items()
        },
        "atomic_evidence": items,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--window-size", type=int, default=DEFAULT_WINDOW_SIZE)
    parser.add_argument("--logs-per-level", type=int, default=3)
    parser.add_argument(
        "--anchor",
        choices=("detected", "ground_truth"),
        default="detected",
        help="Window anchor. The Ostovar localization labels were derived around detected points.",
    )
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    annotation_dir = workspace / "data" / "annotation"
    log_dir = workspace / "data" / "cdrift-evaluation" / "EvaluationLogs" / "Ostovar"
    output_dir = workspace / "Code" / "outputs" / "ostovar_pilot"
    evidence_dir = output_dir / "evidence"
    master_dir = output_dir / "master_evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    master_dir.mkdir(parents=True, exist_ok=True)

    ground_truth = load_csv(annotation_dir / "ground_truth.csv")
    benchmark = load_csv(annotation_dir / "benchmark_table.csv")
    manifest = make_manifest(ground_truth, benchmark, log_dir, args.window_size)
    pilot = select_pilot(
        manifest,
        args.logs_per_level,
        require_detected_trace=args.anchor == "detected",
    )

    manifest_fields = list(manifest[0])
    write_csv(output_dir / "experiment_cases.csv", manifest, manifest_fields)
    write_csv(output_dir / "pilot_cases.csv", pilot, manifest_fields)

    pilot_by_file: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for case in pilot:
        pilot_by_file[case["filename"]].append(case)

    audits: list[dict[str, Any]] = []
    for filename in sorted(pilot_by_file):
        traces, audit = read_xes(log_dir / filename)
        audits.append(audit)
        for case in pilot_by_file[filename]:
            anchor_trace = (
                int(case["detected_trace"])
                if args.anchor == "detected"
                else int(case["ground_truth_trace"])
            )
            evidence = build_evidence(
                traces,
                anchor_trace,
                args.window_size,
                args.anchor,
            )
            payload = {
                "schema_version": "ostovar-pilot-0.2",
                "case": {
                    "case_id": case["case_id"],
                    "dataset": case["dataset"],
                    "filename": case["filename"],
                    "noise_pct": case["noise_pct"],
                    "drift_sequence": case["drift_sequence"],
                    "ground_truth_trace": case["ground_truth_trace"],
                    "detected_trace": int(case["detected_trace"])
                    if case["detected_trace"]
                    else None,
                },
                "evidence": evidence,
            }
            base_name = Path(filename).name
            if base_name.endswith(".xes.gz"):
                base_name = base_name[:-7]
            safe_name = f"{base_name}__drift_{case['drift_sequence']}.json"
            (evidence_dir / safe_name).write_text(
                json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False),
                encoding="utf-8",
            )
            (master_dir / safe_name).write_text(
                json.dumps(
                    flatten_master_evidence(payload),
                    indent=2,
                    ensure_ascii=False,
                    allow_nan=False,
                ),
                encoding="utf-8",
            )

    (output_dir / "schema_audit.json").write_text(
        json.dumps(audit_summary(audits), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Manifest cases: {len(manifest)}")
    print(f"Pilot logs: {len(pilot_by_file)}")
    print(f"Pilot drift cases: {len(pilot)}")
    print(f"Evidence files: {len(list(evidence_dir.glob('*.json')))}")
    print(f"Master evidence files: {len(list(master_dir.glob('*.json')))}")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
