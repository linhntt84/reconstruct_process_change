#!/usr/bin/env python3
"""A3: apply the official configuration to cached candidates; compare with archived evidence."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from pcr.paths import PAPER_V1_EVIDENCE as EV, RESULTS  # noqa: E402

OUT = RESULTS / "e0_parameter_setting"
DIRS = {"0": "ostovar_atomic_b200_algorithm_1_2_v1", "2.5": "ostovar_atomic_noise_2p5_b200_algorithm_1_2_v1",
        "5": "ostovar_atomic_noise_5p0_b200_algorithm_1_2_v1"}
TAU = {"CF_OCC": .95, "CF_DIR": .99, "CF_POS": .99, "CF_REL": .99, "CF_LAG": .99}
EPS = {"CF_OCC": 0, "CF_DIR": 0, "CF_POS": 0, "CF_REL": .10, "CF_LAG": 0}

def official_region(c):
    return next(k for k, v in c["regions"].items() if [0.99, 0.10] in v)

def unit_key(u):
    return json.dumps(u["value"] if isinstance(u, dict) and "value" in u else u)

ok = bad = 0
for f in sorted((OUT / "cache/size3/w200_b100").glob("case_*.json")):
    c = json.loads(f.read_text())
    mine = {(x["j"], json.dumps(x["u"])): (round(x["r"], 9), round(x["q"], 9))
            for x in c["stage2"][official_region(c)] if x["q"] >= TAU[x["j"]] and x["r"] >= EPS[x["j"]] and x["r"] > 0}
    off = json.loads((EV / DIRS[c["meta"]["noise_pct"]] / "evidence" / f.name).read_text())["evidence"]
    theirs = {}
    for e in off:
        u = e["analysis_unit"]
        u = u["value"] if "value" in u else list(u["values"])
        theirs[(e["indicator"], json.dumps(u))] = (round(e["observed_change"], 9), round(e["empirical_strength"], 9))
    same = mine == theirs
    ok += same; bad += not same
    if not same:
        print(f.stem, c["meta"]["noise_pct"], "mine", len(mine), "official", len(theirs),
              "only_mine", sorted(set(mine) - set(theirs))[:4], "only_official", sorted(set(theirs) - set(mine))[:4])
print(f"identical evidence sets (unit, r, q): {ok}/{ok + bad}")
