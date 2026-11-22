#!/usr/bin/env python3
"""E1 step 3: score ProDrift characterizations with the same metrics as pipeline v2
(O, MR, PI; references split into required/optional activities).

Deterministic mapping, fixed before scoring and independent of the references:
  * each ProDrift statement -> (pattern, subject activities); subject activities are the
    leaves of the fragment trees the statement names (or the named activities);
      moved, both positions sequential        -> SerialMove
      moved into/out of a conditional branch  -> ConditionalMove
      moved into/out of a parallel branch     -> ParallelMove
      two moved statements exchanging places  -> Swap
      inserted/removed (sequential/conditional/parallel branch) -> Serial/Conditional/ParallelRemoval
      substituted                             -> Substitute (old and new fragment)
      (not) loopable                          -> Loop
      (not) skippable                         -> Skip
      conditional <-> sequential              -> ConditionalToSequence
      parallel <-> sequential                 -> ParallelToSequence
  * main hypothesis: a Swap pair if present; otherwise the statement whose subject has the
    most activities (ties: first statement). Other statements are secondary changes, like
    `secondary_activities` of the LLM extraction (they enter O_strict and overclaim, not O).
  * drift matching: reference drift k (cp = 900/1900) is matched to the first ProDrift
    detection with detected trace in [cp, cp + 500); unmatched drifts and drifts without
    statements score 0.
References: the deterministic rule of E0 (`build_tuning_references.py`), for every size it
supports (2-5). Size 1 needs its own conventions (pending, E11a).
Sensitivity variants of O as for the LLM: O_strict, O_noise_optional, O_F1 (see score.py).
Output: results/e1_prodrift/scores.csv and a summary on stdout.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
sys.path.insert(0, str(ROOT / "experiments" / "p0_llm_calibration"))
import build_tuning_references as refrule  # noqa: E402
from pcr.logs import read_mxml  # noqa: E402
from pcr.paths import OSTOVAR_FULL, RESULTS  # noqa: E402
from score import NOISE_ACTIVITIES, PATTERN_FAMILY, object_f1, object_score  # noqa: E402

OUT = RESULTS / "e1_prodrift"
OPERATORS = {"Seq", "XOR", "AND", "XorLoop", "OR", "tau", "DRIFT_PO"}
CPS = {1: 900, 2: 1900}
MATCH_SPAN = 500
REF_CACHE = OUT / "references_sizes2to5.csv"


def leaves(tree: str) -> set[str]:
    return {t for t in re.findall(r"[A-Za-z0-9_]+", tree) if t not in OPERATORS}


def subject_items(text: str) -> list[str]:
    return re.findall(r"(Fragment \d+|Activity \S+?)(?=,| and | were| was| is| in |$)", text)


def activities_of(item: str, fragments: dict) -> set[str]:
    if item.startswith("Activity "):
        name = item.split(" ", 1)[1]
        return set() if name in OPERATORS else {name}
    tree = fragments.get(item)
    return (leaves(tree["left"]) | leaves(tree["right"])) if tree else set()


def classify(statement: str, fragments: dict) -> dict:
    s = statement.strip()
    body = s.split(", while after the drift")[0]
    head = re.sub(r"^(Before|After) the drift, ", "", body)
    if " is substituted by " in s:
        m = re.match(r"After the drift, (.+?) in Fragment \d+ is substituted by (.+?)\.$", s)
        items = [m.group(1), m.group(2)] if m else []
        return {"pattern": "Substitute", "items": items}
    if ("loopable" in s and "loopback" not in s) or "skippable" in s:
        # singular ("Fragment 3 was ...") or plural ("Fragment 16, and Activity e were ...")
        subject = re.split(r" (?:was|were) ", head, maxsplit=1)[0]
        items = re.findall(r"Fragment \d+|Activity [^,\s]+", subject)
        return {"pattern": "Loop" if "loopable" in s else "Skip", "items": items}
    m = re.match(r"Before the drift, (.+) were (conditional|parallel|sequential), while after the drift "
                 r"they are (conditional|parallel|sequential)", s)
    if m:
        kinds = {m.group(2), m.group(3)}
        items = re.findall(r"Fragment \d+|Activity [^,\s]+", m.group(1))
        return {"pattern": "ParallelToSequence" if "parallel" in kinds else "ConditionalToSequence", "items": items}
    if " is inserted in " in s or "it is removed" in s:
        subject = re.match(r"(?:After the drift, )?(Fragment \d+|Activity \S+) (?:is inserted|was in)", head)
        context = s
        variant = ("ConditionalRemoval" if "conditional branch" in context
                   else "ParallelRemoval" if "parallel branch" in context else "SerialRemoval")
        return {"pattern": variant, "items": [subject.group(1)] if subject else []}
    if "has moved to" in s:
        subject = re.match(r"(Fragment \d+|Activity \S+) was in", head)
        before = s.split(", while after the drift")[0]
        after = s.split("has moved to", 1)[1]
        places = []
        for part in (before, after):
            places.append("conditional" if "conditional branch" in part else
                          "parallel" if "parallel branch" in part else
                          "loop" if "loop" in part else "sequence")
        variant = ("ConditionalMove" if "conditional" in places else
                   "ParallelMove" if "parallel" in places else
                   "Loop" if "loop" in places else "SerialMove")
        old = re.search(r"was in (Fragment \d+ (?:between .+?|in a .+?|before .+?|after .+?))(?:, while)", s)
        new = re.search(r"has moved to (Fragment \d+.*?)\.?$", s)
        return {"pattern": variant, "items": [subject.group(1)] if subject else [],
                "from": old.group(1).strip() if old else "", "to": new.group(1).strip() if new else ""}
    return {"pattern": "other", "items": []}


def characterize(statements: list[str], fragments: dict) -> dict:
    parsed = []
    for st in statements:
        c = classify(st, fragments)
        c["activities"] = set().union(*(activities_of(i, fragments) for i in c["items"])) if c["items"] else set()
        c["statement"] = st
        parsed.append(c)
    if not parsed:
        return {"pattern": "none", "central": set(), "secondary": set(), "n_statements": 0}
    moves = [p for p in parsed if p["pattern"].endswith("Move") and p.get("from") and p.get("to")]
    for i, a in enumerate(moves):
        for b in moves[i + 1:]:
            if a["from"].split(" ", 2)[-1] == b["to"].split(" ", 2)[-1] and \
                    a["to"].split(" ", 2)[-1] == b["from"].split(" ", 2)[-1]:
                main = [a, b]
                central = a["activities"] | b["activities"]
                rest = [p for p in parsed if p not in main]
                return {"pattern": "Swap", "central": central,
                        "secondary": set().union(*(p["activities"] for p in rest)) - central if rest else set(),
                        "n_statements": len(parsed)}
    main = max(parsed, key=lambda p: (len(p["activities"]), -parsed.index(p)))
    rest = [p for p in parsed if p is not main]
    return {"pattern": main["pattern"], "central": main["activities"],
            "secondary": set().union(*(p["activities"] for p in rest)) - main["activities"] if rest else set(),
            "n_statements": len(parsed)}


def references() -> dict:
    """(size, pattern, drift) -> (required, optional). Sizes 2-5 via the E0 rule."""
    if not REF_CACHE.exists():
        rows = []
        for size in (2, 3, 4, 5):
            for pattern in refrule.PATTERNS:
                traces = read_mxml(OSTOVAR_FULL / f"Size{size}/Atomic/{pattern}/output/{pattern}.mxml.gz")
                for drift in (1, 2):
                    changed = refrule.changed_activities(traces, drift)
                    required, optional = refrule.required_optional(pattern, size, changed)
                    rows.append({"size": size, "pattern": pattern, "drift": drift,
                                 "required": json.dumps(required), "optional": json.dumps(optional),
                                 "derivation": json.dumps(changed)})
        with REF_CACHE.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    with REF_CACHE.open(encoding="utf-8") as handle:
        return {(int(r["size"]), r["pattern"], int(r["drift"])): (set(json.loads(r["required"])),
                                                                 set(json.loads(r["optional"])))
                for r in csv.DictReader(handle)}


def main():
    refs = references()
    detections = defaultdict(list)
    with (OUT / "detections.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            r = json.loads(line)
            if r.get("dataset", "ostovar") == "ostovar":
                detections[(r["size"], r["log"])].append(r)
    rows = []
    for (size, log), dets in sorted(detections.items()):
        if size == 1:
            continue
        pattern = log.split("_")[0]
        noise = {"": "0", "2": "2.5", "5": "5"}[log.split("_")[1] if "_" in log else ""]
        for drift, cp in CPS.items():
            required, optional = refs[(size, pattern, drift)]
            hit = next((d for d in sorted(dets, key=lambda d: d["drift_index"]) if d["drift_index"] > 0
                        and cp <= d["detected_trace"] < cp + MATCH_SPAN), None)
            ch = characterize(hit["statements"], hit["fragments"]) if hit else \
                {"pattern": "none", "central": set(), "secondary": set(), "n_statements": 0}
            truth = PATTERN_FAMILY[pattern]
            predicted = PATTERN_FAMILY.get(ch["pattern"], "")
            o = object_score(ch["central"], required, optional) if ch["central"] else 0.0
            mr = min(o, float(predicted == truth))
            pi_raw = 1.0 if ch["pattern"] == pattern else 0.5 if predicted == truth else 0.0
            rows.append({"size": size, "split": "tuning" if size in (2, 4) else "evaluation",
                         "pattern": pattern, "noise": noise, "drift": drift, "detected": bool(hit),
                         "detected_trace": hit["detected_trace"] if hit else "",
                         "n_statements": ch["n_statements"], "predicted_pattern": ch["pattern"],
                         "central": json.dumps(sorted(ch["central"])), "secondary": json.dumps(sorted(ch["secondary"])),
                         "required": json.dumps(sorted(required)), "optional": json.dumps(sorted(optional)),
                         "O": o, "MR_raw": float(predicted == truth), "PI_raw": pi_raw,
                         "MR": mr, "PI": min(o, mr, pi_raw),
                         "overclaim": float(bool(ch["secondary"] - required - optional)),
                         "O_strict": object_score(ch["central"] | ch["secondary"], required, optional)
                         if ch["central"] else 0.0,
                         "O_noise_optional": object_score(ch["central"], required, optional | NOISE_ACTIVITIES)
                         if ch["central"] else 0.0,
                         "O_F1": object_f1(ch["central"], required, optional)})
    with (OUT / "scores.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    def summary(label, items):
        print(f"{label:28s} n={len(items):3d} detected={mean(r['detected'] for r in items):.3f} "
              f"O={mean(r['O'] for r in items):.3f} MR={mean(r['MR'] for r in items):.3f} "
              f"PI={mean(r['PI'] for r in items):.3f} O_strict={mean(r['O_strict'] for r in items):.3f} "
              f"O_noise={mean(r['O_noise_optional'] for r in items):.3f} O_F1={mean(r['O_F1'] for r in items):.3f} "
              f"overclaim={mean(r['overclaim'] for r in items):.3f}")
    for size in (2, 3, 4, 5):
        summary(f"size {size}", [r for r in rows if r["size"] == size])
        for noise in ("0", "2.5", "5"):
            summary(f"  size {size} noise {noise}", [r for r in rows if r["size"] == size and r["noise"] == noise])
    print("by pattern (sizes 3+5):")
    for pattern in refrule.PATTERNS:
        summary(f"  {pattern}", [r for r in rows if r["size"] in (3, 5) and r["pattern"] == pattern])


if __name__ == "__main__":
    main()
