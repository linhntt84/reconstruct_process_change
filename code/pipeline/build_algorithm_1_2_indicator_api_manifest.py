#!/usr/bin/env python3
"""Build per-indicator E* API inputs and an immutable 130-job manifest."""

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
DEFAULT_SOURCE = EXPERIMENT / "artifacts/official/ostovar_atomic_b200_dir_gated_pos_rel_lag/evidence/tau_mixed"
DEFAULT_PROMPT = EXPERIMENT / "prompts/INTERPRET_EVIDENCE_V1_VI.md"
DEFAULT_OUTPUT = EXPERIMENT / "artifacts/api/ostovar_atomic_b200_algorithm_1_2_per_indicator_v1"
INDICATORS = ("CF_OCC", "CF_DIR", "CF_POS", "CF_REL", "CF_LAG")
TAU_BY_INDICATOR = {
    "CF_OCC": 0.95,
    "CF_DIR": 0.99,
    "CF_POS": 0.99,
    "CF_REL": 0.99,
    "CF_LAG": 0.99,
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_to_workspace(path: Path) -> str:
    return str(path.resolve().relative_to(WORKSPACE.resolve()))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--run-id", default="ieee_access_ostovar_b200_algorithm_1_2_per_indicator_v1")
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--provider", default="INT2")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--max-completion-tokens", type=int, default=0)
    args = parser.parse_args()

    sources = sorted(args.source.glob("*.json"))
    if len(sources) != 26:
        raise SystemExit(f"Expected 26 source cases, found {len(sources)}")
    prompt_hash = sha256_file(args.prompt)
    prompt_path = relative_to_workspace(args.prompt)
    jobs = []
    for source_path in sources:
        source = json.loads(source_path.read_text(encoding="utf-8"))
        case_id = source["case"]["case_id"]
        for indicator in INDICATORS:
            short = indicator[3:] if indicator.startswith("CF_") else indicator
            selected = [item for item in source["evidence"] if item["indicator"] == indicator]
            tau = TAU_BY_INDICATOR[indicator]
            below_tau = [item["id"] for item in selected if float(item["empirical_strength"]) < tau]
            if below_tau:
                raise AssertionError(f"{case_id} {indicator} contains evidence below tau {tau}: {below_tau}")
            payload = {
                "schema_version": "ieee-access-structured-evidence-per-indicator-1.0",
                "case": source["case"],
                "condition": {
                    "indicator": indicator,
                    "qualification_tau": tau,
                    "reference_pairs_B": 200,
                    "evidence_count": len(selected),
                },
                "evidence": selected,
            }
            evidence_path = args.output / "evidence" / short / f"{case_id}.json"
            write_json(evidence_path, payload)
            jobs.append({
                "run_id": args.run_id,
                "paper_scope": "IEEE_ACCESS",
                "dataset": "synthetic_process_log",
                "case_id": case_id,
                "condition": f"{short}_ONLY",
                "window_condition": "WINDOW_ORACLE_STABLE",
                "prompt_path": prompt_path,
                "prompt_hash": prompt_hash,
                "schema_version": payload["schema_version"],
                "evidence_path": relative_to_workspace(evidence_path),
                "evidence_hash": sha256_file(evidence_path),
                "model": args.model,
                "provider": args.provider,
                "temperature": args.temperature,
                "top_p": args.top_p,
                "max_completion_tokens": args.max_completion_tokens or "",
                "seed_if_supported": "",
                "expected_output_format": "markdown",
            })

    manifest = args.output / "manifest.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(jobs[0]))
        writer.writeheader()
        writer.writerows(jobs)
    write_json(args.output / "manifest.meta.json", {
        "job_count": len(jobs),
        "case_count": len(sources),
        "conditions": [f"{code[3:] if code.startswith('CF_') else code}_ONLY" for code in INDICATORS],
        "manifest_sha256": sha256_file(manifest),
        "prompt_sha256": prompt_hash,
    })
    print(f"Per-indicator E* files: {len(jobs)}")
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
