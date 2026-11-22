#!/usr/bin/env python3
"""Table "Localization and qualified evidence on the evaluation changes" (Section VII-D); no API calls.

Per evaluation set and noise level, over the drift cases of results/p2_main/cases.csv:
  Scope   |A*| / number of activities observed in the window pair (label map), mean over cases
  Recall  share of the required reference activities inside A*, mean
  Cover.  share of the required reference activities that occur as a unit of at least one qualified item in E*, mean
  |E*|    number of qualified evidence items, median
  Prompt  median prompt tokens of the GLM explanations (run 1)
Required references: Ostovar as score_p2.ostovar_references (required, without the optional activities);
CDLG: added | deleted | moved of the version-1 references, restricted to observed activities (cases with no
observed reference activity are excluded, n = 99).
Output: results/p5_stats/localization_table.{csv,md}.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(ROOT / "experiments" / "p0_llm_calibration"))
from score_p2 import cdlg_references, ostovar_references  # noqa: E402

P2 = ROOT / "results" / "p2_main"
RUN = P2 / "runs" / "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC" / "glm-5.3-flash" / "run1"
OUT = ROOT / "results" / "p5_stats"
SETS = {"ostovar3": "Ostovar 3", "ostovar5": "Ostovar 5", "cdlg": "CDLG"}


def units(item: dict) -> set[str]:
    unit = item.get("analysis_unit", {})
    if isinstance(unit.get("values"), list):  # pair units (REL, LAG, T_WAIT)
        return {v for v in unit["values"] if isinstance(v, str)}
    return {unit["value"]} if isinstance(unit.get("value"), str) else set()


def main():
    ost = ostovar_references()
    cdlg = cdlg_references()
    groups = defaultdict(list)
    with (P2 / "cases.csv").open(encoding="utf-8") as handle:
        for case in csv.DictReader(handle):
            if case["set"] not in SETS or case["kind"] != "drift":
                continue
            cid = case["case_id"]
            audit = json.loads((P2 / "audit" / f"{cid}.json").read_text())
            lm = audit["label_map"]
            if case["set"] == "cdlg":
                r = cdlg[cid]
                real = set().union(*(json.loads(r[k]) for k in
                                     ("activities_added_real", "activities_deleted_real", "activities_moved_real")))
            else:
                real = ost[cid][1]
            required = {lm[a] for a in real if a in lm}
            if not required:
                continue
            region = set(audit["localized_activities"])
            evidence = json.loads((P2 / "evidence" / f"{cid}.json").read_text())["evidence"]
            covered = set().union(*(units(e) for e in evidence)) if evidence else set()
            record = json.loads((RUN / f"{cid}.json").read_text())
            groups[(case["set"], float(case["noise_pct"]))].append({
                "scope": len(region) / len(lm),
                "recall": len(required & region) / len(required),
                "coverage": len(required & covered) / len(required),
                "e_size": len(evidence),
                "prompt": record["usage"]["prompt_tokens"],
            })
    rows = []
    for (s, noise), cases in sorted(groups.items(), key=lambda x: (list(SETS).index(x[0][0]), x[0][1])):
        rows.append({"set": SETS[s], "noise_pct": noise, "n": len(cases),
                     "scope": round(mean(c["scope"] for c in cases), 3),
                     "recall": round(mean(c["recall"] for c in cases), 3),
                     "coverage": round(mean(c["coverage"] for c in cases), 3),
                     "median_e_size": median(c["e_size"] for c in cases),
                     "median_prompt_tokens": median(c["prompt"] for c in cases)})
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "localization_table.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    md = ["| Set | Noise | n | Scope | Recall | Cover. | |E*| (med.) | Prompt (med.) |", "|---|---|---|---|---|---|---|---|"]
    md += [f"| {r['set']} | {r['noise_pct']:g}% | {r['n']} | {r['scope']:.3f} | {r['recall']:.3f} | {r['coverage']:.3f} | "
           f"{r['median_e_size']:.1f} | {r['median_prompt_tokens'] / 1000:.1f}k |" for r in rows]
    (OUT / "localization_table.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
