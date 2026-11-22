#!/usr/bin/env python3
"""E4a step 4 (P0b), part 2: LLM generation on the P0b evidence, with the unchanged prompt R3.

Same request settings and record format as experiments/p0_llm_calibration/run_generation.py
(pcr.llm.generate), output under results/e4a_time_injection/p0b/runs/<prompt>/<model>/run<k>/.
Resumes: cases with a successful record are skipped.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_RESULTS, REPO  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "p0_llm_calibration"))
from pcr.llm import FatalAPIError, generate, load_config, load_dotenv  # noqa: E402
from run_generation import support_level  # noqa: E402

DATA = E4_RESULTS / "e4a_time_injection"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--prompt", type=Path, default=REPO / "prompts" / "INTERPRET_EVIDENCE_V2_EN_R3.md")
    parser.add_argument("--set", default="p0b")
    parser.add_argument("--run-index", default="1")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--evidence-dir", type=Path, help="other evidence folder (e.g. control-flow regression); "
                        "default: <set>/evidence")
    parser.add_argument("--case-list", type=Path, help="optional file with one case_id per line")
    args = parser.parse_args()
    # Absolute paths inside the repository: pcr.llm.generate records them relative to the repo root
    # *after* the API call, so a bad path would waste a paid call. Check before calling.
    args.prompt = args.prompt.resolve()
    args.prompt.relative_to(REPO)
    if args.evidence_dir:
        args.evidence_dir = args.evidence_dir.resolve()
        args.evidence_dir.relative_to(REPO)
    from pcr.llm import split_prompt
    split_prompt(args.prompt)
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        kinds = {r["case_id"]: r["type"] for r in csv.DictReader(handle)}
    evidence_dir = args.evidence_dir or DATA / args.set / "evidence"
    evidence = sorted(evidence_dir.glob("*.json"))
    if args.case_list:
        wanted = set(args.case_list.read_text().split())
        evidence = [p for p in evidence if p.stem in wanted]
    for p in evidence:
        kinds.setdefault(p.stem, "null" if p.stem.startswith("null_") else "drift")
    run_dir = DATA / args.set / "runs" / args.prompt.stem / args.model / f"run{args.run_index}"
    run_dir.mkdir(parents=True, exist_ok=True)
    todo = [p for p in evidence if not ((run_dir / f"{p.stem}.json").exists() and
            json.loads((run_dir / f"{p.stem}.json").read_text()).get("status") == "success")]
    print(f"{len(evidence)} cases, {len(todo)} to call -> {run_dir}", flush=True)
    load_dotenv()
    config = load_config()

    def call(path: Path):
        try:
            record = generate(args.prompt, path, args.model, config)
        except FatalAPIError as exc:
            return path.stem, f"FATAL {exc}"
        except Exception as exc:
            record = {"status": "failed", "error": str(exc)}
        record.update({"case_id": path.stem, "kind": kinds[path.stem], "run_index": args.run_index,
                       "support_level": support_level(record.get("text"))})
        (run_dir / f"{path.stem}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        if record.get("text"):
            (run_dir / f"{path.stem}.md").write_text(record["text"], encoding="utf-8")
        return path.stem, f"{record['status']} {record['support_level']} {record.get('latency_seconds', '')}s"

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(call, p) for p in todo]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            print(f"[{done}/{len(todo)}] {cid} {kinds[cid]} {status}", flush=True)


if __name__ == "__main__":
    main()
