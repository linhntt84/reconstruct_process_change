#!/usr/bin/env python3
"""P0-C step 2: LLM generation on the tuning split (PAID API CALLS unless --dry-run).

Output per call: results/p0_llm_calibration/runs/<prompt>/<config>/<model>/run<k>/<case_id>.{json,md}
Resumes by skipping successful outputs. Stops the whole run on authentication or quota errors.

Example:
  python experiments/p0_llm_calibration/run_generation.py --config B --model glm-5.3-flash \
      --prompt prompts/INTERPRET_EVIDENCE_V2_EN.md --run-index 1 --limit 5
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pcr.llm import FatalAPIError, generate, load_config, load_dotenv, split_prompt  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402

OUT = RESULTS / "p0_llm_calibration"
LEVEL = re.compile(r"Support level:\s*(Insufficient evidence|Weak hypothesis|Supported hypothesis)", re.I)


def support_level(text: str | None) -> str:
    match = LEVEL.search(text or "")
    return match.group(1).lower() if match else "unparsed"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", choices=("A", "B"), default="B")
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt", type=Path, default=ROOT / "prompts" / "INTERPRET_EVIDENCE_V2_EN.md")
    parser.add_argument("--run-index", type=int, default=1)
    parser.add_argument("--kinds", nargs="+", default=["drift", "null"])
    parser.add_argument("--case-list", type=Path, help="optional file with one case_id per line")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    prompt = args.prompt if args.prompt.is_absolute() else (ROOT / args.prompt)
    split_prompt(prompt)  # validate sections
    with (OUT / f"cases_{args.config}.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["kind"] in args.kinds]
    if args.case_list:
        wanted = set(args.case_list.read_text().split())
        cases = [r for r in cases if r["case_id"] in wanted]
    if args.limit:
        cases = cases[:args.limit]
    run_dir = OUT / "runs" / prompt.stem / args.config / args.model / f"run{args.run_index}"
    todo = []
    for row in cases:
        target = run_dir / f"{row['case_id']}.json"
        if target.exists() and json.loads(target.read_text()).get("status") == "success":
            continue
        todo.append(row)
    print(f"{len(cases)} cases, {len(cases) - len(todo)} already done, {len(todo)} to call -> {run_dir}")
    if args.dry_run:
        total = sum(int(r["evidence_chars"]) for r in todo)
        print(f"dry run: about {total / 4:,.0f} evidence tokens + prompt per call; no API call made")
        return

    load_dotenv()
    config = load_config()
    run_dir.mkdir(parents=True, exist_ok=True)
    stop = threading.Event()

    def call(row):
        if stop.is_set():
            return row["case_id"], "skipped (stopped)"
        try:
            record = generate(prompt, ROOT / row["evidence_path"], args.model, config)
        except FatalAPIError as exc:
            stop.set()
            return row["case_id"], f"FATAL {exc}"
        except Exception as exc:  # recorded and retried on the next resume
            record = {"status": "failed", "error": str(exc)}
        record.update({"case_id": row["case_id"], "kind": row["kind"], "config": args.config,
                       "run_index": args.run_index, "support_level": support_level(record.get("text"))})
        (run_dir / f"{row['case_id']}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2),
                                                        encoding="utf-8")
        if record.get("text"):
            (run_dir / f"{row['case_id']}.md").write_text(record["text"], encoding="utf-8")
        return row["case_id"], f"{record['status']} {record['support_level']} {record.get('latency_seconds', '')}s"

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(call, row) for row in todo]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            print(f"[{done}/{len(todo)}] {cid} {status}", flush=True)
    if stop.is_set():
        sys.exit("stopped on a fatal API error (authentication or quota); fix it and rerun to resume")


if __name__ == "__main__":
    main()
