#!/usr/bin/env python3
"""P0-C step 1: materialize v2 evidence for the tuning split (no LLM).

Writes, per configuration:
  results/p0_llm_calibration/evidence/<config>/<case_id>.json   payload sent to the LLM
  results/p0_llm_calibration/audit/<config>/<case_id>.json      private audit (labels, A*, seed)
  results/p0_llm_calibration/cases_<config>.csv                 case index with hashes
Configurations: B = configs/pipeline_v2.json (selected), A = sensitivity (0.99/0.99/0.10/0.10).
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))

from sweep_evidence import build_tasks  # noqa: E402
from pcr.logs import read_mxml  # noqa: E402
from pcr.paths import RESULTS  # noqa: E402
from pcr.pipeline import build_evidence, llm_payload, load_config  # noqa: E402

OUT = RESULTS / "p0_llm_calibration"
SIZES = {"2", "4"}


def config_for(name: str) -> dict:
    config = load_config()
    if name == "A":
        config = copy.deepcopy(config)
        config["localization"]["tau_loc"] = 0.99
        config["qualification"]["tau"] = 0.99
        config["qualification"]["eps_rel"] = 0.10
        config["spec_version"] += "+sensitivity-A"
    return config


def job(task):
    name = task["config"]
    target = OUT / "evidence" / name / f"{task['id']}.json"
    if target.exists():
        return task["id"], "cached"
    started = time.perf_counter()
    traces = read_mxml(Path(task["log"]))
    a, w, g = task["anchor"], task["window"], task.get("guard", 0)
    doc = build_evidence(traces[a - g - w:a - g], traces[a + g:a + g + w], config_for(name), task["seed"], task["id"])
    doc["_audit"]["elapsed_seconds"] = round(time.perf_counter() - started, 2)
    target.parent.mkdir(parents=True, exist_ok=True)
    (OUT / "audit" / name).mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(llm_payload(doc), ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "audit" / name / f"{task['id']}.json").write_text(
        json.dumps({"meta": task["meta"], "kind": task["kind"], **doc["_audit"]}, ensure_ascii=False), encoding="utf-8")
    return task["id"], f"done {doc['_audit']['elapsed_seconds']}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", choices=("A", "B"), default="B")
    parser.add_argument("--workers", type=int, default=9)
    args = parser.parse_args()
    tasks = [t for t in build_tasks("tuning", 200, 100) if t["meta"]["fragment_size"] in SIZES]
    guard = load_config()["guard_traces"]
    for t in tasks:
        t["config"] = args.config
        t["guard"] = guard
        if t["kind"] == "null":  # same geometry inside the stable prefix: L+ ends at trace 850
            t["anchor"] = 850 - guard - t["window"]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(job, t) for t in tasks]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            print(f"[{done}/{len(tasks)}] {cid} {status}", flush=True)
    rows = []
    for t in sorted(tasks, key=lambda t: t["id"]):
        path = OUT / "evidence" / args.config / f"{t['id']}.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        rows.append({"case_id": t["id"], "kind": t["kind"], "fragment_size": t["meta"]["fragment_size"],
                     "change_pattern": t["meta"]["change_pattern"], "noise_pct": t["meta"]["noise_pct"],
                     "drift_sequence": t["meta"].get("drift_sequence", ""),
                     "n_evidence": len(doc["evidence"]), "evidence_chars": path.stat().st_size,
                     "evidence_path": str(path.relative_to(ROOT)),
                     "evidence_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    with (OUT / f"cases_{args.config}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {OUT / f'cases_{args.config}.csv'} ({len(rows)} cases)")


if __name__ == "__main__":
    main()
