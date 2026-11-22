#!/usr/bin/env python3
"""E0 sweep cache: run Stages 1-2 once per case with zero threshold floors.

For each case it stores every Stage-1 DFG edge candidate (change, q) and, for
every distinct A* produced by the (tau_loc, eps_loc) grid, every Stage-2
candidate (indicator, unit, r, q, serialized size). Any (tau_j, eps_j) can then
be applied offline without re-running the bootstrap. No LLM calls.

Modes:
  tuning  held-out Ostovar fragment sizes (tuning_references.csv) + null pairs
  size3   evaluated Ostovar size 3, official seeds (adapter check / description)
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_tuning_references import FROZEN_SIZE3, OUT  # noqa: E402
from pcr.logs import neutralize_windows, read_mxml  # noqa: E402
from pcr.paths import OSTOVAR_FULL  # noqa: E402
from pcr.evidence.control_flow_indicators import CONTROL_FLOW_INDICATORS  # noqa: E402
from pcr.evidence.reference_windows import (  # noqa: E402
    bootstrap_reference_context_pairs, build_control_flow_context, common_analysis_universes)
from pcr.evidence.relational_candidate_gate import (  # noqa: E402
    qualify_relational_candidate_activities_from_directly_follows)
from pcr.evidence import (  # noqa: E402
    algorithm_1_change_localization_and_qualification,
    algorithm_2_evidence_construction_from_qualified_changes)

TAU_LOC_GRID = (0.95, 0.975, 0.99, 0.995)
EPS_LOC_GRID = (0.05, 0.10, 0.15, 0.20)
NOISE_SUFFIX = {"0": "", "2.5": "_2", "5": "_5"}
OFFICIAL_SEED = 20260910


def seed_for(key: str) -> int:
    return 20261111 + int(hashlib.sha256(key.encode()).hexdigest()[:8], 16)


def run_pair(before, after, bs, seed, loc_grid=None):
    pre, post, label_map = neutralize_windows(
        [{"activities": t} for t in before], [{"activities": t} for t in after], True)
    gate = qualify_relational_candidate_activities_from_directly_follows(
        pre, post, bs, seed, tau=0.0, minimum_support_change=min(EPS_LOC_GRID))
    edges = [{"s": e["source"], "t": e["target"], "d": e["absolute_change"], "q": e["empirical_strength"]}
             for e in gate.qualified_edges]
    nonrel = {k: v for k, v in CONTROL_FLOW_INDICATORS.items() if k != "CF_REL"}
    base_universes = common_analysis_universes(build_control_flow_context(pre, nonrel),
                                               build_control_flow_context(post, nonrel))
    regions = {}
    for tau_loc, eps_loc in (loc_grid or [(t, e) for t in TAU_LOC_GRID for e in EPS_LOC_GRID]):
        if True:
            region = sorted({a for e in edges if e["q"] >= tau_loc and e["d"] >= eps_loc
                             for a in (e["s"], e["t"])})
            regions.setdefault(json.dumps(region), []).append([tau_loc, eps_loc])
    stage2 = {}
    for key in regions:
        region = json.loads(key)
        rset = set(region)
        universes = {k: list(v) for k, v in base_universes.items()}
        universes["CF_POS"] = [u for u in universes["CF_POS"] if u in rset]
        universes["CF_REL"] = list(combinations(region, 2))
        universes["CF_LAG"] = [u for u in universes["CF_LAG"] if u[0] in rset and u[1] in rset]
        before_ctx = build_control_flow_context(pre, CONTROL_FLOW_INDICATORS, universes)
        after_ctx = build_control_flow_context(post, CONTROL_FLOW_INDICATORS, universes)
        refs = bootstrap_reference_context_pairs(pre, post, CONTROL_FLOW_INDICATORS, universes, bs, seed)
        changes = algorithm_1_change_localization_and_qualification(
            before_ctx, after_ctx, CONTROL_FLOW_INDICATORS, refs,
            {k: 0.0 for k in CONTROL_FLOW_INDICATORS},
            minimum_observed_change={k: 0.0 for k in CONTROL_FLOW_INDICATORS})
        items = algorithm_2_evidence_construction_from_qualified_changes(
            before_ctx, after_ctx, changes, CONTROL_FLOW_INDICATORS)
        sizes = [len(json.dumps(item, ensure_ascii=False, indent=2)) for item in items]
        stage2[key] = [{"j": c.indicator, "u": list(c.analysis_unit) if isinstance(c.analysis_unit, tuple)
                        else c.analysis_unit, "r": c.observed_change, "q": c.empirical_strength,
                        "n": c.reference_count, "chars": size}
                       for c, size in zip(changes, sizes)]
    return {"label_map": label_map, "edges": edges, "regions": regions, "stage2": stage2}


def job(task):
    target = Path(task["target"])
    if target.exists():
        return task["id"], "cached"
    started = time.perf_counter()
    traces = read_mxml(Path(task["log"]))
    a, w = task["anchor"], task["window"]
    result = run_pair(traces[a - w:a], traces[a:a + w], task["bs"], task["seed"], task.get("loc_grid"))
    result.update({k: task[k] for k in ("id", "kind", "meta", "anchor", "window", "bs", "seed")})
    result["elapsed_seconds"] = round(time.perf_counter() - started, 2)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False))
    return task["id"], f"done {result['elapsed_seconds']}s"


def build_tasks(mode, window, bs):
    cache = OUT / "cache" / mode / f"w{window}_b{bs}"
    tasks = []
    if mode == "tuning":
        with (OUT / "tuning_references.csv").open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        logs = {}
        for row in rows:
            tasks.append({"id": row["case_id"], "kind": "drift", "meta": row,
                          "log": str(OSTOVAR_FULL / row["source_log"]), "anchor": int(row["anchor_trace"]),
                          "seed": seed_for(row["case_id"])})
            logs.setdefault(row["source_log"], row)
        for log, row in logs.items():
            nid = "null_" + hashlib.sha256(log.encode()).hexdigest()[:16]
            # Two 200-trace windows ending 50 traces before the first drift onset (900).
            tasks.append({"id": nid, "kind": "null", "meta": {k: row[k] for k in
                          ("fragment_size", "change_pattern", "noise_pct", "source_log")},
                          "log": str(OSTOVAR_FULL / log), "anchor": 850 - window, "seed": seed_for(nid)})
    else:
        with FROZEN_SIZE3.open(encoding="utf-8-sig") as handle:
            frozen = list(csv.DictReader(handle))
        for noise, suffix in NOISE_SUFFIX.items():
            cases = []
            for row in frozen:
                pattern, drift = row["change_pattern"], row["drift_sequence"]
                filename = f"Atomic_{pattern}_output_{pattern}{suffix}.xes.gz"
                key = (f"ostovar::{filename}::{drift}" if noise == "0"
                       else f"ostovar::{ {'2.5': '5', '5': '10'}[noise] }::{filename}::{drift}".replace(" ", ""))
                cid = "case_" + hashlib.sha256(key.encode()).hexdigest()[:16]
                cases.append((cid, row, pattern, suffix, int(drift)))
            cases.sort()
            for index, (cid, row, pattern, suffix, drift) in enumerate(cases):
                meta = {"case_id": cid, "fragment_size": "3", "change_pattern": pattern, "noise_pct": noise,
                        "drift_sequence": drift, "affected_activities_real": row["affected_activities_real"]}
                tasks.append({"id": cid, "kind": "drift", "meta": meta,
                              "log": str(OSTOVAR_FULL / f"Size3/Atomic/{pattern}/output/{pattern}{suffix}.mxml.gz"),
                              "anchor": 900 if drift == 1 else 1900, "seed": OFFICIAL_SEED + index})
    for task in tasks:
        task.update({"window": window, "bs": bs, "target": str(cache / f"{task['id']}.json")})
    return tasks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("tuning", "size3"), default="tuning")
    parser.add_argument("--window", type=int, default=200)
    parser.add_argument("--bs", type=int, default=100)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--current-loc-only", action="store_true",
                        help="Only the current (tau_loc=0.99, eps_loc=0.10) A*; for window/B_S sweeps")
    args = parser.parse_args()
    tasks = build_tasks(args.mode, args.window, args.bs)
    if args.current_loc_only:
        for task in tasks:
            task["loc_grid"] = [(0.99, 0.10)]
            task["target"] = task["target"].replace(f"w{args.window}_b{args.bs}", f"w{args.window}_b{args.bs}_curloc")
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
    log_runtime({
        "run": Path(tasks[0]["target"]).parent.name, "mode": args.mode, "window": args.window, "B_S": args.bs,
        "localization_grid": "current only" if args.current_loc_only else "4x4",
        "tasks": len(tasks), "computed": computed, "workers": args.workers,
        "start": start_wall.isoformat(timespec="seconds"),
        "end": datetime.now().astimezone().isoformat(timespec="seconds"),
        "wall_seconds": round(time.perf_counter() - start, 1),
        "sum_task_seconds": round(sum(json.loads(Path(t["target"]).read_text()).get("elapsed_seconds", 0)
                                      for t in tasks if Path(t["target"]).exists()), 1),
        "hardware": hardware(), "source": "measured by sweep_evidence.py"})


def hardware():
    try:
        chip = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True,
                              text=True).stdout.strip()
    except OSError:
        chip = platform.processor()
    return f"{chip}, {os.cpu_count()} cores, Python {platform.python_version()}"


def log_runtime(row):
    path = OUT / "runtime_log.csv"
    new = not path.exists()
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row))
        if new:
            writer.writeheader()
        writer.writerow(row)


if __name__ == "__main__":
    main()
