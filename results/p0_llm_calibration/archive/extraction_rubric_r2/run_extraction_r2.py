#!/usr/bin/env python3
"""P0-C step 3: blind extraction of generated explanations with Claude (claude -p).

Uses the claude.ai subscription of the logged-in Claude Code user; never enables extra
usage. On a usage limit it waits until the reported reset (or 30 minutes) and resumes.
Outputs mirror the generation tree under results/p0_llm_calibration/extractions/<variant>/.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pcr.extract import UsageLimitReached, extract  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402

OUT = RESULTS / "p0_llm_calibration"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=Path, required=True,
                        help="generation directory, e.g. results/p0_llm_calibration/runs/INTERPRET_EVIDENCE_V2_EN/B")
    parser.add_argument("--variant", choices=("main", "vocab_free"), default="main")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--case-list", type=Path, help="text file of <model>/<case_id> lines to extract")
    parser.add_argument("--pause", type=float, default=2.0, help="seconds between calls")
    parser.add_argument("--max-wait-hours", type=float, default=6.0)
    args = parser.parse_args()
    runs = args.runs if args.runs.is_absolute() else ROOT / args.runs
    sources = sorted(p for p in runs.rglob("*.json") if json.loads(p.read_text()).get("status") == "success")
    jobs = []
    for source in sources:
        target = OUT / "extractions" / args.variant / source.relative_to(OUT / "runs")
        if not target.exists():
            jobs.append((source, target))
    if args.case_list:
        wanted = {line.strip() for line in args.case_list.read_text().splitlines() if line.strip()}
        jobs = [j for j in jobs if f"{j[0].parent.parent.name}/{j[0].stem}" in wanted]
    if args.limit:
        jobs = jobs[:args.limit]
    print(f"{len(sources)} explanations, {len(jobs)} to extract ({args.variant})", flush=True)
    waited = 0.0
    index = 0
    while index < len(jobs):
        source, target = jobs[index]
        record = json.loads(source.read_text(encoding="utf-8"))
        try:
            result = extract(record["text"], args.variant)
        except UsageLimitReached as exc:
            delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
            waited += delay
            if waited > args.max_wait_hours * 3600:
                sys.exit(f"usage limit; waited {waited / 3600:.1f} h in total, stopping. Rerun to resume.")
            print(f"{datetime.now():%H:%M} usage limit ({exc}); waiting {delay / 60:.0f} min", flush=True)
            time.sleep(delay)
            continue
        except Exception as exc:
            print(f"[{index + 1}/{len(jobs)}] error {source.name}: {exc}", flush=True)
            index += 1
            continue
        result.update({"source": str(source.relative_to(ROOT)), "case_id": record["case_id"],
                       "generation_model": record["model"], "run_index": record["run_index"]})
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{index + 1}/{len(jobs)}] {source.parent.parent.name}/{source.stem} "
              f"{result['extraction']['support_level']} {result['latency_seconds']}s", flush=True)
        index += 1
        time.sleep(args.pause)


if __name__ == "__main__":
    main()
