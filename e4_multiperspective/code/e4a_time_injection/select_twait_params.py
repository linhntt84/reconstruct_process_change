#!/usr/bin/env python3
"""E4a step 3: choose T_WAIT parameters (min_obs, eps_time) on the 24 tuning cases, LLM-free.

Rule written before running (docs/NHAT_KY_E4_VI.md):
  recall   = share of T_SLOW/T_FAST/M tuning cases with >= 1 T_WAIT item on a pair into X
  spurious = mean number of T_WAIT items per case on pairs not into X (all 24 cases, incl. N)
  (i) keep configurations with recall = 1.0; (ii) minimum spurious; (iii) ties: smaller eps_time,
  then smaller min_obs. If no configuration passes (i), stop and report.
Also checks that the control-flow part equals pcr.pipeline.build_evidence exactly.
Outputs: e4_multiperspective/results/e4a_time_injection/twait_grid.csv, twait_selection.json
"""
from __future__ import annotations

import csv
import gzip
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_RESULTS  # noqa: E402
from pipeline_mp import REPO, build_evidence_mp, to_traces, twait_candidates  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e0_parameter_setting"))
from sweep_evidence import seed_for  # noqa: E402
from pcr.pipeline import build_evidence, load_config  # noqa: E402

DATA = E4_RESULTS / "e4a_time_injection"
MIN_OBS = (5, 10, 20, 30)
EPS = (0.0, 0.1, 0.2, 0.3)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs-per-window", type=int, default=0, help="T_WAIT reference size (B = 2x); 0 = shared")
    parser.add_argument("--tau", type=float, default=0.0, help="T_WAIT tau; 0 = shared")
    parser.add_argument("--tag", default="")
    args = parser.parse_args()
    config = load_config()
    tau = args.tau or config["qualification"]["tau"]
    pairs = args.pairs_per_window or config["reference"]["pairs_per_stable_window"]
    chance = max(0, 2 * pairs + 1 - __import__("math").ceil(tau * (2 * pairs + 1) - 1e-9)) / (2 * pairs + 1)
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["split"] == "tuning"]
    per_case = []
    cf_identical = 0
    for case in cases:
        with gzip.open(DATA / "cases" / f"{case['case_id']}.json.gz", "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        seed = seed_for(case["case_id"])
        pre, post = to_traces(data["before"]), to_traces(data["after"])
        candidates = twait_candidates(pre, post, config, seed, min(MIN_OBS), pairs)
        # control-flow part must be identical to the unmodified pipeline
        doc = build_evidence_mp(data["before"], data["after"], config, seed, case["case_id"],
                                time_params={"min_obs": 10, "eps_time": 0.0, "tau": tau, "pairs_per_window": pairs},
                                precomputed=candidates)
        base = build_evidence([t["activities"] for t in pre], [t["activities"] for t in post], config,
                              seed=seed, case_id=case["case_id"])
        cf_items = [i for i in doc["evidence"] if i["indicator"] != "T_WAIT"]
        cf_identical += json.dumps(cf_items, sort_keys=True) == json.dumps(base["evidence"], sort_keys=True)
        per_case.append({"case": case, "candidates": candidates, "cf_units": base["screening"]["units_tested"]})
        print(f"{case['case_id']} {case['type']:6s} target={case['time_target'] or '-':4s} "
              f"T_WAIT candidates={len(candidates)}", flush=True)

    grid = []
    for m in MIN_OBS:
        for eps in EPS:
            hits, spurious, n_time, null_items, null_expected = 0, [], 0, [], []
            for pc in per_case:
                case, target = pc["case"], pc["case"]["time_target"]
                kept = [c for c in pc["candidates"] if c["obs_before"] >= m and c["obs_after"] >= m
                        and c["effect"] >= eps and c["q"] >= tau]
                eligible = [c for c in pc["candidates"] if c["obs_before"] >= m and c["obs_after"] >= m
                            and c["effect"] >= eps]
                into = [c for c in kept if target and c["u"][1] == target]
                spurious.append(len(kept) - len(into))
                if target:
                    n_time += 1
                    hits += bool(into)
                if case["type"] == "N":
                    null_items.append(len(kept))
                    null_expected.append(round(len(eligible) * chance, 3))
            grid.append({"min_obs": m, "eps_time": eps, "recall": round(hits / n_time, 4),
                         "spurious_mean": round(sum(spurious) / len(spurious), 3),
                         "null_twait_items": json.dumps(null_items), "null_expected_total": json.dumps(null_expected)})
    suffix = f"_{args.tag}" if args.tag else ""
    with (DATA / f"twait_grid{suffix}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(grid[0]))
        writer.writeheader()
        writer.writerows(grid)
    passing = [g for g in grid if g["recall"] == 1.0]
    selection = {"cf_identical_cases": f"{cf_identical}/{len(per_case)}", "n_passing": len(passing),
                 "tau_time": tau, "pairs_per_window_time": pairs}
    if passing:
        best = min(passing, key=lambda g: (g["spurious_mean"], g["eps_time"], g["min_obs"]))
        selection["selected"] = best
    (DATA / f"twait_selection{suffix}.json").write_text(json.dumps(selection, indent=2), encoding="utf-8")
    for g in grid:
        print(g)
    print(json.dumps(selection, indent=2))


if __name__ == "__main__":
    main()
