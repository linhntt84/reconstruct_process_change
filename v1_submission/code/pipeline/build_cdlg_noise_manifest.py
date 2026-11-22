#!/usr/bin/env python3
"""Build a paired API manifest for the CDLG 5% and 10% noise conditions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
WORKSPACE = EXPERIMENT.parents[1]
DEFAULT_PROMPT = EXPERIMENT / "prompts/INTERPRET_EVIDENCE_V1_VI.md"
DEFAULT_OUTPUT = EXPERIMENT / "artifacts/api/cdlg_noise_5_10_b200_tau_0p99_one_per_log100_v1"
DEFAULT_MANIFEST = EXPERIMENT / "manifests/cdlg_noise_5_10_b200_tau_0p99_one_per_log100_v1.csv"
SOURCES = {
    "NOISE_5": EXPERIMENT / "artifacts/official/cdlg_noise_5_b200_tau_0p99_one_per_log100_v1/evidence/tau_p99",
    "NOISE_10": EXPERIMENT / "artifacts/official/cdlg_noise_10_b200_tau_0p99_one_per_log100_v1/evidence/tau_p99",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def workspace_path(path: Path) -> str:
    return str(path.resolve().relative_to(WORKSPACE.resolve()))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--run-id", default="ieee_access_cdlg_noise_5_10_b200_tau_0p99_v1")
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--provider", default="INT2")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    args = parser.parse_args()

    prompt_hash = sha256_file(args.prompt)
    jobs: list[dict[str, Any]] = []
    for condition, source_dir in SOURCES.items():
        files = sorted(source_dir.glob("*.json"))
        if len(files) != 100:
            raise SystemExit(f"{condition}: expected 100 evidence files, found {len(files)}")
        for source_path in files:
            source = json.loads(source_path.read_text(encoding="utf-8"))
            case_id = source["case"]["case_id"]
            public = {
                "schema_version": "ieee-access-structured-evidence-1.1",
                "case": source["case"],
                "evidence": source["evidence"],
            }
            evidence_path = args.output / "evidence" / condition.lower() / source_path.name
            write_json(evidence_path, public)
            jobs.append({
                "run_id": args.run_id,
                "paper_scope": "IEEE_ACCESS",
                "dataset": "CDLG",
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

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(jobs[0]))
        writer.writeheader()
        writer.writerows(jobs)
    write_json(args.manifest.with_suffix(".meta.json"), {
        "job_count": len(jobs),
        "paired_clean_case_count": 100,
        "conditions": list(SOURCES),
        "reference_pairs": 200,
        "tau": 0.99,
        "manifest_sha256": sha256_file(args.manifest),
        "prompt_sha256": prompt_hash,
        "sources": {name: workspace_path(path) for name, path in SOURCES.items()},
    })
    print(f"Jobs: {len(jobs)}")
    print(f"Manifest: {args.manifest}")


if __name__ == "__main__":
    main()
