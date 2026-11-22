#!/usr/bin/env python3
"""E11a: independent derivation of Ostovar affected-activity references by projection.

Principle (different from the per-activity statistics of the E0 rule): the affected activities of a
drift are the activities whose deletion makes the behaviour before and after the drift
indistinguishable. Behaviour of a segment = feature vector of
  presence[a]  share of traces containing activity a,
  df[(x, y)]   share of traces containing the directly-follows pair x -> y (start/end markers added).
(Occurrence counts are not used: in loop regions they fluctuate beyond the sampling noise of presence.)
Distance D = max |feature_before - feature_after|.
Indistinguishable: D <= delta, delta = largest D between the two halves of a stable segment of the
same log (the three stable segments of the noise-free log, each split in halves), i.e. the
within-log sampling noise.
Search: every sufficient set of MINIMUM size among the candidate activities (those appearing in a
feature that differs by more than delta; the pool is extended with the activities of the features that
still differ after deleting the whole pool, e.g. a loop p1 p2 p9: deleting p1, p9 creates p2 -> p2),
by increasing size (exact; capped at MAX_EVALS, then greedy fallback).
Reference = union of all minimum sufficient sets (when deleting either of two blocks removes the
difference, e.g. parallel -> sequence, both are affected); `n_minimum_sets` > 1 flags such ties.
Segments as E0: drift 1: [0,850) vs [1050,1850); drift 2: [1050,1850) vs [2050,2999); noise-free log.
No pattern conventions here (applied afterwards, identically for every source).
Output: results/e11a_ostovar_references/projection_sizes<sizes>.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
from pcr.logs import read_mxml  # noqa: E402
from pcr.paths import OSTOVAR_FULL, RESULTS  # noqa: E402
from build_tuning_references import PATTERNS, SEGMENTS  # noqa: E402

OUT = RESULTS / "e11a_ostovar_references"
STABLE_SPLITS = (((0, 425), (425, 850)), ((1050, 1450), (1450, 1850)), ((2050, 2525), (2525, 2999)))


def variants(traces):
    return Counter(tuple(t) for t in traces)


def features(var, drop=frozenset()):
    n = sum(var.values())
    pres, df = Counter(), Counter()
    for t, w in var.items():
        p = ("^",) + tuple(a for a in t if a not in drop) + ("$",)
        for a in set(p[1:-1]):
            pres[a] += w
        for e in set(zip(p, p[1:])):
            df[e] += w
    f = {("p", a): v / n for a, v in pres.items()}
    f.update({("d",) + e: v / n for e, v in df.items()})
    return f


def distance(a, b):
    return max((abs(a.get(k, 0.0) - b.get(k, 0.0)) for k in set(a) | set(b)), default=0.0)


MAX_EVALS = 300_000


def derive(traces, drift, delta):
    (a0, a1), (b0, b1) = SEGMENTS[drift]
    pre, post = variants(traces[a0:a1]), variants(traces[b0:b1])
    d = lambda s: distance(features(pre, s), features(post, s))  # noqa: E731
    f0, f1 = features(pre), features(post)
    diff = [k for k in set(f0) | set(f1) if abs(f0.get(k, 0) - f1.get(k, 0)) > delta]
    cand = sorted({x for k in diff for x in k[1:] if x not in ("^", "$")})
    if not diff:
        return [], [], 0, "no difference", cand
    evals, minimum = 0, []
    for _ in range(6):  # expand the candidate pool when deleting the whole pool leaves a difference
        for size in range(1, len(cand) + 1):
            for combo in combinations(cand, size):
                evals += 1
                if evals > MAX_EVALS:
                    break
                if d(frozenset(combo)) <= delta:
                    minimum.append(sorted(combo))
            if minimum or evals > MAX_EVALS:
                break
        if minimum or evals > MAX_EVALS:
            break
        g0, g1 = features(pre, frozenset(cand)), features(post, frozenset(cand))
        extra = {x for k in set(g0) | set(g1) if abs(g0.get(k, 0) - g1.get(k, 0)) > delta
                 for x in k[1:] if x not in ("^", "$")} - set(cand)
        if not extra:
            break
        cand = sorted(set(cand) | extra)
    if minimum:
        union = sorted({a for m in minimum for a in m})
        return union, minimum, round(d(frozenset(union)), 4), "exact", cand
    chosen = set()  # greedy fallback
    while d(frozenset(chosen)) > delta:
        rest = [a for a in cand if a not in chosen]
        if not rest:
            break
        chosen.add(min(rest, key=lambda a: (d(frozenset(chosen | {a})), a)))
    for a in sorted(chosen):
        if d(frozenset(chosen - {a})) <= delta:
            chosen.discard(a)
    return sorted(chosen), [sorted(chosen)], round(d(frozenset(chosen)), 4), "greedy (search capped)", cand


def noise_delta(traces):
    return max(distance(features(variants(traces[x0:x1])), features(variants(traces[y0:y1])))
               for (x0, x1), (y0, y1) in STABLE_SPLITS)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", type=int, nargs="+", default=[1, 2, 3, 4, 5])
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for size in args.sizes:
        for pattern in PATTERNS:
            traces = read_mxml(OSTOVAR_FULL / f"Size{size}/Atomic/{pattern}/output/{pattern}.mxml.gz")
            delta = noise_delta(traces)
            for drift in (1, 2):
                s, minimum, final, method, cand = derive(traces, drift, delta)
                rows.append({"size": size, "pattern": pattern, "drift": drift, "delta": round(delta, 4),
                             "changed_projection": json.dumps(s), "minimum_sets": json.dumps(minimum),
                             "n_minimum_sets": len(minimum), "search": method, "candidates": json.dumps(cand),
                             "distance_after": final})
                print(size, pattern, drift, s, "min sets", len(minimum), method, "delta", round(delta, 3), flush=True)
    name = "projection_sizes" + "".join(map(str, args.sizes)) + ".csv"
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
