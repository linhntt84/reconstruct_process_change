#!/usr/bin/env python3
"""P2 steps 2-3: LLM generation (PAID API CALLS) and blind extraction with rubric r5 (Claude, claude -p).

  python experiments/p2_main/run_p2.py generate --model glm-5.3-flash [--sets ostovar3 ...] [--dry-run]
  python experiments/p2_main/run_p2.py extract --runs results/p2_main/runs/<prompt>/<model>/run1 \
         [--sets ostovar3] [--kinds drift] [--limit N]

Generation: frozen prompt R3-MP-CONC, request settings of configs/llm_generation.json (pcr.llm.generate),
one record per case in results/p2_main/runs/<prompt>/<model>/run<k>/<case_id>.{json,md}; resumes by
skipping successful records; stops on authentication or quota errors.
Extraction: e4_multiperspective/code/extract_e4.extract_r5 (rubric r5 = r3 + time/resource fields), output
results/p2_main/extractions_r5/<prompt>/<model>/run<k>/<case_id>.json; waits on usage limits and resumes.
The extractor sees only the explanation text.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p0_llm_calibration"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))
sys.path.insert(0, str(HERE))

OUT = ROOT / "results" / "p2_main"
PROMPT = ROOT / "e4_multiperspective" / "code" / "prompts" / "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC.md"


def load_cases(sets, kinds) -> list[dict]:
    with (OUT / "cases.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return [r for r in rows if (not sets or r["set"] in sets) and (not kinds or r["kind"] in kinds)]


def generate_all(args):
    from pcr.llm import FatalAPIError, generate, load_config, load_dotenv, split_prompt
    from run_generation import support_level
    split_prompt(PROMPT)
    cases = load_cases(args.sets, args.kinds)
    if args.case:
        cases = [r for r in cases if r["case_id"] in args.case]
    if args.limit:
        cases = cases[:args.limit]
    run_dir = OUT / "runs" / PROMPT.stem / args.model / f"run{args.run_index}"
    todo = [r for r in cases if not ((run_dir / f"{r['case_id']}.json").exists() and json.loads(
        (run_dir / f"{r['case_id']}.json").read_text()).get("status") == "success")]
    print(f"{len(cases)} cases, {len(todo)} to call -> {run_dir}", flush=True)
    if args.dry_run:
        print(f"dry run: about {sum(int(r['evidence_chars']) for r in todo) / 4:,.0f} evidence tokens; no API call")
        return
    load_dotenv()
    if args.key_env:  # models without a prefix entry in configs/llm_generation.json (e.g. Qwen, E6)
        import os
        os.environ[load_config()["fallback_api_key_env"]] = os.environ[args.key_env]
    config = load_config()
    if args.drop_request:  # provider-specific: e.g. Qwen via litellm rejects "thinking" (reasoning on by default)
        for key in args.drop_request:
            config["request"].pop(key, None)
    run_dir.mkdir(parents=True, exist_ok=True)
    stop = threading.Event()

    def call(row):
        if stop.is_set():
            return row["case_id"], "skipped (stopped)"
        try:
            if args.stream:
                from stream_generate import generate_stream
                record = generate_stream(PROMPT, ROOT / row["evidence_path"], args.model, config)
            else:
                record = generate(PROMPT, ROOT / row["evidence_path"], args.model, config)
        except FatalAPIError as exc:
            stop.set()
            return row["case_id"], f"FATAL {exc}"
        except Exception as exc:  # recorded; retried on the next resume
            record = {"status": "failed", "error": str(exc)}
        record.update({"case_id": row["case_id"], "set": row["set"], "kind": row["kind"],
                       "run_index": args.run_index, "spec_version": "2.0", "key_env": args.key_env or "",
                       "support_level": support_level(record.get("text"))})
        (run_dir / f"{row['case_id']}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2),
                                                        encoding="utf-8")
        if record.get("text"):
            (run_dir / f"{row['case_id']}.md").write_text(record["text"], encoding="utf-8")
        return row["case_id"], f"{row['set']} {record['status']} {record['support_level']} " \
                               f"{record.get('latency_seconds', '')}s"

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(call, r) for r in todo]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            print(f"[{done}/{len(todo)}] {cid} {status}", flush=True)
    if stop.is_set():
        sys.exit("stopped on a fatal API error (authentication or quota); fix it and rerun to resume")


def extract_all(args):
    from extract_e4 import UsageLimitReached, extract_r5
    runs = args.runs if args.runs.is_absolute() else ROOT / args.runs
    wanted = {r["case_id"] for r in load_cases(args.sets, args.kinds)}
    order = [r["case_id"] for r in load_cases(args.sets, args.kinds)]
    jobs = []
    for cid in order:
        source = runs / f"{cid}.json"
        if cid not in wanted or not source.exists() or json.loads(source.read_text()).get("status") != "success":
            continue
        target = OUT / "extractions_r5" / runs.relative_to(OUT / "runs") / f"{cid}.json"
        if not target.exists():
            jobs.append((source, target))
    if args.limit:
        jobs = jobs[:args.limit]
    print(f"{len(jobs)} explanations to extract (rubric r5)", flush=True)
    waited, index = 0.0, 0
    while index < len(jobs):
        source, target = jobs[index]
        record = json.loads(source.read_text(encoding="utf-8"))
        try:
            result = extract_r5(record["text"])
        except UsageLimitReached as exc:
            delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
            waited += delay
            if waited > args.max_wait_hours * 3600:
                sys.exit(f"usage limit; waited {waited / 3600:.1f} h, stopping. Rerun to resume.")
            print(f"{datetime.now():%H:%M} usage limit ({exc}); waiting {delay / 60:.0f} min", flush=True)
            time.sleep(delay)
            continue
        except Exception as exc:
            print(f"[{index + 1}/{len(jobs)}] error {source.stem}: {exc}", flush=True)
            index += 1
            continue
        result.update({"source": str(source.relative_to(ROOT)), "case_id": record["case_id"],
                       "generation_model": record.get("model"), "run_index": record.get("run_index")})
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{index + 1}/{len(jobs)}] {source.stem} {result['extraction']['support_level']} "
              f"{result['latency_seconds']}s", flush=True)
        index += 1
        time.sleep(args.pause)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("--model", required=True)
    g.add_argument("--run-index", type=int, default=1)
    g.add_argument("--workers", type=int, default=4)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--key-env", default="", help="env var holding the API key for models without a prefix entry")
    g.add_argument("--stream", action="store_true", help="streaming transport (gateway 120 s limit), E6")
    g.add_argument("--drop-request", nargs="*", default=[], help="request settings to omit for this model")
    g.add_argument("--case", nargs="*", default=[], help="only these case ids")
    e = sub.add_parser("extract")
    e.add_argument("--runs", type=Path, required=True)
    e.add_argument("--pause", type=float, default=2.0)
    e.add_argument("--max-wait-hours", type=float, default=8.0)
    for p in (g, e):
        p.add_argument("--sets", nargs="*", default=[])
        p.add_argument("--kinds", nargs="*", default=[])
        p.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    generate_all(args) if args.cmd == "generate" else extract_all(args)


if __name__ == "__main__":
    main()
