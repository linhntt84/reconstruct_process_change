#!/usr/bin/env python3
"""P4 / E10: extraction without the benchmark pattern vocabulary (R3, R2, R4 #4; author approved 2026-11-17).

Concern: the main rubric (r5) lists the 13 Ostovar pattern names, so the extractor might map a vague description onto
the nearest admissible label. E10 removes every pattern name from the rubric. Instead the extractor answers the same
two plain-language questions as the human graders of E11b (kind of change; structure where a fragment was added,
removed or moved), and the pattern is derived deterministically from the two answers with the fixed table of the
grader workbook (build_e11b_package.guide_pattern). All other fields, the extraction mechanism (claude -p, no tools,
empty directory, JSON schema) and the model are those of r5.

Sample: the 100 explanations of E11b (results/p4_grading/e11b_sample.csv), so E10 can be compared with r5, with
the r5 repeat and with the two human graders on the same rows.

  python experiments/p4_grading/e10_vocab_free.py extract     (Claude, 100 calls)
  python experiments/p4_grading/e10_vocab_free.py analyze     (no API)
Output: results/p4_grading/e10_vocab_free/{extractions/...,e10_summary.md,e10_rows.csv}
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))
sys.path.insert(0, str(HERE))
import extract_e4  # noqa: E402
from build_e11b_package import guide_pattern  # noqa: E402
from pcr.extract import ACTIVITY, UsageLimitReached  # noqa: E402

ORIG_SCHEMA_R4 = extract_e4.schema_r4
P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p4_grading" / "e10_vocab_free"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"

CHANGE_TYPES = ["1_added_or_removed", "2_replaced", "3_two_fragments_exchanged", "4_one_fragment_moved",
                "5_repetition_started_or_stopped", "6_became_skippable_or_mandatory",
                "7_concurrent_became_ordered_or_reverse", "8_alternatives_became_ordered_or_reverse",
                "9_only_branch_frequencies", "10_only_time_or_resource", "11_other_control_flow",
                "12_no_hypothesis"]
STRUCTURES = ["a_sequence", "b_concurrent_branch", "c_alternative_branch", "d_not_applicable"]

GUIDE_FIELDS = """
change_type
  What the main hypothesis says happened to the changed part of the process, as one of:
  1_added_or_removed: an activity or fragment newly appears or disappears entirely.
  2_replaced: an old activity disappears and a new one appears at the same place.
  3_two_fragments_exchanged: X before Y becomes Y before X; both change position.
  4_one_fragment_moved: only ONE fragment changes position; the rest keeps its order.
  5_repetition_started_or_stopped: an activity now repeats within a case (or stops repeating).
  6_became_skippable_or_mandatory: the activity remains, but some cases now bypass it (or it becomes mandatory
    again).
  7_concurrent_became_ordered_or_reverse: activities that ran concurrently in any order now follow one fixed order
    (or the reverse); no activity is added, removed or moved.
  8_alternatives_became_ordered_or_reverse: previously only one of two branches was executed, now both are executed
    one after the other (or the reverse).
  9_only_branch_frequencies: the same branches remain, but the share of cases taking each branch changes.
  10_only_time_or_resource: order and structure of the steps are unchanged; only timing or resource allocation
    changes.
  11_other_control_flow: a change of order or structure that fits none of 1-9.
  12_no_hypothesis: the explanation declares insufficient evidence and names no specific change.
  If the explanation states both a control-flow change and a timing or resource change, answer for the
  control-flow part (1-9 or 11).

structure
  Only when change_type is 1 or 4: where the fragment was added, removed or moved:
  a_sequence: within a chain of consecutive steps.
  b_concurrent_branch: as a branch running concurrently with another branch, or into or out of a concurrent region.
  c_alternative_branch: as a branch that only some cases take, or into or out of a region of alternatives.
  d_not_applicable: change_type is not 1 or 4.
