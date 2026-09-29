#!/usr/bin/env python3
"""Freeze the A* regions used by the uniform evidence-tau=0.95 run.

The evidence threshold is 0.95 for CF_OCC, CF_DIR, CF_POS, CF_REL, and
CF_LAG.  The independent directly-follows localization gate remains 0.99,
as recorded in the source run metadata.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
KEY = PACKAGE / "internal_after_grading/private_tau095_blind_key_26.csv"
SOURCE = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/artifacts/official/"
    "ostovar_atomic_noise_0_b200_algorithm_1_2_tau_sensitivity/"
    "evidence/tau_p95"
)
OUTPUT = PACKAGE / "localization/astar_regions_tau095_evidence_v1.csv"


def main() -> None:
    with KEY.open(encoding="utf-8-sig", newline="") as handle:
        keys = list(csv.DictReader(handle))

    rows: list[dict[str, str]] = []
    for key in keys:
        artifact = json.loads((SOURCE / f"{key['case_id']}.json").read_text())
        gate = artifact["relational_candidate_gate"]
        audit = gate["qualification_audit"]
        if float(gate["tau"]) != 0.99:
            raise SystemExit(f"Unexpected localization tau for {key['case_id']}")
        rows.append({
            "grading_id": key["grading_id"],
            "case_id": key["case_id"],
            "native_noise_percent": key["native_noise_percent"],
            "evidence_tau": "0.95",
            "localization_tau_dir": "0.99",
            "localized_a_star_anon": json.dumps(
                audit["selected_activities"], ensure_ascii=False
            ),
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} frozen A* regions to {OUTPUT}")


if __name__ == "__main__":
    main()
