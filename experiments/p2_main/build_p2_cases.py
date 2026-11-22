#!/usr/bin/env python3
"""P2 step 1: evidence for every evaluation case with the frozen pipeline (spec_version 2.0). No LLM.

Sets (docs/PIPELINE_V2_SPEC_VI.md, section 10; decisions in docs/EXPERIMENT_LOG_VI.md, 2026-11-13):
  ostovar3  Ostovar size 3, 26 drifts x 3 noise levels (references: ostovar_size3_..._v2.csv)
  ostovar5  Ostovar size 5, 26 drifts x 3 noise levels (references: ostovar_size5_references_v2.csv)
  cdlg      the 100 CDLG cases of the submitted version (cdlg_case_ground_truth_one_per_log100_v1.csv)
  e4a       E4a evaluation split (time injection, 104 cases)
  e4b       E4b evaluation split (resource injection, 40 cases)
  null      Ostovar: one pair per evaluated log (39 size 3 + 39 size 5), L- = [350,550), L+ = [650,850);
            CDLG: 50 logs drawn with seed 20261113 among logs whose first change point is >= 550;
            same geometry, L+ ends 50 traces before the first change point.
Windows (spec section 1): w = 200, g = 50, L- = [cp - g - w, cp - g), L+ = [end + g, end + g + w),
end = cp for sudden changes and the end of the transition for gradual CDLG changes.
Ostovar and CDLG are treated as activity-only logs (spec section 10): the control-flow evidence of
pcr.pipeline.build_evidence, with screening.by_family = {control_flow}. E4a/E4b go through
build_evidence_mp with the frozen config_time.json / config_org.json.
Seed of every case: sweep_evidence.seed_for(case_id).
Outputs: results/p2_main/evidence/<case_id>.json (LLM payload), audit/<case_id>.json, cases.csv.
Requires Python >= 3.9 (pandas not needed).
"""
from __future__ import annotations

import argparse
import ast
import csv
import gzip
import hashlib
import json
import random
import sys
import time
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
sys.path.insert(0, str(ROOT / "experiments" / "e1_prodrift"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))

from pcr.logs import _local, is_technical_activity, read_mxml  # noqa: E402
from pcr.paths import OSTOVAR_FULL, REFERENCES, RESULTS  # noqa: E402
from pcr.pipeline import build_evidence, llm_payload, load_config  # noqa: E402
from sweep_evidence import NOISE_SUFFIX, seed_for  # noqa: E402
from run_prodrift import CDLG  # noqa: E402

OUT = RESULTS / "p2_main"
E4 = ROOT / "e4_multiperspective"
W, G = 200, 50
NULL_SEED, N_CDLG_NULL = 20261113, 50


def read_cdlg(log: str) -> list[list[str]]:
    number = int(log.split("_")[1])
    with zipfile.ZipFile(CDLG / f"without_noise_part_{1 if number <= 50 else 2}.zip") as archive, \
            archive.open(log) as handle:
        root = ET.parse(handle).getroot()
    traces = []
    for trace in root:
        if _local(trace.tag) != "trace":
            continue
        acts = []
        for event in trace:
            if _local(event.tag) != "event":
                continue
            fields = {e.get("key"): e.get("value") for e in event}
            name = fields.get("concept:name")
            if fields.get("lifecycle:transition", "complete").lower() == "complete" and name \
                    and not is_technical_activity(name):
                acts.append(name)
        traces.append(acts)
    return traces


def ostovar_tasks() -> list[dict]:
    tasks, logs = [], {}
    with (REFERENCES / "ostovar_size3_atomic_object_ground_truth_v2.csv").open(encoding="utf-8-sig") as handle:
        size3 = list(csv.DictReader(handle))
    for noise, suffix in NOISE_SUFFIX.items():  # case ids as in the submitted version (sweep_evidence size3)
        for row in size3:
            pattern, drift = row["change_pattern"], row["drift_sequence"]
            filename = f"Atomic_{pattern}_output_{pattern}{suffix}.xes.gz"
            key = (f"ostovar::{filename}::{drift}" if noise == "0"
                   else f"ostovar::{ {'2.5': '5', '5': '10'}[noise] }::{filename}::{drift}".replace(" ", ""))
            cid = "case_" + hashlib.sha256(key.encode()).hexdigest()[:16]
            log = f"Size3/Atomic/{pattern}/output/{pattern}{suffix}.mxml.gz"
            tasks.append({"id": cid, "set": "ostovar3", "kind": "drift", "type": pattern, "source": log,
                          "noise_pct": noise, "drift": drift, "start": 900 if drift == "1" else 1900})
            logs.setdefault(log, ("3", pattern, noise))
    with (REFERENCES / "ostovar_size5_references_v2.csv").open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            tasks.append({"id": row["case_id"], "set": "ostovar5", "kind": "drift", "type": row["change_pattern"],
                          "source": row["source_log"], "noise_pct": row["noise_pct"],
                          "drift": row["drift_sequence"], "start": int(row["anchor_trace"])})
            logs.setdefault(row["source_log"], ("5", row["change_pattern"], row["noise_pct"]))
    for log, (size, pattern, noise) in sorted(logs.items()):
        tasks.append({"id": "null_" + hashlib.sha256(log.encode()).hexdigest()[:16], "set": f"null_ostovar{size}",
                      "kind": "null", "type": pattern, "source": log, "noise_pct": noise, "drift": "",
                      "start": 850 - G - W})  # L- = [350, 550), L+ = [650, 850)
    for t in tasks:
        t["end"] = t["start"]
    return tasks


