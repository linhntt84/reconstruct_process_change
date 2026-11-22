#!/usr/bin/env python3
"""P2, CDLG only: activity-role extraction (rubric r5a) and scoring with the version-1 CDLG definition.

Rubric r5 records one mechanism per hypothesis, but the version-1 CDLG metrics need a role per activity
(added / deleted / moved) and an operation class. The submitted version obtained them with a separate
blind grading pass (predicted_objects, predicted_object_role_pairs, predicted_pattern, supporting_quote;
score_predictions.py of model2_deepseek_cdlg_blind_v1). This script repeats that pass with the same
blind Claude extractor mechanism as rubric r5 (claude -p, no tools, JSON schema), and scores exactly as
version 1:
  Object set (author decision 2026-11-18, consistent with Ostovar and with the version-1 rubric, which
  recorded only the activities of the main change): the r5a objects and (activity, role) pairs are
  restricted to the activities of the main hypothesis recorded by rubric r5 (central_activities), and the
  operation class is derived from the retained roles. Activities claimed only as additional changes are
  reported as `overclaim` (r5 secondary activities outside the reference), as for Ostovar. The previous
  rule (every claimed activity, main or additional) is kept as O_all / MR_all / PI_all / RTU_all.
  O      = 1 if predicted_objects == affected, 0.5 if >= ceil(2/3 |affected|) correct, else 0;
  MR_raw = same on (activity, role) pairs; MR = min(O, MR_raw);
  PI_raw = 1 if MR_raw = 1, operation class exact and the quote is verbatim in the explanation;
           0.5 if MR_raw >= 0.5, quote valid and class != unclear; else 0; PI = min(O, MR, PI_raw).
affected = added | deleted | moved of data/references/cdlg_case_ground_truth_one_per_log100_v1.csv, restricted
to activities observed in the pair (label map); a case with no observed affected activity is excluded (n = 99).

  python experiments/p2_main/cdlg_roles.py extract --runs results/p2_main/runs/<prompt>/<model>/run1
  python experiments/p2_main/cdlg_roles.py score   --runs results/p2_main/runs/<prompt>/<model>/run1
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pcr.extract import LIMIT_MARKERS, MODEL, UsageLimitReached, claude_binary, cli_version  # noqa: E402

OUT = ROOT / "results" / "p2_main"
RUBRIC = HERE / "EXTRACTION_RUBRIC_CDLG_ROLES_EN.md"
CLASSES = ["only_added", "only_deleted", "only_moved", "deleted_and_added", "added_and_moved",
           "deleted_and_moved", "other", "unclear"]
CODE = {"type": "string", "pattern": "^A[0-9]{2,3}$"}
SCHEMA = {"type": "object", "additionalProperties": False,
          "properties": {"predicted_objects": {"type": "array", "items": CODE},
                         "object_role_pairs": {"type": "array", "items": {
                             "type": "object", "additionalProperties": False, "required": ["activity", "role"],
                             "properties": {"activity": CODE,
                                            "role": {"type": "string", "enum": ["added", "deleted", "moved"]}}}},
                         "operation_class": {"type": "string", "enum": CLASSES},
                         "supporting_quote": {"type": "string"}, "note": {"type": "string"}},
          "required": ["predicted_objects", "object_role_pairs", "operation_class", "supporting_quote", "note"]}


def extract_roles(explanation: str, timeout: int = 600) -> dict:
    prompt_text = RUBRIC.read_text(encoding="utf-8").split("\n", 2)[2]
    schema_text = json.dumps(SCHEMA)
    with tempfile.TemporaryDirectory(prefix="pcr_extract_cdlg_") as workdir:
        prompt_file = Path(workdir) / "system.md"
        prompt_file.write_text(prompt_text, encoding="utf-8")
        command = [claude_binary(), "-p", "--model", MODEL, "--system-prompt-file", str(prompt_file),
                   "--tools", "", "--strict-mcp-config", "--disable-slash-commands",
                   "--no-session-persistence", "--output-format", "json", "--json-schema", schema_text]
        started, t0 = datetime.now(timezone.utc).isoformat(), time.perf_counter()
        proc = subprocess.run(command, input="Explanation to record:\n\n" + explanation, text=True,
                              capture_output=True, cwd=workdir, timeout=timeout)
    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError:
        envelope = {"is_error": True, "result": (proc.stdout or "") + (proc.stderr or "")}
    message = str(envelope.get("result", "")) + " " + (proc.stderr or "")
    if envelope.get("is_error") or proc.returncode != 0:
        if LIMIT_MARKERS.search(message):
            reset = re.search(r"\|(\d{10})", message)
            raise UsageLimitReached(message.strip()[:300], int(reset.group(1)) if reset else None)
        raise RuntimeError(f"claude exited {proc.returncode}: {message.strip()[:500]}")
    output = envelope.get("structured_output") or json.loads(envelope.get("result") or "{}")
    return {"extraction": output, "model": MODEL, "rubric": "r5a-cdlg-roles",
            "rubric_sha256": hashlib.sha256(prompt_text.encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema_text.encode()).hexdigest(), "started_at_utc": started,
            "latency_seconds": round(time.perf_counter() - t0, 2), "cli_version": cli_version(),
            "usage": envelope.get("usage")}


def cdlg_ids() -> list[str]:
    with (OUT / "cases.csv").open(encoding="utf-8") as handle:
        return [r["case_id"] for r in csv.DictReader(handle) if r["set"] == "cdlg"]


def do_extract(runs: Path, pause: float, max_wait_hours: float) -> None:
    rel = runs.relative_to(OUT / "runs")
    jobs = [(runs / f"{c}.json", OUT / "extractions_r5a_cdlg" / rel / f"{c}.json") for c in cdlg_ids()]
    jobs = [j for j in jobs if j[0].exists() and not j[1].exists()
            and json.loads(j[0].read_text()).get("status") == "success"]
    print(f"{len(jobs)} CDLG explanations to extract (rubric r5a)", flush=True)
    waited, i = 0.0, 0
    while i < len(jobs):
        source, target = jobs[i]
        record = json.loads(source.read_text(encoding="utf-8"))
        try:
            result = extract_roles(record["text"])
        except UsageLimitReached as exc:
            delay = max(60.0, exc.reset_epoch - time.time() + 60) if exc.reset_epoch else 1800.0
            waited += delay
            if waited > max_wait_hours * 3600:
                sys.exit("usage limit; stopping. Rerun to resume.")
            print(f"{datetime.now():%H:%M} usage limit; waiting {delay / 60:.0f} min", flush=True)
            time.sleep(delay)
            continue
        except Exception as exc:
            print(f"[{i + 1}/{len(jobs)}] error {source.stem}: {exc}", flush=True)
            i += 1
            continue
        result.update({"source": str(source.relative_to(ROOT)), "case_id": record["case_id"],
                       "generation_model": record.get("model")})
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        e = result["extraction"]
        print(f"[{i + 1}/{len(jobs)}] {source.stem} {e['operation_class']} {[(p['activity'], p['role']) for p in e['object_role_pairs']]}", flush=True)
        i += 1
        time.sleep(pause)


def graded(correct: int, predicted: set, reference: set) -> float:
    if predicted == reference:
        return 1.0
    return 0.5 if correct >= math.ceil(2 * len(reference) / 3) else 0.0


def class_of(roles: set) -> str:
    """Operation class from a set of roles (rubric r5a mapping)."""
    table = {frozenset({"added"}): "only_added", frozenset({"deleted"}): "only_deleted",
             frozenset({"moved"}): "only_moved", frozenset({"deleted", "added"}): "deleted_and_added",
             frozenset({"added", "moved"}): "added_and_moved", frozenset({"deleted", "moved"}): "deleted_and_moved",
             frozenset({"added", "deleted", "moved"}): "other"}
    return table.get(frozenset(roles), "unclear")


def do_score(runs: Path) -> None:
    rel = runs.relative_to(OUT / "runs")
    with (ROOT / "data" / "references" / "cdlg_case_ground_truth_one_per_log100_v1.csv").open(encoding="utf-8-sig") as h:
        refs = {r["case_id"]: r for r in csv.DictReader(h)}
    rows = []
    for cid in cdlg_ids():
        path = OUT / "extractions_r5a_cdlg" / rel / f"{cid}.json"
        if not path.exists():
            continue
        e = json.loads(path.read_text(encoding="utf-8"))["extraction"]
        text = json.loads((runs / f"{cid}.json").read_text(encoding="utf-8"))["text"]
        lm = json.loads((OUT / "audit" / f"{cid}.json").read_text(encoding="utf-8"))["label_map"]
        ref = refs[cid]
        ref_pairs = {(lm[a], role) for role, k in (("added", "activities_added_real"),
                     ("deleted", "activities_deleted_real"), ("moved", "activities_moved_real"))
                     for a in json.loads(ref[k]) if a in lm}
        affected = {a for a, _ in ref_pairs}
        if not affected:  # no observable reference (e.g. deleted activity never occurs): excluded, no 0/0 rule
            continue
        main_path = OUT / "extractions_r5" / rel / f"{cid}.json"
        e5 = json.loads(main_path.read_text(encoding="utf-8"))["extraction"]
        central = {a.upper() for a in e5.get("central_activities", [])}
        secondary = {a.upper() for a in e5.get("secondary_activities", [])} - central
        all_objects = {a.upper() for a in e["predicted_objects"]}
        all_pairs = {(p["activity"].upper(), p["role"]) for p in e["object_role_pairs"]}
        quote = e["supporting_quote"].strip()
        quote_valid = bool(quote) and quote in text

        def score(objects, pairs, op_class):
            objects = objects | {a for a, _ in pairs}  # every paired code is an object (rubric rule)
            o = graded(len(objects & affected), objects, affected)
            mr_raw = graded(len(pairs & ref_pairs), pairs, ref_pairs)
            exact = op_class == ref["operation_class"]
            pi_raw = 1.0 if mr_raw == 1.0 and exact and quote_valid else \
                0.5 if mr_raw >= 0.5 and quote_valid and op_class != "unclear" else 0.0
            mr = min(o, mr_raw)
            pi = min(o, mr, pi_raw)
            return o, mr_raw, pi_raw, mr, pi, float(o == mr == pi == 1.0), len(pairs & ref_pairs)

        main_pairs = {p for p in all_pairs if p[0] in central}
        main_class = class_of({r for _, r in main_pairs})
        o, mr_raw, pi_raw, mr, pi, rtu, hit = score(all_objects & central, main_pairs, main_class)
        o_a, _, _, mr_a, pi_a, rtu_a, _ = score(all_objects, all_pairs, e["operation_class"])
        rows.append({"case_id": cid, "local_change_type": ref["local_change_type"],
                     "global_drift_type": ref["global_drift_type"], "operation_class": ref["operation_class"],
                     "predicted_class": main_class, "predicted_class_all": e["operation_class"],
                     "n_affected": len(affected),
                     "O": o, "MR_raw": mr_raw, "PI_raw": pi_raw, "MR": mr, "PI": pi,
                     "quote_valid": float(quote_valid),
                     "role_coverage": hit / len(ref_pairs) if ref_pairs else 0.0,
                     "RTU": rtu, "overclaim": float(bool(secondary - affected)),
                     "O_all": o_a, "MR_all": mr_a, "PI_all": pi_a, "RTU_all": rtu_a})
    target = OUT / f"scores_cdlg_roles_{'_'.join(rel.parts)}.csv"
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    def line(label, rs):
        return f"{label:24s} n={len(rs):3d} " + " ".join(
            f"{m} {mean(r[m] for r in rs):.3f}" for m in ("O", "MR", "PI", "RTU", "overclaim", "RTU_all", "role_coverage", "quote_valid"))
    print(line("all", rows))
    for key in ("operation_class", "global_drift_type"):
        for v in sorted({r[key] for r in rows}):
            print(line(f"  {key}={v}", [r for r in rows if r[key] == v]))
    print(f"-> {target}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", choices=("extract", "score"))
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--pause", type=float, default=2.0)
    parser.add_argument("--max-wait-hours", type=float, default=8.0)
    args = parser.parse_args()
    runs = (args.runs if args.runs.is_absolute() else ROOT / args.runs).resolve()
    do_extract(runs, args.pause, args.max_wait_hours) if args.cmd == "extract" else do_score(runs)


if __name__ == "__main__":
    main()
