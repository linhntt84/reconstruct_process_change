#!/usr/bin/env python3
"""E11a: evaluation references for Ostovar fragment sizes 1 and 5 (procedure in README.md).
  size 5: E0 rule (name-based conventions, valid for the shared base model of sizes 2-5); accepted because
          the independent projection derivation agrees on 26/26 required sets.
  size 1: role-based decisions in size1_decisions.json (both sources + trace inspection).
Writes data/references/ostovar_size{1,5}_references_v2.csv (one row per change and noise level, case ids
`ostovar_eval::size<k>::<pattern>::<noise>::<drift>`)."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from derive_projection import OSTOVAR_FULL, OUT, PATTERNS, ROOT, read_mxml  # noqa: E402
import build_tuning_references as rule  # noqa: E402

NOISE = (("0", ""), ("2.5", "_2"), ("5", "_5"))


def main():
    with (OUT / "compare_sizes12345.csv").open(encoding="utf-8") as h:
        comp = {(int(r["size"]), r["pattern"], int(r["drift"])): r for r in csv.DictReader(h)}
    decisions = json.loads((HERE / "size1_decisions.json").read_text())["cases"]
    for size in (1, 5):
        rows = []
        for pattern in PATTERNS:
            for drift in (1, 2):
                c = comp[(size, pattern, drift)]
                if size == 5:
                    assert c["agree_required"] == "True"
                    req, opt = json.loads(c["rule_required"]), json.loads(c["rule_optional"])
                    source = "E0 rule; projection agrees"
                else:
                    req, opt = decisions[pattern]["required"], decisions[pattern]["optional"]
                    source = "role-based decision (size1_decisions.json): " + decisions[pattern]["reason"]
                for noise, suffix in NOISE:
                    key = f"ostovar_eval::size{size}::{pattern}::{noise}::{drift}"
                    rows.append({"case_id": "case_" + hashlib.sha256(key.encode()).hexdigest()[:16],
                                 "split": "evaluation", "fragment_size": size, "change_pattern": pattern,
                                 "noise_pct": noise, "drift_sequence": drift, "anchor_trace": 900 if drift == 1 else 1900,
                                 "source_log": f"Size{size}/Atomic/{pattern}/output/{pattern}{suffix}.mxml.gz",
                                 "required_activities_real": json.dumps(req), "optional_activities_real": json.dumps(opt),
                                 "rule_required": c["rule_required"], "projection_required": c["projection_required"],
                                 "agree_required": c["agree_required"], "reference_source": source})
        path = ROOT / "data" / "references" / f"ostovar_size{size}_references_v2.csv"
        with path.open("w", encoding="utf-8", newline="") as h:
            w = csv.DictWriter(h, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        print(path, len(rows), "rows")


if __name__ == "__main__":
    main()
