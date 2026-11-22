#!/usr/bin/env python3
"""E4a step 5: rule-based baseline on multi-perspective evidence (design in docs/NHAT_KY_E4_VI.md).

Two variants, same evidence documents as the LLM:
  v1       the version-1 engine unchanged (experiments/e2_rule_baseline/engine_v1.py, read only);
           it has no rule for time items
  v1_time  v1 + R09_TWAIT: every T_WAIT item on a pair A -> B yields the claim "the time into B
           increased/decreased" (sign of the median change), mechanism timing_changed
Screening per family, one statistical principle for all families: a family counts as changed
when P(>= n items by chance | lambda = expected items of that family) < 0.01 (Poisson).
Output frame as the LLM (Observed differences / Inference / Support level); records in the
LLM record format under <set>/runs/RULE_BASELINE_E4_<variant>/rule-engine/run1/.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_RESULTS, REPO  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e2_rule_baseline"))
import engine_v1  # noqa: E402

DATA = E4_RESULTS / "e4a_time_injection"
ALPHA = 0.01


def chance_tail(n: int, lam: float) -> float:
    return 1.0 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(n))


def family_changed(n: int, lam: float) -> bool:
    return n > 0 and chance_tail(n, lam) < ALPHA


def time_claims(items: list[dict]) -> list[dict]:
    claims = []
    for it in items:
        a, b = it["analysis_unit"]["values"]
        before, after = it["components_before"]["median_hours"], it["components_after"]["median_hours"]
        direction = "increased" if after > before else "decreased"
        claims.append({"rule_id": "R09_TWAIT", "activities": [b], "evidence_ids": [it["id"]],
                       "explanation": f"The time from {a} to the completion of {b} {direction}: median "
                                      f"{before:.2f} h before versus {after:.2f} h after. This is consistent "
                                      f"with a change in the timing of {b}."})
    return claims


def render(document: dict, variant: str) -> tuple[str, str]:
    items = document.get("evidence", [])
    cf_items = [i for i in items if i["indicator"] != "T_WAIT"]
    tw_items = [i for i in items if i["indicator"] == "T_WAIT"]
    fam = document["screening"].get("by_family", {
        "control_flow": {"items": len(cf_items),
                         "items_expected_without_change": document["screening"]["items_expected_without_change"]},
        "time": {"items": 0, "items_expected_without_change": 0.0}})
    cf_ok = family_changed(len(cf_items), fam["control_flow"]["items_expected_without_change"])
    tw_ok = variant == "v1_time" and family_changed(len(tw_items), fam["time"]["items_expected_without_change"])
    result = engine_v1.interpret(cf_items)
    claims = (result["claims"] if cf_ok else []) + (time_claims(tw_items) if tw_ok else [])
    lines = ["### Observed differences", ""]
    if not items:
        lines.append("The evidence establishes no behavioural difference at the configured thresholds.")
    else:
        lines += [f"- {o['text']} [{o['evidence_id']}]" for o in engine_v1.interpret(items)["observations"]]
        for name, f in fam.items():
            lines.append(f"- {name.replace('_', ' ')}: {f['items']} items qualified; about "
                         f"{f['items_expected_without_change']:.3f} expected without any change.")
    lines += ["", "### Inference", ""]
    if not claims:
        level = "insufficient evidence"
        lines += ["Support level: Insufficient evidence", "",
                  "The evidence is insufficient to infer a change in the process."]
    else:
        level = "supported hypothesis"
        lines += ["Support level: Supported hypothesis", ""]
        lines += [f"- {c['explanation']} [{', '.join(c['evidence_ids'])}]" for c in claims]
        lines += ["", "Rule matches are hypotheses based on the qualified evidence, not proof of the "
                  "underlying process change; several matches may reflect one change."]
    return "\n".join(lines) + "\n", level


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", default="p0b_mp")
    args = parser.parse_args()
    for variant in ("v1", "v1_time"):
        out = DATA / args.set / "runs" / f"RULE_BASELINE_E4_{variant}" / "rule-engine" / "run1"
        out.mkdir(parents=True, exist_ok=True)
        counts = {}
        for path in sorted((DATA / args.set / "evidence").glob("*.json")):
            document = json.loads(path.read_text())
            text, level = render(document, variant)
            record = {"status": "success", "model": "rule-engine", "variant": variant, "case_id": path.stem,
                      "evidence_path": str(path.relative_to(REPO)), "text": text, "support_level": level,
                      "screening_rule": f"Poisson tail per family < {ALPHA}", "run_index": "1"}
            (out / f"{path.stem}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
            (out / f"{path.stem}.md").write_text(text, encoding="utf-8")
            counts[level] = counts.get(level, 0) + 1
        print(variant, counts)


if __name__ == "__main__":
    main()
