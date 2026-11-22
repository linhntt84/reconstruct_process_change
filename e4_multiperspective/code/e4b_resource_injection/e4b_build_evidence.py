#!/usr/bin/env python3
"""E4b: evidence with the multi-perspective pipeline (control-flow + T_WAIT + O_ASSIGN + O_CONC).
Writes results/e4b_resource_injection/<out>/{evidence,audit}/<case_id>.json. Requires Python >= 3.9."""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_ROOT, E4_RESULTS  # noqa: E402
from pipeline_mp import REPO, build_evidence_mp  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e0_parameter_setting"))
from sweep_evidence import seed_for  # noqa: E402
from pcr.pipeline import llm_payload, load_config  # noqa: E402

DATA = E4_RESULTS / "e4b_resource_injection"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", default="tuning")
    parser.add_argument("--out", default="p0b")
    args = parser.parse_args()
    config = load_config()
    tp = json.loads((E4_ROOT / "code" / "config_time.json").read_text())
    op = json.loads((E4_ROOT / "code" / "config_org.json").read_text())
    time_params = {k: tp[k] for k in ("min_obs", "eps_time", "tau", "pairs_per_window")}
    org_params = {k: op[k] for k in ("families", "min_obs", "eps", "eps_by_family", "tau", "pairs_per_window") if k in op}
    out = DATA / args.out
    (out / "evidence").mkdir(parents=True, exist_ok=True)
    (out / "audit").mkdir(parents=True, exist_ok=True)
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["split"] == args.split]
    for case in cases:
        with gzip.open(DATA / "cases" / f"{case['case_id']}.json.gz", "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        doc = build_evidence_mp(data["before"], data["after"], config, seed_for(case["case_id"]), case_id=case["case_id"],
                                time_params=time_params, org_params=org_params)
        (out / "evidence" / f"{case['case_id']}.json").write_text(json.dumps(llm_payload(doc), ensure_ascii=False, indent=1), encoding="utf-8")
        (out / "audit" / f"{case['case_id']}.json").write_text(json.dumps({"kind": case["type"], **doc["_audit"]}, ensure_ascii=False, indent=1), encoding="utf-8")
        fam = {k: v["items"] for k, v in doc["screening"]["by_family"].items()}
        print(case["case_id"], case["type"], case["target"], fam, flush=True)


if __name__ == "__main__":
    main()