def cdlg_tasks() -> list[dict]:
    with (REFERENCES / "cdlg_case_ground_truth_one_per_log100_v1.csv").open(encoding="utf-8-sig") as handle:
        cases = list(csv.DictReader(handle))
    with (REFERENCES / "cdlg_gold_standard.csv").open(encoding="utf-8-sig") as handle:
        gold = {r["log_name"]: r for r in csv.DictReader(handle)}
    tasks = [{"id": c["case_id"], "set": "cdlg", "kind": "drift", "type": c["local_change_type"],
              "source": c["log_name"], "noise_pct": "0", "drift": c["drift_id"],
              "start": int(c["change_trace_start"]), "end": int(c["change_trace_end"])} for c in cases]
    eligible = sorted({c["log_name"] for c in cases
                       if min(ast.literal_eval(gold[c["log_name"]]["change_point"])) >= W + 2 * G + G + W})
    for log in sorted(random.Random(NULL_SEED).sample(eligible, N_CDLG_NULL)):
        first = min(ast.literal_eval(gold[log]["change_point"]))
        anchor = first - G - W - G  # L+ = [first - 250, first - 50)
        tasks.append({"id": "null_cdlg_" + hashlib.sha256(log.encode()).hexdigest()[:12], "set": "null_cdlg",
                      "kind": "null", "type": "", "source": log, "noise_pct": "0", "drift": "",
                      "start": anchor, "end": anchor})
    return tasks


def e4_tasks(name: str) -> list[dict]:
    folder = {"e4a": "e4a_time_injection", "e4b": "e4b_resource_injection"}[name]
    with (E4 / "results" / folder / "cases.csv").open(encoding="utf-8") as handle:
        rows = [r for r in csv.DictReader(handle) if r["split"] == "evaluation"]
    return [{"id": r["case_id"], "set": name, "kind": "null" if r["type"] == "N" else "drift", "type": r["type"],
             "source": str((E4 / "results" / folder / "cases" / f"{r['case_id']}.json.gz").relative_to(ROOT)),
             "noise_pct": "", "drift": "", "start": "", "end": ""} for r in rows]


def by_family_cf(document: dict) -> dict:
    s = document["screening"]
    s["by_family"] = {"control_flow": {"units_tested": s["units_tested"], "items": len(document["evidence"]),
                                       "items_expected_without_change": s["items_expected_without_change"]}}
    return document


def job(task: dict) -> tuple[str, str]:
    target = OUT / "evidence" / f"{task['id']}.json"
    if target.exists():
        return task["id"], "cached"
    started = time.perf_counter()
    config, seed = load_config(), seed_for(task["id"])
    if task["set"] in ("e4a", "e4b"):
        from pipeline_mp import build_evidence_mp
        tp = json.loads((E4 / "code" / "config_time.json").read_text())
        op = json.loads((E4 / "code" / "config_org.json").read_text())
        time_params = {k: tp[k] for k in ("min_obs", "eps_time", "tau", "pairs_per_window")}
        org_params = {k: op[k] for k in ("families", "min_obs", "eps", "eps_by_family", "tau", "pairs_per_window")
                      if k in op}
        with gzip.open(ROOT / task["source"], "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        doc = build_evidence_mp(data["before"], data["after"], config, seed, case_id=task["id"],
                                time_params=time_params, org_params=org_params if task["set"] == "e4b" else None)
    else:
        traces = (read_cdlg(task["source"]) if "cdlg" in task["set"]
                  else read_mxml(OSTOVAR_FULL / task["source"]))
        before = traces[task["start"] - G - W:task["start"] - G]
        after = traces[task["end"] + G:task["end"] + G + W]
        if len(before) != W or len(after) != W:
            raise ValueError(f"{task['id']}: windows {len(before)}/{len(after)} traces")
        doc = by_family_cf(build_evidence(before, after, config, seed=seed, case_id=task["id"]))
    doc["_audit"]["elapsed_seconds"] = round(time.perf_counter() - started, 2)
    (OUT / "audit").mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(llm_payload(doc), ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "audit" / f"{task['id']}.json").write_text(
        json.dumps({"task": task, "seed": seed, **doc["_audit"]}, ensure_ascii=False, default=str), encoding="utf-8")
    return task["id"], f"done {doc['_audit']['elapsed_seconds']}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--sets", nargs="+", default=["ostovar", "cdlg", "e4a", "e4b"])
    args = parser.parse_args()
    tasks = []
    for name in args.sets:
        tasks += ostovar_tasks() if name == "ostovar" else cdlg_tasks() if name == "cdlg" else e4_tasks(name)
    ids = [t["id"] for t in tasks]
    assert len(ids) == len(set(ids)), "duplicate case ids"
    (OUT / "evidence").mkdir(parents=True, exist_ok=True)
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(job, t) for t in tasks]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            print(f"[{done}/{len(tasks)}] {cid} {status}", flush=True)
    rows = []
    for t in tasks:
        path = OUT / "evidence" / f"{t['id']}.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        fam = {k: v["items"] for k, v in doc["screening"].get("by_family", {}).items()}
        rows.append({"case_id": t["id"], "set": t["set"], "kind": t["kind"], "type": t["type"],
                     "source": t["source"], "noise_pct": t["noise_pct"], "drift": t["drift"],
                     "start": t["start"], "end": t["end"], "n_evidence": len(doc["evidence"]),
                     "items_by_family": json.dumps(fam),
                     "items_expected_without_change": doc["screening"]["items_expected_without_change"],
                     "evidence_chars": path.stat().st_size, "evidence_path": str(path.relative_to(ROOT)),
                     "evidence_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    with (OUT / "cases.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {OUT / 'cases.csv'} ({len(rows)} cases)")


if __name__ == "__main__":
    main()
