#!/usr/bin/env python3
"""P3 ablations, step 1: evidence variants (no LLM). Design: docs/P3_ABLATION_PLAN_VI.md.

Every variant reuses the P2 case ids, windows and seeds (results/p2_main/cases.csv), so P2 run 1 of
glm-5.3-flash is the paired reference. Output per experiment:
results/p3_ablation/<exp>/{evidence,audit}/<case_id>.json and cases.csv (same columns as P2).

  e3_noselect   no evidence selection: Stage 2 qualification off (tau = eps_rel = 0), Stage 1 localization
                kept, so every candidate unit of the five control-flow families (POS/REL/LAG inside the
                localized region) is listed; no screening block (nothing was screened). ostovar3, cdlg, null_ostovar3, null_cdlg.
  e3_full       no selection at all: Stage 1 localization off (tau_loc = eps_loc = 0) and Stage 2 off
                (tau = eps_rel = 0), no screening block. cdlg, null_cdlg only: Ostovar does not fit the model
                context (median ~0.8 M prompt tokens); added 2026-11-16, author approved.
  e3b_v2en      same evidence as P2; prompt INTERPRET_EVIDENCE_V2_EN (without the reading rules added in
                R2/R3). ostovar3, null_ostovar3.
  e5_no_<FAM>   leave one control-flow family out (CF_OCC, CF_DIR, CF_POS, CF_REL, CF_LAG): pipeline rerun
                without that family, screening recomputed. ostovar3.
  e5_no_time    E4a type M: P2 evidence without the time family (items and screening entry removed).
  e5_no_cf      E4a type M: P2 evidence without the control-flow family.
  e8_labels     E4b (BPI 2017): original activity labels instead of A01... (anonymize_activities = false).
  e9_shuffle    P2 evidence with the evidence items in random order (seed_for(case_id) + 9). ostovar3, cdlg.
"""
from __future__ import annotations

import argparse
import copy
import csv
import gzip
import hashlib
import json
import random
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))

P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p3_ablation"
CF_FAMILIES = ["CF_OCC", "CF_DIR", "CF_POS", "CF_REL", "CF_LAG"]
FAMILY_PREFIX = {"CF_OCC": "OCC", "CF_DIR": "DIR", "CF_POS": "POS", "CF_REL": "REL", "CF_LAG": "LAG"}
EXPERIMENTS = {
    "e3_noselect": ("ostovar3", "cdlg", "null_ostovar3", "null_cdlg"),
    "e3_full": ("cdlg", "null_cdlg"),
    "e3b_v2en": ("ostovar3", "null_ostovar3"),
    **{f"e5_no_{f[3:].lower()}": ("ostovar3",) for f in CF_FAMILIES},
    "e5_no_time": ("e4a:M",), "e5_no_cf": ("e4a:M",),
    "e8_labels": ("e4b",),
    "e9_shuffle": ("ostovar3", "cdlg"),
}


def p2_cases() -> list[dict]:
    with (P2 / "cases.csv").open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def select(cases: list[dict], specs) -> list[dict]:
    out = []
    for spec in specs:
        set_, _, type_ = spec.partition(":")
        out += [c for c in cases if c["set"] == set_ and (not type_ or c["type"] == type_)]
    return out


def task_of(c: dict) -> dict:
    audit = json.loads((P2 / "audit" / f"{c['case_id']}.json").read_text(encoding="utf-8"))
    return audit["task"]


def rebuild(c: dict, config: dict) -> dict:
    """Rerun the P2 evidence construction of case c with a modified pipeline config."""
    from build_p2_cases import G, W, by_family_cf, read_cdlg
    from pcr.logs import read_mxml
    from pcr.paths import OSTOVAR_FULL
    from pcr.pipeline import build_evidence
    from sweep_evidence import seed_for
    task, seed = task_of(c), seed_for(c["case_id"])
    if task["set"] in ("e4a", "e4b"):
        from pipeline_mp import build_evidence_mp
        E4 = ROOT / "e4_multiperspective"
        tp = json.loads((E4 / "code" / "config_time.json").read_text())
        op = json.loads((E4 / "code" / "config_org.json").read_text())
        time_params = {k: tp[k] for k in ("min_obs", "eps_time", "tau", "pairs_per_window")}
        org_params = {k: op[k] for k in ("families", "min_obs", "eps", "eps_by_family", "tau", "pairs_per_window")
                      if k in op}
        with gzip.open(ROOT / task["source"], "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        return build_evidence_mp(data["before"], data["after"], config, seed, case_id=c["case_id"],
                                 time_params=time_params, org_params=org_params if task["set"] == "e4b" else None)
    traces = read_cdlg(task["source"]) if "cdlg" in task["set"] else read_mxml(OSTOVAR_FULL / task["source"])
    start, end = int(task["start"]), int(task["end"])
    return by_family_cf(build_evidence(traces[start - G - W:start - G], traces[end + G:end + G + W], config,
                                       seed=seed, case_id=c["case_id"]))