"""


def system_prompt() -> str:
    text = extract_e4.RUBRIC_R5.read_text(encoding="utf-8").split("\n", 2)[2]
    text = (text.replace("{{PATTERN_FIELD}}", GUIDE_FIELDS).replace("{{ALTERNATIVE_PATTERN_NAME}}", "")
            .replace("{{ALTERNATIVE_PATTERN_HINT}}", "").replace("{{ALTERNATIVE_PATTERN_NONE}}", ""))
    assert "Swap" not in text and "SerialMove" not in text and "Frequency (" not in text
    return text


def schema() -> dict:
    s = ORIG_SCHEMA_R4("vocab_free")
    s["properties"]["resource_activities"] = ACTIVITY
    s["properties"]["change_type"] = {"type": "string", "enum": CHANGE_TYPES}
    s["properties"]["structure"] = {"type": "string", "enum": STRUCTURES}
    s["required"] = list(s["properties"])
    return s


def extract_vf(explanation: str) -> dict:
    """extract_e4.extract_r4 with the E10 prompt and schema (same command line and settings)."""
    saved = extract_e4.system_prompt_r4, extract_e4.schema_r4
    extract_e4.system_prompt_r4 = lambda variant="main": system_prompt()
    extract_e4.schema_r4 = lambda variant="main": schema()
    try:
        result = extract_e4.extract_r4(explanation, "vocab_free")
    finally:
        extract_e4.system_prompt_r4, extract_e4.schema_r4 = saved
    result["rubric"] = "r5-vocab-free-guided (E10)"
    return result


def derived_pattern(e: dict) -> str:
    return guide_pattern(e["change_type"].split("_")[0], e["structure"].split("_")[0]) or "other"


def sample() -> list[dict]:
    with (ROOT / "results" / "p4_grading" / "e11b_sample.csv").open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def target(s: dict) -> Path:
    return OUT / "extractions" / PROMPT / s["model"] / "run1" / f"{s['case_id']}.json"


def extract():
    jobs = [s for s in sample() if not target(s).exists()]
    print(f"{len(jobs)} extractions to run; prompt sha256 "
          f"{hashlib.sha256(system_prompt().encode()).hexdigest()[:12]}", flush=True)
    (OUT / "rubric_e10.md").parent.mkdir(parents=True, exist_ok=True)
    (OUT / "rubric_e10.md").write_text(system_prompt(), encoding="utf-8")
    i = 0
    while i < len(jobs):
        s = jobs[i]
        record = json.loads((P2 / "runs" / PROMPT / s["model"] / "run1" / f"{s['case_id']}.json").read_text())
        try:
            result = extract_vf(record["text"])
        except UsageLimitReached as exc:
            delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
            print(f"{datetime.now():%H:%M} usage limit; waiting {delay / 60:.0f} min", flush=True)
            time.sleep(delay)
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"[{i + 1}/{len(jobs)}] error {s['id']}: {exc}", flush=True)
            i += 1
            continue
        result.update({"case_id": s["case_id"], "sample_id": s["id"], "generation_model": s["model"]})
        target(s).parent.mkdir(parents=True, exist_ok=True)
        target(s).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{i + 1}/{len(jobs)}] {s['id']} ok", flush=True)
        i += 1
        time.sleep(2.0)


def analyze():
    from score_e11b import REPEAT, claude_extractions, kappa, scores
    from score_p2 import cdlg_references, e4_cases, ostovar_references
    rows_s = sample()
    refs = {"ost": ostovar_references(), "cdlg": cdlg_references(), "e4": e4_cases()}
    main = claude_extractions(rows_s)
    repeat = claude_extractions(rows_s, REPEAT)
    rows, md = [], ["# E10: extraction without the pattern vocabulary", "",
                    "Generated by experiments/p4_grading/e10_vocab_free.py. Same 100 explanations as E11b. "
                    "r5 = main rubric (13 pattern names listed); r5 repeat = second r5 pass; E10 = no pattern names, "
                    "pattern derived from two plain-language answers with the fixed table of the grader workbook.", ""]
    for s in rows_s:
        if not target(s).exists():
            continue
        vf = dict(json.loads(target(s).read_text())["extraction"])
        vf["pattern"] = derived_pattern(vf)
        vf["alternative_pattern"] = "none"
        m = main[s["id"]]
        row = {"id": s["id"], "set": s["set"], "kind": s["kind"], "model": s["model"],
               "pattern_r5": m.get("pattern"), "pattern_e10": vf["pattern"],
               "change_type": vf["change_type"], "structure": vf["structure"],
               "mechanism_r5": m.get("mechanism"), "mechanism_e10": vf.get("mechanism"),
               "support_r5": m.get("support_level"), "support_e10": vf.get("support_level"),
               "central_same": set(m["central_activities"]) == set(vf["central_activities"])}
        if s["set"] not in ("cdlg",) and not (s["kind"] == "null" and s["set"] not in ("e4a", "e4b")):
            a, b = scores(m, s, refs), scores(vf, s, refs)
            for k in ("O", "MR", "PI", "RTU"):
                if k in a:
                    row[f"{k}_r5"], row[f"{k}_e10"] = a[k], b.get(k)
            if s["id"] in repeat and "PI" in a:
                row["PI_r5_repeat"] = scores(repeat[s["id"]], s, refs).get("PI")
        rows.append(row)
    ost = [r for r in rows if r["set"] in ("ostovar3", "ostovar5")]
    cf = [r for r in rows if r.get("PI_r5") is not None]

    def share(xs, f):
        return f"{sum(map(f, xs))}/{len(xs)}"
    md += [f"Rows extracted: {len(rows)}/100.", "", "## Agreement with r5", "",
           "| Quantity | Rows | Value |", "|---|---|---|",
           f"| Pattern identical (Ostovar) | {len(ost)} | {share(ost, lambda r: r['pattern_r5'] == r['pattern_e10'])} |",
           f"| Cohen κ pattern (Ostovar) | {len(ost)} | {kappa([r['pattern_r5'] for r in ost], [r['pattern_e10'] for r in ost]):.3f} |",
           f"| Pattern identical (all rows) | {len(rows)} | {share(rows, lambda r: r['pattern_r5'] == r['pattern_e10'])} |",
           f"| Support level identical | {len(rows)} | {share(rows, lambda r: r['support_r5'] == r['support_e10'])} |",
           f"| Main-hypothesis activities identical | {len(rows)} | {share(rows, lambda r: r['central_same'])} |",
           "", "## Scores on rows with a pattern reference (Ostovar, E4a)", "",
           "| Set | n | O r5 / E10 | MR r5 / E10 | PI r5 / E10 | PI r5 repeat | PI identical r5 vs E10 |",
           "|---|---|---|---|---|---|---|"]
    for name, xs in (("Ostovar 3+5", ost), ("E4a", [r for r in cf if r["set"] == "e4a"]), ("All", cf)):
        if not xs:
            continue

        def mean(k):
            v = [r[k] for r in xs if r.get(k) is not None]
            return f"{sum(v) / len(v):.3f}" if v else "—"
        md.append(f"| {name} | {len(xs)} | {mean('O_r5')} / {mean('O_e10')} | {mean('MR_r5')} / {mean('MR_e10')} | "
                  f"{mean('PI_r5')} / {mean('PI_e10')} | {mean('PI_r5_repeat')} | "
                  f"{share(xs, lambda r: r['PI_r5'] == r['PI_e10'])} |")
    diffs = Counter((r["pattern_r5"], r["pattern_e10"]) for r in rows if r["pattern_r5"] != r["pattern_e10"])
    md += ["", "## Pattern disagreements (r5 -> E10)", "", "| r5 | E10 | n |", "|---|---|---|"]
    md += [f"| {a} | {b} | {n} |" for (a, b), n in diffs.most_common()]
    (OUT / "e10_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with (OUT / "e10_rows.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print("\n".join(md))


if __name__ == "__main__":
    {"extract": extract, "analyze": analyze}[sys.argv[1]]()
