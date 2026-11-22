#!/usr/bin/env python3
"""E0: derive affected-activity references for held-out Ostovar fragment sizes.

Ostovar fragment sizes 2-5 share one base model; only the changed fragment
grows (e.g. SerialMove: p1,p2 -> p1,p2,p7 -> p1,p2,p7,p8 -> ...). Size 1 uses a
different base model and is not handled here.

The rule is deterministic and computed on the noise-free log only, from long
stable segments far from the evaluation windows:
  drift 1: pre=[0,850), post=[1050,1850); drift 2: pre=[1050,1850), post=[2050,2999)

An activity is structurally changed if it is added/deleted, its case-presence
changes by >= 0.10, its mean occurrences per trace change by >= 0.20, or both
its directly-follows predecessor and successor sets change (edge support > 1%).
For scoring (pipeline v2) the reference is split into required activities (changed,
without conventions) and optional ones (decided by a convention; neither credited nor
penalized). `affected_activities_real` keeps the version-1 convention set.
Pattern conventions copied from the frozen size-3 reference:
  - Conditional/Parallel Move/Removal: drop the 'o*' partner-branch activity.
  - ConditionalToSequence: drop the sibling conditional branch p5..p(4+k).
  - Skip: add the re-entry anchor o1.
The rule is validated by reproducing the frozen size-3 reference before use.
No LLM, no evaluation-set tuning.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from pcr.logs import read_mxml  # noqa: E402
from pcr.paths import OSTOVAR_FULL, REFERENCES, RESULTS  # noqa: E402

FROZEN_SIZE3 = REFERENCES / "ostovar_size3_atomic_object_ground_truth_v1.csv"
OUT = RESULTS / "e0_parameter_setting"
PATTERNS = ["ConditionalMove", "ConditionalRemoval", "ConditionalToSequence", "Frequency",
            "Loop", "ParallelMove", "ParallelRemoval", "ParallelToSequence", "SerialMove",
            "SerialRemoval", "Skip", "Substitute", "Swap"]
SEGMENTS = {1: ((0, 850), (1050, 1850)), 2: ((1050, 1850), (2050, 2999))}
EDGE_EPS, PRESENCE_DELTA, COUNT_DELTA = 0.01, 0.10, 0.20



def segment_stats(traces):
    n = len(traces)
    presence, counts, edges = Counter(), Counter(), Counter()
    for trace in traces:
        presence.update(set(trace))
        counts.update(trace)
        edges.update(set(zip(trace, trace[1:])))
    return ({a: c / n for a, c in presence.items()}, {a: c / n for a, c in counts.items()},
            {e: c / n for e, c in edges.items()})


def changed_activities(traces, drift):
    (a0, a1), (b0, b1) = SEGMENTS[drift]
    p0, c0, e0 = segment_stats(traces[a0:a1])
    p1, c1, e1 = segment_stats(traces[b0:b1])
    changed = {}
    for a in sorted(set(p0) | set(p1)):
        preds = [{x for (x, y), v in e.items() if y == a and v > EDGE_EPS} for e in (e0, e1)]
        succs = [{y for (x, y), v in e.items() if x == a and v > EDGE_EPS} for e in (e0, e1)]
        reasons = []
        if p0.get(a, 0) <= EDGE_EPS < p1.get(a, 0):
            reasons.append("added")
        if p1.get(a, 0) <= EDGE_EPS < p0.get(a, 0):
            reasons.append("deleted")
        if abs(p0.get(a, 0) - p1.get(a, 0)) >= PRESENCE_DELTA:
            reasons.append(f"presence {p0.get(a, 0):.2f}->{p1.get(a, 0):.2f}")
        if abs(c0.get(a, 0) - c1.get(a, 0)) >= COUNT_DELTA:
            reasons.append(f"count {c0.get(a, 0):.2f}->{c1.get(a, 0):.2f}")
        if preds[0] != preds[1] and succs[0] != succs[1]:
            reasons.append("pred+succ changed")
        if reasons:
            changed[a] = reasons
    return changed


def reference(pattern, size, changed):
    ref = set(changed)
    if pattern in {"ConditionalMove", "ConditionalRemoval", "ParallelMove", "ParallelRemoval"}:
        ref = {a for a in ref if not a.startswith("o")}
    if pattern == "ConditionalToSequence":
        ref -= {f"p{i}" for i in range(5, 5 + size)}
    if pattern == "Skip":
        ref.add("o1")
    return sorted(ref)


def required_optional(pattern, size, changed):
    """Split for scoring: required = structurally changed without the pattern conventions;
    optional = activities whose inclusion the conventions decide (neither credited nor penalized)."""
    changed_set = set(changed)
    optional = set()
    if pattern in {"ConditionalMove", "ConditionalRemoval", "ParallelMove", "ParallelRemoval"}:
        optional = {a for a in changed_set if a.startswith("o")}
    if pattern == "ConditionalToSequence":
        optional = {f"p{i}" for i in range(5, 5 + size)}
    if pattern == "Skip":
        optional = {"o1"}
    return sorted(changed_set - optional), sorted(optional)


def case_id(size, pattern, noise, drift):
    key = f"ostovar_tuning::size{size}::{pattern}::{noise}::{drift}"
    return "case_" + hashlib.sha256(key.encode()).hexdigest()[:16]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", type=int, nargs="+", default=[2, 4, 5])
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    frozen = {}
    with FROZEN_SIZE3.open(encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            frozen[(row["change_pattern"], int(row["drift_sequence"]))] = sorted(
                json.loads(row["affected_activities_real"]))

    validation, rows = [], []
    for size in sorted({3, *args.sizes}):
        for pattern in PATTERNS:
            traces = read_mxml(OSTOVAR_FULL / f"Size{size}/Atomic/{pattern}/output/{pattern}.mxml.gz")
            for drift in (1, 2):
                changed = changed_activities(traces, drift)
                ref = reference(pattern, size, changed)
                required, optional = required_optional(pattern, size, changed)
                if size == 3:
                    validation.append({"pattern": pattern, "drift": drift, "derived": json.dumps(ref),
                                       "frozen": json.dumps(frozen[(pattern, drift)]),
                                       "match": ref == frozen[(pattern, drift)]})
                    continue
                for noise, suffix in (("0", ""), ("2.5", "_2"), ("5", "_5")):
                    rows.append({
                        "case_id": case_id(size, pattern, noise, drift), "split": "tuning",
                        "fragment_size": size, "change_pattern": pattern, "noise_pct": noise,
                        "drift_sequence": drift, "anchor_trace": 900 if drift == 1 else 1900,
                        "source_log": f"Size{size}/Atomic/{pattern}/output/{pattern}{suffix}.mxml.gz",
                        "affected_activities_real": json.dumps(ref),
                        "required_activities_real": json.dumps(required),
                        "optional_activities_real": json.dumps(optional),
                        "derivation": json.dumps({a: changed.get(a, ["pattern convention"]) for a in ref},
                                                 ensure_ascii=False),
                    })

    for name, data in (("size3_reference_rule_validation.csv", validation),
                       ("tuning_references.csv", rows)):
        with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    mismatches = [v for v in validation if not v["match"]]
    print(f"Size-3 validation: {len(validation) - len(mismatches)}/{len(validation)} match")
    for v in mismatches:
        print("  MISMATCH", v["pattern"], v["drift"], "derived", v["derived"], "frozen", v["frozen"])
    print(f"Wrote {len(rows)} tuning cases to {OUT / 'tuning_references.csv'}")


if __name__ == "__main__":
    main()
