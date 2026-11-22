#!/usr/bin/env python3
"""P4 / E11b: test-retest of the blind Claude extractor (author approved 2026-11-15).

A second, independent extraction of the 100 explanations of the E11b sample (about 10% of the 1,056 explanations of
P2 run 1 for glm-5.3-flash and deepseek-v4-flash): rubric r5 for all 100, rubric r5a for the 24 CDLG rows. Same code,
rubric and settings as the first extraction (extract_e4.extract_r5, cdlg_roles.extract_roles); each call is a fresh
session, so the second pass does not see the first.

Output: results/p4_grading/extractor_repeat/{extractions_r5,extractions_r5a_cdlg}/<prompt>/<model>/run1/<case>.json
(same layout as results/p2_main). score_e11b.py adds the source "Claude_repeat" when these files exist.
"""
from __future__ import annotations

import csv
import json
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))
from cdlg_roles import extract_roles  # noqa: E402
from extract_e4 import UsageLimitReached, extract_r5  # noqa: E402

P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p4_grading" / "extractor_repeat"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"


def main():
    with (ROOT / "results" / "p4_grading" / "e11b_sample.csv").open(encoding="utf-8") as handle:
        sample = list(csv.DictReader(handle))
    jobs = []
    for s in sample:
        rel = Path(PROMPT) / s["model"] / "run1" / f"{s['case_id']}.json"
        jobs.append(("r5", P2 / "runs" / rel, OUT / "extractions_r5" / rel))
        if s["set"] == "cdlg":
            jobs.append(("r5a", P2 / "runs" / rel, OUT / "extractions_r5a_cdlg" / rel))
    jobs = [j for j in jobs if not j[2].exists()]
    print(f"{len(jobs)} extractions to run", flush=True)
    i = 0
    while i < len(jobs):
        kind, source, target = jobs[i]
        record = json.loads(source.read_text(encoding="utf-8"))
        try:
            result = extract_r5(record["text"]) if kind == "r5" else extract_roles(record["text"])
        except UsageLimitReached as exc:
            delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
            print(f"{datetime.now():%H:%M} usage limit; waiting {delay / 60:.0f} min", flush=True)
            time.sleep(delay)
            continue
        except Exception as exc:
            print(f"[{i + 1}/{len(jobs)}] error {kind} {source.stem}: {exc}", flush=True)
            i += 1
            continue
        result.update({"source": str(source.relative_to(ROOT)), "case_id": record["case_id"],
                       "generation_model": record.get("model"), "pass": "repeat"})
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{i + 1}/{len(jobs)}] {kind} {source.stem} ok", flush=True)
        i += 1
        time.sleep(2.0)


if __name__ == "__main__":
    main()
