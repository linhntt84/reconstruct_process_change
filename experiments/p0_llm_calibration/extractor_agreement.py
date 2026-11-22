#!/usr/bin/env python3
"""Repeatability of the blind extractor: agreement between two independent extractions
of the same explanations (score files from `score.py --tag <a>` and `--tag <b>`).

Reports raw agreement and Cohen's kappa for support level, pattern, mechanism family
(drift only), and agreement / mean absolute difference for O, MR and PI.
Usage: extractor_agreement.py r3rep1 r3rep2
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results" / "p0_llm_calibration"
FAMILY = {"SerialRemoval": "removal", "ParallelRemoval": "removal", "ConditionalRemoval": "removal",
          "SerialMove": "move", "ConditionalMove": "move", "ParallelMove": "move", "Swap": "move",
          "ConditionalToSequence": "to_sequence", "ParallelToSequence": "to_sequence",
          "Substitute": "substitute", "Loop": "loop", "Skip": "skip", "Frequency": "frequency"}


def load(tag: str) -> dict:
    with (OUT / f"scores_main_{tag}.csv").open(encoding="utf-8") as handle:
        return {(r["prompt"], r["model"], r["case_id"]): r for r in csv.DictReader(handle)}


def kappa(a: list, b: list) -> float:
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / n ** 2
    return float("nan") if pe == 1 else (po - pe) / (1 - pe)


def main():
    first, second = load(sys.argv[1]), load(sys.argv[2])
    keys = sorted(set(first) & set(second))
    drift = [k for k in keys if first[k]["kind"] == "drift"]
    print(f"paired outputs: {len(keys)} (drift {len(drift)})")
    for field, subset in (("support_level", keys), ("pattern", drift)):
        a = [first[k][field] for k in subset]
        b = [second[k][field] for k in subset]
        agree = sum(x == y for x, y in zip(a, b))
        print(f"{field:14s} agreement {agree}/{len(subset)} = {agree / len(subset):.3f}  kappa {kappa(a, b):.3f}")
    a = [FAMILY.get(first[k]["pattern"], "none") for k in drift]
    b = [FAMILY.get(second[k]["pattern"], "none") for k in drift]
    agree = sum(x == y for x, y in zip(a, b))
    print(f"{'family':14s} agreement {agree}/{len(drift)} = {agree / len(drift):.3f}  kappa {kappa(a, b):.3f}")
    for metric in ("O", "MR", "PI", "PI_alt"):
        x = [float(first[k][metric]) for k in drift]
        y = [float(second[k][metric]) for k in drift]
        same = sum(p == q for p, q in zip(x, y))
        print(f"{metric:14s} identical {same}/{len(drift)} = {same / len(drift):.3f}  "
              f"mean {sum(x) / len(x):.3f} vs {sum(y) / len(y):.3f}")
    print("disagreements (drift):")
    for k in drift:
        f, s = first[k], second[k]
        if f["pattern"] != s["pattern"] or f["O"] != s["O"]:
            print(f"  {k[0][-3:]} {k[2]} ref={f['reference_pattern']} "
                  f"pattern {f['pattern']}/{s['pattern']} O {f['O']}/{s['O']} PI {f['PI']}/{s['PI']}")


if __name__ == "__main__":
    main()
