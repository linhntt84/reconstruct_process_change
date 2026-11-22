#!/usr/bin/env python3
"""Build leakage-safe CDLG localization inputs directly from evaluation ZIPs."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import math
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Any

from ostovar_pilot import is_technical_activity, parse_timestamp, summarize_window


MEASURES = ("activity_probability", "directly_follows_probability")
NOISE_DIR = {"0": "without_noise", "5": "with_noise_5", "10": "with_noise_10"}
PUBLIC_TYPE = {"recurring": "recurrent"}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def opaque_id(noise: str, episode_key: str) -> str:
    value = f"{noise}::{episode_key}"
    return "cdlg_" + hashlib.sha256(value.encode()).hexdigest()[:12]


def zip_for_log(dataset_dir: Path, noise: str, log_name: str) -> Path:
    number = int(log_name.split("_", 2)[1])
    part = 1 if number <= 50 else 2
    folder = NOISE_DIR[noise]
    return dataset_dir / folder / f"{folder}_part_{part}.zip"


def read_xes_from_zip(zip_path: Path, member: str) -> list[dict[str, Any]]:
    traces: list[dict[str, Any]] = []
    with zipfile.ZipFile(zip_path) as archive, archive.open(member) as stream:
        for _, elem in ET.iterparse(stream, events=("end",)):
            if local_name(elem.tag) != "trace":
                continue
            trace_id: str | None = None
            activities: list[str] = []
            timestamps: list[str] = []
            for child in elem:
                kind = local_name(child.tag)
                if kind == "event":
                    attrs = {
                        attr.attrib.get("key"): attr.attrib.get("value")
                        for attr in child
                        if attr.attrib.get("key")
                    }
                    activity = attrs.get("concept:name")
                    if activity and not is_technical_activity(activity):
                        activities.append(str(activity))
                        if attrs.get("time:timestamp"):
                            timestamps.append(parse_timestamp(str(attrs["time:timestamp"])))
                elif child.attrib.get("key") == "concept:name":
                    trace_id = child.attrib.get("value")
            traces.append(
                {
                    "trace_id": trace_id or f"trace_{len(traces)}",
                    "activities": activities,
                    "timestamps": timestamps,
                }
            )
            elem.clear()
    return traces


def detector_points(path: Path, noise: str) -> dict[str, list[int]]:
    wanted = NOISE_DIR[noise]
    result: dict[str, list[int]] = {}
    for row in read_csv(path):
        if row["noise_level"] != wanted:
            continue
        result[row["log_name"]] = [int(x) for x in ast.literal_eval(row["detected_cp"])]
    return result


def official_episodes(dataset_dir: Path, noise: str) -> list[dict[str, str]]:
    """Reconstruct episode labels directly from CDLG's official drift_info.csv."""
    sizes: dict[str, int] = {}
    for row in read_csv(dataset_dir / "gold_standard.csv"):
        sizes[row["log_name"]] = int(float(row["log_size"]))

    drift_types: dict[tuple[str, str], str] = {}
    changes: dict[tuple[str, str, str], dict[str, str]] = defaultdict(dict)
    for row in read_csv(dataset_dir / "drift_info.csv"):
        log_name = row["log_name"]
        drift_id = row["drift_or_noise_id"]
        attribute = row["drift_attribute"]
        if attribute == "drift_type":
            drift_types[(log_name, drift_id)] = row["value"]
        elif attribute.startswith("change_info_"):
            changes[(log_name, drift_id, attribute)][row["drift_sub_attribute"]] = row["value"]

    episodes: list[dict[str, str]] = []
    for (log_name, drift_id, change_id), change in sorted(changes.items()):
        coordinates = [int(x) for x in ast.literal_eval(change["change_trace_index"])]
        episodes.append(
            {
                "noise_pct": noise,
                "episode_key": f"N{noise}-{Path(log_name).stem}-{drift_id}-{change_id}",
                "log_name": log_name,
                "n_traces": str(sizes[log_name]),
                "drift_id": drift_id,
                "change_id": change_id,
                "drift_type": drift_types[(log_name, drift_id)],
                "change_type": change["change_type"],
                "ground_start_trace": str(coordinates[0]),
                "ground_end_trace": str(coordinates[-1]),
                "ground_added": change.get("activities_added", "[]"),
                "ground_deleted": change.get("activities_deleted", "[]"),
                "ground_moved": change.get("activities_moved", "[]"),
                "process_tree_before": change.get("process_tree_before", ""),
                "process_tree_after": change.get("process_tree_after", ""),
            }
        )
    return episodes


