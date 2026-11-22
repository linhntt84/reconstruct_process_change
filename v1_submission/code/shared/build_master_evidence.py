#!/usr/bin/env python3
"""Build official ACIIDS master evidence for Ostovar and CDLG.

Private ground truth is used only to select stable windows and evaluate outputs.
Public case IDs and contexts contain no benchmark family, filename, coordinates,
generator label, or process-tree truth.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve()
WORKSPACE = HERE.parents[3]
PILOT_CODE = WORKSPACE / "Code"
if str(PILOT_CODE) not in sys.path:
    sys.path.insert(0, str(PILOT_CODE))

from build_cdlg_localization_inputs import official_episodes, read_xes_from_zip, zip_for_log  # noqa: E402
from ostovar_pilot import read_xes  # noqa: E402

from common import write_csv, write_json  # noqa: E402
from evidence_features import EvidenceConfig, build_candidate_evidence, neutralize_windows  # noqa: E402


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def neutral_id(private_key: str) -> str:
    return "case_" + hashlib.sha256(private_key.encode()).hexdigest()[:16]


CDLG_NOISE_PARAMETERS = {"0": (0.0, 0.0), "5": (0.2, 0.2), "10": (0.4, 0.2)}
OSTOVAR_NATIVE_PERCENT = {"0": 0.0, "5": 2.5, "10": 5.0}


def build_master(
    case_id: str,
    before_traces: list[dict[str, Any]],
    after_traces: list[dict[str, Any]],
    config: EvidenceConfig,
    window_condition: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    families, private = build_candidate_evidence(before_traces, after_traces, config)
    master = {
        "schema_version": "aciids-master-evidence-1.0",
        "case_id": case_id,
        "window_summary": {
            "before_n_traces": len(before_traces),
            "after_n_traces": len(after_traces),
            "window_condition": window_condition,
        },
        "evidence_config": config.to_dict(),
        "evidence_families": families,
    }
    return master, private


def choose_cdlg(rows: list[dict[str, str]], target: int, seed: int) -> list[dict[str, str]]:
    """Balanced random sampling by official global type, preferring unique logs."""
    if target >= len(rows):
        return sorted(rows, key=lambda row: row["episode_key"])
    rng = random.Random(seed)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["drift_type"]].append(row)
    labels = sorted(grouped)
    quotas = {label: target // len(labels) for label in labels}
    for label in labels[: target % len(labels)]:
        quotas[label] += 1
    chosen: list[dict[str, str]] = []
    used_logs: set[str] = set()
    for label in labels:
        candidates = list(grouped[label])
        rng.shuffle(candidates)
        unique = [row for row in candidates if row["log_name"] not in used_logs]
        repeated = [row for row in candidates if row["log_name"] in used_logs]
        selected = (unique + repeated)[: quotas[label]]
        chosen.extend(selected)
        used_logs.update(row["log_name"] for row in selected)
    return sorted(chosen, key=lambda row: row["episode_key"])


def ostovar_cases(workspace: Path, dry_count: int = 0, seed: int = 20270901, window_offset: int = 0,
                   noise_setting: str = "0") -> list[dict[str, Any]]:
    rows = read_csv(workspace / "Code/outputs/ostovar_pilot/experiment_cases.csv")
    wanted_noise = OSTOVAR_NATIVE_PERCENT[noise_setting]
    rows = [row for row in rows if float(row.get("noise_pct", 0.0)) == wanted_noise]
    if dry_count:
        rng = random.Random(seed)
        rng.shuffle(rows)
        selected_rows, seen_levels = [], set()
        for row in rows:
            if row["level"] not in seen_levels or len(selected_rows) >= 3:
                selected_rows.append(row)
                seen_levels.add(row["level"])
            if len(selected_rows) == dry_count:
                break
        rows = selected_rows
    output = []
    cache: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        filename = row["filename"]
        if filename not in cache:
            traces, _ = read_xes(workspace / "Data/cdrift-evaluation/EvaluationLogs/Ostovar" / filename)
            cache[filename] = traces
        traces = cache[filename]
        anchor = int(row["ground_truth_trace"]) + window_offset
        before_start, before_end = anchor - 200, anchor
        after_start, after_end = anchor, anchor + 200
        private_key = (
            f"ostovar::{filename}::{row['drift_sequence']}"
            if noise_setting == "0"
            else f"ostovar::{noise_setting}::{filename}::{row['drift_sequence']}"
        )
        output.append({
            "case_id": neutral_id(private_key),
            "dataset_private": "Ostovar",
            "private_key": private_key,
            "source_name_private": filename,
            "before": traces[before_start:before_end],
            "after": traces[after_start:after_end],
            "private_truth": {
                "level": row["level"],
                "change_pattern": row["change_pattern"],
                "ground_start": int(row["ground_truth_trace"]),
                "ground_end": int(row["ground_truth_trace"]),
                "before_window": [before_start, before_end],
                "after_window": [after_start, after_end],
                "noise_tier": noise_setting,
                "noise_percent": OSTOVAR_NATIVE_PERCENT[noise_setting],
                "noise_source": "native_ostovar_benchmark",
            },
        })
    return output


def cdlg_cases(workspace: Path, target: int, seed: int, dry_count: int = 0, window_offset: int = 0,
               noise_setting: str = "0") -> list[dict[str, Any]]:
    dataset_dir = workspace / "Data/concept-drift-characterization/evaluation_paper/data_collection/datasets_evaluation"
    chosen = choose_cdlg(official_episodes(dataset_dir, noise_setting), target, seed)
    if dry_count:
        rng = random.Random(seed + 1)
        rng.shuffle(chosen)
        selected_rows, seen_labels = [], set()
        for row in chosen:
            if row["drift_type"] not in seen_labels or len(selected_rows) >= 4:
                selected_rows.append(row)
                seen_labels.add(row["drift_type"])
            if len(selected_rows) == dry_count:
                break
        chosen = selected_rows
    output = []
    cache: dict[str, list[dict[str, Any]]] = {}
    for row in chosen:
        log_name = row["log_name"]
        if log_name not in cache:
            cache[log_name] = read_xes_from_zip(zip_for_log(dataset_dir, noise_setting, log_name), log_name)
        traces = cache[log_name]
        onset, transition_end = int(row["ground_start_trace"]), int(row["ground_end_trace"])
        before_start, before_end = onset - 200 + window_offset, onset + window_offset
        after_start, after_end = transition_end + window_offset, transition_end + 200 + window_offset
        if before_start < 0 or after_end > len(traces):
            continue
        private_key = f"cdlg::{noise_setting}::{row['episode_key']}"
        output.append({
            "case_id": neutral_id(private_key),
            "dataset_private": "CDLG",
            "private_key": private_key,
            "source_name_private": log_name,
            "before": traces[before_start:before_end],
            "after": traces[after_start:after_end],
            "private_truth": {
                "episode_key": row["episode_key"],
                "local_type": row["change_type"],
                "global_type": row["drift_type"],
                "ground_start": onset,
                "ground_end": transition_end,
                "before_window": [before_start, before_end],
                "after_window": [after_start, after_end],
                "ground_added": row["ground_added"],
                "ground_deleted": row["ground_deleted"],
                "ground_moved": row["ground_moved"],
                "process_tree_before": row["process_tree_before"],
                "process_tree_after": row["process_tree_after"],
                "noise_setting": noise_setting,
                "noise_source": "native_cdlg_benchmark",
            },
        })
    return output


def diverse_dry_sample(cases: list[dict[str, Any]], dataset: str, count: int, seed: int) -> list[dict[str, Any]]:
    candidates = [case for case in cases if case["dataset_private"] == dataset]
    rng = random.Random(seed + (1 if dataset == "CDLG" else 0))
    rng.shuffle(candidates)
    if dataset == "Ostovar":
        selected, seen = [], set()
        for case in candidates:
            level = case["private_truth"]["level"]
            if level not in seen or len(selected) >= 3:
                selected.append(case)
                seen.add(level)
            if len(selected) == count:
                break
        return selected
    selected, seen = [], set()
    for case in candidates:
        label = case["private_truth"]["global_type"]
        if label not in seen or len(selected) >= 4:
            selected.append(case)
            seen.add(label)
        if len(selected) == count:
            break
    return selected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, default=WORKSPACE)
    parser.add_argument("--mode", choices=("dry10", "official"), default="dry10")
    parser.add_argument("--cdlg-target", type=int, default=120)
    parser.add_argument("--seed", type=int, default=20270901)
    parser.add_argument("--window-offset", type=int, default=0, help="Shift both benchmark stable-window boundaries by this many traces")
    parser.add_argument("--noise-setting", choices=("0", "5", "10"), default="0")
    parser.add_argument("--dataset", choices=("Ostovar", "CDLG"), action="append",
                        help="Dataset(s) to materialize; default is both")
    parser.add_argument("--artifact-namespace", default=None, help="Override output artifact namespace")
    parser.add_argument("--neutralize-activity-labels", dest="neutralize_activity_labels", action="store_true")
    parser.add_argument("--no-neutralize-activity-labels", dest="neutralize_activity_labels", action="store_false")
    parser.set_defaults(neutralize_activity_labels=True)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    experiment = workspace / "Experiments/ACIIDS_2027"
    base_namespace = "dry_run" if args.mode == "dry10" else "official"
    offset_tag = f"_offset_{args.window_offset:+d}".replace("+", "p").replace("-", "m") if args.window_offset else ""
    namespace = args.artifact_namespace or (base_namespace + offset_tag)
    window_condition = "WINDOW_ORACLE_STABLE" if args.window_offset == 0 else f"WINDOW_ORACLE_SHIFT_{args.window_offset:+d}"
    root = experiment / "artifacts" / namespace
    masters_dir, private_dir = root / "master_evidence", root / "private_truth"
    label_maps_dir = private_dir / "activity_label_maps"
    config = EvidenceConfig()

    dry_count = 5 if args.mode == "dry10" else 0
    datasets = set(args.dataset or ("Ostovar", "CDLG"))
    all_ostovar = (ostovar_cases(workspace, dry_count=dry_count, seed=args.seed, window_offset=args.window_offset,
                                 noise_setting=args.noise_setting) if "Ostovar" in datasets else [])
    all_cdlg = (cdlg_cases(workspace, args.cdlg_target, args.seed, dry_count=dry_count, window_offset=args.window_offset,
                           noise_setting=args.noise_setting) if "CDLG" in datasets else [])
    if args.mode == "dry10":
        cases = all_ostovar + all_cdlg
    else:
        cases = all_ostovar + all_cdlg

    index_rows = []
    for case in sorted(cases, key=lambda item: item["case_id"]):
        before, after, label_map = neutralize_windows(
            case["before"], case["after"], enabled=args.neutralize_activity_labels
        )
        master, private_evaluation = build_master(case["case_id"], before, after, config, window_condition)
        master_path = masters_dir / f"{case['case_id']}.json"
        private_path = private_dir / f"{case['case_id']}.json"
        label_map_path = label_maps_dir / f"{case['case_id']}.json"
        write_json(master_path, master)
        write_json(label_map_path, {
            "case_id": case["case_id"],
            "neutralization_enabled": args.neutralize_activity_labels,
            "original_to_public": label_map,
        })
        write_json(private_path, {
            "case_id": case["case_id"],
            "dataset": case["dataset_private"],
            "private_key": case["private_key"],
            "source_name": case["source_name_private"],
            "benchmark_truth": case["private_truth"],
            "empirical_change_reference": private_evaluation["empirical_change_reference"],
            "affected_activities_public": private_evaluation["affected_activities"],
            "activity_label_map_path": str(label_map_path.relative_to(workspace)),
        })
        index_rows.append({
            "case_id": case["case_id"],
            "dataset_private": case["dataset_private"],
            "master_evidence_path": str(master_path.relative_to(workspace)),
            "private_truth_path": str(private_path.relative_to(workspace)),
            "activity_label_map_path": str(label_map_path.relative_to(workspace)),
            "window_condition": window_condition,
            "before_n_traces": len(case["before"]),
            "after_n_traces": len(case["after"]),
        })
    write_csv(root / "master_index.csv", index_rows)
    write_json(root / "experiment_config.json", {
        "mode": args.mode,
        "random_seed": args.seed,
        "window_offset_traces": args.window_offset,
        "window_condition": window_condition,
        "noise_setting": args.noise_setting,
        "noise_parameters": {
            "cdlg_trace_selection_probability": CDLG_NOISE_PARAMETERS[args.noise_setting][0],
            "cdlg_continuation_probability": CDLG_NOISE_PARAMETERS[args.noise_setting][1],
            "cdlg_source": "native_benchmark_zip",
            "ostovar_native_noise_percent": OSTOVAR_NATIVE_PERCENT[args.noise_setting],
            "ostovar_source": "native_benchmark_log",
        },
        "neutralize_activity_labels": args.neutralize_activity_labels,
        "conditions": ["C1_ACTIVITY", "C2_DFG", "C3_RELATIONAL", "C4_SEQUENCE_TEMPORAL"],
        "evidence_config": config.to_dict(),
    })
    print(f"Mode: {args.mode}")
    print(f"Ostovar materialized: {len(all_ostovar)}")
    print(f"CDLG materialized: {len(all_cdlg)}")
    print(f"Master cases written: {len(index_rows)}")
    print(f"Output: {root}")


if __name__ == "__main__":
    main()
