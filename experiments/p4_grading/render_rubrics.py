#!/usr/bin/env python3
"""Write the extraction rubric exactly as the extractor receives it; no API calls.

The rubric files contain placeholders ({{PATTERN_FIELD}} and three alternative-pattern hints) that the code fills
at run time with the list of the 13 Ostovar patterns (src/pcr/extract.PATTERN_FIELD). This script fills them the same
way for rubric r5, which produced every reported extraction (e4_multiperspective/code/extract_e4.extract_r5), so the
measurement instrument can be read as one standalone document.
Output: prompts/EXTRACTION_RUBRIC_R5_RENDERED_EN.md
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))
import extract_e4  # noqa: E402

OUT = ROOT / "prompts" / "EXTRACTION_RUBRIC_R5_RENDERED_EN.md"


def main():
    extract_e4.RUBRIC_R4 = extract_e4.RUBRIC_R5  # extract_r5 renders r5 through system_prompt_r4
    body = extract_e4.system_prompt_r4("main")
    header = ("# Extraction rubric r5, as sent to the extractor\n\n"
              "Rendered by `experiments/p4_grading/render_rubrics.py` from "
              "`e4_multiperspective/code/EXTRACTION_RUBRIC_E4_R5_EN.md` with the pattern list of "
              "`src/pcr/extract.py`. This is the system prompt of every reported extraction "
              "(Claude Opus 5.5, `claude-opus-5-5`); the explanation is passed as the user message.\n\n---\n\n")
    OUT.write_text(header + body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(body)} characters)")


if __name__ == "__main__":
    main()