def match_episodes(
    episodes: list[dict[str, str]], detections: dict[str, list[int]], tolerance_fraction: float
) -> list[dict[str, Any]]:
    """Match each episode onset to one detector point without exposing GT to inputs."""
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in episodes:
        grouped[row["log_name"]].append(row)
    matched: list[dict[str, Any]] = []
    for log_name, rows in grouped.items():
        available = set(detections.get(log_name, []))
        for row in sorted(rows, key=lambda x: int(x["ground_start_trace"])):
            if not available:
                continue
            onset = int(row["ground_start_trace"])
            candidate = min(available, key=lambda x: (abs(x - onset), x))
            tolerance = math.ceil(int(row["n_traces"]) * tolerance_fraction)
            if abs(candidate - onset) > tolerance:
                continue
            available.remove(candidate)
            item: dict[str, Any] = dict(row)
            item["detected_trace"] = candidate
            item["detector_error_private"] = candidate - onset
            matched.append(item)
    return matched


def balanced_sample(rows: list[dict[str, Any]], per_type: int) -> list[dict[str, Any]]:
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_type[row["drift_type"]].append(row)
    chosen: list[dict[str, Any]] = []
    for drift_type in ("sudden", "gradual", "incremental", "recurring"):
        ranked = sorted(
            by_type[drift_type],
            key=lambda x: (abs(int(x["detector_error_private"])), x["episode_key"]),
        )
        chosen.extend(ranked[:per_type])
    return sorted(chosen, key=lambda x: (x["log_name"], int(x["ground_start_trace"])))


def select_entities(
    traces: list[dict[str, Any]], start: int, end: int, reference_size: int, top_k: int
) -> dict[str, list[str]]:
    early = summarize_window(traces[start : min(end, start + reference_size)])
    late = summarize_window(traces[max(start, end - reference_size) : end])
    selected: dict[str, list[str]] = {}
    for measure in MEASURES:
        entities = set(early[measure]) | set(late[measure])
        selected[measure] = sorted(
            entities,
            key=lambda entity: (
                -abs(float(late[measure].get(entity, 0)) - float(early[measure].get(entity, 0))),
                entity,
            ),
        )[:top_k]
    return selected


