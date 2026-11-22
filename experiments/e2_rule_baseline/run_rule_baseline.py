#!/usr/bin/env python3
"""E2: rule-based (non-LLM) interpretation of the same pipeline-v2 evidence the LLM receives,
scored with the same blind extractor, rubric and metrics as the LLM.

The interpretation rules are the version-1 engine (`engine_v1.py`, copied verbatim from the
submitted study, SHA-256 recorded in the README); rules and thresholds are unchanged.
A thin v2 wrapper adds two things, fixed before any scoring:
  1. screening, the same principle the LLM prompt (R3) states: if the number of evidence
     items is not clearly larger than the number expected without change, the output is
     "Insufficient evidence". Concrete rule: n_items <= max(2, 3 * items_expected_without_change);
  2. the same output frame as the LLM ("### Observed differences", "### Inference",
     "Support level: ..."), so that the extractor reads both kinds of output the same way.
The baseline never sees case ids of the source, references or the dataset name.

Output records mirror the LLM generation records, so `run_extraction.py` and `score.py`
work unchanged: results/p0_llm_calibration/runs/RULE_BASELINE_V2/<config>/rule-engine-v1/run1/
(or another results folder via --out).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "src"))
import engine_v1  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402

NAME = "RULE_BASELINE_V2"
MODEL = "rule-engine-v1"
INSUFFICIENT = "The evidence is insufficient to infer a structural change in the process."


def screened_out(n_items: int, expected: float) -> bool:
    return n_items <= max(2.0, 3.0 * expected)


def render(document: dict) -> tuple[str, str, dict]:
    items = document.get("evidence", [])
    expected = float(document.get("screening", {}).get("items_expected_without_change", 0.0))
    result = engine_v1.interpret(items)
    lines = ["### Observed differences", ""]
    if not items:
        lines.append("The evidence establishes no behavioural difference at the configured thresholds.")
    else:
        lines += [f"- {o['text']} [{o['evidence_id']}]" for o in result["observations"]]
        lines.append(f"- {len(items)} evidence items qualified; about {expected:.2f} would be expected "
                     "without any change.")
    lines += ["", "### Inference", ""]
    if not items:
        level = "insufficient evidence"
        lines += ["Support level: Insufficient evidence", "", "No inference can be made."]
    elif screened_out(len(items), expected) or not result["claims"]:
        level = "insufficient evidence"
        lines += ["Support level: Insufficient evidence", "", INSUFFICIENT]
    else:
        level = "supported hypothesis"
        lines += ["Support level: Supported hypothesis", ""]
        lines += [f"- {c['explanation']} [{', '.join(c['evidence_ids'])}]" for c in result["claims"]]
        lines += ["", "Rule matches are hypotheses based on the qualified evidence, not proof of the "
                  "underlying process edit; several matches may reflect one change."]
    return "\n".join(lines) + "\n", level, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-dir", type=Path, default=RESULTS / "p0_llm_calibration" / "evidence" / "B")
    parser.add_argument("--case-list", type=Path, help="optional file with one case_id per line")
    parser.add_argument("--out", type=Path, default=RESULTS / "p0_llm_calibration" / "runs" / NAME / "B" / MODEL / "run1")
    args = parser.parse_args()
    files = sorted(args.evidence_dir.glob("*.json"))
    if args.case_list:
        wanted = {line.strip().split("/")[-1] for line in args.case_list.read_text().splitlines() if line.strip()}
        files = [f for f in files if f.stem in wanted]
    args.out.mkdir(parents=True, exist_ok=True)
    engine_sha = hashlib.sha256((HERE / "engine_v1.py").read_bytes()).hexdigest()
    counts = {}
    for path in files:
        document = json.loads(path.read_text(encoding="utf-8"))
        text, level, result = render(document)
        record = {"status": "success", "model": MODEL, "engine_version": result["version"],
                  "engine_sha256": engine_sha, "engine_config": result["config"],
                  "screening_rule": "n_items <= max(2, 3 * items_expected_without_change)",
                  "evidence_path": str(path.relative_to(ROOT)),
                  "evidence_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                  "finished_at_utc": datetime.now(timezone.utc).isoformat(),
                  "n_items": len(document.get("evidence", [])), "n_claims": len(result["claims"]),
                  "rule_ids": sorted({c["rule_id"] for c in result["claims"]}),
                  "text": text, "case_id": path.stem, "config": args.out.parents[1].name,
                  "run_index": "1", "support_level": level}
        (args.out / f"{path.stem}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        (args.out / f"{path.stem}.md").write_text(text, encoding="utf-8")
        counts[level] = counts.get(level, 0) + 1
    print(f"{len(files)} cases -> {args.out}: {counts}")


if __name__ == "__main__":
    main()
