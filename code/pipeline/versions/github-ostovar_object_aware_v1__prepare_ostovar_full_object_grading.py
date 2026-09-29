#!/usr/bin/env python3
"""Join complete Ostovar LLM responses with object-aware Size3 references."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


GRADING_FIELDS = [
    "status", "predicted_operation", "predicted_objects",
    "correct_object_role_pairs", "missing_object_role_pairs",
    "incorrect_object_role_pairs", "object_role_coverage", "MR", "MR_note",
    "PI", "PI_quote", "PI_failure_reason", "reference_conflict",
    "unsupported_claim_present", "adjudication_note",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--ground-truth", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    truth_rows = read_csv(args.ground_truth)
    truth = {row["case_id"]: row for row in truth_rows}
    if len(truth) != 26:
        raise SystemExit(f"Expected 26 unique ground-truth cases, found {len(truth)}")

    outputs: dict[str, dict] = {}
    for path in sorted((args.run_dir / "responses").glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        case_id = record.get("case_id")
        if case_id in outputs:
            raise SystemExit(f"Duplicate response for {case_id}")
        outputs[case_id] = record
    missing = sorted(set(truth) - set(outputs))
    extra = sorted(set(outputs) - set(truth))
    if missing or extra:
        raise SystemExit(f"Join mismatch: missing={missing}, extra={extra}")

    rows = []
    for case_id in sorted(truth):
        reference, response = truth[case_id], outputs[case_id]
        text = response.get("visible_text", "")
        if response.get("status") != "success_complete" or not text.strip():
            raise SystemExit(f"Incomplete response: {case_id} ({response.get('status')})")
        row = dict(reference)
        row.update({
            "llm_explanation_full": text,
            "response_status": response["status"],
            "finish_reason": str(response.get("finish_reason", "")),
            "model": str(response.get("model", "")),
            "prompt_tokens": str(response.get("usage", {}).get("prompt_tokens", "")),
            "completion_tokens": str(response.get("usage", {}).get("completion_tokens", "")),
            "total_tokens": str(response.get("usage", {}).get("total_tokens", "")),
        })
        row.update({field: "" for field in GRADING_FIELDS})
        rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} complete explanations to {args.output}")


if __name__ == "__main__":
    main()
