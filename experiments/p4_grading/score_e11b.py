#!/usr/bin/env python3
"""P4 / E11b: agreement between the two human graders and the blind Claude extractor.

  python experiments/p4_grading/score_e11b.py results/p4_grading/returned/<grader1>.xlsx \
         results/p4_grading/returned/<grader2>.xlsx
  python experiments/p4_grading/score_e11b.py --self-test     (Claude vs a copy of itself: everything = 1)

Two levels, for the pairs grader1-grader2, grader1-Claude, grader2-Claude:
  fields  Cohen's kappa on support_level, mechanism, pattern, time_direction, CDLG operation_class;
          exact match and mean Jaccard on central_activities (and CDLG objects);
  scores  the paper's metrics computed from each extraction with the P2 scoring functions
          (Ostovar O/MR/PI, CDLG O/MR/PI with r5a, E4a time_detected/PI, E4b target_claimed, null: claims
          a change); share of identical scores and weighted kappa on PI levels {0, 0.5, 1}.
Writes results/p4_grading/e11b_agreement.md and e11b_rows.csv.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(HERE))
from build_e11b_package import guide_pattern  # noqa: E402
from score_p2 import (cdlg_references, e4_cases, ostovar_references, score_drift, score_e4a,  # noqa: E402
                      score_e4b)

P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p4_grading"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"
LISTS = ("central_activities", "secondary_activities", "alternative_activities", "time_activities",
         "resource_activities", "cdlg_objects")


def codes(value) -> list[str]:
    return [v.strip().upper() for v in str(value or "").replace(";", ",").split(",") if v.strip()]


def read_grader(path: Path) -> tuple[str, dict]:
    ws = load_workbook(path, read_only=True)["Cham"]
    rows = list(ws.iter_rows(values_only=True))
    name, header = str(rows[0][1] or path.stem.split("grader_")[-1]), list(rows[1])  # B1 may be left empty
    out = {}
    for row in rows[3:]:
        if not row[0]:
            continue
        r = dict(zip(header, row))
        e = {k: (str(r.get(k) or "").strip()) for k in header if k}
        for k in LISTS:
            e[k] = codes(r.get(k))
        e["perspectives"] = [p.strip().lower() for p in str(r.get("perspectives") or "").split(",") if p.strip()]
        # guide columns (2026-11-15): an empty pattern cell falls back to the pattern implied by the two answers
        e["pattern_from_guide"] = guide_pattern(e.get("dan_loai_thay_doi", ""), e.get("dan_cau_truc", ""))
        e["pattern"] = e.get("pattern") or e["pattern_from_guide"]
        e["alternative_pattern"] = e.get("alternative_pattern") or "none"
        e["time_direction"] = e.get("time_direction") or "none"
        # accept "A01:deleted" as well as free forms such as 'A01 "deleted"' (2026-11-18, H067 of grader 1)
        e["cdlg_role_pairs"] = [(a.upper(), role.lower()) for a, role in re.findall(
            r"(A\d{2})\W+(added|deleted|moved)", str(r.get("cdlg_role_pairs") or ""), re.I)]
        out[r["id"]] = e
    return name, out


REPEAT = OUT / "extractor_repeat"  # second Claude pass on the sample (rerun_extractor.py)


def claude_extractions(sample: list[dict], base: Path = P2) -> dict:
    out = {}
    for s in sample:
        rel = Path(PROMPT) / s["model"] / "run1" / f"{s['case_id']}.json"
        if not (base / "extractions_r5" / rel).exists():
            continue
        e = dict(json.loads((base / "extractions_r5" / rel).read_text())["extraction"])
        path = base / "extractions_r5a_cdlg" / rel
        if path.exists():
            a = json.loads(path.read_text())["extraction"]
            e.update({"cdlg_objects": [x.upper() for x in a["predicted_objects"]],
                      "cdlg_role_pairs": [(p["activity"].upper(), p["role"]) for p in a["object_role_pairs"]],
                      "cdlg_operation_class": a["operation_class"], "cdlg_quote": a["supporting_quote"]})
        out[s["id"]] = e
    return out


def graded(correct: int, predicted: set, reference: set) -> float:
    if predicted == reference:
        return 1.0
    return 0.5 if correct >= math.ceil(2 * len(reference) / 3) else 0.0


def norm_quote(s: str) -> str:
    s = re.sub(r"[→←–—\-]+", " - ", s)
    s = re.sub(r"[\"'“”‘’`*]", "", s)
    return " ".join(s.replace(" - ", " ").split()).lower()


def main_class(e: dict) -> str:
    """Operation class from the roles of the main-hypothesis activities (cdlg_roles.class_of)."""
    from cdlg_roles import class_of
    central = {a.upper() for a in e.get("central_activities", [])}
    return class_of({r for a, r in map(tuple, e.get("cdlg_role_pairs", [])) if a in central})


def scores(e: dict, s: dict, refs: dict) -> dict:
    """The paper's metrics for one extraction (same definitions as score_p2 / cdlg_roles)."""
    if s["kind"] == "null" and s["set"] not in ("e4a", "e4b"):
        return {"claims_change": float(e["support_level"] != "insufficient")}
    lm = json.loads((P2 / "audit" / f"{s['case_id']}.json").read_text())["label_map"]
    if s["set"] in ("ostovar3", "ostovar5"):
        pattern, req, opt = refs["ost"][s["case_id"]]
        r = score_drift(e, pattern, {lm[a] for a in req if a in lm}, {lm[a] for a in opt if a in lm})
        return {k: r[k] for k in ("O", "MR", "PI", "RTU", "overclaim")}
    if s["set"] == "cdlg":
        ref = refs["cdlg"][s["case_id"]]
        ref_pairs = {(lm[a], role) for role, k in (("added", "activities_added_real"), ("deleted",
                     "activities_deleted_real"), ("moved", "activities_moved_real")) for a in json.loads(ref[k]) if a in lm}
        affected = {a for a, _ in ref_pairs}
        if not affected:  # no observable reference: excluded from the scores, as in cdlg_roles.py
            return {}
        # main hypothesis only, as in cdlg_roles.py (author decision 2026-11-18)
        central = {a.upper() for a in e.get("central_activities", [])}
        pairs = {p for p in map(tuple, e.get("cdlg_role_pairs", [])) if p[0] in central}
        objects = (set(e.get("cdlg_objects", [])) & central) | {a for a, _ in pairs}
        o = graded(len(objects & affected), objects, affected)
        mr_raw = graded(len(pairs & ref_pairs), pairs, ref_pairs)
        text = json.loads((P2 / "runs" / PROMPT / s["model"] / "run1" / f"{s['case_id']}.json").read_text())["text"]
        quote = str(e.get("cdlg_quote", "")).strip()
        # verbatim up to dash/arrow punctuation, quotes, case and whitespace (graders type → as "-"; 2026-11-17)
        ok = bool(quote) and norm_quote(quote) in norm_quote(text)
        cls = main_class(e)
        pi_raw = 1.0 if mr_raw == 1.0 and cls == ref["operation_class"] and ok else \
            0.5 if mr_raw >= 0.5 and ok and cls != "unclear" else 0.0
        return {"O": o, "MR": min(o, mr_raw), "PI": min(o, mr_raw, pi_raw)}
    case = refs["e4"][s["case_id"]]
    if s["set"] == "e4a":
        r = score_e4a(e, case, lm)
        return {k: r[k] for k in ("time_detected", "O", "PI", "time_false_claim") if k in r}
    r = score_e4b(e, case, lm)
    return {k: r[k] for k in ("target_claimed", "target_main", "n_resource_claims") if k in r}


