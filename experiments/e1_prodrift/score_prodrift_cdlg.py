#!/usr/bin/env python3
"""E1 on CDLG: score ProDrift on the 100 evaluated CDLG cases (one change episode per log,
frozen version-1 selection and references in data/references/).

Scoring follows the version-1 CDLG definition (score_predictions.py of the submitted study):
  * affected set = added ∪ deleted ∪ moved activities of the reference;
  * O  = 1 if the predicted activity set equals the affected set, 0.5 if at least
         ceil(2/3 · |affected|) affected activities are predicted, else 0;
  * MR_raw on (activity, role) pairs, role ∈ {added, deleted, moved}, same thresholds;
  * PI_raw = 1 if MR_raw = 1 and the operation class (only_added, deleted_and_added, ...)
         is exact; 0.5 if MR_raw >= 0.5 and a class is predicted; else 0;
  * MR = min(O, MR_raw); PI = min(O, MR, PI_raw).
  (The version-1 quote-validity condition for PI does not apply to template statements.)
  O_F1 (F1 of predicted vs affected activities) is reported as for Ostovar.
  Sensitivity favourable to ProDrift: *_best columns use the best-scoring detection inside
  the window instead of the first one.

ProDrift prediction for a case:
  * matched detection: the first ProDrift detection whose trace position lies in
    [change_trace_start, change_trace_end + 500); none -> all scores 0;
  * main statement (author decision 2026-11-18, as for Ostovar in score_prodrift.characterize and as
    for the LLM explanations): the statement of that detection with the most activities; its
    activities and roles are the prediction. Every statement together is kept as *_all (the
    previous rule) for sensitivity;
  * roles: inserted -> added, removed -> deleted, moved (any variant) -> moved,
    substituted -> old fragment deleted + new fragment added; other statement types
    (loop, skip, choice/parallel <-> sequence) contribute activities without a role;
  * operation class from the set of roles: {added} only_added, {deleted} only_deleted,
    {moved} only_moved, {deleted, added} deleted_and_added, {added, moved} added_and_moved,
    {deleted, moved} deleted_and_moved, anything else 'other'; no statement -> 'none'.
Activity names containing spaces ("Random activity 1") are replaced by tokens before the
statement parser of score_prodrift.py is applied, and mapped back afterwards.
--isolated scores the run on the isolated single-change logs (segment between the
neighbouring change points; detected positions are shifted back to source-log traces).
Output: results/e1_prodrift/scores_cdlg.csv or scores_cdlg_isolated.csv, and a summary.
"""
from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "experiments" / "p0_llm_calibration"))
from pcr.paths import REFERENCES, RESULTS  # noqa: E402
from score import object_f1  # noqa: E402
from score_prodrift import OPERATORS, classify, leaves  # noqa: E402

OUT = RESULTS / "e1_prodrift"
GROUND_TRUTH = REFERENCES / "cdlg_case_ground_truth_one_per_log100_v1.csv"
MATCH_SPAN = 500
CLASSES = {frozenset({"added"}): "only_added", frozenset({"deleted"}): "only_deleted",
           frozenset({"moved"}): "only_moved", frozenset({"deleted", "added"}): "deleted_and_added",
           frozenset({"added", "moved"}): "added_and_moved", frozenset({"deleted", "moved"}): "deleted_and_moved"}


def tree_names(tree: str) -> set[str]:
    return {t.strip() for t in re.split(r"[(),]", tree) if t.strip() and t.strip() not in OPERATORS}


def tokenize(statements: list[str], fragments: dict, extra: set[str]):
    """Replace names that are not plain identifiers by tokens; return mapping token -> name."""
    names = set(extra)
    for tree in fragments.values():
        names |= tree_names(tree["left"]) | tree_names(tree["right"])
    special = sorted((n for n in names if not re.fullmatch(r"[A-Za-z0-9_]+", n)), key=len, reverse=True)
    mapping = {f"ZQN{i}": n for i, n in enumerate(special)}

    def sub(text: str) -> str:
        for token, name in mapping.items():
            text = text.replace(name, token)
        return text
    statements = [sub(s) for s in statements]
    fragments = {k: {"left": sub(v["left"]), "right": sub(v["right"])} for k, v in fragments.items()}
    return statements, fragments, mapping


