#!/usr/bin/env python3
"""E4a step 4 (P0b), part 1: evidence for the E4a cases with the multi-perspective pipeline.

Writes results/e4a_time_injection/p0b/evidence/<case_id>.json (payload sent to the LLM, as
pcr.pipeline.llm_payload) and p0b/audit/<case_id>.json (label map, A*, T_WAIT audit).
Default: the 24 tuning cases. Requires Python >= 3.9.
"""
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

DATA = E4_RESULTS / "e4a_time_injection"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", default="tuning")
    parser.add_argument("--out", default="p0b")
    args = parser.parse_args()
    config = load_config()
    time_params = json.loads((E4_ROOT / "code" / "config_time.json").read_text())
    params = {k: time_params[k] for k in ("min_obs", "eps_time", "tau", "pairs_per_window") if k in time_params}
    out = DATA / args.out
    (out / "evidence").mkdir(parents=True, exist_ok=True)
    (out / "audit").mkdir(parents=True, exist_ok=True)
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["split"] == args.split]
    for case in cases:
        with gzip.open(DATA / "cases" / f"{case['case_id']}.json.gz", "rt", encoding="utf-8") as handle:
            data = json.load(handle)
        document = build_evidence_mp(data["before"], data["after"], config, seed_for(case["case_id"]),
                                     case_id=case["case_id"], time_params=params)
        (out / "evidence" / f"{case['case_id']}.json").write_text(
            json.dumps(llm_payload(document), ensure_ascii=False, indent=1), encoding="utf-8")
        (out / "audit" / f"{case['case_id']}.json").write_text(
            json.dumps({"kind": case["type"], **document["_audit"]}, ensure_ascii=False, indent=1), encoding="utf-8")
        families = {}
        for item in document["evidence"]:
            families[item["indicator"]] = families.get(item["indicator"], 0) + 1
        print(case["case_id"], case["type"], families, document["screening"], flush=True)


if __name__ == "__main__":
    main()
