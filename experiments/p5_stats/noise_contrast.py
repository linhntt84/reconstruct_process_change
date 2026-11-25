#!/usr/bin/env python3
"""Noise contrast on Ostovar (Section VII-A, response to Reviewer 4, Concern 6); no API calls.

For each model and fragment size, every change at 0% noise is paired with the same change (pattern, change point)
at 5% noise. Per case, the metric is the mean of the three runs; the difference is bootstrapped over the 26 pairs
(5,000 resamples, seed 1, 95% percentile interval), and the exact McNemar test uses the majority outcome
(metric = 1 in at least two of three runs).
Inputs: results/p2_main/cases.csv, results/p2_main/scores_INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC_<model>_run{1,2,3}.csv
Output: results/p5_stats/noise_contrast.csv and a summary printed to stdout.
"""
from __future__ import annotations

import csv
import random
from math import comb
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p5_stats" / "noise_contrast.csv"
MODELS = ("glm-5.3-flash", "deepseek-v4-flash")


def mcnemar(b: int, c: int) -> float:
    n = b + c
    if n == 0:
        return 1.0
    return min(1.0, 2 * sum(comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)


def main():
    with (P2 / "cases.csv").open(encoding="utf-8") as handle:
        cases = [c for c in csv.DictReader(handle) if c["kind"] == "drift" and c["set"] in ("ostovar3", "ostovar5")]
    rows = []
    for model in MODELS:
        runs = []
        for k in (1, 2, 3):
            with (P2 / f"scores_INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC_{model}_run{k}.csv").open(encoding="utf-8") as h:
                runs.append({r["case_id"]: r for r in csv.DictReader(h)})
        for s in ("ostovar3", "ostovar5"):
            for metric in ("PI", "RTU"):
                by = {}
                for c in cases:
                    if c["set"] != s:
                        continue
                    v = [float(r[c["case_id"]][metric]) for r in runs]
                    by[(c["type"], c["drift"], float(c["noise_pct"]))] = (mean(v), sum(x == 1.0 for x in v) >= 2)
                keys = sorted((t, d) for (t, d, n) in by if n == 0.0)
                diff = [by[(t, d, 5.0)][0] - by[(t, d, 0.0)][0] for t, d in keys]
                b = sum(by[(t, d, 0.0)][1] and not by[(t, d, 5.0)][1] for t, d in keys)
                c_ = sum(by[(t, d, 5.0)][1] and not by[(t, d, 0.0)][1] for t, d in keys)
                random.seed(1)
                boot = sorted(mean(random.choices(diff, k=len(diff))) for _ in range(5000))
                rows.append({"model": model, "set": s, "metric": metric, "n_pairs": len(keys),
                             "mean_0": round(mean(by[(t, d, 0.0)][0] for t, d in keys), 3),
                             "mean_5": round(mean(by[(t, d, 5.0)][0] for t, d in keys), 3),
                             "diff": round(mean(diff), 3), "ci_low": round(boot[124], 3), "ci_high": round(boot[4874], 3),
                             "mcnemar_b": b, "mcnemar_c": c_, "p": round(mcnemar(b, c_), 3)})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
