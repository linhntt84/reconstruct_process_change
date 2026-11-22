#!/usr/bin/env python3
"""Detect candidate BPI 2017 control-flow change points before Algorithms 1--2.

The detector is intentionally separate from evidence qualification. It orders
cases by their first event timestamp, represents each 200-case window through
activity and directly-follows trace support, and scans adjacent windows. The
output coordinates are detected candidates, never benchmark ground truth.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
WORKSPACE = EXPERIMENT.parents[1]
DEFAULT_LOG = WORKSPACE / "Data/BPI2017/BPI Challenge 2017.csv"
DEFAULT_OUTPUT = EXPERIMENT / "artifacts/official/bpi2017_control_flow_detection_v1"


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value)


def load_complete_traces(path: Path) -> list[dict[str, Any]]:
    starts: dict[str, datetime] = {}
    ends: dict[str, datetime] = {}
    events: defaultdict[str, list[tuple[datetime, int, str, str]]] = defaultdict(list)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for position, row in enumerate(csv.DictReader(handle)):
            case_id = row["case:concept:name"]
            timestamp = parse_time(row["time:timestamp"])
            if case_id not in starts or timestamp < starts[case_id]:
                starts[case_id] = timestamp
            if case_id not in ends or timestamp > ends[case_id]:
                ends[case_id] = timestamp
            if row["lifecycle:transition"].lower() == "complete":
                events[case_id].append((
                    timestamp, position, row["concept:name"], row["org:resource"].strip(),
                ))
    traces = []
    for case_id, start in starts.items():
        ordered = sorted(events.get(case_id, []))
        if ordered:
            traces.append({
                "case_id": case_id,
                "start_time": start,
                "end_time": ends[case_id],
                "activities": [activity for _, _, activity, _ in ordered],
                "complete_timestamps": [timestamp for timestamp, _, _, _ in ordered],
                "complete_resources": [resource for _, _, _, resource in ordered],
            })
    traces.sort(key=lambda trace: (trace["start_time"], trace["case_id"]))
    return traces


def trace_supports(traces: Iterable[dict[str, Any]]) -> tuple[dict[str, float], dict[tuple[str, str], float]]:
    traces = list(traces)
    activity_counts: Counter = Counter()
    edge_counts: Counter = Counter()
    for trace in traces:
        sequence = trace["activities"]
        activity_counts.update(set(sequence))
        edge_counts.update(set(zip(sequence, sequence[1:])))
    denominator = len(traces)
    return (
        {key: value / denominator for key, value in activity_counts.items()},
        {key: value / denominator for key, value in edge_counts.items()},
    )


def rms_change(before: dict[Any, float], after: dict[Any, float]) -> float:
    keys = set(before) | set(after)
    if not keys:
        return 0.0
    return math.sqrt(sum((after.get(key, 0.0) - before.get(key, 0.0)) ** 2 for key in keys) / len(keys))


def maximum_change(before: dict[Any, float], after: dict[Any, float]) -> float:
    return max((abs(after.get(key, 0.0) - before.get(key, 0.0)) for key in set(before) | set(after)), default=0.0)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--window-size", type=int, default=200)
    parser.add_argument("--step", type=int, default=50)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--minimum-separation", type=int, default=1000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    traces = load_complete_traces(args.log)
    scan_rows = []
    for boundary in range(args.window_size, len(traces) - args.window_size + 1, args.step):
        before = traces[boundary - args.window_size:boundary]
        after = traces[boundary:boundary + args.window_size]
        before_activity, before_edge = trace_supports(before)
        after_activity, after_edge = trace_supports(after)
        activity_rms = rms_change(before_activity, after_activity)
        edge_rms = rms_change(before_edge, after_edge)
        scan_rows.append({
            "boundary_case_index": boundary,
            "first_after_case_id": after[0]["case_id"],
            "first_after_start_time": after[0]["start_time"].isoformat(),
            "before_start_index": boundary - args.window_size,
            "before_end_index_exclusive": boundary,
            "after_start_index": boundary,
            "after_end_index_exclusive": boundary + args.window_size,
            "activity_support_rms_change": round(activity_rms, 10),
            "dfg_support_rms_change": round(edge_rms, 10),
            "combined_change_score": round((activity_rms + edge_rms) / 2, 10),
            "max_activity_support_change": round(maximum_change(before_activity, after_activity), 10),
            "max_dfg_support_change": round(maximum_change(before_edge, after_edge), 10),
        })

    local_maxima = []
    for index, row in enumerate(scan_rows):
        score = row["combined_change_score"]
        left = scan_rows[index - 1]["combined_change_score"] if index else float("-inf")
        right = scan_rows[index + 1]["combined_change_score"] if index + 1 < len(scan_rows) else float("-inf")
        if score >= left and score >= right:
            local_maxima.append(row)
    selected = []
    for row in sorted(local_maxima, key=lambda item: (-item["combined_change_score"], item["boundary_case_index"])):
        if all(abs(row["boundary_case_index"] - old["boundary_case_index"]) >= args.minimum_separation for old in selected):
            selected.append(row)
        if len(selected) == args.top_k:
            break
    selected.sort(key=lambda item: item["boundary_case_index"])
    candidate_rows = [
        {"candidate_rank_by_score": rank, **row}
        for rank, row in enumerate(sorted(selected, key=lambda item: -item["combined_change_score"]), 1)
    ]

    write_csv(args.output / "scan_scores.csv", scan_rows)
    write_csv(args.output / "candidate_change_points.csv", candidate_rows)
    metadata = {
        "dataset": "BPI Challenge 2017",
        "source": str(args.log.resolve()),
        "event_filter": "lifecycle:transition == complete",
        "case_order": "first event timestamp, then case id",
        "trace_count": len(traces),
        "window_size_cases": args.window_size,
        "scan_step_cases": args.step,
        "minimum_candidate_separation_cases": args.minimum_separation,
        "candidate_count": len(candidate_rows),
        "coordinate_semantics": "detected candidate boundary; not ground truth",
        "score": "mean of activity-support RMS change and DFG trace-support RMS change",
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "run_metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Complete traces:", len(traces))
    print("Scan boundaries:", len(scan_rows))
    print("Candidates:", len(candidate_rows))
    print("Output:", args.output)


if __name__ == "__main__":
    main()
