#!/usr/bin/env python3
"""Run Algorithms 1 and 2 on Ostovar and measure how tau controls |E*|."""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
WORKSPACE = EXPERIMENT.parents[1]
ACIIDS_CODE = WORKSPACE / "Experiments/ACIIDS_2027/Code"
if str(ACIIDS_CODE) not in sys.path:
    sys.path.insert(0, str(ACIIDS_CODE))

from build_master_evidence import cdlg_cases, ostovar_cases  # noqa: E402
from evidence_features import neutralize_windows  # noqa: E402

from control_flow_evidence import (  # noqa: E402
    algorithm_1_change_localization_and_qualification,
    algorithm_2_evidence_construction_from_qualified_changes,
)
from control_flow_evidence.control_flow_indicators import CONTROL_FLOW_INDICATORS, aciids_affected_activities  # noqa: E402
from itertools import combinations
from control_flow_evidence.reference_windows import (  # noqa: E402
    bootstrap_reference_context_pairs,
    build_control_flow_context,
    common_analysis_universes,
)
from control_flow_evidence.relational_candidate_gate import (  # noqa: E402
    qualify_relational_candidate_activities_from_directly_follows,
)


def write_json(path: Path, value: object) -> int:
    text = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return len(text)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="Ostovar", choices=("Ostovar", "CDLG"))
    parser.add_argument("--level", default="Atomic", choices=("Atomic", "Composite"))
    parser.add_argument("--noise", default="0", choices=("0", "5", "10"))
    parser.add_argument(
        "--cdlg-target", type=int, default=6,
        help="Number of balanced CDLG episodes to select; ignored for Ostovar.",
    )
    parser.add_argument("--max-cases", type=int, default=0, help="0 means every matching case")
    parser.add_argument(
        "--case-ids-file", type=Path,
        help=("Optional CSV containing a case_id column. Restricts the run to "
              "exactly that case set before slicing with --case-start/--case-stop."),
    )
    parser.add_argument("--case-start", type=int, default=0,
                        help="Zero-based start index in the sorted case list")
    parser.add_argument("--case-stop", type=int,
                        help="Exclusive stop index in the sorted case list")
    parser.add_argument("--reference-pairs-per-state", type=int, default=100)
    parser.add_argument("--taus", type=float, nargs="+", default=[0.8, 0.9, 0.95, 0.975, 0.99])
    parser.add_argument(
        "--tau-by-indicator", nargs="+", metavar="INDICATOR=TAU",
        help="Run one mixed profile, e.g. CF_OCC=0.95 CF_DIR=0.99 ...",
    )
    parser.add_argument("--seed", type=int, default=20260910)
    parser.add_argument(
        "--region-seed", type=int,
        help="Independent seed for random_matched activity selection; defaults to --seed",
    )
    parser.add_argument("--include-zero-changes", action="store_true",
                        help="Reproduce the pseudocode literally; usually makes E* explode because tied zeros get q=1")
    parser.add_argument(
        "--minimum-change-by-indicator", nargs="+", metavar="INDICATOR=VALUE",
        help="Materiality gate, e.g. CF_OCC=0 CF_DIR=0 CF_POS=0 CF_REL=0.10 CF_LAG=0",
    )
    parser.add_argument(
        "--max-affected-activities", type=int, default=0,
        help="Top changed activities used by CF_REL and CF_LAG; 0 keeps every eligible activity",
    )
    parser.add_argument(
        "--rel-candidate-gate", choices=("qualified_dir_edges", "affected_support"),
        default="qualified_dir_edges",
    )
    parser.add_argument("--rel-gate-tau", type=float, default=0.99)
    parser.add_argument("--rel-gate-minimum-edge-change", type=float, default=0.10)
    parser.add_argument(
        "--lag-candidate-endpoints", choices=("either", "both"), default="both",
        help="Require either or both endpoints of a CF_LAG pair to be in the qualified activity set",
    )
    parser.add_argument(
        "--pos-candidate-gate", choices=("qualified_dir_activities", "all"),
        default="qualified_dir_activities",
        help="Restrict CF_POS to activities incident to qualified directly-follows edges",
    )
    parser.add_argument(
        "--activity-region-mode",
        choices=("affected", "random_matched", "all", "outside"),
        default="affected",
        help=("Activity region used to gate CF_POS, CF_REL, and CF_LAG: the "
              "localized A*, a size-matched random region, all activities, or "
              "the complement of A*. CF_OCC and CF_DIR remain ungated."),
    )
    parser.add_argument("--resume", action="store_true", help="Reuse complete per-case evidence files already in output")
    parser.add_argument("--output", type=Path, default=EXPERIMENT / "artifacts/algorithm_1_2_tau_sensitivity")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tau_profiles: list[tuple[str, float | dict[str, float]]]
    if args.tau_by_indicator:
        mixed = {}
        for entry in args.tau_by_indicator:
            code, separator, raw_value = entry.partition("=")
            if not separator or code not in CONTROL_FLOW_INDICATORS:
                raise SystemExit(f"Invalid --tau-by-indicator entry: {entry}")
            mixed[code] = float(raw_value)
        missing = set(CONTROL_FLOW_INDICATORS) - set(mixed)
        if missing:
            raise SystemExit(f"Missing mixed thresholds: {sorted(missing)}")
        tau_profiles = [("mixed", mixed)]
    else:
        tau_profiles = [(str(value), value) for value in args.taus]
    minimum_changes = {code: 0.0 for code in CONTROL_FLOW_INDICATORS}
    if args.minimum_change_by_indicator:
        for entry in args.minimum_change_by_indicator:
            code, separator, raw_value = entry.partition("=")
            if not separator or code not in CONTROL_FLOW_INDICATORS:
                raise SystemExit(f"Invalid --minimum-change-by-indicator entry: {entry}")
            minimum_changes[code] = float(raw_value)
    if args.dataset == "Ostovar":
        cases = [case for case in ostovar_cases(WORKSPACE, noise_setting=args.noise)
                 if case["private_truth"]["level"] == args.level]
    else:
        cases = cdlg_cases(
            WORKSPACE, target=args.cdlg_target, seed=args.seed,
            noise_setting=args.noise,
        )
    cases.sort(key=lambda case: case["case_id"])
    indexed_cases = list(enumerate(cases))
    if args.case_ids_file:
        with args.case_ids_file.open(encoding="utf-8-sig", newline="") as handle:
            requested_ids = {row["case_id"] for row in csv.DictReader(handle)}
        available_ids = {case["case_id"] for case in cases}
        missing_ids = requested_ids - available_ids
        if missing_ids:
            raise SystemExit(
                f"{len(missing_ids)} requested case IDs are unavailable: "
                f"{sorted(missing_ids)[:10]}"
            )
        indexed_cases = [
            (case_index, case) for case_index, case in indexed_cases
            if case["case_id"] in requested_ids
        ]
    indexed_cases = indexed_cases[args.case_start:args.case_stop]
    if args.max_cases:
        indexed_cases = indexed_cases[:args.max_cases]
    if not indexed_cases:
        raise SystemExit("No matching Ostovar cases")

    summary: list[dict[str, Any]] = []
    for progress_index, (case_index, case) in enumerate(indexed_cases):
        if args.resume and len(tau_profiles) == 1:
            profile_tag, tau = tau_profiles[0]
            tag = profile_tag.replace("0.", "p").replace(".", "p")
            existing = args.output / "evidence" / f"tau_{tag}" / f"{case['case_id']}.json"
            if existing.is_file():
                payload = json.loads(existing.read_text(encoding="utf-8"))
                evidence = payload["evidence"]
                counts = Counter(item["indicator"] for item in evidence)
                summary.append({
                    "case_id": case["case_id"], "tau": profile_tag,
                    "tau_profile_json": json.dumps(tau, sort_keys=True) if isinstance(tau, dict) else "",
                    "reference_pairs": payload["algorithm_1"]["reference_pairs"],
                    "candidate_units": payload.get("algorithm_1", {}).get("candidate_units", ""),
                    "evidence_items": len(evidence),
                    **{f"n_{code}": counts[code] for code in CONTROL_FLOW_INDICATORS},
                    "serialized_characters": existing.stat().st_size,
                    "estimated_tokens": math.ceil(existing.stat().st_size / 4),
                })
                print(f"[{progress_index + 1}/{len(indexed_cases)}] {case['case_id']} (resumed)", flush=True)
                continue
        pre, post, label_map = neutralize_windows(case["before"], case["after"], True)
        non_relational = {code: indicator for code, indicator in CONTROL_FLOW_INDICATORS.items() if code != "CF_REL"}
        preliminary_pre = build_control_flow_context(pre, non_relational)
        preliminary_post = build_control_flow_context(post, non_relational)
        universes = common_analysis_universes(preliminary_pre, preliminary_post)
        rel_gate_audit = None
        if args.rel_candidate_gate == "qualified_dir_edges":
            rel_gate = qualify_relational_candidate_activities_from_directly_follows(
                pre, post, args.reference_pairs_per_state, args.seed + case_index,
                tau=args.rel_gate_tau,
                minimum_support_change=args.rel_gate_minimum_edge_change,
            )
            ranked_affected = rel_gate.activities
            rel_gate_audit = {
                "tested_edge_count": rel_gate.tested_edge_count,
                "qualified_edge_count": len(rel_gate.qualified_edges),
                "selected_activities": rel_gate.activities,
            }
        else:
            ranked_affected = aciids_affected_activities(
                pre, post, support_delta_threshold=args.rel_gate_minimum_edge_change,
            )
        affected = (ranked_affected[:args.max_affected_activities]
                    if args.max_affected_activities > 0 else ranked_affected)
        affected_set = set(affected)
        all_activities = sorted(universes["CF_POS"])
        if args.activity_region_mode == "affected":
            region = list(affected)
        elif args.activity_region_mode == "random_matched":
            if len(affected) > len(all_activities):
                raise SystemExit(f"A* larger than activity universe for {case['case_id']}")
            region_seed = args.region_seed if args.region_seed is not None else args.seed
            region_rng = random.Random(region_seed + 1_000_003 * (case_index + 1))
            region = sorted(region_rng.sample(all_activities, len(affected)))
        elif args.activity_region_mode == "all":
            region = all_activities
        else:
            region = [activity for activity in all_activities if activity not in affected_set]
        region_set = set(region)
        universes["CF_REL"] = list(combinations(region, 2))
        pos_candidates_before_gate = len(universes["CF_POS"])
        if args.pos_candidate_gate == "qualified_dir_activities" or args.activity_region_mode != "affected":
            universes["CF_POS"] = [
                activity for activity in universes["CF_POS"] if activity in region_set
            ]
        lag_candidates_before_gate = len(universes["CF_LAG"])
        universes["CF_LAG"] = [
            unit for unit in universes["CF_LAG"]
            if ((unit[0] in region_set and unit[1] in region_set)
                if args.lag_candidate_endpoints == "both"
                else (unit[0] in region_set or unit[1] in region_set))
        ]
        pre_context = build_control_flow_context(pre, CONTROL_FLOW_INDICATORS, universes)
        post_context = build_control_flow_context(post, CONTROL_FLOW_INDICATORS, universes)
        references = bootstrap_reference_context_pairs(
            pre, post, CONTROL_FLOW_INDICATORS, universes,
            args.reference_pairs_per_state, args.seed + case_index,
        )
        expected_reference_pairs = 2 * args.reference_pairs_per_state
        write_json(args.output / "private_label_maps" / f"{case['case_id']}.json", label_map)
        threshold_floor = {
            code: min(float(profile[code]) if isinstance(profile, dict) else float(profile)
                      for _, profile in tau_profiles)
            for code in CONTROL_FLOW_INDICATORS
        }
        calibrated_changes = algorithm_1_change_localization_and_qualification(
            pre_context, post_context, CONTROL_FLOW_INDICATORS, references, threshold_floor,
            minimum_observed_change=None if args.include_zero_changes else minimum_changes,
        )
        for profile_tag, tau in tau_profiles:
            threshold = lambda code: float(tau[code]) if isinstance(tau, dict) else float(tau)
            qualified = [change for change in calibrated_changes
                         if change.empirical_strength >= threshold(change.indicator)]
            evidence = algorithm_2_evidence_construction_from_qualified_changes(
                pre_context, post_context, qualified, CONTROL_FLOW_INDICATORS,
            )
            counts = Counter(item["indicator"] for item in evidence)
            payload = {
                "schema_version": "ieee-access-algorithm-1-2-evidence-1.1",
                "case": {"case_id": case["case_id"], "dataset": args.dataset},
                "algorithm_1": {
                    "tau": tau,
                    "reference_pairs": expected_reference_pairs,
                    "candidate_units": sum(map(len, universes.values())),
                    "qualification": "q_j_u >= tau",
                    "finite_sample_correction": True,
                    "minimum_observed_change_by_indicator": None if args.include_zero_changes else minimum_changes,
                },
                "algorithm_2": {
                    "evidence_count": len(evidence),
                    "evidence_id_format": "{indicator_without_CF_}{within_indicator_index:03d}",
                },
                "relational_candidate_gate": {
                    "method": args.rel_candidate_gate,
                    "support_delta_threshold": args.rel_gate_minimum_edge_change,
                    "tau": args.rel_gate_tau if args.rel_candidate_gate == "qualified_dir_edges" else None,
                    "max_affected_activities": args.max_affected_activities,
                    "eligible_activity_count": len(ranked_affected),
                    "affected_activity_count": len(affected),
                    "candidate_pair_count": len(universes["CF_REL"]),
                    "qualification_audit": rel_gate_audit,
                },
                "activity_region": {
                    "mode": args.activity_region_mode,
                    "selection_seed": (args.region_seed if args.region_seed is not None else args.seed)
                    if args.activity_region_mode == "random_matched" else None,
                    "all_activity_count": len(all_activities),
                    "affected_activities": affected,
                    "affected_activity_count": len(affected),
                    "selected_activities": region,
                    "selected_activity_count": len(region),
                    "overlap_with_affected": len(region_set & affected_set),
                },
                "lag_candidate_gate": {
                    "method": f"{args.lag_candidate_endpoints}_endpoints_in_qualified_activities",
                    "candidate_pair_count_before_gate": lag_candidates_before_gate,
                    "candidate_pair_count": len(universes["CF_LAG"]),
                },
                "position_candidate_gate": {
                    "method": args.pos_candidate_gate,
                    "candidate_activity_count_before_gate": pos_candidates_before_gate,
                    "candidate_activity_count": len(universes["CF_POS"]),
                },
                "indicator_change_functions": {
                    code: indicator.change_function for code, indicator in CONTROL_FLOW_INDICATORS.items()
                },
                "evidence": evidence,
            }
            tag = profile_tag.replace("0.", "p").replace(".", "p")
            characters = write_json(args.output / "evidence" / f"tau_{tag}" / f"{case['case_id']}.json", payload)
            summary.append({
                "case_id": case["case_id"], "tau": profile_tag,
                "tau_profile_json": json.dumps(tau, sort_keys=True) if isinstance(tau, dict) else "",
                "reference_pairs": expected_reference_pairs, "candidate_units": sum(map(len, universes.values())),
                "evidence_items": len(evidence),
                **{f"n_{code}": counts[code] for code in CONTROL_FLOW_INDICATORS},
                "serialized_characters": characters,
                "estimated_tokens": math.ceil(characters / 4),
            })
        print(f"[{progress_index + 1}/{len(indexed_cases)}] {case['case_id']}", flush=True)
    summary_name = ("tau_sensitivity.csv" if args.case_start == 0 and args.case_stop is None
                    else f"tau_sensitivity_{args.case_start}_{args.case_stop or 'end'}.csv")
    write_csv(args.output / summary_name, summary)
    write_json(args.output / "run_metadata.json", {
        "dataset": args.dataset,
        "level": args.level if args.dataset == "Ostovar" else None,
        "noise": args.noise,
        "cdlg_target": args.cdlg_target if args.dataset == "CDLG" else None,
        "case_count": len(indexed_cases),
        "case_start": args.case_start,
        "case_stop": args.case_stop,
        "case_ids_file": str(args.case_ids_file) if args.case_ids_file else None,
        "taus": args.taus if not args.tau_by_indicator else None,
        "tau_by_indicator": tau_profiles[0][1] if args.tau_by_indicator else None,
        "reference_pairs_per_stable_state": args.reference_pairs_per_state,
        "total_reference_pairs": 2 * args.reference_pairs_per_state,
        "random_seed": args.seed,
        "activity_region_seed": args.region_seed if args.region_seed is not None else args.seed,
        "include_zero_changes": args.include_zero_changes,
        "minimum_change_by_indicator": None if args.include_zero_changes else minimum_changes,
        "max_affected_activities": args.max_affected_activities,
        "rel_candidate_gate": args.rel_candidate_gate,
        "rel_gate_tau": args.rel_gate_tau,
        "rel_gate_minimum_edge_change": args.rel_gate_minimum_edge_change,
        "lag_candidate_endpoints": args.lag_candidate_endpoints,
        "pos_candidate_gate": args.pos_candidate_gate,
        "activity_region_mode": args.activity_region_mode,
        "indicator_change_functions": {
            code: indicator.change_function for code, indicator in CONTROL_FLOW_INDICATORS.items()
        },
    })
    print(f"Wrote {args.output / summary_name}")


if __name__ == "__main__":
    main()
