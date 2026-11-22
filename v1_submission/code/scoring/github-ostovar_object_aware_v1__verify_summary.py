#!/usr/bin/env python3
"""Recompute aggregate metrics from object-gated scoring-policy-v2 outputs."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCORED = [
    ROOT / "scored_results/noise0_scored_policy_v2.csv",
    ROOT / "scored_results/noise2p5_5p0_scored_policy_v2.csv",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def aggregate(rows: list[dict[str, str]]) -> dict[str, float | int]:
    tp = sum(len(json.loads(row["localization_tp"])) for row in rows)
    fp = sum(len(json.loads(row["localization_fp"])) for row in rows)
    fn = sum(len(json.loads(row["localization_fn"])) for row in rows)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    mean = lambda field: sum(float(row[field]) for row in rows) / len(rows)
    return {
        "cases": len(rows),
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "micro_precision": precision,
        "micro_recall": recall,
        "micro_f1": f1,
        "macro_precision": mean("localization_precision"),
        "macro_recall": mean("localization_recall"),
        "macro_f1": mean("localization_f1"),
        "mean_OBJECT": mean("OBJECT"),
        "mean_MR": mean("MR"),
        "mean_PI": mean("PI"),
        "pattern_exact": sum(row["pattern_exact"] == "true" for row in rows),
    }


def main() -> None:
    rows = [row for path in SCORED for row in read_rows(path)]
    groups = {
        "0.0": [row for row in rows if row["native_noise_percent"] == "0.0"],
        "2.5": [row for row in rows if row["native_noise_percent"] == "2.5"],
        "5.0": [row for row in rows if row["native_noise_percent"] == "5.0"],
        "all": rows,
    }
    for label, group in groups.items():
        result = aggregate(group)
        metrics = ", ".join(
            f"{key}={value:.6f}" if isinstance(value, float) else f"{key}={value}"
            for key, value in result.items()
        )
        print(f"noise={label}: {metrics}")


if __name__ == "__main__":
    main()
