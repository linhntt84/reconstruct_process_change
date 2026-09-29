#!/usr/bin/env python3
"""Build a shuffled, answer-blind grading package for the second-model run."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
MANIFEST = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/manifests/model2_deepseek_v4_flash/"
    "ostovar_integrated_26.csv"
)
RUN = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/runs/"
    "model2_deepseek_v4_flash_ostovar_integrated_26"
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
SEED = "second-model-blind-v1-20260918"


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-incomplete",
        action="store_true",
        help="Write a provisional package containing only successful responses.",
    )
    args = parser.parse_args()

    manifest = read_csv(MANIFEST)
    truth_rows = read_csv(TRUTH)
    truth = {row["case_id"]: row for row in truth_rows}
    if len(manifest) != 26 or len(truth) != 26:
        raise SystemExit(
            f"Expected 26 manifest and reference rows; found {len(manifest)} and {len(truth)}"
        )

    audit_rows: list[dict[str, object]] = []
    successes: list[tuple[Path, dict[str, object]]] = []
    for job in manifest:
        stem = f"{job['case_id']}__{job['condition']}"
        response_path = RUN / "responses" / f"{stem}.json"
        markdown_path = RUN / "markdown" / f"{stem}.md"
        if response_path.exists():
            response = json.loads(response_path.read_text(encoding="utf-8"))
            status = str(response.get("status", "missing_status"))
            usage = response.get("usage") or {}
            visible_text = str(response.get("visible_text") or "")
            error = str(response.get("error") or "")
        else:
            response = {}
            status = "missing_response"
            usage = {}
            visible_text = ""
            error = ""
        valid = status == "success_complete" and bool(visible_text.strip())
        if valid:
            successes.append((response_path, response))
        audit_rows.append(
            {
                "case_id": job["case_id"],
                "condition": job["condition"],
                "status": status,
                "valid_for_grading": str(valid).lower(),
                "markdown_present": str(markdown_path.exists()).lower(),
                "model": response.get("model", job["model"]),
                "prompt_tokens": usage.get("prompt_tokens", ""),
                "completion_tokens": usage.get("completion_tokens", ""),
                "reasoning_tokens": (usage.get("completion_tokens_details") or {}).get(
                    "reasoning_tokens", ""
                ),
                "total_tokens": usage.get("total_tokens", ""),
                "error": error,
                "response_path": str(response_path.relative_to(WORKSPACE)),
            }
        )

    if len(successes) != 26 and not args.allow_incomplete:
        failed = [row["case_id"] for row in audit_rows if row["valid_for_grading"] != "true"]
        raise SystemExit(
            f"Only {len(successes)}/26 valid responses. Retry before the final build: {failed}"
        )

    public_rows: list[dict[str, object]] = []
    private_rows: list[dict[str, object]] = []
    for response_path, response in successes:
        case_id = str(response["case_id"])
        if case_id not in truth:
            raise SystemExit(f"Response case absent from ground truth: {case_id}")
        reference = truth[case_id]
        explanation = str(response["visible_text"])
        grading_id = "ITEM-" + sha256_text(f"{SEED}|{case_id}")[:12]
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
                "condition": response["condition"],
                "model": response["model"],
                "native_noise_percent": reference["native_noise_percent"],
                "change_pattern": reference["change_pattern"],
                "affected_activities_anon": reference["affected_activities_anon"],
                "activities_added_anon": reference["activities_added_anon"],
                "activities_deleted_anon": reference["activities_deleted_anon"],
                "activities_moved_anon": reference["activities_moved_anon"],
                "activities_reweighted_anon": reference[
                    "activities_reweighted_anon"
                ],
                "object_role_pairs_anon": reference["object_role_pairs_anon"],
                "explanation_sha256": sha256_text(explanation),
                "response_sha256": hashlib.sha256(response_path.read_bytes()).hexdigest(),
                "source_response": str(response_path.relative_to(WORKSPACE)),
            }
        )

    # Sorting by an opaque hash provides deterministic shuffling. Adding a retried
    # case later does not alter identifiers or the relative order of existing rows.
    public_rows.sort(key=lambda row: str(row["grading_id"]))
    private_rows.sort(key=lambda row: str(row["grading_id"]))
    if len({row["grading_id"] for row in public_rows}) != len(public_rows):
        raise SystemExit("Opaque grading-ID collision")

    public_fields = [
        "grading_id",
        "llm_explanation_full",
        "predicted_objects",
        "predicted_pattern",
        "prediction_note",
    ]
    private_fields = list(private_rows[0])
    audit_fields = list(audit_rows[0])
    write_csv(PUBLIC, public_rows, public_fields)
    write_csv(PRIVATE, private_rows, private_fields)
    write_csv(AUDIT, audit_rows, audit_fields)

    for stale in BATCH_DIR.glob("blind_batch_*.csv"):
        stale.unlink()
    for start in range(0, len(public_rows), 13):
        batch = public_rows[start : start + 13]
        write_csv(
            BATCH_DIR / f"blind_batch_{start // 13 + 1:02d}.csv",
            batch,
            public_fields,
        )

    successful_audits = [row for row in audit_rows if row["valid_for_grading"] == "true"]
    summary = {
        "schema_version": "model2-blind-package-1.0",
        "expected_cases": 26,
        "valid_cases": len(successes),
        "invalid_cases": 26 - len(successes),
        "final_package": len(successes) == 26,
        "prompt_tokens": sum(int(row["prompt_tokens"] or 0) for row in successful_audits),
        "completion_tokens": sum(
            int(row["completion_tokens"] or 0) for row in successful_audits
        ),
        "reasoning_tokens": sum(
            int(row["reasoning_tokens"] or 0) for row in successful_audits
        ),
        "total_tokens": sum(int(row["total_tokens"] or 0) for row in successful_audits),
        "public_grading_input": str(PUBLIC.relative_to(PACKAGE)),
        "private_key": str(PRIVATE.relative_to(PACKAGE)),
    }
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Public blind sheet: {PUBLIC} ({len(public_rows)} rows)")
    print(f"Private key: {PRIVATE} ({len(private_rows)} rows)")
    print(f"Run audit: {AUDIT} (26 rows)")
    print(f"Final package: {summary['final_package']}")


if __name__ == "__main__":
    main()
