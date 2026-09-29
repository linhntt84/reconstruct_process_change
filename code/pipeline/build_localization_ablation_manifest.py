#!/usr/bin/env python3
"""Audit localization-ablation evidence and build an immutable API manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
WORKSPACE = EXPERIMENT.parents[1]
DEFAULT_SOURCE = EXPERIMENT / "artifacts/official/ostovar_localization_ablation_v1"
DEFAULT_PROMPT = EXPERIMENT / "prompts/INTERPRET_EVIDENCE_V1_VI.md"
DEFAULT_OUTPUT = EXPERIMENT / "artifacts/api/ostovar_localization_ablation_v1"
DEFAULT_MANIFEST = EXPERIMENT / "manifests/ostovar_localization_ablation_v1.csv"
CONDITIONS = {
    **{f"RANDOM_REGION_R{i}": f"random_matched_r{i}" for i in range(1, 6)},
    "NO_LOCALIZATION": "all",
    "OUTSIDE_A_STAR": "outside",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def workspace_path(path: Path) -> str:
    return str(path.resolve().relative_to(WORKSPACE.resolve()))


def write_json(path: Path, value: Any) -> int:
    text = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return len(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--run-id", default="ieee_access_ostovar_localization_ablation_v1")
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--provider", default="INT2")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    args = parser.parse_args()

    prompt_hash = sha256_file(args.prompt)
    condition_files: dict[str, list[Path]] = {}
    expected_names: set[str] | None = None
    for condition, directory in CONDITIONS.items():
        files = sorted((args.source / directory / "evidence" / "tau_mixed").glob("*.json"))
        if len(files) != 26:
            raise SystemExit(f"{condition}: expected 26 files, found {len(files)}")
        names = {path.name for path in files}
        if expected_names is None:
            expected_names = names
        elif names != expected_names:
            raise SystemExit(f"{condition}: case set differs from other conditions")
        condition_files[condition] = files

    jobs: list[dict[str, Any]] = []
    audit: list[dict[str, Any]] = []
    for condition, files in condition_files.items():
        for source_path in files:
            source = json.loads(source_path.read_text(encoding="utf-8"))
            region = source["activity_region"]
            mode = region["mode"]
            selected = region["selected_activities"]
            affected = region["affected_activities"]
            if len(selected) != len(set(selected)):
                raise SystemExit(f"{condition} {source_path.name}: duplicate selected activities")
            if condition.startswith("RANDOM_REGION"):
                if mode != "random_matched" or len(selected) != len(affected):
                    raise SystemExit(f"{condition} {source_path.name}: invalid matched region")
            elif condition == "NO_LOCALIZATION":
                if mode != "all" or len(selected) != region["all_activity_count"]:
                    raise SystemExit(f"{condition} {source_path.name}: incomplete all-activity region")
            elif mode != "outside" or region["overlap_with_affected"] != 0:
                raise SystemExit(f"{condition} {source_path.name}: outside region overlaps A*")

            case_id = source["case"]["case_id"]
            public = {
                "schema_version": "ieee-access-structured-evidence-1.1",
                "case": source["case"],
                "evidence": source["evidence"],
            }
            evidence_path = args.output / "evidence" / condition.lower() / f"{case_id}.json"
            characters = write_json(evidence_path, public)
            counts = Counter(item["indicator"] for item in public["evidence"])
            jobs.append({
                "run_id": args.run_id,
                "paper_scope": "IEEE_ACCESS",
                "dataset": source["case"].get("dataset", "synthetic_process_log"),
                "case_id": case_id,
                "condition": condition,
                "window_condition": "WINDOW_ORACLE_STABLE",
                "prompt_path": workspace_path(args.prompt),
                "prompt_hash": prompt_hash,
                "schema_version": public["schema_version"],
                "evidence_path": workspace_path(evidence_path),
                "evidence_hash": sha256_file(evidence_path),
                "model": args.model,
                "provider": args.provider,
                "temperature": args.temperature,
                "top_p": args.top_p,
                "max_completion_tokens": "",
                "seed_if_supported": "",
                "expected_output_format": "markdown",
            })
            audit.append({
                "case_id": case_id,
                "condition": condition,
                "region_mode": mode,
                "all_activities": region["all_activity_count"],
                "affected_activities": len(affected),
                "selected_activities": len(selected),
                "overlap_with_affected": region["overlap_with_affected"],
                "candidate_units": source["algorithm_1"]["candidate_units"],
                "evidence_items": len(public["evidence"]),
                **{f"n_{code}": counts[code] for code in
                   ("CF_OCC", "CF_DIR", "CF_POS", "CF_REL", "CF_LAG")},
                "serialized_characters": characters,
                "estimated_evidence_tokens": (characters + 3) // 4,
            })

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(jobs[0]))
        writer.writeheader()
        writer.writerows(jobs)
    audit_path = args.output / "selection_audit.csv"
    with audit_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(audit[0]))
        writer.writeheader()
        writer.writerows(audit)
    write_json(args.manifest.with_suffix(".meta.json"), {
        "job_count": len(jobs),
        "case_count": 26,
        "conditions": list(CONDITIONS),
        "qualification_seed": 20260910,
        "random_region_seeds": [202609151, 202609152, 202609153, 202609154, 202609155],
        "manifest_sha256": sha256_file(args.manifest),
        "prompt_sha256": prompt_hash,
        "source_root": workspace_path(args.source),
        "audit_path": workspace_path(audit_path),
    })
    print(f"Audited evidence files: {len(audit)}")
    print(f"Manifest jobs: {len(jobs)}")
    print(f"Manifest: {args.manifest}")
    print(f"Audit: {audit_path}")


if __name__ == "__main__":
    main()
