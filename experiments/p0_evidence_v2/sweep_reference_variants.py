#!/usr/bin/env python3
"""P0-A: compare W0 reference constructions on the tuning split (no LLM).

For each tuning case (Ostovar sizes 2 and 4, drift + null pairs) and one
reference mode (bootstrap = v1, permutation = v2 candidate), store:
  * Stage-1 DFG edges with rank counts (#ref < d, #ref <= d, B);
  * for the A* obtained at (tau_loc, eps_loc) = (0.99, 0.10) under each tie
    rule, every Stage-2 candidate with r, rank counts and the unit support in
    L- and L+.
Tie rule, tau and minimum support are then applied offline (analyze_variants.py).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))

from sweep_evidence import build_tasks, hardware, seed_for  # noqa: E402,F401
from pcr.logs import neutralize_windows, read_mxml  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402
from pcr.evidence.control_flow_indicators import CONTROL_FLOW_INDICATORS  # noqa: E402
from pcr.evidence.reference_windows import build_control_flow_context, common_analysis_universes  # noqa: E402
from pcr.evidence.qualification_v2 import (  # noqa: E402
    localization_rank_counts, qualification_rank_counts, reference_context_pairs, strength, support_table)

OUT = RESULTS / "p0_evidence_v2"
TAU_LOC, EPS_LOC = 0.99, 0.10
SIZES = {"2", "4"}


def run_pair(before, after, bs, seed, mode):
    pre, post, label_map = neutralize_windows(
        [{"activities": t} for t in before], [{"activities": t} for t in after], True)
    edges = localization_rank_counts(pre, post, bs, seed, EPS_LOC, mode)
    nonrel = {k: v for k, v in CONTROL_FLOW_INDICATORS.items() if k != "CF_REL"}
    base = common_analysis_universes(build_control_flow_context(pre, nonrel),
                                     build_control_flow_context(post, nonrel))
    regions = {}
    for ties in ("le", "lt"):
        region = sorted({a for e in edges if strength(e["lt"], e["le"], e["n"], ties) >= TAU_LOC
                         for a in (e["s"], e["t"])})
        regions.setdefault(json.dumps(region), []).append(ties)
    stage2 = {}
    for key in regions:
        rset = set(json.loads(key))
        universes = {k: list(v) for k, v in base.items()}
        universes["CF_POS"] = [u for u in universes["CF_POS"] if u in rset]
        universes["CF_REL"] = list(combinations(sorted(rset), 2))
        universes["CF_LAG"] = [u for u in universes["CF_LAG"] if u[0] in rset and u[1] in rset]
        before_ctx = build_control_flow_context(pre, CONTROL_FLOW_INDICATORS, universes)
        after_ctx = build_control_flow_context(post, CONTROL_FLOW_INDICATORS, universes)
        refs = reference_context_pairs(pre, post, CONTROL_FLOW_INDICATORS, universes, bs, seed, mode)
        items = qualification_rank_counts(before_ctx, after_ctx, CONTROL_FLOW_INDICATORS, refs)
        units = [(i["j"], i["u"]) for i in items]
        sb, sa = support_table(units, pre), support_table(units, post)
        for item in items:
            item["sb"], item["sa"] = sb[(item["j"], item["u"])], sa[(item["j"], item["u"])]
            if isinstance(item["u"], tuple):
                item["u"] = list(item["u"])
        stage2[key] = items
    return {"label_map": label_map, "edges": edges, "regions": regions, "stage2": stage2}


def job(task):
    target = Path(task["target"])
    if target.exists():
        return task["id"], "cached"
    started = time.perf_counter()
    traces = read_mxml(Path(task["log"]))
    a, w = task["anchor"], task["window"]
    result = run_pair(traces[a - w:a], traces[a:a + w], task["bs"], task["seed"], task["mode"])
    result.update({k: task[k] for k in ("id", "kind", "meta", "anchor", "window", "bs", "seed", "mode")})
    result["elapsed_seconds"] = round(time.perf_counter() - started, 2)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False))
    return task["id"], f"done {result['elapsed_seconds']}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", choices=("bootstrap", "permutation"), required=True)
    parser.add_argument("--window", type=int, default=200)
    parser.add_argument("--bs", type=int, default=100)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    tasks = [t for t in build_tasks("tuning", args.window, args.bs) if t["meta"]["fragment_size"] in SIZES]
    run = f"{args.reference}_w{args.window}_b{args.bs}"
    for task in tasks:
        task.update({"mode": args.reference, "target": str(OUT / "cache" / run / f"{task['id']}.json")})
    if args.limit:
        tasks = tasks[:args.limit]
    start_wall, start = datetime.now().astimezone(), time.perf_counter()
    computed = 0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(job, t) for t in tasks]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            computed += status.startswith("done")
            print(f"[{done}/{len(tasks)}] {cid} {status}", flush=True)
    if args.limit:
        return
    import csv
    row = {"run": run, "reference": args.reference, "window": args.window, "B_S": args.bs, "tasks": len(tasks),
           "computed": computed, "workers": args.workers, "start": start_wall.isoformat(timespec="seconds"),
           "end": datetime.now().astimezone().isoformat(timespec="seconds"),
           "wall_seconds": round(time.perf_counter() - start, 1),
           "sum_task_seconds": round(sum(json.loads(Path(t["target"]).read_text()).get("elapsed_seconds", 0)
                                         for t in tasks), 1),
           "hardware": hardware(), "source": "measured by sweep_reference_variants.py"}
    path = OUT / "runtime_log.csv"
    new = not path.exists()
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row))
        if new:
            writer.writeheader()
        writer.writerow(row)


if __name__ == "__main__":
    main()
