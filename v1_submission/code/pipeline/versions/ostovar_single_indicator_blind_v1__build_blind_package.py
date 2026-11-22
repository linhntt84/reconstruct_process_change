#!/usr/bin/env python3
"""Build the answer-blind package for the 130 single-indicator responses."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
RUN = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/runs/"
    "ostovar_atomic_b200_algorithm_1_2_per_indicator_v1"
)
TRUTH = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/ground_truth/"
    "ostovar_size3_atomic_noise_0_object_ground_truth_v1.csv"
)
PUBLIC = PACKAGE / "grading_inputs/blind_items.csv"
PRIVATE = PACKAGE / "internal_after_grading/private_blind_key.csv"
AUDIT = PACKAGE / "provenance/run_audit.csv"
SUMMARY = PACKAGE / "provenance/run_summary.json"
BATCH_DIR = PACKAGE / "grading_inputs/batches"
CHECKSUMS = PACKAGE / "SHA256SUMS"
FOR_CLAUDE = PACKAGE / "for_claude"
SEED = "ostovar-single-indicator-blind-v1-20260918"
EXPECTED_CONDITIONS = {"OCC_ONLY", "DIR_ONLY", "POS_ONLY", "REL_ONLY", "LAG_ONLY"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def response_identity(path: Path) -> tuple[str, str]:
    try:
        case_id, condition = path.stem.split("__", 1)
    except ValueError as exc:
        raise SystemExit(f"Unexpected response filename: {path.name}") from exc
    return case_id, condition


def main() -> None:
    truth_rows = read_csv(TRUTH)
    truth = {row["case_id"]: row for row in truth_rows}
    response_paths = sorted((RUN / "responses").glob("*.json"))
    if len(truth) != 26:
        raise SystemExit(f"Expected 26 truth rows; found {len(truth)}")
    if len(response_paths) != 130:
        raise SystemExit(f"Expected 130 responses; found {len(response_paths)}")

    public_rows: list[dict[str, object]] = []
    private_rows: list[dict[str, object]] = []
    audit_rows: list[dict[str, object]] = []
    condition_counts: Counter[str] = Counter()

    for response_path in response_paths:
        case_id, condition = response_identity(response_path)
        if case_id not in truth:
            raise SystemExit(f"Response case absent from ground truth: {case_id}")
        if condition not in EXPECTED_CONDITIONS:
            raise SystemExit(f"Unexpected single-indicator condition: {condition}")

        response = json.loads(response_path.read_text(encoding="utf-8"))
        status = str(response.get("status", "missing_status"))
        explanation = str(response.get("visible_text") or "")
        valid = status == "success_complete" and bool(explanation.strip())
        usage = response.get("usage") or {}
        condition_counts[condition] += int(valid)

        audit_rows.append(
            {
                "case_id": case_id,
                "condition": condition,
                "status": status,
                "valid_for_grading": str(valid).lower(),
                "model": response.get("model", ""),
                "prompt_tokens": usage.get("prompt_tokens", ""),
                "completion_tokens": usage.get("completion_tokens", ""),
                "reasoning_tokens": (usage.get("completion_tokens_details") or {}).get(
                    "reasoning_tokens", ""
                ),
                "total_tokens": usage.get("total_tokens", ""),
                "response_path": str(response_path.relative_to(WORKSPACE)),
            }
        )
        if not valid:
            continue

        reference = truth[case_id]
        grading_id = "ITEM-" + sha256_text(f"{SEED}|{case_id}|{condition}")[:12]
        public_rows.append(
            {
                "grading_id": grading_id,
                "llm_explanation_full": explanation,
                "predicted_objects": "",
                "predicted_pattern": "",
                "prediction_note": "",
            }
        )
        private_rows.append(
            {
                "grading_id": grading_id,
                "case_id": case_id,
                "condition": condition,
                "model": response.get("model", ""),
                "native_noise_percent": reference["native_noise_percent"],
                "change_pattern": reference["change_pattern"],
                "affected_activities_anon": reference["affected_activities_anon"],
                "activities_added_anon": reference["activities_added_anon"],
                "activities_deleted_anon": reference["activities_deleted_anon"],
                "activities_moved_anon": reference["activities_moved_anon"],
                "activities_reweighted_anon": reference["activities_reweighted_anon"],
                "object_role_pairs_anon": reference["object_role_pairs_anon"],
                "explanation_sha256": sha256_text(explanation),
                "response_sha256": sha256_file(response_path),
                "source_response": str(response_path.relative_to(WORKSPACE)),
            }
        )

    invalid = [row for row in audit_rows if row["valid_for_grading"] != "true"]
    if invalid:
        raise SystemExit(
            "Blind package refused because some responses are invalid: "
            + ", ".join(f"{row['case_id']}::{row['condition']}" for row in invalid)
        )
    if condition_counts != Counter({condition: 26 for condition in EXPECTED_CONDITIONS}):
        raise SystemExit(f"Unexpected condition counts: {dict(condition_counts)}")

    public_rows.sort(key=lambda row: str(row["grading_id"]))
    private_rows.sort(key=lambda row: str(row["grading_id"]))
    if len({row["grading_id"] for row in public_rows}) != 130:
        raise SystemExit("Opaque grading-ID collision")

    public_fields = [
        "grading_id",
        "llm_explanation_full",
        "predicted_objects",
        "predicted_pattern",
        "prediction_note",
    ]
    write_csv(PUBLIC, public_rows, public_fields)
    write_csv(PRIVATE, private_rows, list(private_rows[0]))
    write_csv(AUDIT, audit_rows, list(audit_rows[0]))

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    for stale in BATCH_DIR.glob("blind_batch_*.csv"):
        stale.unlink()
    for start in range(0, len(public_rows), 13):
        write_csv(
            BATCH_DIR / f"blind_batch_{start // 13 + 1:02d}.csv",
            public_rows[start : start + 13],
            public_fields,
        )

    FOR_CLAUDE.mkdir(parents=True, exist_ok=True)
    for stale in FOR_CLAUDE.iterdir():
        if stale.is_file():
            stale.unlink()
    shutil.copy2(
        PACKAGE / "protocol/RUBRIC_BLIND_V1_VI.md",
        FOR_CLAUDE / "RUBRIC_BLIND_V1_VI.md",
    )
    shutil.copy2(
        PACKAGE / "protocol/PROMPT_FOR_GRADER.md",
        FOR_CLAUDE / "PROMPT_FOR_GRADER.md",
    )
    for batch_path in sorted(BATCH_DIR.glob("blind_batch_*.csv")):
        shutil.copy2(batch_path, FOR_CLAUDE / batch_path.name)

    summary = {
        "schema_version": "single-indicator-blind-package-1.0",
        "expected_cases": 130,
        "valid_cases": len(public_rows),
        "invalid_cases": 130 - len(public_rows),
        "final_package": len(public_rows) == 130,
        "conditions_hidden_from_grader": sorted(EXPECTED_CONDITIONS),
        "valid_cases_by_condition": dict(sorted(condition_counts.items())),
        "batch_size": 13,
        "batch_count": len(list(BATCH_DIR.glob("blind_batch_*.csv"))),
        "prompt_tokens": sum(int(row["prompt_tokens"] or 0) for row in audit_rows),
        "completion_tokens": sum(int(row["completion_tokens"] or 0) for row in audit_rows),
        "reasoning_tokens": sum(int(row["reasoning_tokens"] or 0) for row in audit_rows),
        "total_tokens": sum(int(row["total_tokens"] or 0) for row in audit_rows),
        "public_grading_input": str(PUBLIC.relative_to(PACKAGE)),
        "private_key": str(PRIVATE.relative_to(PACKAGE)),
    }
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    checksum_paths = [
        PUBLIC,
        PRIVATE,
        AUDIT,
        SUMMARY,
        PACKAGE / "protocol/RUBRIC_BLIND_V1_VI.md",
        PACKAGE / "protocol/PROMPT_FOR_GRADER.md",
        *sorted(BATCH_DIR.glob("blind_batch_*.csv")),
    ]
    CHECKSUMS.write_text(
        "".join(
            f"{sha256_file(path)}  {path.relative_to(PACKAGE)}\n"
            for path in checksum_paths
        ),
        encoding="utf-8",
    )

    print(f"Public blind sheet: {PUBLIC} ({len(public_rows)} rows)")
    print(f"Blind batches: {summary['batch_count']} x {summary['batch_size']} rows")
    print(f"Private key: {PRIVATE} ({len(private_rows)} rows)")
    print(f"Final package: {summary['final_package']}")


if __name__ == "__main__":
    main()
