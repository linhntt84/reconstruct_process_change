#!/usr/bin/env python3
"""DeepSeek reasoning traces of the submitted version (response to Reviewer 6, Concern 5a); no API calls.

Reads the archived version-1 DeepSeek responses (noise-free Ostovar and CDLG; run 1 = model2_* folders, runs 2 and 3 =
*_repeats_v1_repeat_1/2) and reports per run: median reasoning tokens, median length of the visible explanation
(characters), returned model identifiers, finish reasons and the dates of the calls.
Input: v1_submission/runs/ (public repository) or the path given as the first argument.
"""
from __future__ import annotations

import collections
import glob
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNS = {
    "run1": ["model2_deepseek_v4_flash_cdlg_integrated_100", "model2_deepseek_v4_flash_ostovar_integrated_26"],
    "run2": ["cdlg_deepseek_noise_0_integrated100_repeats_v1_repeat_1", "ostovar_deepseek_noise_0_repeats_v1_repeat_1"],
    "run3": ["cdlg_deepseek_noise_0_integrated100_repeats_v1_repeat_2", "ostovar_deepseek_noise_0_repeats_v1_repeat_2"],
}


def main():
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "v1_submission" / "runs"
    for run, folders in RUNS.items():
        reasoning, visible = [], []
        models, finish, dates = collections.Counter(), collections.Counter(), set()
        for folder in folders:
            for path in glob.glob(str(base / folder / "responses" / "*.json")):
                record = json.loads(Path(path).read_text(encoding="utf-8"))
                tokens = ((record.get("usage") or {}).get("completion_tokens_details") or {}).get("reasoning_tokens")
                if tokens is None:
                    continue
                reasoning.append(tokens)
                visible.append(len(record.get("visible_text") or ""))
                models[(record.get("raw_response") or {}).get("model")] += 1
                finish[record.get("finish_reason")] += 1
                dates.add((record.get("started_at_utc") or "")[:10])
        print(f"{run}: n={len(reasoning)} median reasoning tokens={statistics.median(reasoning)} "
              f"median visible chars={statistics.median(visible)} models={dict(models)} finish={dict(finish)} "
              f"dates={sorted(dates)}")


if __name__ == "__main__":
    main()