def activities_of(item: str, fragments: dict) -> set[str]:
    if item.startswith("Activity "):
        name = item.split(" ", 1)[1]
        return set() if name in OPERATORS else {name}
    tree = fragments.get(item)
    return (leaves(tree["left"]) | leaves(tree["right"])) if tree else set()


def predict(statements: list[str], fragments: dict, reference_names: set[str]) -> dict:
    statements, fragments, mapping = tokenize(statements, fragments, reference_names)
    back = lambda acts: {mapping.get(a, a) for a in acts}  # noqa: E731
    objects, pairs, roles = set(), set(), set()
    for st in statements:
        try:
            c = classify(st, fragments)
        except AttributeError:  # unseen template: keep its activities out, no role
            c = {"pattern": "other", "items": []}
        acts = [back(activities_of(i, fragments)) for i in c["items"]]
        everything = set().union(*acts) if acts else set()
        objects |= everything
        if c["pattern"] == "Substitute" and len(acts) == 2:
            pairs |= {(a, "deleted") for a in acts[0]} | {(a, "added") for a in acts[1]}
            roles |= {"deleted", "added"}
        elif c["pattern"].endswith("Removal"):
            role = "added" if " is inserted " in st else "deleted"
            pairs |= {(a, role) for a in everything}
            roles.add(role)
        elif " has moved to " in st:  # any relocation, including into/out of a loop block
            pairs |= {(a, "moved") for a in everything}
            roles.add("moved")
        else:
            roles.add("other")
    if not statements:
        op = "none"
    else:
        op = CLASSES.get(frozenset(roles), "other")
    return {"objects": objects, "pairs": pairs, "operation_class": op, "n_statements": len(statements)}


def graded(predicted: set, reference: set) -> float:
    if predicted == reference:
        return 1.0
    return 0.5 if len(predicted & reference) >= math.ceil(2 * len(reference) / 3) else 0.0


