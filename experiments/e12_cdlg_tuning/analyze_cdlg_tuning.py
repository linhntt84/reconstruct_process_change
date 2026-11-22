#!/usr/bin/env python3
"""E12 analysis: apply the pre-registered E0/P0-B selection rule to the CDLG tuning pool (no LLM).

Rule (as for Ostovar, single tau): feasible = mean A* recall >= 0.95 and mean E* coverage >= 0.95;
choose the feasible configuration with the smallest median |E*|; ties -> lower mean |E*| on no-change
pairs; remaining ties -> closest (grid steps) to the frozen v2 configuration.
Then compare the frozen v2 configuration and the CDLG-selected one on the 99 CDLG evaluation changes
and 50 evaluation no-change pairs. Outputs: results/e12_cdlg_tuning/{grid_tuning.csv, selection.json,
comparison.csv, comparison.md}.
"""
from __future__ import annotations

import csv
import json
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
from analyze_grid import GRID, FEASIBLE_COVERAGE, FEASIBLE_RECALL, summarize  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402

OUT = RESULTS / "e12_cdlg_tuning"
FROZEN = {"tau": 0.995, "tau_occ": 0.995, "tau_loc": 0.995, "eps_loc": 0.10, "eps_rel": 0.20}
KEYS = ("tau", "tau_occ", "tau_loc", "eps_loc", "eps_rel")


def load(split: str):
    cases, nulls = [], []
    for path in sorted((OUT / "cache" / split).glob("*.json")):
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
            if not entry["ref"]:  # no observable reference activity (as the excluded evaluation case)
                continue
            cases.append(entry)
        else:
            nulls.append(entry)
    return cases, nulls


def distance(cfg):
    return sum(abs(GRID[k].index(cfg[k]) - GRID[k].index(FROZEN[k])) for k in KEYS)


def main():
    tune_c, tune_n = load("tuning")
    eval_c, eval_n = load("evaluation")
    print(f"tuning: {len(tune_c)} changes, {len(tune_n)} no-change pairs; "
          f"evaluation: {len(eval_c)} changes, {len(eval_n)} no-change pairs")
    rows = []
    for values in product(*GRID.values()):
        cfg = dict(zip(GRID, values))
        if cfg["tau_occ"] != cfg["tau"]:
            continue
        row = summarize(tune_c, tune_n, cfg)
        row["distance_to_frozen"] = distance(cfg)
        rows.append(row)
    with (OUT / "grid_tuning.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    feasible = [r for r in rows if r["mean_a_recall"] >= FEASIBLE_RECALL and r["mean_coverage"] >= FEASIBLE_COVERAGE]
    frozen_row = next(r for r in rows if all(r[k] == FROZEN[k] for k in KEYS))
    report = {"n_tuning_changes": len(tune_c), "n_tuning_null": len(tune_n), "n_configs": len(rows),
              "n_feasible": len(feasible), "frozen_on_tuning": frozen_row,
              "frozen_is_feasible": frozen_row in feasible,
              "max_recall_on_tuning": max(r["mean_a_recall"] for r in rows),
              "max_coverage_on_tuning": max(r["mean_coverage"] for r in rows)}
    if feasible:
        best = min(r["median_e_size"] for r in feasible)
        tied = [r for r in feasible if r["median_e_size"] == best]
        bnull = min(r.get("null_mean_e_size", 0) for r in tied)
        tied = [r for r in tied if r.get("null_mean_e_size", 0) == bnull]
        chosen = min(tied, key=lambda r: (r["distance_to_frozen"], r["mean_tokens"]))
        report.update({"selected": chosen, "n_tied": len(tied)})
        selected = {k: chosen[k] for k in KEYS}
    else:
        selected = None
    # also the configuration with the highest tuning recall (then coverage, then smaller E*)
    top = max(rows, key=lambda r: (round(r["mean_a_recall"], 6), round(r["mean_coverage"], 6), -r["median_e_size"]))
    report["max_recall_config"] = {k: top[k] for k in KEYS}
    (OUT / "selection.json").write_text(json.dumps(report, indent=2, default=str))

    configs = [("frozen v2 (Ostovar tuning)", FROZEN)]
    if selected:
        configs.append(("selected on CDLG tuning", selected))
    configs.append(("max recall on CDLG tuning", report["max_recall_config"]))
    comp = []
    for label, cfg in configs:
        for split, (c, n) in (("tuning", (tune_c, tune_n)), ("evaluation", (eval_c, eval_n))):
            s = summarize(c, n, cfg)
            comp.append({"config": label, **{k: cfg[k] for k in KEYS}, "split": split, "n": len(c),
                         "a_recall": round(s["mean_a_recall"], 3), "a_size": round(s["mean_a_size"], 1),
                         "coverage": round(s["mean_coverage"], 3),
                         "full_coverage": round(s["cases_full_coverage"], 3),
                         "median_e": s["median_e_size"], "null_mean_e": round(s.get("null_mean_e_size", 0), 2),
                         "null_nonempty": round(s.get("null_nonempty", 0), 3)})
    with (OUT / "comparison.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(comp[0]))
        writer.writeheader()
        writer.writerows(comp)
    md = ["# E12: CDLG-specific parameter selection (no LLM)", "",
          f"Tuning: {len(tune_c)} changes / {len(tune_n)} no-change pairs; evaluation: {len(eval_c)} / {len(eval_n)}.",
          f"Feasible configurations on CDLG tuning: {len(feasible)} of {len(rows)}; frozen v2 feasible: "
          f"{report['frozen_is_feasible']}.", "",
          "| Config | tau | tau_loc | eps_loc | eps_rel | Split | A* recall | |A*| | Coverage | Full cov. | Median |E*| | Null |E*| | Null nonempty |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in comp:
        md.append(f"| {r['config']} | {r['tau']} | {r['tau_loc']} | {r['eps_loc']} | {r['eps_rel']} | {r['split']} | "
                  f"{r['a_recall']} | {r['a_size']} | {r['coverage']} | {r['full_coverage']} | {r['median_e']} | "
                  f"{r['null_mean_e']} | {r['null_nonempty']} |")
    (OUT / "comparison.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
