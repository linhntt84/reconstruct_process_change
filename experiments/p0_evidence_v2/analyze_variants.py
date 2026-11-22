#!/usr/bin/env python3
"""P0-A analysis: reference mode x tie rule x tau profile x minimum support (no LLM).

Drift cases (Ostovar sizes 2, 4): A* recall/precision, E* coverage of the
reference activities, on-target share, |E*|. Null pairs: share with nonempty
E*, mean |E*|, and which families produce the items.
Minimum support m keeps a unit only if max(support in L-, support in L+) >= m.
"""
from __future__ import annotations

import csv
import json
import sys
from itertools import product
from pathlib import Path
from statistics import mean, median

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from pcr.paths import RESULTS  # noqa: E402
from pcr.evidence.qualification_v2 import strength  # noqa: E402

OUT = RESULTS / "p0_evidence_v2"
FAMILIES = ("CF_OCC", "CF_DIR", "CF_POS", "CF_REL", "CF_LAG")
TAU_PROFILES = {"v1 (OCC .95, others .99)": {"CF_OCC": 0.95}, "all .99": {"CF_OCC": 0.99},
                "all .95": {j: 0.95 for j in FAMILIES}}
MIN_SUPPORT = (0, 5, 10, 20)
EPS_REL = 0.10


def mentions(unit):
    return set(unit) if isinstance(unit, list) else {unit}


def load(reference, window=200, bs=100):
    cases, nulls = [], []
    for path in sorted((OUT / "cache" / f"{reference}_w{window}_b{bs}").glob("*.json")):
        d = json.loads(path.read_text())
        region_of = {t: k for k, ties in d["regions"].items() for t in ties}
        e = {"id": d["id"], "meta": d["meta"], "region_of": region_of,
             "regions": {k: set(json.loads(k)) for k in d["regions"]}, "stage2": d["stage2"]}
        if d["kind"] == "drift":
            real = json.loads(d["meta"]["affected_activities_real"])
            e["ref"] = {d["label_map"][a] for a in real if a in d["label_map"]}
            cases.append(e)
        else:
            nulls.append(e)
    return cases, nulls


def evidence(e, ties, taus, m):
    key = e["region_of"][ties]
    items = []
    for x in e["stage2"][key]:
        tau = taus.get(x["j"], 0.99)
        if strength(x["lt"], x["le"], x["n"], ties) < tau:
            continue
        if x["j"] == "CF_REL" and x["r"] < EPS_REL:
            continue
        if max(x["sb"], x["sa"]) < m:
            continue
        items.append(x)
    return e["regions"][key], items


def summarize(cases, nulls, ties, taus, m):
    rows = []
    for c in cases:
        region, items = evidence(c, ties, taus, m)
        ref = c["ref"]
        covered = set().union(*(mentions(x["u"]) for x in items)) & ref if items else set()
        rows.append({"rec": len(region & ref) / len(ref), "prec": len(region & ref) / len(region) if region else 0,
                     "cov": len(covered) / len(ref),
                     "ont": mean(bool(mentions(x["u"]) & ref) for x in items) if items else 0, "n": len(items)})
    out = {"a_recall": mean(r["rec"] for r in rows), "a_precision": mean(r["prec"] for r in rows),
           "coverage": mean(r["cov"] for r in rows), "full_coverage": mean(r["cov"] == 1 for r in rows),
           "on_target": mean(r["ont"] for r in rows), "median_E": median(r["n"] for r in rows),
           "drift_empty": mean(r["n"] == 0 for r in rows)}
    null_ev = [evidence(n, ties, taus, m) for n in nulls]
    out.update({"null_nonempty_A": mean(bool(r) for r, _ in null_ev),
                "null_nonempty_E": mean(bool(i) for _, i in null_ev),
                "null_mean_E": mean(len(i) for _, i in null_ev)})
    for j in FAMILIES:
        out[f"null_{j}"] = mean(sum(x["j"] == j for x in i) for _, i in null_ev)
    return out


def main():
    rows = []
    for reference in ("bootstrap", "permutation"):
        cases, nulls = load(reference)
        if not cases:
            continue
        for ties, (tname, taus), m in product(("le", "lt"), TAU_PROFILES.items(), MIN_SUPPORT):
            row = {"reference": reference, "ties": ties, "tau": tname, "min_support": m,
                   "drift_cases": len(cases), "null_pairs": len(nulls)}
            row.update({k: round(v, 4) if isinstance(v, float) else v
                        for k, v in summarize(cases, nulls, ties, taus, m).items()})
            rows.append(row)
    path = OUT / "variants_tuning_sizes24.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    cols = ("reference", "ties", "tau", "min_support", "a_recall", "coverage", "on_target", "median_E",
            "null_nonempty_A", "null_nonempty_E", "null_mean_E")
    print("\t".join(cols))
    for r in rows:
        print("\t".join(str(r[c]) for c in cols))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
