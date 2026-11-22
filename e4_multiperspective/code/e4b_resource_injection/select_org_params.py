#!/usr/bin/env python3
"""E4b step 6: choose min_obs for the resource families on the 12 E4b tuning cases (LLM-free).

Rule written before running (docs/NHAT_KY_E4_VI.md, step 6):
  recall   = share of R1/R4 cases with an O_ASSIGN item on X, and of R2 cases with an O_ASSIGN
             item on Y or an O_HAND item on (X, Y)
  spurious = mean number of resource items per case on other units (all 12 cases, incl. N)
  keep configurations with recall = 1.0, then minimum spurious, ties -> smaller min_obs.
Resource families use B = 2000 and tau = 0.9995, as T_WAIT.
Outputs: results/e4b_resource_injection/org_grid.csv, org_selection.json
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
from pipeline_mp import REPO, org_candidates, to_traces  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e0_parameter_setting"))
from sweep_evidence import seed_for  # noqa: E402
from pcr.evidence.organizational_indicators import eligible_organizational_units  # noqa: E402
from pcr.pipeline import load_config  # noqa: E402

DATA = E4_RESULTS / "e4b_resource_injection"
MIN_OBS = (20, 50, 100)
TAU, PAIRS = 0.9995, 1000


def main():
    config = load_config()
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["split"] == "tuning"]
    per_case = []
    for case in cases:
        with gzip.open(DATA / "cases" / f"{case['case_id']}.json.gz", "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        pre, post = to_traces(data["before"]), to_traces(data["after"])
        cands = org_candidates(pre, post, config, seed_for(case["case_id"]), min(MIN_OBS), PAIRS)
        allowed = {m: {(k, u) for k, us in eligible_organizational_units(pre, post, m).items() for u in us}
                   for m in MIN_OBS}
        per_case.append((case, cands, allowed))
        print(case["case_id"], case["type"], case["target"], "candidates", len(cands), flush=True)
    grid = []
    for m in MIN_OBS:
        hits, n_target, spurious, null_items = 0, 0, [], []
        for case, cands, allowed in per_case:
            kept = [c for c in cands if (c["j"], c["u"]) in allowed[m] and c["q"] >= TAU]
            target, source = case["target"], case["source"]
            def on_target(c):
                if c["j"] == "O_ASSIGN":
                    return bool(target) and c["u"] == target
                return bool(source) and tuple(c["u"]) == (source, target)
            good = [c for c in kept if on_target(c)]
            spurious.append(len(kept) - len(good))
            if case["type"] != "N":
                n_target += 1
                hits += bool(good)
            else:
                null_items.append(len(kept))
        grid.append({"min_obs": m, "recall": round(hits / n_target, 4), "spurious_mean": round(sum(spurious) / len(spurious), 3),
                     "null_resource_items": json.dumps(null_items)})
    with (DATA / "org_grid.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(grid[0]))
        writer.writeheader()
        writer.writerows(grid)
    passing = [g for g in grid if g["recall"] == 1.0]
    selection = {"tau": TAU, "pairs_per_window": PAIRS, "n_passing": len(passing), "grid": grid}
    if passing:
        selection["selected"] = min(passing, key=lambda g: (g["spurious_mean"], g["min_obs"]))
    (DATA / "org_selection.json").write_text(json.dumps(selection, indent=2), encoding="utf-8")
    print(json.dumps(selection, indent=2))


if __name__ == "__main__":
    main()
