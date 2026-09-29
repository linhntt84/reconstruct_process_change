#!/usr/bin/env python3
"""Clone a frozen IEEE Access manifest for a second interpretation model."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[3]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_workspace_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else WORKSPACE / path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--provider", default=None)
    args = parser.parse_args()

    source = args.source_manifest.resolve()
    if not source.is_file():
        raise SystemExit(f"Source manifest not found: {source}")

    with source.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        fieldnames = reader.fieldnames
        rows = list(reader)
    if not fieldnames or not rows:
        raise SystemExit("Source manifest is empty")

    for row in rows:
        prompt_path = resolve_workspace_path(row["prompt_path"])
        evidence_path = resolve_workspace_path(row["evidence_path"])
        if sha256_file(prompt_path) != row["prompt_hash"]:
            raise SystemExit(f"Prompt hash mismatch: {prompt_path}")
        if sha256_file(evidence_path) != row["evidence_hash"]:
            raise SystemExit(f"Evidence hash mismatch: {evidence_path}")
        row["run_id"] = args.run_id
        row["model"] = args.model
        if args.provider is not None:
            row["provider"] = args.provider

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing manifest: {output}")
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    metadata = {
        "job_count": len(rows),
        "model": args.model,
        "provider": args.provider or rows[0]["provider"],
        "source_manifest": str(source.relative_to(WORKSPACE)),
        "source_manifest_sha256": sha256_file(source),
        "manifest_sha256": sha256_file(output),
        "invariant_fields": [
            "case_id", "condition", "window_condition", "prompt_path",
            "prompt_hash", "evidence_path", "evidence_hash", "temperature",
            "top_p", "max_completion_tokens", "expected_output_format",
        ],
    }
    meta_path = output.with_suffix(".meta.json")
    meta_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Cloned {len(rows)} jobs to {output}")
    print(f"Manifest SHA-256: {metadata['manifest_sha256']}")


if __name__ == "__main__":
    main()
