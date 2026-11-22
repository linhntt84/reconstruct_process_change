#!/usr/bin/env python3
"""E11a: compare the two derivations of Ostovar references (and the author's size-3 labels).
  rule        E0 per-activity statistics (experiments/e0_parameter_setting/build_tuning_references.py)
  projection  minimum deleting set (derive_projection.py)
  author      size 3 only: data/references/ostovar_size3_atomic_object_ground_truth_v2.csv
The same pattern conventions (required / optional) are applied to every source, so the comparison is on
the required set; optional activities are listed. Output: results/e11a_ostovar_references/compare_sizes<sizes>.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from derive_projection import OSTOVAR_FULL, OUT, PATTERNS, ROOT, read_mxml  # noqa: E402
import build_tuning_references as rule  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", type=int, nargs="+", default=[1, 2, 3, 4, 5])
    args = parser.parse_args()
    author = {}
    with (ROOT / "data/references/ostovar_size3_atomic_object_ground_truth_v2.csv").open(encoding="utf-8") as h:
        for r in csv.DictReader(h):
            author[(r["change_pattern"], int(r["drift_sequence"]))] = sorted(json.loads(r["affected_activities_real"]))
    tag = "".join(map(str, args.sizes))
    with (OUT / f"projection_sizes{tag}.csv").open(encoding="utf-8") as h:
        proj = {(int(r["size"]), r["pattern"], int(r["drift"])): r for r in csv.DictReader(h)}
    rows = []
    for size in args.sizes:
        for pattern in PATTERNS:
            traces = read_mxml(OSTOVAR_FULL / f"Size{size}/Atomic/{pattern}/output/{pattern}.mxml.gz")
            for drift in (1, 2):
                changed_rule = rule.changed_activities(traces, drift)
                r_req, r_opt = rule.required_optional(pattern, size, changed_rule)
                p = proj[(size, pattern, drift)]
                p_req, p_opt = rule.required_optional(pattern, size, {a: [] for a in json.loads(p["changed_projection"])})
                row = {"size": size, "pattern": pattern, "drift": drift,
                       "rule_required": json.dumps(r_req), "projection_required": json.dumps(p_req),
                       "rule_optional": json.dumps(r_opt), "projection_optional": json.dumps(p_opt),
                       "agree_required": r_req == p_req,
                       "only_rule": json.dumps(sorted(set(r_req) - set(p_req))),
                       "only_projection": json.dumps(sorted(set(p_req) - set(r_req))),
                       "projection_minimum_sets": p["minimum_sets"], "projection_search": p["search"],
                       "rule_evidence": json.dumps({a: changed_rule.get(a, []) for a in sorted(set(r_req) | set(p_req))})}
                if size == 3:
                    a_req = sorted(set(author[(pattern, drift)]) - set(r_opt) - set(p_opt))
                    row.update({"author_v2": json.dumps(author[(pattern, drift)]),
                                "rule_matches_author": rule.reference(pattern, size, changed_rule) == author[(pattern, drift)],
                                "projection_matches_author": rule.reference(pattern, size, {a: [] for a in json.loads(p["changed_projection"])}) == author[(pattern, drift)]})
                rows.append(row)
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with (OUT / f"compare_sizes{tag}.csv").open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    for size in args.sizes:
        rs = [r for r in rows if r["size"] == size]
        line = f"size {size}: rule = projection on required set {sum(r['agree_required'] for r in rs)}/{len(rs)}"
        if size == 3:
            line += (f"; rule = author {sum(r['rule_matches_author'] for r in rs)}/{len(rs)}"
                     f"; projection = author {sum(r['projection_matches_author'] for r in rs)}/{len(rs)}")
        print(line)
        for r in rs:
            if not r["agree_required"] or (size == 3 and not r["projection_matches_author"]):
                print("   ", r["pattern"], r["drift"], "only rule", r["only_rule"], "only projection", r["only_projection"],
                      "| author", r.get("author_v2", ""))


if __name__ == "__main__":
    main()
