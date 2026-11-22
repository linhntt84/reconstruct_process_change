#!/usr/bin/env python3
"""Run B: control-flow regression of prompt R3-MP against R3 on the 50 cases of the R3 check.

Both sets of outputs (R3: existing, read only; R3-MP: new) are extracted with the same
rubric r4 and scored like P0-C (O, MR, PI on required/optional references; null: share of
"insufficient"). Decision rule written before running (docs/NHAT_KY_E4_VI.md).

  python regression_cf.py extract
  python regression_cf.py score
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

OUT = E4_RESULTS / "e4a_time_injection" / "regression_cf"
CASES = REPO / "experiments" / "p0_llm_calibration" / "prompt_r3_check_cases.txt"
SOURCES = {
    "R3": REPO / "results" / "p0_llm_calibration" / "runs" / "INTERPRET_EVIDENCE_V2_EN_R3" / "B" / "glm-5.3-flash" / "run1",
    "R3_MP": OUT / "runs" / "INTERPRET_EVIDENCE_V2_EN_R3_MP" / "glm-5.3-flash" / "run1",
}


def case_ids() -> list[str]:
    return [c for c in CASES.read_text().split() if c]


def do_extract() -> None:
    for name, folder in SOURCES.items():
        target = OUT / "extractions_r4" / name
        target.mkdir(parents=True, exist_ok=True)
        todo = [c for c in case_ids() if not (target / f"{c}.json").exists()
                and (folder / f"{c}.json").exists()
                and json.loads((folder / f"{c}.json").read_text()).get("status") == "success"]
        print(f"{name}: {len(todo)} to extract", flush=True)
        i = 0
        while i < len(todo):
            record = json.loads((folder / f"{todo[i]}.json").read_text())
            try:
                result = extract_r4(record["text"])
            except UsageLimitReached as exc:
                delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
                print(f"usage limit, waiting {delay / 60:.0f} min", flush=True)
                time.sleep(delay)
                continue
            result.update({"case_id": todo[i], "source": str((folder / f"{todo[i]}.json").relative_to(REPO))})
            (target / f"{todo[i]}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"[{name} {i + 1}/{len(todo)}] {todo[i]} {result['extraction']['support_level']} "
                  f"{result['extraction'].get('pattern')}", flush=True)
            i += 1
            time.sleep(2)


def do_score() -> None:
    with (REPO / "results" / "e0_parameter_setting" / "tuning_references.csv").open(encoding="utf-8") as handle:
        refs = {r["case_id"]: r for r in csv.DictReader(handle)}
    rows = []
    for name in SOURCES:
        for c in case_ids():
            path = OUT / "extractions_r4" / name / f"{c}.json"
            if not path.exists():
                continue
            e = json.loads(path.read_text())["extraction"]
            audit = json.loads((REPO / "results" / "p0_llm_calibration" / "audit" / "B" / f"{c}.json").read_text())
            row = {"prompt": name, "case_id": c, "kind": audit["kind"], "support_level": e["support_level"],
                   "pattern": e.get("pattern", ""), "time_claim": float(bool(e.get("time_activities")))}
            if audit["kind"] == "drift":
                ref, lm = refs[c], audit["label_map"]
                required = {lm[a] for a in json.loads(ref["required_activities_real"]) if a in lm}
                optional = {lm[a] for a in json.loads(ref["optional_activities_real"]) if a in lm}
                o = object_score(set(e["central_activities"]), required, optional)
                truth, predicted = PATTERN_FAMILY[ref["change_pattern"]], PATTERN_FAMILY.get(e.get("pattern", ""), "")
                mr = min(o, float(predicted == truth))
                pi_raw = 1.0 if e.get("pattern") == ref["change_pattern"] else 0.5 if predicted == truth else 0.0
                row.update({"reference_pattern": ref["change_pattern"], "O": o, "MR": mr, "PI": min(o, mr, pi_raw)})
            rows.append(row)
    with (OUT / "scores.csv").open("w", encoding="utf-8", newline="") as handle:
        fields = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    paired = {}
    for r in rows:
        paired.setdefault(r["case_id"], {})[r["prompt"]] = r
    both = [d for d in paired.values() if len(d) == len(SOURCES)]
    drift = [d for d in both if d["R3"]["kind"] == "drift"]
    null = [d for d in both if d["R3"]["kind"] != "drift"]
    print(f"paired {len(both)} (drift {len(drift)}, null {len(null)})")
    for name in SOURCES:
        print(f"{name:6s} drift O={mean(d[name]['O'] for d in drift):.3f} MR={mean(d[name]['MR'] for d in drift):.3f} "
              f"PI={mean(d[name]['PI'] for d in drift):.3f} supported={sum(d[name]['support_level'] == 'supported' for d in drift)}/{len(drift)} "
              f"| null changed={sum(d[name]['support_level'] != 'insufficient' for d in null)}/{len(null)} "
              f"| time claims={sum(d[name]['time_claim'] for d in both):.0f}/{len(both)}")
    flips = [(d["R3"]["case_id"], d["R3"]["reference_pattern"], d["R3"]["pattern"], d["R3_MP"]["pattern"],
              d["R3"]["MR"], d["R3_MP"]["MR"]) for d in drift if d["R3"]["MR"] != d["R3_MP"]["MR"]]
    print("MR changes (case, reference, R3 pattern, R3-MP pattern, MR R3, MR R3-MP):")
    for f in flips:
        print("  ", f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("extract", "score"))
    do_extract() if parser.parse_args().action == "extract" else do_score()


if __name__ == "__main__":
    main()
