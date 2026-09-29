#!/usr/bin/env python3
"""Build answer-blind grading files for the Ostovar localization ablation."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
DEFAULT_RUN = EXPERIMENT / "runs/ostovar_localization_ablation_v1"
DEFAULT_TRUTH = EXPERIMENT / "ground_truth/ostovar_size3_atomic_noise_0_object_ground_truth_v1.csv"
DEFAULT_OUTPUT = DEFAULT_RUN / "grading_package_object_blind_v1"
EXPECTED_CONDITIONS = {
    *(f"RANDOM_REGION_R{i}" for i in range(1, 6)),
    "NO_LOCALIZATION",
    "OUTSIDE_A_STAR",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN)
    parser.add_argument("--ground-truth", type=Path, default=DEFAULT_TRUTH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--seed", type=int, default=20260919)
    parser.add_argument("--batch-size", type=int, default=13)
    args = parser.parse_args()

    truth_rows = read_csv(args.ground_truth)
    truth = {row["case_id"]: row for row in truth_rows}
    if len(truth) != 26:
        raise SystemExit(f"Expected 26 ground-truth cases, found {len(truth)}")

    records: list[tuple[Path, dict]] = []
    for path in sorted((args.run_dir / "responses").glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("status") != "success_complete" or not record.get("visible_text", "").strip():
            raise SystemExit(f"Incomplete response: {path}")
        records.append((path, record))
    if len(records) != 182:
        raise SystemExit(f"Expected 182 complete responses, found {len(records)}")

    counts = Counter(record["condition"] for _, record in records)
    if set(counts) != EXPECTED_CONDITIONS or any(counts[name] != 26 for name in counts):
        raise SystemExit(f"Unexpected condition distribution: {dict(counts)}")
    if {record["case_id"] for _, record in records} != set(truth):
        raise SystemExit("Response case set does not match the 26-case ground truth")

    rng = random.Random(args.seed)
    rng.shuffle(records)
    public_rows: list[dict[str, str]] = []
    private_rows: list[dict[str, str]] = []
    for path, record in records:
        case_id = record["case_id"]
        condition = record["condition"]
        reference = truth[case_id]
        grading_id = "ITEM-" + hashlib.sha256(
            f"{args.seed}|{case_id}|{condition}".encode()
        ).hexdigest()[:12]
        explanation = record["visible_text"]
        public_rows.append({
            "grading_id": grading_id,
            "llm_explanation_full": explanation,
            "predicted_objects": "",
            "predicted_pattern": "",
            "prediction_note": "",
        })
        private_rows.append({
            "grading_id": grading_id,
            "case_id": case_id,
            "condition": condition,
            "native_noise_percent": reference["native_noise_percent"],
            "change_pattern": reference["change_pattern"],
            "affected_activities_anon": reference["affected_activities_anon"],
            "activities_added_anon": reference["activities_added_anon"],
            "activities_deleted_anon": reference["activities_deleted_anon"],
            "activities_moved_anon": reference["activities_moved_anon"],
            "activities_reweighted_anon": reference["activities_reweighted_anon"],
            "object_role_pairs_anon": reference["object_role_pairs_anon"],
            "explanation_sha256": hashlib.sha256(explanation.encode()).hexdigest(),
            "source_response": str(path.relative_to(EXPERIMENT)),
        })

    if len({row["grading_id"] for row in public_rows}) != 182:
        raise SystemExit("Opaque grading ID collision")

    write_csv(args.output_dir / "ostovar_localization_blind_182.csv", public_rows)
    write_csv(args.output_dir / "private_localization_blind_key_182.csv", private_rows)
    batch_dir = args.output_dir / "batches"
    for start in range(0, len(public_rows), args.batch_size):
        number = start // args.batch_size + 1
        write_csv(batch_dir / f"blind_batch_{number:02d}.csv", public_rows[start:start + args.batch_size])

    print(f"Public master: {args.output_dir / 'ostovar_localization_blind_182.csv'}")
    print(f"Private key: {args.output_dir / 'private_localization_blind_key_182.csv'}")
    print(f"Blind batches: {(len(public_rows) + args.batch_size - 1) // args.batch_size}")


if __name__ == "__main__":
    main()
