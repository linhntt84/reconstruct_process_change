#!/usr/bin/env python3
"""Build the fresh 26-case blind package for the completed noisy run."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
MANIFEST = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/manifests/model2_deepseek_v4_flash/"
    "ostovar_noise_5p0_integrated_26.csv"
)
RUN = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/runs/"
    "model2_deepseek_v4_flash_ostovar_noise_5p0_integrated_26"
)
TRUTH = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/ground_truth/"
    "ostovar_size3_atomic_noise_5p0_object_ground_truth_v1.csv"
)

PUBLIC = PACKAGE / "for_claude/blind_items.csv"
PRIVATE = PACKAGE / "internal_after_grading/private_blind_key.csv"
AUDIT = PACKAGE / "provenance/run_audit.csv"
SUMMARY = PACKAGE / "provenance/run_summary.json"
BATCH_DIR = PACKAGE / "for_claude/batches"
CHECKSUMS = PACKAGE / "SHA256SUMS"

# Unique to this grading round; it does not reuse clean-run or CDLG blind IDs.
SEED = "noise-5p0-second-model-blind-v1-20260920-f84d29"


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
    manifest = read_csv(MANIFEST)
    truth_rows = read_csv(TRUTH)
    truth = {row["case_id"]: row for row in truth_rows}
    manifest_ids = {row["case_id"] for row in manifest}

    if len(manifest) != 26 or len(truth_rows) != 26:
        raise SystemExit(
            f"Expected 26 manifest and truth rows; found {len(manifest)} and {len(truth_rows)}"
        )
    if manifest_ids != set(truth):
        raise SystemExit("Manifest and noisy ground-truth case sets do not match")

    audit_rows: list[dict[str, object]] = []
    public_rows: list[dict[str, object]] = []
    private_rows: list[dict[str, object]] = []

    for job in manifest:
        stem = f"{job['case_id']}__{job['condition']}"
        response_path = RUN / "responses" / f"{stem}.json"
        markdown_path = RUN / "markdown" / f"{stem}.md"
        if not response_path.exists():
            raise SystemExit(f"Missing response: {response_path}")

        response = json.loads(response_path.read_text(encoding="utf-8"))
        status = str(response.get("status", "missing_status"))
        explanation = str(response.get("visible_text") or "").strip()
        usage = response.get("usage") or {}
        valid = status == "success_complete" and bool(explanation)

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
                "response_path": str(response_path.relative_to(WORKSPACE)),
            }
        )
        if not valid:
            continue

        case_id = str(response["case_id"])
        reference = truth[case_id]
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

    if len(public_rows) != 26:
        invalid = [
            row["case_id"] for row in audit_rows if row["valid_for_grading"] != "true"
        ]
        raise SystemExit(f"Only {len(public_rows)}/26 valid responses: {invalid}")

    public_rows.sort(key=lambda row: str(row["grading_id"]))
    private_rows.sort(key=lambda row: str(row["grading_id"]))
    if len({row["grading_id"] for row in public_rows}) != 26:
        raise SystemExit("Opaque grading-ID collision")

    public_fields = list(public_rows[0])
    write_csv(PUBLIC, public_rows, public_fields)
    write_csv(PRIVATE, private_rows, list(private_rows[0]))
    write_csv(AUDIT, audit_rows, list(audit_rows[0]))

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    for stale in BATCH_DIR.glob("blind_batch_*.csv"):
        stale.unlink()
    for start in range(0, 26, 13):
        write_csv(
            BATCH_DIR / f"blind_batch_{start // 13 + 1:02d}.csv",
            public_rows[start : start + 13],
            public_fields,
        )

    summary = {
        "schema_version": "model2-noisy-blind-package-1.0",
        "expected_cases": 26,
        "valid_cases": 26,
        "invalid_cases": 0,
        "final_package": True,
        "prompt_tokens": sum(int(row["prompt_tokens"] or 0) for row in audit_rows),
        "completion_tokens": sum(
            int(row["completion_tokens"] or 0) for row in audit_rows
        ),
        "reasoning_tokens": sum(
            int(row["reasoning_tokens"] or 0) for row in audit_rows
        ),
        "total_tokens": sum(int(row["total_tokens"] or 0) for row in audit_rows),
        "public_grading_input": str(PUBLIC.relative_to(PACKAGE)),
        "private_key": str(PRIVATE.relative_to(PACKAGE)),
    }
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    checksum_targets = [PUBLIC, PRIVATE, AUDIT, SUMMARY, *sorted(BATCH_DIR.glob("*.csv"))]
    lines = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(PACKAGE)}"
        for path in checksum_targets
    ]
    CHECKSUMS.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Public blind sheet: {PUBLIC} ({len(public_rows)} rows)")
    print(f"Private key: {PRIVATE} ({len(private_rows)} rows)")
    print(f"Batches: {len(list(BATCH_DIR.glob('blind_batch_*.csv')))} x 13")
    print("Final package: True")


if __name__ == "__main__":
    main()
