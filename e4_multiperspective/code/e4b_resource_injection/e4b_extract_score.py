#!/usr/bin/env python3
"""E4b: blind extraction with rubric r5 and scoring with the measures written before running
(docs/NHAT_KY_E4_VI.md, design A + B): target_claimed, target_main, background resource claims.

  python e4b_extract_score.py extract [--set p0b]
  python e4b_extract_score.py score   [--set p0b]
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_RESULTS, REPO  # noqa: E402
from extract_e4 import UsageLimitReached, extract_r5  # noqa: E402

DATA = E4_RESULTS / "e4b_resource_injection"
RESOURCE_MECHANISMS = {"resource_allocation_changed", "handover_changed"}


def do_extract(set_name: str) -> None:
    for run_dir in sorted((DATA / set_name / "runs").glob("*/*/run*")):
        out = DATA / set_name / "extractions_r5" / run_dir.relative_to(DATA / set_name / "runs")
        out.mkdir(parents=True, exist_ok=True)
        todo = [p for p in sorted(run_dir.glob("*.json")) if not (out / p.name).exists()
                and json.loads(p.read_text()).get("status") == "success"]
        print(f"{run_dir.name}: {len(todo)} to extract", flush=True)
        i = 0
        while i < len(todo):
            record = json.loads(todo[i].read_text())
            try:
                result = extract_r5(record["text"])
            except UsageLimitReached as exc:
                delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
                time.sleep(delay)
                continue
            result.update({"case_id": record["case_id"], "source": str(todo[i].relative_to(REPO))})
            (out / todo[i].name).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            e = result["extraction"]
            print(f"[{i + 1}/{len(todo)}] {record['case_id']} {e['mechanism']} res={e.get('resource_activities')}", flush=True)
            i += 1
            time.sleep(2)


def do_score(set_name: str) -> None:
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = {r["case_id"]: r for r in csv.DictReader(handle)}
    rows = []
    for path in sorted((DATA / set_name / "extractions_r5").rglob("*.json")):
        ex = json.loads(path.read_text())
        case = cases[ex["case_id"]]
        lm = json.loads((DATA / set_name / "audit" / f"{ex['case_id']}.json").read_text())["label_map"]
        e = ex["extraction"]
        central, secondary = set(e["central_activities"]), set(e.get("secondary_activities", []))
        res = set(e.get("resource_activities", []))
        row = {"run": str(path.parent.relative_to(DATA / set_name / "extractions_r5")), "case_id": ex["case_id"],
               "type": case["type"], "support_level": e["support_level"], "mechanism": e["mechanism"],
               "perspectives": json.dumps(e.get("perspectives", [])), "resource_activities": json.dumps(sorted(res)),
               "n_resource_claims": len(res)}
        if case["type"] != "N":
            x = lm[case["target"]]
            row["target_claimed"] = float(x in (res | central | secondary) and "resource" in e.get("perspectives", []))
            row["target_main"] = float(x in central and e["mechanism"] in RESOURCE_MECHANISMS)
            row["other_resource_claims"] = len(res - {x})
        rows.append(row)
    with (DATA / set_name / "scores.csv").open("w", encoding="utf-8", newline="") as handle:
        fields = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    for kind in ("R1_REASSIGN", "R2_CONSOLIDATE", "R4_SHRINK", "N"):
        items = [r for r in rows if r["type"] == kind]
        if not items:
            continue
        text = f"{kind:15s} n={len(items)} supported={sum(r['support_level'] == 'supported' for r in items)} " \
               f"resource claims/case={mean(r['n_resource_claims'] for r in items):.1f}"
        if kind != "N":
            text += f" target_claimed={mean(r['target_claimed'] for r in items):.2f} " \
                    f"target_main={mean(r['target_main'] for r in items):.2f}"
        print(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("extract", "score"))
    parser.add_argument("--set", default="p0b")
    args = parser.parse_args()
    do_extract(args.set) if args.action == "extract" else do_score(args.set)


if __name__ == "__main__":
    main()
