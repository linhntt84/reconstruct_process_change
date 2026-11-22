#!/usr/bin/env python3
"""E4b secondary check (not used for selection): with the selected resource configuration, does the
target activity already show an O_ASSIGN / O_CONC item on the ORIGINAL (not injected) windows?
Output: results/e4b_resource_injection/target_stability_check.csv"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from build_e4b import G, OUT, W, load_traces  # noqa: E402
from pipeline_mp import eligible_org_units, org_candidates, to_traces  # noqa: E402
from sweep_evidence import seed_for  # noqa: E402  (path added by build_e4b)
from pcr.pipeline import load_config  # noqa: E402


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "org_conc_selection.json"
    sel = json.loads((OUT / name).read_text())["selected"]
    eps = {"O_ASSIGN": sel["eps_assign"], "O_CONC": sel["eps_conc"]}
    traces, config = load_traces(), load_config()
    with (OUT / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["type"] != "N"]
    rows = []
    for case in cases:
        cp = int(case["pseudo_cp"])
        pre, post = to_traces(traces[cp - G - W:cp - G]), to_traces(traces[cp + G:cp + G + W])
        allowed = set(eligible_org_units(pre, post, sel["min_obs"])["O_ASSIGN"])
        cands = org_candidates(pre, post, config, seed_for(case["case_id"]), sel["min_obs"], 1000)
        hit = {c["j"]: round(c["r"], 4) for c in cands if c["j"] in eps and c["u"] == case["target"]
               and c["u"] in allowed and c["r"] >= eps[c["j"]] and c["q"] >= 0.9995}
        rows.append({"case_id": case["case_id"], "split": case["split"], "type": case["type"], "target": case["target"],
                     "assign_item_before_injection": hit.get("O_ASSIGN", ""), "conc_item_before_injection": hit.get("O_CONC", "")})
        print(rows[-1], flush=True)
    with (OUT / name.replace("org_conc_selection", "target_stability_check").replace(".json", ".csv")).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    flagged = [r for r in rows if r["assign_item_before_injection"] != "" or r["conc_item_before_injection"] != ""]
    print(f"{len(flagged)}/{len(rows)} targets with a resource item before injection")


if __name__ == "__main__":
    main()