def score(pred: dict, affected: set, ref_pairs: set, op_class: str) -> dict:
    o = graded(pred["objects"], affected) if pred["objects"] else 0.0
    mr_raw = graded(pred["pairs"], ref_pairs) if pred["pairs"] else 0.0
    if mr_raw == 1.0 and pred["operation_class"] == op_class:
        pi_raw = 1.0
    elif mr_raw >= 0.5 and pred["operation_class"] != "none":
        pi_raw = 0.5
    else:
        pi_raw = 0.0
    mr = min(o, mr_raw)
    pi = min(o, mr, pi_raw)
    return {"O": o, "MR_raw": mr_raw, "MR": mr, "PI_raw": pi_raw, "PI": pi,
            "O_F1": object_f1(pred["objects"], affected), "RTU": float(o == mr == pi == 1.0)}


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--isolated", action="store_true",
                        help="score ProDrift run on the isolated single-change logs (make_window_logs.py)")
    args = parser.parse_args()
    dataset = "cdlg_isolated" if args.isolated else "cdlg"
    offsets = {}
    if args.isolated:
        with (OUT / "window_logs" / "index_cdlg_isolated.csv").open(encoding="utf-8") as handle:
            offsets = {r["case"]: int(r["segment_start"]) for r in csv.DictReader(handle)}
    detections: dict[str, list[dict]] = {}
    with (OUT / "detections.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            r = json.loads(line)
            if r.get("dataset") == dataset:
                if args.isolated and r["detected_trace"] != "":
                    r["detected_trace"] += offsets[r["log"]]  # back to source-log trace positions
                detections.setdefault(r["log"], []).append(r)
    rows = []
    with GROUND_TRUTH.open(encoding="utf-8-sig") as handle:
        cases = list(csv.DictReader(handle))
    for case in cases:
        log = case["case_id"] if args.isolated else case["log_name"].replace(".xes", "")
        start, end = int(case["change_trace_start"]), int(case["change_trace_end"])
        added, deleted, moved = (set(json.loads(case[f"activities_{k}_real"])) for k in ("added", "deleted", "moved"))
        affected = added | deleted | moved
        audit = ROOT / "results" / "p2_main" / "audit" / f"{case['case_id']}.json"
        if audit.exists() and not affected & set(json.loads(audit.read_text(encoding="utf-8"))["label_map"]):
            continue  # no affected activity observed in the window pair: no observable reference (as for the LLM)
        ref_pairs = {(a, "added") for a in added} | {(a, "deleted") for a in deleted} | {(a, "moved") for a in moved}
        dets = [d for d in detections.get(log, []) if d["drift_index"] > 0]
        in_window = [d for d in sorted(dets, key=lambda d: d["drift_index"])
                     if start <= d["detected_trace"] < end + MATCH_SPAN]
        status = next((d["status"] for d in detections.get(log, [])), "missing")
        hit = in_window[0] if in_window else None
        empty = {"objects": set(), "pairs": set(), "operation_class": "none", "n_statements": 0}
        pred_all = predict(hit["statements"], hit["fragments"], affected) if hit else empty
        if hit and hit["statements"]:
            per = [predict([st], hit["fragments"], affected) for st in hit["statements"]]
            pred = max(enumerate(per), key=lambda x: (len(x[1]["objects"]), -x[0]))[1]
            pred["n_statements"] = len(hit["statements"])
        else:
            pred = pred_all
        main_score = score(pred, affected, ref_pairs, case["operation_class"])
        all_score = score(pred_all, affected, ref_pairs, case["operation_class"])
        # Sensitivity, favourable to ProDrift: the best-scoring detection inside the window.
        best = max((score(predict(d["statements"], d["fragments"], affected), affected, ref_pairs,
                          case["operation_class"]) for d in in_window),
                   key=lambda x: (x["RTU"], x["PI"], x["MR"], x["O"], x["O_F1"]), default=None)
        rows.append({"case_id": case["case_id"], "log": log, "drift_id": case["drift_id"],
                     "change_id": case["change_id"], "global_drift_type": case["global_drift_type"],
                     "local_change_type": case["local_change_type"], "change_trace_start": start,
                     "change_trace_end": end, "operation_class": case["operation_class"],
                     "prodrift_status": status, "n_detections_log": len(dets),
                     "n_detections_window": len(in_window), "detected": bool(hit),
                     "detected_trace": hit["detected_trace"] if hit else "",
                     "n_statements": pred["n_statements"], "predicted_class": pred["operation_class"],
                     "predicted_objects": json.dumps(sorted(pred["objects"]), ensure_ascii=False),
                     "reference_objects": json.dumps(sorted(affected), ensure_ascii=False),
                     "predicted_pairs": json.dumps(sorted(pred["pairs"]), ensure_ascii=False),
                     "reference_pairs": json.dumps(sorted(ref_pairs), ensure_ascii=False),
                     # as for the LLM explanations: an activity of another statement outside the reference
                     "overclaim": float(bool((pred_all["objects"] - pred["objects"]) - affected)),
                     **main_score, **{f"{k}_all": all_score[k] for k in ("O", "MR", "PI", "RTU")},
                     **{f"{k}_best": (best[k] if best else 0.0) for k in ("O", "MR", "PI", "RTU", "O_F1")}})
    with (OUT / f"scores_{dataset}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    def summary(label, items):
        if not items:
            return
        print(f"{label:24s} n={len(items):3d} detected={mean(r['detected'] for r in items):.3f} "
              f"O={mean(r['O'] for r in items):.3f} MR={mean(r['MR'] for r in items):.3f} "
              f"PI={mean(r['PI'] for r in items):.3f} RTU={mean(r['RTU'] for r in items):.3f} "
              f"O_F1={mean(r['O_F1'] for r in items):.3f} | best-in-window: "
              f"O={mean(r['O_best'] for r in items):.3f} MR={mean(r['MR_best'] for r in items):.3f} "
              f"PI={mean(r['PI_best'] for r in items):.3f} RTU={mean(r['RTU_best'] for r in items):.3f}")
    summary("CDLG all", rows)
    for key in ("local_change_type", "global_drift_type", "operation_class"):
        for value in sorted({r[key] for r in rows}):
            summary(f"  {key[:6]}={value}", [r for r in rows if r[key] == value])
    print("ProDrift status:", Counter(r["prodrift_status"] for r in rows))
    print("detections per log (median/max):", sorted(r["n_detections_log"] for r in rows)[50],
          max(r["n_detections_log"] for r in rows),
          "| detections in window (median):", sorted(r["n_detections_window"] for r in rows)[50])


if __name__ == "__main__":
    main()