def kappa(a: list, b: list, weights: dict | None = None) -> float:
    """Cohen's kappa; with weights {label: value}, linear-weighted kappa."""
    n = len(a)
    if n == 0:
        return float("nan")
    labels = sorted(set(a) | set(b), key=str)
    def dist(x, y):
        if weights is None:
            return float(x != y)
        span = max(weights.values()) - min(weights.values()) or 1
        return abs(weights[x] - weights[y]) / span
    observed = sum(dist(x, y) for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    expected = sum(ca[x] * cb[y] * dist(x, y) for x in labels for y in labels) / (n * n)
    return 1.0 if expected == 0 else 1 - observed / expected


def jaccard(x: list, y: list) -> float:
    x, y = set(x), set(y)
    return 1.0 if not x and not y else len(x & y) / len(x | y)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("graders", nargs="*", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    with (OUT / "e11b_sample.csv").open(encoding="utf-8") as handle:
        sample = list(csv.DictReader(handle))
    by_id = {s["id"]: s for s in sample}
    sources = {"Claude": claude_extractions(sample)}
    repeat = claude_extractions(sample, REPEAT) if REPEAT.exists() else {}
    if repeat:  # extractor test-retest
        sources["Claude_repeat"] = repeat
        if len(repeat) < len(sample):
            print(f"warning: Claude_repeat covers {len(repeat)}/{len(sample)} rows")
    if args.self_test:
        sources["Claude_copy"] = json.loads(json.dumps(sources["Claude"]))
    for path in args.graders:
        name, data = read_grader(path)
        missing = [i for i in by_id if not data.get(i, {}).get("support_level")]
        if missing:
            print(f"warning: {name}: {len(missing)} rows without support_level, e.g. {missing[:5]}")
        sources[name] = data
    refs = {"ost": ostovar_references(), "cdlg": cdlg_references(), "e4": e4_cases()}
    names = list(sources)
    pairs = [(names[i], names[j]) for i in range(len(names)) for j in range(i + 1, len(names))]
    rows, lines = [], ["# E11b: agreement between graders and the Claude extractor", ""]
    computed = {n: {i: scores(sources[n][i], by_id[i], refs) for i in by_id if sources[n].get(i, {}).get("support_level")}
                for n in names}
    for i in by_id:
        for n in names:
            if i in computed[n]:
                rows.append({"id": i, "source": n, **{k: by_id[i][k] for k in ("model", "set", "kind")},
                             **computed[n][i]})
    lines += ["| Pair | n | κ support | κ mechanism | κ pattern | central exact | central Jaccard | "
              "κ time_dir | κ CDLG class | CDLG objects exact | scores identical | weighted κ PI |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for a, b in pairs:
        ids = [i for i in by_id if i in computed[a] and i in computed[b]]
        A, B = sources[a], sources[b]
        cd = [i for i in ids if by_id[i]["set"] == "cdlg"]
        same = [computed[a][i] == computed[b][i] for i in ids if computed[a][i] or computed[b][i]]
        pi = [i for i in ids if "PI" in computed[a][i] and "PI" in computed[b][i]]
        w = {0.0: 0.0, 0.5: 0.5, 1.0: 1.0}
        lines.append("| " + " | ".join([
            f"{a} – {b}", str(len(ids)),
            f"{kappa([A[i]['support_level'] for i in ids], [B[i]['support_level'] for i in ids]):.2f}",
            f"{kappa([A[i]['mechanism'] for i in ids], [B[i]['mechanism'] for i in ids]):.2f}",
            f"{kappa([A[i].get('pattern', '') for i in ids], [B[i].get('pattern', '') for i in ids]):.2f}",
            f"{sum(set(A[i]['central_activities']) == set(B[i]['central_activities']) for i in ids) / len(ids):.2f}",
            f"{sum(jaccard(A[i]['central_activities'], B[i]['central_activities']) for i in ids) / len(ids):.2f}",
            f"{kappa([A[i]['time_direction'] for i in ids], [B[i]['time_direction'] for i in ids]):.2f}",
            f"{kappa([main_class(A[i]) for i in cd], [main_class(B[i]) for i in cd]):.2f}",
            f"{sum(set(A[i].get('cdlg_objects', [])) & set(A[i]['central_activities']) == set(B[i].get('cdlg_objects', [])) & set(B[i]['central_activities']) for i in cd) / max(1, len(cd)):.2f}",
            f"{sum(same) / len(same):.2f}",
            f"{kappa([computed[a][i]['PI'] for i in pi], [computed[b][i]['PI'] for i in pi], w):.2f}"]) + " |")
    lines += ["", "Scores identical = every metric of the case (see score_e11b.scores) equal under both extractions.",
              "Weighted κ PI over the cases with a PI score (Ostovar, CDLG, E4a drift)."]
    (OUT / "e11b_agreement.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    keys = sorted({k for r in rows for k in r}, key=lambda k: (k not in ("id", "source", "model", "set", "kind"), k))
    with (OUT / "e11b_rows.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
