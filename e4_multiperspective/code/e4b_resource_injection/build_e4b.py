#!/usr/bin/env python3
"""E4b: resource changes injected into real BPI Challenge 2017 windows (design: docs/NHAT_KY_E4_VI.md, step 6).

Traces: complete events only, ordered by case start (first event of any lifecycle), which reproduces
the trace coordinates of the Adams et al. (2023) change points used in the submitted study.
Target activities are restricted to activities whose resource assignment is stable between the
original windows (no O_ASSIGN item before injection), so that a detected change on the target is due
to the injection (real logs show strong weekly resource churn on some activities).
Each case uses a pseudo change point cp: L- = [cp - 250, cp - 50), L+ = [cp + 50, cp + 250).
Pairs do not overlap and stay >= 300 traces away from the four Adams change points.
Types (injection in L+ only; activities and timestamps never change):
  R1_REASSIGN    every event of X gets a real resource that never performed X in L-
  R2_CONSOLIDATE whenever Y directly follows X, Y gets the resource of that X (handover X->Y disappears)
  R4_SHRINK      every event of X gets the resource that performed X most often in L-
  N              no injection
Outputs: e4_multiperspective/results/e4b_resource_injection/{cases.csv, cases/*.json.gz, sanity.csv}
Requires pandas (Python >= 3.9).
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import random
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_ROOT, E4_RESULTS, REPO  # noqa: E402
from pipeline_mp import org_candidates, to_traces  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e0_parameter_setting"))
from pcr.pipeline import load_config  # noqa: E402

BPI = Path(REPO.parent / "GitHub_Master_Results/data/raw_local/Data/BPI2017/BPI Challenge 2017.csv")
ADAMS = E4_ROOT / "docs" / "bpi2017_adams_2023_change_points.csv"
OUT = E4_RESULTS / "e4b_resource_injection"
SEED = 20261113
W, G, MARGIN = 200, 50, 300
MIN_OBS, MAX_TOP_SHARE, MIN_HANDOVER = 50, 0.5, 0.5
TYPES = ("R1_REASSIGN", "R2_CONSOLIDATE", "R4_SHRINK", "N")
PER_TYPE = {"tuning": 3, "evaluation": 10}


def load_traces() -> list[list[list[str]]]:
    df = pd.read_csv(BPI, usecols=["case:concept:name", "concept:name", "org:resource",
                                   "lifecycle:transition", "time:timestamp"])
    df["t"] = pd.to_datetime(df["time:timestamp"], format="mixed", utc=True)
    order = df.groupby("case:concept:name")["t"].min().sort_values(kind="mergesort")
    comp = df[df["lifecycle:transition"] == "complete"].sort_values(["case:concept:name", "t"], kind="mergesort")
    grouped = {cid: g for cid, g in comp.groupby("case:concept:name", sort=False)}
    traces = []
    for cid in order.index:
        g = grouped.get(cid)
        traces.append([] if g is None else
                      [[a, t.isoformat(), str(r)] for a, t, r in zip(g["concept:name"], g["t"], g["org:resource"])])
    return traces


def change_points(n: int) -> list[int]:
    with ADAMS.open(encoding="utf-8") as handle:
        bounds = [0] + [int(r["boundary_case_index"]) for r in csv.DictReader(handle)] + [n]
    cps = []
    for lo, hi in zip(bounds, bounds[1:]):
        start = lo + (MARGIN if lo else 0)
        end = hi - (MARGIN if hi != n else 0)
        cp = start + W + G
        while cp + G + W <= end:
            cps.append(cp)
            cp += 2 * (W + G)
    return cps


def activity_stats(window):
    occ, res = Counter(), {}
    for t in window:
        for a, _, r in t:
            occ[a] += 1
            res.setdefault(a, Counter())[r] += 1
    return occ, res


def eligible_activities(before, after):
    ob, rb = activity_stats(before)
    oa, _ = activity_stats(after)
    return sorted(a for a in ob if ob[a] >= MIN_OBS and oa.get(a, 0) >= MIN_OBS
                  and rb[a].most_common(1)[0][1] / ob[a] < MAX_TOP_SHARE)


def eligible_pairs(before, after, acts):
    def pairs(window):
        count, hand = Counter(), Counter()
        for t in window:
            for (a, _, ra), (b, _, rb) in zip(t, t[1:]):
                count[(a, b)] += 1
                hand[(a, b)] += ra != rb
        return count, hand
    cb, hb = pairs(before)
    ca, _ = pairs(after)
    return sorted(p for p in cb if p[1] in acts and cb[p] >= MIN_OBS and ca.get(p, 0) >= MIN_OBS
                  and hb[p] / cb[p] >= MIN_HANDOVER and p[0] != p[1])


def changed_assignments(before, after, cid: str) -> set[str]:
    """Activities whose resource profile already changes between the original windows: O_ASSIGN items
    of the multi-perspective pipeline (config_org.json) before any injection."""
    org = json.loads((E4_ROOT / "code" / "config_org.json").read_text())
    seed = int(hashlib.sha256(f"stability::{cid}".encode()).hexdigest()[:8], 16)
    cands = org_candidates(to_traces(before), to_traces(after), load_config(), seed, org["min_obs"],
                           org["pairs_per_window"])
    return {c["u"] for c in cands if c["j"] == "O_ASSIGN" and c["r"] >= org["eps"] and c["q"] >= org["tau"]}


def inject(kind, before, after, rng, unstable: set[str]):
    after = [[list(e) for e in t] for t in after]
    acts = [a for a in eligible_activities(before, after) if a not in unstable]
    _, res_before = activity_stats(before)
    info = {}
    if kind == "R1_REASSIGN":
        x = rng.choice(acts)
        active = sorted({r for t in after for _, _, r in t} - set(res_before[x]) - {"User_1"})
        new = rng.choice(active)
        for t in after:
            for e in t:
                if e[0] == x:
                    e[2] = new
        info = {"target": x, "required": [x], "optional": [], "new_resource": new}
    elif kind == "R4_SHRINK":
        x = rng.choice(acts)
        top = res_before[x].most_common(1)[0][0]
        for t in after:
            for e in t:
                if e[0] == x:
                    e[2] = top
        info = {"target": x, "required": [x], "optional": [], "kept_resource": top,
                "pool_before": len(res_before[x])}
    elif kind == "R2_CONSOLIDATE":
        x, y = rng.choice(eligible_pairs(before, after, set(acts)))  # target Y is stable
        for t in after:
            for prev, e in zip(t, t[1:]):
                if prev[0] == x and e[0] == y:
                    e[2] = prev[2]
        info = {"target": y, "source": x, "required": [y], "optional": [x]}
    return after, info


def check(original, injected, kind, info) -> dict:
    same = all([(e[0], e[1]) for e in a] == [(e[0], e[1]) for e in b] for a, b in zip(original, injected))
    changed = Counter(e1[0] for a, b in zip(original, injected) for e1, e2 in zip(a, b) if e1[2] != e2[2])
    allowed = {info.get("target")} if kind != "N" else set()
    return {"activities_timestamps_unchanged": same, "resource_changes_by_activity": json.dumps(dict(changed)),
            "only_target_changed": set(changed) <= allowed}


def main():
    traces = load_traces()
    cps = change_points(len(traces))
    rng = random.Random(SEED)
    slots = list(cps)
    rng.shuffle(slots)
    plan = []
    for split in ("tuning", "evaluation"):
        for kind in TYPES:
            for _ in range(PER_TYPE[split]):
                plan.append((split, kind, slots.pop()))
    (OUT / "cases").mkdir(parents=True, exist_ok=True)
    rows, sanity = [], []
    for split, kind, cp in sorted(plan, key=lambda p: p[2]):
        cid = "e4b_" + hashlib.sha256(f"e4b::{cp}::{kind}".encode()).hexdigest()[:16]
        before, after = traces[cp - G - W:cp - G], traces[cp + G:cp + G + W]
        unstable = changed_assignments(before, after, cid)
        injected, info = (after, {}) if kind == "N" else inject(kind, before, after, random.Random(f"{SEED}:{cid}"), unstable)
        info["unstable_before_injection"] = sorted(unstable)
        with gzip.open(OUT / "cases" / f"{cid}.json.gz", "wt", encoding="utf-8") as handle:
            json.dump({"before": before, "after": injected}, handle)
        rows.append({"case_id": cid, "split": split, "type": kind, "pseudo_cp": cp,
                     "window_before": f"[{cp - G - W},{cp - G})", "window_after": f"[{cp + G},{cp + G + W})",
                     "target": info.get("target", ""), "source": info.get("source", ""),
                     "required_activities_real": json.dumps(info.get("required", [])),
                     "optional_activities_real": json.dumps(info.get("optional", [])),
                     "details": json.dumps({k: v for k, v in info.items() if k not in ("required", "optional")}),
                     "perspectives": json.dumps(["resource"] if kind != "N" else [])})
        sanity.append({"case_id": cid, "type": kind, **check(after, injected, kind, info)})
        print(split, kind, cp, info.get("target", ""), flush=True)
    for name, data in (("cases.csv", rows), ("sanity.csv", sanity)):
        with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    bad = [s for s in sanity if not s["activities_timestamps_unchanged"] or not s["only_target_changed"]]
    print(f"{len(rows)} cases from {len(cps)} slots -> {OUT}; sanity failures: {len(bad)}")


if __name__ == "__main__":
    main()
