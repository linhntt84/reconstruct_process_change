#!/usr/bin/env python3
"""P0-B: E0 grid re-run under evidence qualification v2 (no LLM).

v2 = permutation reference W0 + conservative ties (q = #ref < r / (B+1)).
Writes caches in the E0 format (field ``q`` holds the v2 strength) so that
``experiments/e0_parameter_setting/analyze_grid.py --cache-suffix _v2perm``
applies the same pre-registered selection rule. Rank counts (lt/le) and unit
support (sb/sa) are kept as extra fields.
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

from sweep_evidence import EPS_LOC_GRID, TAU_LOC_GRID, build_tasks, hardware, log_runtime  # noqa: E402
from pcr.logs import neutralize_windows, read_mxml  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402
from pcr.evidence.algorithm_1_change_localization_and_qualification import QualifiedChange  # noqa: E402
from pcr.evidence.algorithm_2_evidence_construction_from_qualified_changes import (  # noqa: E402
    algorithm_2_evidence_construction_from_qualified_changes)
from pcr.evidence.control_flow_indicators import CONTROL_FLOW_INDICATORS  # noqa: E402
from pcr.evidence.reference_windows import build_control_flow_context, common_analysis_universes  # noqa: E402
from pcr.evidence.qualification_v2 import (  # noqa: E402
    localization_rank_counts, qualification_rank_counts, reference_context_pairs, strength, support_table)

E0_CACHE = RESULTS / "e0_parameter_setting" / "cache" / "tuning"
SIZES = {"2", "4"}
TIES = "lt"


def run_pair(before, after, bs, seed, mode):
    pre, post, label_map = neutralize_windows(
        [{"activities": t} for t in before], [{"activities": t} for t in after], True)
    raw_edges = localization_rank_counts(pre, post, bs, seed, min(EPS_LOC_GRID), mode)
    edges = [{**e, "q": strength(e["lt"], e["le"], e["n"], TIES)} for e in raw_edges]
    nonrel = {k: v for k, v in CONTROL_FLOW_INDICATORS.items() if k != "CF_REL"}
    base = common_analysis_universes(build_control_flow_context(pre, nonrel),
                                     build_control_flow_context(post, nonrel))
    regions = {}
    for tau_loc in TAU_LOC_GRID:
        for eps_loc in EPS_LOC_GRID:
            region = sorted({a for e in edges if e["q"] >= tau_loc and e["d"] >= eps_loc for a in (e["s"], e["t"])})
            regions.setdefault(json.dumps(region), []).append([tau_loc, eps_loc])
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
        for item in items:
            item["q"] = strength(item["lt"], item["le"], item["n"], TIES)
        changes = [QualifiedChange(i["j"], i["u"], i["r"], i["q"], i["n"]) for i in items]
        built = algorithm_2_evidence_construction_from_qualified_changes(
            before_ctx, after_ctx, changes, CONTROL_FLOW_INDICATORS)
        units = [(i["j"], i["u"]) for i in items]
        sb, sa = support_table(units, pre), support_table(units, post)
        for item, ev in zip(items, built):
            item["sb"], item["sa"] = sb[(item["j"], item["u"])], sa[(item["j"], item["u"])]
            item["chars"] = len(json.dumps(ev, ensure_ascii=False, indent=2))
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
    a, w, g = task["anchor"], task["window"], task.get("guard", 0)
    result = run_pair(traces[a - g - w:a - g], traces[a + g:a + g + w], task["bs"], task["seed"], task["mode"])
    result.update({k: task[k] for k in ("id", "kind", "meta", "anchor", "window", "bs", "seed", "mode")})
    result["ties"] = TIES
    result["elapsed_seconds"] = round(time.perf_counter() - started, 2)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False))
    return task["id"], f"done {result['elapsed_seconds']}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", choices=("bootstrap", "permutation"), default="permutation")
    parser.add_argument("--window", type=int, default=200)
    parser.add_argument("--bs", type=int, default=100)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--guard", type=int, default=50, help="guard band g around the change point (v1: 0)")
    args = parser.parse_args()
    suffix = {"permutation": "_v2perm", "bootstrap": "_v2boot"}[args.reference]
    if args.guard:
        suffix += f"_g{args.guard}"
    run = f"w{args.window}_b{args.bs}{suffix}"
    tasks = [t for t in build_tasks("tuning", args.window, args.bs) if t["meta"]["fragment_size"] in SIZES]
    for task in tasks:
        task.update({"mode": args.reference, "guard": args.guard,
                     "target": str(E0_CACHE / run / f"{task['id']}.json")})
        if task["kind"] == "null":  # same geometry inside the stable prefix: L+ ends at trace 850
            task["anchor"] = 850 - args.guard - args.window
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
    log_runtime({
        "run": run, "mode": "tuning (sizes 2,4)", "window": args.window, "B_S": args.bs,
        "localization_grid": f"4x4, v2 {args.reference} + ties {TIES}, guard {args.guard}", "tasks": len(tasks),
        "computed": computed, "workers": args.workers, "start": start_wall.isoformat(timespec="seconds"),
        "end": datetime.now().astimezone().isoformat(timespec="seconds"),
        "wall_seconds": round(time.perf_counter() - start, 1),
        "sum_task_seconds": round(sum(json.loads(Path(t["target"]).read_text()).get("elapsed_seconds", 0)
                                      for t in tasks), 1),
        "hardware": hardware(), "source": "measured by p0_evidence_v2/sweep_grid_v2.py"})


if __name__ == "__main__":
    main()
