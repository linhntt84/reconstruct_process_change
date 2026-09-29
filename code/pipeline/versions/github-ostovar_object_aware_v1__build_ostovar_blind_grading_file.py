#!/usr/bin/env python3
"""Create a minimal, shuffled, blind Ostovar grading sheet and private key."""

from __future__ import annotations

import argparse
import csv
import hashlib
import random
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
DEFAULT_INPUTS = [
    EXPERIMENT / "runs/ostovar_atomic_noise_2p5_b200_algorithm_1_2_v1/grading_package_object_v1/object_grading_full_26.csv",
    EXPERIMENT / "runs/ostovar_atomic_noise_5p0_b200_algorithm_1_2_v1/grading_package_object_v1/object_grading_full_26.csv",
]
DEFAULT_PUBLIC = EXPERIMENT / "grading/ostovar_blind_object_pattern_52.csv"
DEFAULT_PRIVATE = EXPERIMENT / "ground_truth/private_ostovar_blind_key_52.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, nargs="+", default=DEFAULT_INPUTS)
    parser.add_argument("--public-output", type=Path, default=DEFAULT_PUBLIC)
    parser.add_argument("--private-output", type=Path, default=DEFAULT_PRIVATE)
    parser.add_argument("--seed", type=int, default=20260917)
    args = parser.parse_args()

    source: list[tuple[Path, dict[str, str]]] = []
    for path in args.inputs:
        rows = read_rows(path)
        if len(rows) != 26:
            raise SystemExit(f"Expected 26 rows in {path}, found {len(rows)}")
        source.extend((path, row) for row in rows)
    if len({row["case_id"] for _, row in source}) != len(source):
        raise SystemExit("case_id is not unique across input files")

    rng = random.Random(args.seed)
    rng.shuffle(source)
    public_rows, private_rows = [], []
    for path, row in source:
        opaque = hashlib.sha256(
            f"{args.seed}|{row['case_id']}".encode()
        ).hexdigest()[:10]
        grading_id = f"ITEM-{opaque}"
        explanation = row["llm_explanation_full"]
        public_rows.append({
            "grading_id": grading_id,
            "llm_explanation_full": explanation,
            "predicted_objects": "",
            "predicted_pattern": "",
            "prediction_note": "",
        })
        private_rows.append({
            "grading_id": grading_id,
            "case_id": row["case_id"],
            "native_noise_percent": row["native_noise_percent"],
            "source_grading_file": str(path.relative_to(EXPERIMENT)),
            "change_pattern": row["change_pattern"],
            "affected_activities_anon": row["affected_activities_anon"],
            "activities_added_anon": row["activities_added_anon"],
            "activities_deleted_anon": row["activities_deleted_anon"],
            "activities_moved_anon": row["activities_moved_anon"],
            "activities_reweighted_anon": row["activities_reweighted_anon"],
            "object_role_pairs_anon": row["object_role_pairs_anon"],
            "explanation_sha256": hashlib.sha256(explanation.encode()).hexdigest(),
        })

    write_rows(args.public_output, public_rows)
    write_rows(args.private_output, private_rows)
    print(f"Public blind sheet: {args.public_output} ({len(public_rows)} rows)")
    print(f"Private lookup key: {args.private_output} ({len(private_rows)} rows)")


if __name__ == "__main__":
    main()
