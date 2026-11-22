#!/usr/bin/env python3
"""P6: the four real BPI Challenge 2017 change points, rerun with pipeline v2 (author 2026-11-17). No LLM.

Change points: the four change points reported by Adams et al. (2023), in trace coordinates (traces ordered by case
start, complete events only; e4_multiperspective/docs/bpi2017_adams_2023_change_points.csv, column
boundary_case_index = first post-change trace). The submitted version took the same four points from an unpublished
manuscript; they coincide with Adams et al., which is now the cited source.
Windows as in the spec: L- = [cp - 250, cp - 50), L+ = [cp + 50, cp + 250). Evidence: multi-perspective pipeline v2
(control-flow families with Stage 1 and 2, T_WAIT, O_ASSIGN, O_CONC; frozen configs), activities anonymized as in
every other set. The original names are kept in the audit file (label_map) for presentation only.
Output: results/p6_bpi2017/{evidence,audit}/<case_id>.json and cases.csv (P2 columns), so run_p2.py can generate.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
E4 = ROOT / "e4_multiperspective"
sys.path.insert(0, str(E4 / "code"))
sys.path.insert(0, str(E4 / "code" / "e4b_resource_injection"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
from build_e4b import ADAMS, G, W, load_traces  # noqa: E402
from pipeline_mp import build_evidence_mp  # noqa: E402
from pcr.pipeline import llm_payload, load_config  # noqa: E402
from sweep_evidence import seed_for  # noqa: E402

OUT = ROOT / "results" / "p6_bpi2017"


def main():
    traces = load_traces()
    config = load_config()
    tp = json.loads((E4 / "code" / "config_time.json").read_text())
    op = json.loads((E4 / "code" / "config_org.json").read_text())
    time_params = {k: tp[k] for k in ("min_obs", "eps_time", "tau", "pairs_per_window")}
    org_params = {k: op[k] for k in ("families", "min_obs", "eps", "eps_by_family", "tau", "pairs_per_window")
                  if k in op}
    for sub in ("evidence", "audit"):
        (OUT / sub).mkdir(parents=True, exist_ok=True)
    with ADAMS.open(encoding="utf-8") as handle:
        points = list(csv.DictReader(handle))
    rows = []
    for p in points:
        cp, week = int(p["boundary_case_index"]), p["week_label"]
        cid = "bpi2017_" + hashlib.sha256(f"bpi2017::{cp}".encode()).hexdigest()[:12]
        before, after = traces[cp - G - W:cp - G], traces[cp + G:cp + G + W]
        doc = build_evidence_mp(before, after, config, seed_for(cid), case_id=cid,
                                time_params=time_params, org_params=org_params)
        path = OUT / "evidence" / f"{cid}.json"
        path.write_text(json.dumps(llm_payload(doc), ensure_ascii=False, indent=1), encoding="utf-8")
        audit = {"task": {"id": cid, "set": "bpi2017", "kind": "real", "change_point": cp, "adams_row": p,
                          "window_before": f"[{cp - G - W},{cp - G})", "window_after": f"[{cp + G},{cp + G + W})"},
                 **doc["_audit"]}
        (OUT / "audit" / f"{cid}.json").write_text(json.dumps(audit, ensure_ascii=False, indent=1, default=str),
                                                   encoding="utf-8")
        s = doc["screening"]
        fam = {k: v["items"] for k, v in s["by_family"].items()}
        rows.append({"case_id": cid, "set": "bpi2017", "kind": "real", "type": week, "source": "BPI Challenge 2017",
                     "noise_pct": "", "drift": "", "start": cp, "end": cp, "n_evidence": len(doc["evidence"]),
                     "items_by_family": json.dumps(fam),
                     "items_expected_without_change": s.get("items_expected_without_change", ""),
                     "evidence_chars": path.stat().st_size, "evidence_path": str(path.relative_to(ROOT)),
                     "evidence_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        print(cid, week, cp, fam, flush=True)
    with (OUT / "cases.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
