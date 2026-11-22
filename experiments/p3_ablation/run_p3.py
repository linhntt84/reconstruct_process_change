#!/usr/bin/env python3
"""P3 ablations, steps 2-4: generation, extraction and scoring with the P2 code on results/p3_ablation/<exp>.

  python experiments/p3_ablation/run_p3.py <exp> generate --model glm-5.3-flash [--workers 4]   (PAID API CALLS)
  python experiments/p3_ablation/run_p3.py <exp> map-labels      (e8_labels only, before extraction)
  python experiments/p3_ablation/run_p3.py <exp> extract         (Claude, rubric r5)
  python experiments/p3_ablation/run_p3.py <exp> roles           (Claude, rubric r5a, CDLG cases only)
  python experiments/p3_ablation/run_p3.py <exp> score
Every command takes --run-index k (default 1).

The P2 modules read their base folder from a module constant OUT (and run_p2 the prompt from PROMPT); this
wrapper points them at the experiment folder, so P3 uses exactly the P2 generation, extraction and scoring code.
e3b_v2en uses prompts/INTERPRET_EVIDENCE_V2_EN.md; every other experiment the frozen R3-MP-CONC prompt.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
P3 = ROOT / "results" / "p3_ablation"
PROMPTS = {"e3b_v2en": ROOT / "prompts" / "INTERPRET_EVIDENCE_V2_EN.md"}
MODEL = "glm-5.3-flash"


def runs_dir(exp: str, prompt: Path, model: str = MODEL, run: int = 1) -> Path:
    return P3 / exp / "runs" / prompt.stem / model / f"run{run}"


def map_labels(exp: str, prompt: Path, run: int = 1):
    """E8: replace original activity names in the explanation by the P2 codes (longest names first)."""
    runs = runs_dir(exp, prompt, run=run)
    report = []
    for path in sorted(runs.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("status") != "success":
            continue
        original = record.get("text_original", record["text"])
        lm = json.loads((P3 / exp / "audit" / f"{record['case_id']}.json").read_text())["label_map"]
        text, counts = original, {}
        for name in sorted(lm, key=len, reverse=True):
            pattern = re.compile(r"(?<![\w])" + re.escape(name) + r"(?![\w])")
            text, n = pattern.subn(lm[name], text)
            if n:
                counts[name] = n
        stripped = {n[2:] for n in lm if n[:2] in ("A_", "O_", "W_")}  # names written without the prefix
        leftovers = sorted(s for s in stripped if re.search(r"(?<![\w])" + re.escape(s) + r"(?![\w])", text))
        record.update({"text_original": original, "text": text, "label_replacements": counts,
                       "label_leftovers": leftovers})
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        path.with_suffix(".md").write_text(text, encoding="utf-8")
        report.append((record["case_id"], sum(counts.values()), leftovers))
    for cid, n, left in report:
        print(f"{cid} replaced {n}" + (f"; names left without prefix: {left}" if left else ""))


def main():
    exp, cmd, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
    run = 1  # --run-index k selects run k for every command (runs 2-3 added 2026-11-15)
    if "--run-index" in rest:
        i = rest.index("--run-index")
        run = int(rest[i + 1])
        if cmd != "generate":
            del rest[i:i + 2]
    import run_p2
    prompt = PROMPTS.get(exp, run_p2.PROMPT)
    run_p2.OUT, run_p2.PROMPT = P3 / exp, prompt
    runs = str(runs_dir(exp, prompt, run=run))
    if cmd == "generate":
        sys.argv = ["run_p2.py", "generate", *rest]
        run_p2.main()
    elif cmd == "map-labels":
        map_labels(exp, prompt, run)
    elif cmd == "extract":
        sys.argv = ["run_p2.py", "extract", "--runs", runs, *rest]
        run_p2.main()
    elif cmd == "roles":
        import cdlg_roles
        cdlg_roles.OUT = P3 / exp
        sys.argv = ["cdlg_roles.py", "extract", "--runs", runs, *rest]
        cdlg_roles.main()
    elif cmd == "score":
        import score_p2
        score_p2.OUT = P3 / exp
        sys.argv = ["score_p2.py", "--runs", runs, *rest]
        score_p2.main()
        if (P3 / exp / "extractions_r5a_cdlg").exists():
            import cdlg_roles
            cdlg_roles.OUT = P3 / exp
            sys.argv = ["cdlg_roles.py", "score", "--runs", runs]
            cdlg_roles.main()
    else:
        sys.exit(f"unknown command {cmd}")


if __name__ == "__main__":
    main()