def temporal_series(
    traces: list[dict[str, Any]], start: int, end: int, n_bins: int,
    entities: dict[str, list[str]],
) -> tuple[int, list[dict[str, Any]]]:
    bin_size = max(1, math.ceil((end - start) / n_bins))
    output: list[dict[str, Any]] = []
    for measure in MEASURES:
        for entity in entities[measure]:
            bins = []
            for bin_start in range(start, end, bin_size):
                bin_end = min(end, bin_start + bin_size)
                summary = summarize_window(traces[bin_start:bin_end])
                bins.append({
                    "start": bin_start,
                    "end": bin_end,
                    "n_traces": bin_end - bin_start,
                    "value": round(float(summary[measure].get(entity, 0)), 6),
                })
            output.append({
                "evidence_id": f"temporal::{measure}::{entity}",
                "measure": measure,
                "entity": entity,
                "bins": bins,
            })
    return bin_size, output


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--noise", choices=("0", "5", "10"), default="0")
    parser.add_argument("--per-type", type=int, default=6)
    parser.add_argument("--radius", type=int, default=None, help="Fixed trace radius; default uses --radius-fraction")
    parser.add_argument("--radius-fraction", type=float, default=0.05)
    parser.add_argument("--output-subdir", default="localization_inputs")
    parser.add_argument("--bins", type=int, default=24)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--reference-size", type=int, default=300)
    parser.add_argument("--detector-tolerance-fraction", type=float, default=0.05)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    dataset_dir = workspace / "Data" / "concept-drift-characterization" / "evaluation_paper" / "data_collection" / "datasets_evaluation"
    detector_csv = workspace / "Data" / "concept-drift-characterization" / "evaluation_paper" / "step_1" / "process_graphs" / "results_datasets_evaluation_approach_evaluated_1.csv"

    episodes = official_episodes(dataset_dir, args.noise)
    detections = detector_points(detector_csv, args.noise)
    matched = match_episodes(episodes, detections, args.detector_tolerance_fraction)
    selected = balanced_sample(matched, args.per_type)
    if args.radius is not None and args.radius <= 0:
        raise SystemExit("--radius must be positive")
    if args.radius_fraction <= 0:
        raise SystemExit("--radius-fraction must be positive")
    out_root = workspace / "Code" / "outputs" / "cdlg_pilot"
    input_root = out_root / args.output_subdir
    input_dir = input_root / "L1_TEMPORAL"
    input_dir.mkdir(parents=True, exist_ok=True)
    index_rows: list[dict[str, Any]] = []
    cache: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in selected:
        log_name = row["log_name"]
        cache_key = (args.noise, log_name)
        if cache_key not in cache:
            zpath = zip_for_log(dataset_dir, args.noise, log_name)
            cache[cache_key] = read_xes_from_zip(zpath, log_name)
        traces = cache[cache_key]
        detected = int(row["detected_trace"])
        radius = args.radius or math.ceil(len(traces) * args.radius_fraction)
        start = max(0, detected - radius)
        end = min(len(traces), detected + radius)
        entities = select_entities(traces, start, end, args.reference_size, args.top_k)
        bin_size, series = temporal_series(traces, start, end, args.bins, entities)
        case_id = opaque_id(args.noise, row["episode_key"])
        payload = {
            "schema_version": "cdlg-localization-input-0.1",
            "artifact_type": "drift_localization_evidence",
            "case": {"case_id": case_id, "dataset": "CDLG evaluation"},
            "candidate_detection": {
                "coordinate_system": "zero_based_xes_trace_order",
                "trace": detected,
                "source": "process_graph_detector",
            },
            "search_region": {
                "start_inclusive": start,
                "end_exclusive": end,
                "bin_size_traces": bin_size,
            },
            "atomic_evidence": [],
            "temporal_evidence": series,
        }
        path = input_dir / f"{case_id}.json"
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        index_rows.append({
            "opaque_case_id": case_id,
            "condition_id": "L1_TEMPORAL",
            "prompt_input_path": str(path.relative_to(workspace)),
            "episode_key_private": row["episode_key"],
            "noise_pct_private": args.noise,
            "log_name_private": log_name,
            "ground_start_private": row["ground_start_trace"],
            "ground_end_private": row["ground_end_trace"],
            "change_type_private": row["change_type"],
            "drift_type_private": PUBLIC_TYPE.get(row["drift_type"], row["drift_type"]),
            "detected_trace": detected,
            "detector_error_private": row["detector_error_private"],
            "search_start": start,
            "search_end": end,
            "search_radius": radius,
            "n_temporal_evidence_items": len(series),
        })
    write_csv(input_root / "localization_index.csv", index_rows)
    print(f"Ground-truth episodes at noise {args.noise}: {len(episodes)}")
    print(f"Detector-matched episodes: {len(matched)}")
    print(f"Balanced pilot cases: {len(index_rows)}")
    print(f"Output: {input_root}")


if __name__ == "__main__":
    main()
