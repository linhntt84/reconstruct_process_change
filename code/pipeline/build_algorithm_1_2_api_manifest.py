#!/usr/bin/env python3
"""Build public E* API inputs and an immutable manifest for 26 Ostovar cases."""

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
DEFAULT_OUTPUT = EXPERIMENT / "artifacts/api/ostovar_atomic_b200_algorithm_1_2_v1"


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
    parser.add_argument("--run-id", default="ieee_access_ostovar_b200_algorithm_1_2_v1")
    parser.add_argument(
        "--window-condition", default="WINDOW_ORACLE_STABLE",
        help="Provenance label for the supplied pre/post windows.",
    )
    parser.add_argument(
        "--expected-cases", type=int, default=26,
        help="Required number of source evidence files (default: 26 for the Atomic benchmark).",
    )
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--provider", default="INT2")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument(
        "--max-completion-tokens", type=int, default=0,
        help="0 omits max_tokens so the provider/model limit applies",
    )
    args = parser.parse_args()

    source_files = sorted(args.source.glob("*.json"))
    if len(source_files) != args.expected_cases:
        raise SystemExit(
            f"Expected {args.expected_cases} source cases, found {len(source_files)} in {args.source}"
        )
    if not args.prompt.is_file():
        raise SystemExit(f"Prompt not found: {args.prompt}")

    input_dir = args.output / "evidence"
    jobs = []
    prompt_path = relative_to_workspace(args.prompt)
    prompt_hash = sha256_file(args.prompt)
    for source_path in source_files:
        source = json.loads(source_path.read_text(encoding="utf-8"))
        case_id = source["case"]["case_id"]
        public_payload = {
            "schema_version": "ieee-access-structured-evidence-1.1",
            "case": source["case"],
            "evidence": source["evidence"],
        }
        evidence_path = input_dir / f"{case_id}.json"
        write_json(evidence_path, public_payload)
        jobs.append({
            "run_id": args.run_id,
            "paper_scope": "IEEE_ACCESS",
            "dataset": source["case"].get("dataset", "process_log"),
            "case_id": case_id,
            "condition": "ALGORITHM_1_2_E_STAR",
            "window_condition": args.window_condition,
            "prompt_path": prompt_path,
            "prompt_hash": prompt_hash,
            "schema_version": public_payload["schema_version"],
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
        "manifest_sha256": sha256_file(manifest),
        "prompt_sha256": prompt_hash,
        "source_directory": relative_to_workspace(args.source),
    })
    print(f"Public E* files: {len(source_files)}")
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
