#!/usr/bin/env python3
"""E0 A4/A5: offline grid over (tau, tau_OCC, tau_loc, eps_loc, eps_REL) on cached candidates.

LLM-free proxies per case and configuration:
  A* recall / precision against the reference affected activities
  E* coverage: share of reference activities mentioned by >= 1 evidence item
  E* on-target share: share of items touching >= 1 reference activity
  |E*| and estimated evidence tokens (serialized characters / 4)
  null pairs (tuning only): |E*| on two windows of the same stable state

Pre-registered selection rule (E0_PARAMETER_SETTING_PLAN_VI.md, section 3):
  feasible = pooled mean A* recall >= 0.95 and pooled mean E* coverage >= 0.95
  choose the feasible configuration with the smallest median |E*|;
  ties -> lower mean null |E*|; remaining ties -> closest to current config.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from itertools import product
from pathlib import Path
from statistics import mean, median

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from pcr.paths import RESULTS  # noqa: E402

OUT = RESULTS / "e0_parameter_setting"
FAMILIES = ("CF_OCC", "CF_DIR", "CF_POS", "CF_REL", "CF_LAG")
GRID = {
    "tau": (0.90, 0.95, 0.975, 0.99, 0.995),
    "tau_occ": (0.90, 0.95, 0.975, 0.99, 0.995),
    "tau_loc": (0.95, 0.975, 0.99, 0.995),
    "eps_loc": (0.05, 0.10, 0.15, 0.20),
    "eps_rel": (0.05, 0.10, 0.15, 0.20),
}
CURRENT = {"tau": 0.99, "tau_occ": 0.95, "tau_loc": 0.99, "eps_loc": 0.10, "eps_rel": 0.10}
FEASIBLE_RECALL, FEASIBLE_COVERAGE = 0.95, 0.95


def mentions(unit):
    return set(unit) if isinstance(unit, list) else {unit}


def load(mode, window, bs, suffix=""):
    cases, nulls = [], []
    for path in sorted((OUT / "cache" / mode / f"w{window}_b{bs}{suffix}").glob("*.json")):
        data = json.loads(path.read_text())
        region_of = {}
        for key, cells in data["regions"].items():
            for tau_loc, eps_loc in cells:
                region_of[(tau_loc, eps_loc)] = key
        entry = {"id": data["id"], "meta": data["meta"], "region_of": region_of,
                 "regions": {k: set(json.loads(k)) for k in data["regions"]}, "stage2": data["stage2"]}
        if data["kind"] == "drift":
            real = json.loads(data["meta"]["affected_activities_real"])
            entry["ref"] = {data["label_map"][a] for a in real if a in data["label_map"]}
            entry["ref_unobserved"] = [a for a in real if a not in data["label_map"]]
            cases.append(entry)
        else:
            nulls.append(entry)
    return cases, nulls


def evidence(entry, cfg):
    key = entry["region_of"][(cfg["tau_loc"], cfg["eps_loc"])]
    items = []
    for x in entry["stage2"][key]:
        tau = cfg["tau_occ"] if x["j"] == "CF_OCC" else cfg["tau"]
        eps = cfg["eps_rel"] if x["j"] == "CF_REL" else 0.0
        if x["q"] >= tau and x["r"] >= eps and x["r"] > 0:
            items.append(x)
    return entry["regions"][key], items


def case_metrics(entry, cfg):
    region, items = evidence(entry, cfg)
    ref = entry["ref"]
    covered = set().union(*(mentions(x["u"]) for x in items)) & ref if items else set()
    on_target = sum(bool(mentions(x["u"]) & ref) for x in items)
    families = {a: {x["j"] for x in items if a in mentions(x["u"])} for a in ref}
    return {
        "a_recall": len(region & ref) / len(ref) if ref else 1.0,
        "a_precision": len(region & ref) / len(region) if region else 0.0,
        "a_size": len(region),
        "coverage": len(covered) / len(ref) if ref else 1.0,
        "multi_family": mean(len(f) >= 2 for f in families.values()) if ref else 1.0,
        "on_target": on_target / len(items) if items else 0.0,
        "e_size": len(items),
        "tokens": sum(x["chars"] for x in items) / 4,
        **{f"n_{j}": sum(x["j"] == j for x in items) for j in FAMILIES},
    }


def summarize(cases, nulls, cfg):
    rows = [case_metrics(c, cfg) for c in cases]
    out = {k: v for k, v in cfg.items()}
    for k in ("a_recall", "a_precision", "coverage", "multi_family", "on_target", "e_size", "tokens", "a_size"):
        out[f"mean_{k}"] = mean(r[k] for r in rows)
    out["median_e_size"] = median(r["e_size"] for r in rows)
    out["cases_full_coverage"] = mean(r["coverage"] == 1.0 for r in rows)
    for j in FAMILIES:
        out[f"mean_n_{j}"] = mean(r[f"n_{j}"] for r in rows)
    if nulls:
        null_sizes = [len(evidence(n, cfg)[1]) for n in nulls]
        out["null_mean_e_size"] = mean(null_sizes)
        out["null_nonempty"] = mean(s > 0 for s in null_sizes)
        out["null_mean_a_size"] = mean(len(evidence(n, cfg)[0]) for n in nulls)
    return out


def distance_to_current(row):
    return sum(abs(GRID[k].index(row[k]) - GRID[k].index(CURRENT[k])) for k in GRID)


def write(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("tuning", "size3"), default="tuning")
    parser.add_argument("--window", type=int, default=200)
    parser.add_argument("--bs", type=int, default=100)
    parser.add_argument("--current-loc-only", action="store_true")
    parser.add_argument("--cache-suffix", default="", help="e.g. _v2perm (pipeline v2 caches from p0_evidence_v2)")
    parser.add_argument("--single-tau", action="store_true",
                        help="pipeline v2: constrain tau_OCC = tau (one threshold for every family)")
    parser.add_argument("--sizes", nargs="+", help="restrict tuning cases/null pairs to these fragment sizes")
    args = parser.parse_args()
    suffix = ("_curloc" if args.current_loc_only else "") + args.cache_suffix
    if args.current_loc_only:
        GRID["tau_loc"], GRID["eps_loc"] = (CURRENT["tau_loc"],), (CURRENT["eps_loc"],)
    if args.single_tau:
        CURRENT["tau_occ"] = CURRENT["tau"]
    cases, nulls = load(args.mode, args.window, args.bs, suffix)
    tag = f"{args.mode}_w{args.window}_b{args.bs}{suffix}" + ("_singletau" if args.single_tau else "")
    if args.sizes:
        cases = [c for c in cases if str(c["meta"]["fragment_size"]) in args.sizes]
        nulls = [n for n in nulls if str(n["meta"]["fragment_size"]) in args.sizes]
        tag += "_sizes" + "".join(args.sizes)
    print(f"{tag}: {len(cases)} drift cases, {len(nulls)} null pairs; "
          f"unobserved reference activities: {sum(len(c['ref_unobserved']) for c in cases)}")

    grid_rows = []
    for values in product(*GRID.values()):
        cfg = dict(zip(GRID, values))
        if args.single_tau and cfg["tau_occ"] != cfg["tau"]:
            continue
        row = summarize(cases, nulls, cfg)
        row["distance_to_current"] = distance_to_current(row)
        row["is_current"] = cfg == CURRENT
        grid_rows.append(row)
    write(OUT / f"grid_{tag}.csv", grid_rows)

    # One-at-a-time sensitivity around the current configuration, per noise level and pooled.
    oat = []
    noises = sorted({c["meta"]["noise_pct"] for c in cases})
    for name, values in GRID.items():
        for value in values:
            cfg = {**CURRENT, name: value}
            for noise in ["pooled", *noises]:
                subset = cases if noise == "pooled" else [c for c in cases if c["meta"]["noise_pct"] == noise]
                nsub = nulls if noise == "pooled" else [n for n in nulls if n["meta"]["noise_pct"] == noise]
                oat.append({"parameter": name, "value": value, "noise": noise, **summarize(subset, nsub, cfg)})
    write(OUT / f"oat_{tag}.csv", oat)

    current = next(r for r in grid_rows if r["is_current"])
    feasible = [r for r in grid_rows if r["mean_a_recall"] >= FEASIBLE_RECALL
                and r["mean_coverage"] >= FEASIBLE_COVERAGE]
    keys = ("tau", "tau_occ", "tau_loc", "eps_loc", "eps_rel")
    report = {"mode": tag, "n_cases": len(cases), "n_null": len(nulls), "n_configs": len(grid_rows),
              "n_feasible": len(feasible), "current": current}
    if feasible and args.mode == "tuning":
        best_size = min(r["median_e_size"] for r in feasible)
        tied = [r for r in feasible if r["median_e_size"] == best_size]
        best_null = min(r.get("null_mean_e_size", 0) for r in tied)
        tied = [r for r in tied if r.get("null_mean_e_size", 0) == best_null]
        chosen = min(tied, key=lambda r: (r["distance_to_current"], r["mean_tokens"]))
        report.update({"selected": chosen, "n_tied_after_rule": len(tied),
                       "current_is_feasible": current in feasible,
                       "current_rank_by_median_e_size": 1 + sum(r["median_e_size"] < current["median_e_size"]
                                                                for r in feasible),
                       "tied_configs": [{k: r[k] for k in keys} for r in tied]})
    (OUT / f"selection_{tag}.json").write_text(json.dumps(report, indent=2, default=str))
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: v[kk] for kk in v if kk in keys or kk.startswith(("mean_a_recall", "mean_coverage", "median_e", "mean_tokens", "null_mean_e"))})
                      for k, v in report.items() if k != "tied_configs"}, indent=1, default=str))


if __name__ == "__main__":
    main()
