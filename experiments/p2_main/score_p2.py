#!/usr/bin/env python3
"""P2 step 4: score rubric-r5 extractions on the evaluation sets (metrics as P0-C, score.py).

Ostovar drift cases: O, MR_raw, PI_raw, MR = min(O, MR_raw), PI = min(O, MR, PI_raw), PI_alt, overclaim, O_strict, O_noise_optional, O_F1 (score.py policy).
  size 3: required = reference v2 (ostovar_size3_atomic_object_ground_truth_v2.csv) minus the optional
          activities of the E0 rule (pattern conventions, e.g. the Skip re-entry anchor o1), optional = those;
          with this convention v2 and the rule coincide on 26/26 changes (E11a).
  size 5: ostovar_size5_references_v2.csv (required / optional).
CDLG drift cases: O on central + secondary activities against added | deleted | moved (version-1 definition of
  the affected set; a CDLG episode can combine several operations, so no main/secondary split, as for
  ProDrift); O_main on central only; O_F1. MR/PI need activity roles, which rubric r5 does not record
  (pending author decision, docs/EXPERIMENT_LOG_VI.md 2026-11-14).
E4a (time injection) and E4b (resource injection): metrics of the E4 P0b scorers
  (e4a: time_detected, O, MR, PI, time_direction_ok, time_false_claim on N; e4b: target_claimed,
  target_main, resource claims per case).
Null pairs: support level (share "insufficient evidence").
Output: results/p2_main/scores_<prompt>_<model>_<run>.csv and a summary printed per set.
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
sys.path.insert(0, str(ROOT / "experiments" / "p0_llm_calibration"))
from score import NOISE_ACTIVITIES, PATTERN_FAMILY, object_f1, object_score  # noqa: E402

OUT = ROOT / "results" / "p2_main"
REF = ROOT / "data" / "references"


def ostovar_references() -> dict[str, tuple[str, set, set]]:
    rule = {}
    with (ROOT / "results" / "e1_prodrift" / "references_sizes2to5.csv").open(encoding="utf-8") as handle:
        for r in csv.DictReader(handle):
            if r["size"] == "3":
                rule[(r["pattern"], r["drift"])] = set(json.loads(r["optional"]))
    refs = {}
    with (REF / "ostovar_size3_atomic_object_ground_truth_v2.csv").open(encoding="utf-8-sig") as handle:
        size3 = {(r["change_pattern"], r["drift_sequence"]): set(json.loads(r["affected_activities_real"]))
                 for r in csv.DictReader(handle)}
    with (OUT / "cases.csv").open(encoding="utf-8") as handle:
        for c in csv.DictReader(handle):
            if c["set"] == "ostovar3":
                key = (c["type"], c["drift"])
                refs[c["case_id"]] = (c["type"], size3[key] - rule[key], rule[key])
    with (REF / "ostovar_size5_references_v2.csv").open(encoding="utf-8") as handle:
        for r in csv.DictReader(handle):
            refs[r["case_id"]] = (r["change_pattern"], set(json.loads(r["required_activities_real"])),
                                  set(json.loads(r["optional_activities_real"])))
    return refs


def score_drift(e: dict, pattern: str, required: set, optional: set) -> dict:
    central = set(e["central_activities"])
    secondary = set(e.get("secondary_activities", [])) - central
    o = object_score(central, required, optional)
    truth, predicted = PATTERN_FAMILY[pattern], PATTERN_FAMILY.get(e.get("pattern", ""), "")
    mr_raw = float(predicted == truth)
    mr = min(o, mr_raw)
    pi_raw = 1.0 if e.get("pattern") == pattern else 0.5 if predicted == truth else 0.0
    pi = min(o, mr, pi_raw)
    alt, pi_alt = e.get("alternative_pattern", "none"), pi
    if alt not in ("", "none") and PATTERN_FAMILY.get(alt) == predicted and alt == pattern:
        o_alt = object_score(set(e.get("alternative_activities", [])) or central, required, optional)
        pi_alt = max(pi, min(o_alt, float(predicted == truth)))
    return {"reference_pattern": pattern, "O": o, "MR_raw": mr_raw, "PI_raw": pi_raw, "MR": mr, "PI": pi,
            "PI_alt": pi_alt,
            "RTU": float(o == mr == pi == 1.0), "alternative_pattern": alt, "n_secondary": len(secondary),
            "overclaim": float(bool(secondary - required - optional)),
            "O_strict": object_score(central | secondary, required, optional),
            "O_F1": object_f1(central, required, optional)}


RESOURCE_MECHANISMS = {"resource_allocation_changed", "handover_changed"}
E4 = ROOT / "e4_multiperspective" / "results"


def e4_cases() -> dict:
    rows = {}
    for folder in ("e4a_time_injection", "e4b_resource_injection"):
        with (E4 / folder / "cases.csv").open(encoding="utf-8") as handle:
            rows.update({r["case_id"]: r for r in csv.DictReader(handle)})
    return rows


def cdlg_references() -> dict:
    with (REF / "cdlg_case_ground_truth_one_per_log100_v1.csv").open(encoding="utf-8-sig") as handle:
        return {r["case_id"]: r for r in csv.DictReader(handle)}


def score_cdlg(e: dict, ref: dict, lm: dict) -> dict:
    affected = {lm[a] for k in ("activities_added_real", "activities_deleted_real", "activities_moved_real")
                for a in json.loads(ref[k]) if a in lm}
    central = set(e["central_activities"])
    claimed = central | set(e.get("secondary_activities", []))
    return {"O": object_score(claimed, affected) if affected else float("nan"),
            "O_main": object_score(central, affected) if affected else float("nan"),
            "O_F1": object_f1(claimed, affected) if affected else float("nan"),
            "operation_class": ref["operation_class"], "n_affected": len(affected)}


def score_e4a(e: dict, case: dict, lm: dict) -> dict:
    central, secondary = set(e["central_activities"]), set(e.get("secondary_activities", []))
    time_acts = set(e.get("time_activities", []))
    if case["type"] == "N":
        return {"time_false_claim": float(bool(time_acts))}
    x = lm[case["time_target"]]
    preds = {lm[a] for a in json.loads(case["time_predecessors"]) if a in lm}
    direction_ok = e.get("time_direction") == case["time_direction"]
    if case["type"] in ("T_SLOW", "T_FAST"):
        o = object_score(central, {x}, preds)
        mr_raw = float(e["mechanism"] == "timing_changed" and "time" in e.get("perspectives", []))
        pi_raw = float(direction_ok)
        mr = min(o, mr_raw)
        pi = min(mr, pi_raw)
    else:  # M: control-flow change plus timing change
        cf_req = {lm[a] for a in json.loads(case["cf_required"]) if a in lm}
        cf_opt = {lm[a] for a in json.loads(case["cf_optional"]) if a in lm}
        o = object_score(central | secondary | time_acts, cf_req | {x}, cf_opt | preds)
        truth, predicted = PATTERN_FAMILY[case["cf_pattern"]], PATTERN_FAMILY.get(e.get("pattern", ""), "")
        mr_raw = float(predicted == truth and x in time_acts)
        mr = min(o, mr_raw)
        cf_pi_raw = 1.0 if e.get("pattern") == case["cf_pattern"] else 0.5 if predicted == truth else 0.0
        pi_raw = min(cf_pi_raw, float(direction_ok))
        pi = min(mr, pi_raw)
    return {"time_detected": float(x in time_acts | central), "O": o, "MR_raw": mr_raw, "PI_raw": pi_raw,
            "MR": mr, "PI": pi,
            "time_direction_ok": float(direction_ok)}


def score_e4b(e: dict, case: dict, lm: dict) -> dict:
    central, secondary = set(e["central_activities"]), set(e.get("secondary_activities", []))
    res = set(e.get("resource_activities", []))
    row = {"n_resource_claims": len(res)}
    if case["type"] != "N":
        x = lm[case["target"]]
        row.update({"target_claimed": float(x in (res | central | secondary) and "resource" in e.get("perspectives", [])),
                    "target_main": float(x in central and e["mechanism"] in RESOURCE_MECHANISMS),
                    "other_resource_claims": len(res - {x})})
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=Path, required=True, help="results/p2_main/runs/<prompt>/<model>/run<k>")
    args = parser.parse_args()
    runs = args.runs if args.runs.is_absolute() else ROOT / args.runs
    rel = runs.relative_to(OUT / "runs")
    with (OUT / "cases.csv").open(encoding="utf-8") as handle:
        cases = {r["case_id"]: r for r in csv.DictReader(handle)}
    refs, cdlg, e4 = ostovar_references(), cdlg_references(), e4_cases()
    rows = []
    for path in sorted((OUT / "extractions_r5" / rel).glob("*.json")):
        ex = json.loads(path.read_text(encoding="utf-8"))
        case = cases[ex["case_id"]]
        e = ex["extraction"]
        row = {"case_id": ex["case_id"], "set": case["set"], "kind": case["kind"], "type": case["type"],
               "noise_pct": case["noise_pct"], "n_evidence": case["n_evidence"],
               "support_level": e["support_level"], "pattern": e.get("pattern", "")}
        if case["kind"] == "drift" and case["set"] in ("ostovar3", "ostovar5"):
            lm = json.loads((OUT / "audit" / f"{ex['case_id']}.json").read_text(encoding="utf-8"))["label_map"]
            pattern, req, opt = refs[ex["case_id"]]
            row.update(score_drift(e, pattern, {lm[a] for a in req if a in lm}, {lm[a] for a in opt if a in lm}))
            row["O_noise_optional"] = object_score(
                set(e["central_activities"]), {lm[a] for a in req if a in lm},
                {lm[a] for a in opt | NOISE_ACTIVITIES if a in lm})
        elif case["set"] in ("cdlg", "e4a", "e4b"):
            lm = json.loads((OUT / "audit" / f"{ex['case_id']}.json").read_text(encoding="utf-8"))["label_map"]
            if case["set"] == "cdlg":
                row.update(score_cdlg(e, cdlg[ex["case_id"]], lm))
            elif case["set"] == "e4a":
                row.update(score_e4a(e, e4[ex["case_id"]], lm))
            else:
                row.update(score_e4b(e, e4[ex["case_id"]], lm))
        rows.append(row)
    if not rows:
        sys.exit("no extractions yet")
    fields = list(dict.fromkeys(k for r in rows for k in r))
    target = OUT / f"scores_{'_'.join(rel.parts)}.csv"
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    groups = defaultdict(list)
    for r in rows:
        groups[(r["set"], r["kind"])].append(r)
    metrics = ("O", "O_main", "MR_raw", "PI_raw", "MR", "PI", "RTU", "overclaim", "O_F1", "time_detected", "time_direction_ok",
               "time_false_claim", "target_claimed", "target_main", "n_resource_claims")
    for (name, kind), rs in sorted(groups.items()):
        levels = defaultdict(int)
        for r in rs:
            levels[r["support_level"]] += 1
        parts = []
        for m in metrics:
            vals = [r[m] for r in rs if m in r and r[m] == r[m]]
            if vals:
                parts.append(f"{m} {mean(vals):.3f}")
        print(f"{name} {kind} n={len(rs)} {' '.join(parts)} | {dict(levels)}")
        if name in ("ostovar3", "ostovar5", "e4a", "e4b") and kind == "drift":
            key = "noise_pct" if name.startswith("ostovar") else "type"
            for v in sorted({r[key] for r in rs}):
                sub = [r for r in rs if r[key] == v]
                print(f"   {key} {v}: n={len(sub)} " + " ".join(
                    f"{m} {mean(r[m] for r in sub):.3f}" for m in ("O", "MR", "PI", "target_claimed", "target_main")
                    if m in sub[0]))
    print(f"-> {target}")


if __name__ == "__main__":
    main()
