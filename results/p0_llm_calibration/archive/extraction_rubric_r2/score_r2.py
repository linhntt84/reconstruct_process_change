#!/usr/bin/env python3
"""P0-C step 4: score extractions on the tuning split.

Drift cases (policy as in version 1, object gate):
  O  = 1 if all required reference activities are named and none outside required/optional,
       0.5 if at least two thirds of the required set is named, else 0. Optional activities
       (pattern conventions, e.g. the Skip re-entry anchor) are neither credited nor penalized;
  MR = min(O, mechanism family correct);
  PI = min(O, MR, PI_raw), PI_raw = 1 for the exact pattern, 0.5 for the right family but
  another variant, 0 otherwise (paper, Section 5, and the v1 rubric).
  O is computed on the main hypothesis (central_activities, rubric r2). Activities the
  explanation claims as separate, additional changes (secondary_activities) do not enter O;
  they are reported as `overclaim` = 1 when any of them lies outside required/optional, and
  O_strict scores central + secondary together (the r1 behaviour) for comparison.
  With the vocabulary-free rubric the family comes from `mechanism`; PI is not defined.
Null pairs: share of explanations declaring "insufficient", "weak", "supported".
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pcr.paths import RESULTS  # noqa: E402

OUT = RESULTS / "p0_llm_calibration"
# Activities injected by the Ostovar noise generator (present only in the noisy logs). Diagnostic only.
NOISE_ACTIVITIES = {"ae", "be", "ce", "de", "ee"}
PATTERN_FAMILY = {"SerialRemoval": "removal", "ParallelRemoval": "removal", "ConditionalRemoval": "removal",
                  "SerialMove": "move", "ConditionalMove": "move", "ParallelMove": "move", "Swap": "move",
                  "ConditionalToSequence": "to_sequence", "ParallelToSequence": "to_sequence",
                  "Substitute": "substitute", "Loop": "loop", "Skip": "skip", "Frequency": "frequency"}
MECHANISM_FAMILY = {"fragment_added": "removal", "fragment_removed": "removal", "fragment_moved": "move",
                    "fragments_swapped": "move", "fragment_substituted": "substitute",
                    "choice_to_sequence": "to_sequence", "sequence_to_choice": "to_sequence",
                    "parallel_to_sequence": "to_sequence", "sequence_to_parallel": "to_sequence",
                    "became_repeated": "loop", "stopped_repeating": "loop", "became_optional": "skip",
                    "became_mandatory": "skip", "branch_frequency_changed": "frequency"}


def object_score(central: set[str], required: set[str], optional: set[str] = frozenset()) -> float:
    """1 if every required activity is named and nothing outside required or optional is;
    0.5 if at least two thirds of the required activities are named; else 0.
    Optional activities (pattern conventions such as anchors) are neither credited nor penalized."""
    correct = central & required
    extra = central - required - set(optional)
    if correct == required and not extra:
        return 1.0
    return 0.5 if len(correct) >= (2 * len(required) + 2) // 3 else 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=("main", "vocab_free"), default="main")
    args = parser.parse_args()
    with (RESULTS / "e0_parameter_setting" / "tuning_references.csv").open(encoding="utf-8") as handle:
        references = {r["case_id"]: r for r in csv.DictReader(handle)}
    rows = []
    for path in sorted((OUT / "extractions" / args.variant).rglob("*.json")):
        ex = json.loads(path.read_text(encoding="utf-8"))
        parts = path.relative_to(OUT / "extractions" / args.variant).parts  # prompt/config/model/run/case
        prompt, config, model, run = parts[:4]
        audit = json.loads((OUT / "audit" / config / f"{ex['case_id']}.json").read_text(encoding="utf-8"))
        e = ex["extraction"]
        row = {"prompt": prompt, "config": config, "model": model, "run": run, "case_id": ex["case_id"],
               "kind": audit["kind"], "noise": audit["meta"]["noise_pct"], "support_level": e["support_level"],
               "mechanism": e["mechanism"], "pattern": e.get("pattern", "")}
        if audit["kind"] == "drift":
            ref = references[ex["case_id"]]
            lm = audit["label_map"]
            required = {lm[a] for a in json.loads(ref["required_activities_real"]) if a in lm}
            optional = {lm[a] for a in json.loads(ref["optional_activities_real"]) if a in lm}
            central = set(e["central_activities"])
            secondary = set(e.get("secondary_activities", [])) - central
            o = object_score(central, required, optional)
            truth = PATTERN_FAMILY[ref["change_pattern"]]
            predicted = (PATTERN_FAMILY.get(e.get("pattern", ""), "") if args.variant == "main"
                         else MECHANISM_FAMILY.get(e["mechanism"], ""))
            mr = min(o, float(predicted == truth))
            pi_raw = 1.0 if e.get("pattern") == ref["change_pattern"] else 0.5 if predicted == truth else 0.0
            row.update({"reference_pattern": ref["change_pattern"], "O": o, "MR": mr,
                        "PI": min(o, mr, pi_raw) if args.variant == "main" else "",
                        "n_secondary": len(secondary),
                        "overclaim": float(bool(secondary - required - optional)),
                        "O_strict": object_score(central | secondary, required, optional),
                        "O_noise_optional": object_score(
                            central, required, optional | {lm[a] for a in NOISE_ACTIVITIES if a in lm})})
        rows.append(row)
    if not rows:
        sys.exit("no extractions yet")
    with (OUT / f"scores_{args.variant}.csv").open("w", encoding="utf-8", newline="") as handle:
        fields = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    groups = defaultdict(list)
    for r in rows:
        groups[(r["prompt"], r["config"], r["model"], r["kind"])].append(r)
    for (prompt, config, model, kind), items in sorted(groups.items()):
        levels = {lvl: mean(r["support_level"] == lvl for r in items) for lvl in ("insufficient", "weak", "supported")}
        text = " ".join(f"{k}={v:.2f}" for k, v in levels.items())
        if kind == "drift":
            text += " O={:.3f} MR={:.3f} overclaim={:.3f} O_strict={:.3f}".format(
                mean(r["O"] for r in items), mean(r["MR"] for r in items),
                mean(r["overclaim"] for r in items), mean(r["O_strict"] for r in items))
            if args.variant == "main":
                text += " PI={:.3f}".format(mean(r["PI"] for r in items))
        print(f"{prompt} {config} {model} {kind} n={len(items)} {text}")


if __name__ == "__main__":
    main()
