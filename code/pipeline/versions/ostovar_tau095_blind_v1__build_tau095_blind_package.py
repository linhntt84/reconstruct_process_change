#!/usr/bin/env python3
"""Build an answer-blind package for the 26 uniform-tau=0.95 explanations."""

from __future__ import annotations

import csv
import hashlib
import json
import random
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
RUN = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/runs/"
    "ostovar_atomic_noise_0_b200_algorithm_1_2_tau_0p95_v1"
)
TRUTH = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/ground_truth/"
    "ostovar_size3_atomic_noise_0_object_ground_truth_v1.csv"
)
PUBLIC = PACKAGE / "grading_inputs/ostovar_tau095_blind_26.csv"
PRIVATE = PACKAGE / "internal_after_grading/private_tau095_blind_key_26.csv"
BATCH_DIR = PACKAGE / "grading_inputs/batches"
SEED = 20260917095


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
    truth_rows = read_csv(TRUTH)
    truth = {row["case_id"]: row for row in truth_rows}
    if len(truth) != 26:
        raise SystemExit(f"Expected 26 reference cases, found {len(truth)}")

    responses: list[tuple[Path, dict]] = []
    for path in sorted((RUN / "responses").glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("status") != "success_complete":
            raise SystemExit(f"Incomplete response: {path}")
        if not record.get("visible_text", "").strip():
            raise SystemExit(f"Empty visible_text: {path}")
        responses.append((path, record))

    if len(responses) != 26:
        raise SystemExit(f"Expected 26 responses, found {len(responses)}")
    if {record["case_id"] for _, record in responses} != set(truth):
        raise SystemExit("Response case set does not match the frozen ground truth")

    random.Random(SEED).shuffle(responses)
    public_rows: list[dict[str, str]] = []
    private_rows: list[dict[str, str]] = []
    for path, record in responses:
        case_id = record["case_id"]
        reference = truth[case_id]
        grading_id = "ITEM-" + hashlib.sha256(
            f"{SEED}|uniform_tau_0.95|{case_id}".encode()
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
            "condition": "UNIFORM_TAU_0P95",
            "native_noise_percent": reference["native_noise_percent"],
            "change_pattern": reference["change_pattern"],
            "affected_activities_anon": reference["affected_activities_anon"],
            "activities_added_anon": reference["activities_added_anon"],
            "activities_deleted_anon": reference["activities_deleted_anon"],
            "activities_moved_anon": reference["activities_moved_anon"],
            "activities_reweighted_anon": reference["activities_reweighted_anon"],
            "object_role_pairs_anon": reference["object_role_pairs_anon"],
            "explanation_sha256": hashlib.sha256(explanation.encode()).hexdigest(),
            "response_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "source_response": str(path.relative_to(WORKSPACE)),
        })

    if len({row["grading_id"] for row in public_rows}) != 26:
        raise SystemExit("Opaque grading-ID collision")

    write_csv(PUBLIC, public_rows)
    write_csv(PRIVATE, private_rows)
    for start in range(0, 26, 13):
        number = start // 13 + 1
        write_csv(
            BATCH_DIR / f"blind_batch_{number:02d}.csv",
            public_rows[start:start + 13],
        )

    print(f"Public master: {PUBLIC} ({len(public_rows)} rows)")
    print(f"Private key: {PRIVATE} ({len(private_rows)} rows)")
    print("Blind batches: 2 x 13 rows")


if __name__ == "__main__":
    main()
