#!/usr/bin/env python3
"""E4b (design A + B): choose min_obs and eps_org for O_ASSIGN on the 12 tuning cases (rule in docs/NHAT_KY_E4_VI.md).
O_ASSIGN only, min_obs = 100, B = 2000, tau = 0.9995. Outputs org_eps_grid.csv, org_eps_selection.json."""
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
EPS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5)
MIN_OBS_GRID, TAU, PAIRS = (20, 50, 100), 0.9995, 1000


def main():
    config = load_config()
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["split"] == "tuning"]
    per_case = []
    for case in cases:
        with gzip.open(DATA / "cases" / f"{case['case_id']}.json.gz", "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        pre, post = to_traces(data["before"]), to_traces(data["after"])
        allowed = {m: set(eligible_organizational_units(pre, post, m)["O_ASSIGN"]) for m in MIN_OBS_GRID}
        cands = [c for c in org_candidates(pre, post, config, seed_for(case["case_id"]), min(MIN_OBS_GRID), PAIRS)
                 if c["j"] == "O_ASSIGN"]
        per_case.append((case, cands, allowed))
        print(case["case_id"], case["type"], case["target"], len(cands), flush=True)
    grid = []
    for m in MIN_OBS_GRID:
      for eps in EPS:
        hits, n_target, other, null_items = 0, 0, [], []
        for case, cands, allowed in per_case:
            kept = [c for c in cands if c["u"] in allowed[m] and c["r"] >= eps and c["q"] >= TAU]
            on = [c for c in kept if case["target"] and c["u"] == case["target"]]
            other.append(len(kept) - len(on))
            if case["type"] == "N":
                null_items.append(len(kept))
            else:
                n_target += 1
                hits += bool(on)
        grid.append({"min_obs": m, "eps_org": eps, "recall": round(hits / n_target, 4), "other_items_mean": round(sum(other) / len(other), 3),
                     "null_items": json.dumps(null_items)})
    with (DATA / "org_eps_grid.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(grid[0]))
        writer.writeheader()
        writer.writerows(grid)
    passing = [g for g in grid if g["recall"] == 1.0]
    selection = {"families": ["O_ASSIGN"], "tau": TAU, "pairs_per_window": PAIRS, "grid": grid}
    if passing:
        selection["selected"] = min(passing, key=lambda g: (g["other_items_mean"], g["eps_org"], g["min_obs"]))
    (DATA / "org_eps_selection.json").write_text(json.dumps(selection, indent=2), encoding="utf-8")
    print(json.dumps(selection, indent=2))


if __name__ == "__main__":
    main()
