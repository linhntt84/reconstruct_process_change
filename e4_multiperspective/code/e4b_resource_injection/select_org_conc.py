#!/usr/bin/env python3
"""E4b (author decision 1 + 2, 2026-11-13): choose min_obs, eps_assign, eps_conc for the resource family
(O_ASSIGN + O_CONC) on the 12 tuning cases. Rule written before running (docs/NHAT_KY_E4_VI.md):
  recall = share of the 9 R1/R2/R4 cases with an O_ASSIGN or O_CONC item on the target activity;
  maximize recall, then minimize the mean number of resource items on other activities (12 cases),
  ties -> smaller eps_assign, smaller eps_conc, smaller min_obs.
B = 2000 (pairs_per_window 1000), tau = 0.9995. Outputs org_conc_grid.csv, org_conc_selection.json.
Also writes org_conc_target_values.csv (r, q of every target unit) for diagnosis."""
from __future__ import annotations

import csv
import gzip
import argparse
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_RESULTS  # noqa: E402
from pipeline_mp import REPO, eligible_org_units, org_candidates, to_traces  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e0_parameter_setting"))
from sweep_evidence import seed_for  # noqa: E402
from pcr.pipeline import load_config  # noqa: E402

DATA = E4_RESULTS / "e4b_resource_injection"
MIN_OBS_GRID = (20, 50, 100)
EPS_ASSIGN = (0.0, 0.1, 0.2, 0.3)
EPS_CONC = (0.0, 0.05, 0.1, 0.2, 0.3)
FAMILIES, TAU, PAIRS = ("O_ASSIGN", "O_CONC"), 0.9995, 1000


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rule", choices=("a", "b"), default="a",
                        help="a: any O_ASSIGN/O_CONC item on the target; b: R2 counts O_ASSIGN only (author decision 2026-11-13)")
    args = parser.parse_args()
    suffix = "" if args.rule == "a" else "_b"
    config = load_config()
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["split"] == "tuning"]
    per_case, target_rows = [], []
    for case in cases:
        with gzip.open(DATA / "cases" / f"{case['case_id']}.json.gz", "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        pre, post = to_traces(data["before"]), to_traces(data["after"])
        allowed = {m: set(eligible_org_units(pre, post, m)["O_ASSIGN"]) for m in MIN_OBS_GRID}
        cands = [{k: v for k, v in c.items() if not k.startswith("_")}
                 for c in org_candidates(pre, post, config, seed_for(case["case_id"]), min(MIN_OBS_GRID), PAIRS)
                 if c["j"] in FAMILIES]
        per_case.append((case, cands, allowed))
        for c in cands:
            if case["target"] and c["u"] == case["target"]:
                target_rows.append({"case_id": case["case_id"], "type": case["type"], "target": case["target"],
                                    "family": c["j"], "r": round(c["r"], 4), "q": round(c["q"], 5)})
        print(case["case_id"], case["type"], case["target"], len(cands), flush=True)
    grid = []
    for m, ea, ec in itertools.product(MIN_OBS_GRID, EPS_ASSIGN, EPS_CONC):
        eps = {"O_ASSIGN": ea, "O_CONC": ec}
        hits, n_target, other, null_items = 0, 0, [], []
        for case, cands, allowed in per_case:
            kept = [c for c in cands if c["u"] in allowed[m] and c["r"] >= eps[c["j"]] and c["q"] >= TAU]
            on = [c for c in kept if case["target"] and c["u"] == case["target"]
                  and (args.rule == "a" or case["type"] != "R2_CONSOLIDATE" or c["j"] == "O_ASSIGN")]
            other.append(len({c["u"] for c in kept} - {case["target"]}))
            if case["type"] == "N":
                null_items.append(len(kept))
            else:
                n_target += 1
                hits += bool(on)
        grid.append({"min_obs": m, "eps_assign": ea, "eps_conc": ec, "recall": round(hits / n_target, 4),
                     "other_activities_mean": round(sum(other) / len(other), 3), "null_items": json.dumps(null_items)})
    for name, rows in ((f"org_conc_grid{suffix}.csv", grid), (f"org_conc_target_values{suffix}.csv", target_rows)):
        with (DATA / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    best = max(g["recall"] for g in grid)
    selected = min((g for g in grid if g["recall"] == best),
                   key=lambda g: (g["other_activities_mean"], g["eps_assign"], g["eps_conc"], g["min_obs"]))
    selection = {"families": list(FAMILIES), "tau": TAU, "pairs_per_window": PAIRS,
                 "rule": args.rule + ": max recall, then min other_activities_mean, ties smaller eps_assign, eps_conc, min_obs",
                 "best_recall": best, "selected": selected}
    (DATA / f"org_conc_selection{suffix}.json").write_text(json.dumps(selection, indent=2), encoding="utf-8")
    print(json.dumps(selection, indent=2))


if __name__ == "__main__":
    main()