def drop_family(doc: dict, family: str) -> dict:
    """Remove one family of a multi-perspective P2 evidence document (items and screening entry)."""
    prefixes = {"time": ("TWAIT",), "control_flow": tuple(FAMILY_PREFIX.values())}[family]
    doc = copy.deepcopy(doc)
    doc["evidence"] = [e for e in doc["evidence"] if not e["id"].startswith(prefixes)]
    s = doc["screening"]
    gone = s["by_family"].pop(family)
    s["units_tested"] -= gone["units_tested"]
    s["items_expected_without_change"] = round(s["items_expected_without_change"] - gone["items_expected_without_change"], 2)
    return doc


def job(exp: str, c: dict) -> tuple[str, str]:
    from pcr.pipeline import llm_payload, load_config
    from sweep_evidence import seed_for
    target = OUT / exp / "evidence" / f"{c['case_id']}.json"
    if target.exists():
        return c["case_id"], "cached"
    p2_doc = json.loads((P2 / "evidence" / f"{c['case_id']}.json").read_text(encoding="utf-8"))
    p2_audit = json.loads((P2 / "audit" / f"{c['case_id']}.json").read_text(encoding="utf-8"))
    audit = dict(p2_audit, p3_experiment=exp)
    if exp == "e3_noselect":
        config = load_config()
        # Stage 1 (localization) kept; Stage 2 qualification off. Version with Stage 1 off as well
        # (tau_loc = eps_loc = 0): median 1,700 items / 1.8 M characters per Ostovar case, beyond the model
        # context; author chose this variant on 2026-11-14 (archive: results/p3_ablation/archive_e3_all_units/).
        config["qualification"].update({"tau": 0.0, "eps_rel": 0.0})
        doc = rebuild(c, config)
        audit.update(doc["_audit"], p3_experiment=exp)
        doc = llm_payload(doc)
        doc.pop("screening")
    elif exp == "e3_full":
        config = load_config()
        config["localization"].update({"tau_loc": 0.0, "eps_loc": 0.0})
        config["qualification"].update({"tau": 0.0, "eps_rel": 0.0})
        doc = rebuild(c, config)
        audit.update(doc["_audit"], p3_experiment=exp)
        doc = llm_payload(doc)
        doc.pop("screening")
    elif exp.startswith("e5_no_") and exp[6:] in ("occ", "dir", "pos", "rel", "lag"):
        family = "CF_" + exp[6:].upper()
        config = load_config()
        config["qualification"]["families"] = [f for f in config["qualification"]["families"] if f != family]
        config["qualification"]["gated_by_localization"] = [
            f for f in config["qualification"]["gated_by_localization"] if f != family]
        doc = rebuild(c, config)
        audit.update(doc["_audit"], p3_experiment=exp)
        doc = llm_payload(doc)
    elif exp in ("e5_no_time", "e5_no_cf"):
        doc = drop_family(p2_doc, "time" if exp == "e5_no_time" else "control_flow")
    elif exp == "e8_labels":
        config = load_config()
        config["anonymize_activities"] = False
        doc = rebuild(c, config)
        # scoring works on the P2 codes: label_map stays the anonymous P2 map (names -> A01...), and the
        # explanation is mapped back to codes before extraction (run_p3.py map-labels)
        audit.update(doc["_audit"], p3_experiment=exp, label_map=p2_audit["label_map"],
                     label_map_original=doc["_audit"]["label_map"])
        doc = llm_payload(doc)
    elif exp == "e9_shuffle":
        doc = copy.deepcopy(p2_doc)
        random.Random(seed_for(c["case_id"]) + 9).shuffle(doc["evidence"])
    elif exp == "e3b_v2en":
        doc = p2_doc
    else:
        raise ValueError(exp)
    (OUT / exp / "audit").mkdir(parents=True, exist_ok=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / exp / "audit" / f"{c['case_id']}.json").write_text(
        json.dumps(audit, ensure_ascii=False, default=str), encoding="utf-8")
    return c["case_id"], f"{len(doc['evidence'])} items"


def write_index(exp: str, cases: list[dict]):
    rows = []
    for c in cases:
        path = OUT / exp / "evidence" / f"{c['case_id']}.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        s = doc.get("screening", {})
        rows.append({**c, "n_evidence": len(doc["evidence"]),
                     "items_by_family": json.dumps({k: v["items"] for k, v in s.get("by_family", {}).items()}),
                     "items_expected_without_change": s.get("items_expected_without_change", ""),
                     "evidence_chars": path.stat().st_size, "evidence_path": str(path.relative_to(ROOT)),
                     "evidence_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    with (OUT / exp / "cases.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", nargs="*", default=list(EXPERIMENTS))
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    cases = p2_cases()
    plan = {exp: select(cases, EXPERIMENTS[exp]) for exp in args.exp}
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(job, exp, c): exp for exp, cs in plan.items() for c in cs}
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            if done % 50 == 0 or done == len(futures):
                print(f"[{done}/{len(futures)}] {futures[future]} {cid} {status}", flush=True)
    for exp, cs in plan.items():
        write_index(exp, cs)
        print(f"{exp}: {len(cs)} cases")


if __name__ == "__main__":
    main()
