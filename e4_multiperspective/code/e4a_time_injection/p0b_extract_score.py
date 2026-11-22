#!/usr/bin/env python3
"""E4a step 4 (P0b), part 3: blind extraction (rubric r4) and scoring as pre-registered in
docs/NHAT_KY_E4_VI.md.

  python p0b_extract_score.py extract   # claude -p on every successful generation record
  python p0b_extract_score.py score     # writes p0b/scores.csv and prints a summary
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
from extract_e4 import UsageLimitReached, extract_r4  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "p0_llm_calibration"))
from score import PATTERN_FAMILY, object_score  # noqa: E402

DATA = E4_RESULTS / "e4a_time_injection"


def run_dirs(set_name: str):
    return sorted((DATA / set_name / "runs").glob("*/*/run*"))


def do_extract(set_name: str) -> None:
    for run_dir in run_dirs(set_name):
        out_dir = DATA / set_name / "extractions_r4" / run_dir.relative_to(DATA / set_name / "runs")
        out_dir.mkdir(parents=True, exist_ok=True)
        records = [p for p in sorted(run_dir.glob("*.json")) if json.loads(p.read_text()).get("status") == "success"]
        todo = [p for p in records if not (out_dir / p.name).exists()]
        print(f"{run_dir}: {len(records)} explanations, {len(todo)} to extract", flush=True)
        index = 0
        while index < len(todo):
            record = json.loads(todo[index].read_text())
            try:
                result = extract_r4(record["text"])
            except UsageLimitReached as exc:
                delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
                print(f"usage limit, waiting {delay / 60:.0f} min", flush=True)
                time.sleep(delay)
                continue
            result.update({"case_id": record["case_id"], "source": str(todo[index].relative_to(REPO))})
            (out_dir / todo[index].name).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            e = result["extraction"]
            print(f"[{index + 1}/{len(todo)}] {record['case_id']} {e['support_level']} {e.get('pattern')} "
                  f"time={e.get('time_activities')} {e.get('time_direction')}", flush=True)
            index += 1
            time.sleep(2)


def do_score(set_name: str) -> None:
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = {r["case_id"]: r for r in csv.DictReader(handle)}
    rows = []
    for path in sorted((DATA / set_name / "extractions_r4").rglob("*.json")):
        ex = json.loads(path.read_text())
        case = cases[ex["case_id"]]
        audit = json.loads((DATA / set_name / "audit" / f"{ex['case_id']}.json").read_text())
        lm = audit["label_map"]
        e = ex["extraction"]
        central, secondary = set(e["central_activities"]), set(e.get("secondary_activities", []))
        time_acts = set(e.get("time_activities", []))
        kind = case["type"]
        row = {"run": str(path.parent.relative_to(DATA / set_name / "extractions_r4")), "case_id": ex["case_id"],
               "type": kind, "support_level": e["support_level"], "mechanism": e["mechanism"],
               "pattern": e.get("pattern", ""), "time_activities": json.dumps(sorted(time_acts)),
               "time_direction": e.get("time_direction", ""), "perspectives": json.dumps(e.get("perspectives", []))}
        if kind == "N":
            row.update({"time_false_claim": float(bool(time_acts))})
        else:
            x = lm[case["time_target"]]
            preds = {lm[a] for a in json.loads(case["time_predecessors"]) if a in lm}
            direction_ok = e.get("time_direction") == case["time_direction"]
            row["time_detected"] = float(x in time_acts | central)
            if kind in ("T_SLOW", "T_FAST"):
                o = object_score(central, {x}, preds)
                mr = min(o, float(e["mechanism"] == "timing_changed" and "time" in e.get("perspectives", [])))
                pi = min(mr, float(direction_ok))
            else:  # M
                cf_req = {lm[a] for a in json.loads(case["cf_required"]) if a in lm}
                cf_opt = {lm[a] for a in json.loads(case["cf_optional"]) if a in lm}
                claimed = central | secondary | time_acts
                o = object_score(claimed, cf_req | {x}, cf_opt | preds)
                truth = PATTERN_FAMILY[case["cf_pattern"]]
                predicted = PATTERN_FAMILY.get(e.get("pattern", ""), "")
                mr = min(o, float(predicted == truth and x in time_acts))
                cf_pi_raw = 1.0 if e.get("pattern") == case["cf_pattern"] else 0.5 if predicted == truth else 0.0
                pi = min(mr, cf_pi_raw, float(direction_ok))
            row.update({"O": o, "MR": mr, "PI": pi, "time_direction_ok": float(direction_ok)})
        rows.append(row)
    fields = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
    with (DATA / set_name / "scores.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    for kind in ("T_SLOW", "T_FAST", "M", "N"):
        items = [r for r in rows if r["type"] == kind]
        if not items:
            continue
        levels = {lvl: sum(r["support_level"] == lvl for r in items) for lvl in ("insufficient", "weak", "supported")}
        text = f"{kind:6s} n={len(items)} {levels}"
        if kind == "N":
            text += f" time_false_claim={mean(r['time_false_claim'] for r in items):.2f}"
        else:
            text += " time_detected={:.2f} O={:.2f} MR={:.2f} PI={:.2f} dir_ok={:.2f}".format(
                *(mean(r[k] for r in items) for k in ("time_detected", "O", "MR", "PI", "time_direction_ok")))
        print(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("extract", "score"))
    parser.add_argument("--set", default="p0b")
    args = parser.parse_args()
    do_extract(args.set) if args.action == "extract" else do_score(args.set)


if __name__ == "__main__":
    main()
