#!/usr/bin/env python3
"""Map reviewed Size3 Ostovar object labels to an evidence run's Axx labels.

The reviewed CSV is keyed by real CPN activity names.  Those names are the
canonical reference: anonymized labels in that CSV are deliberately ignored,
because the labeling utility and the evidence pipeline use different ordering
rules.  This script applies each run's own private real-to-anonymous map.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
WORKSPACE = EXPERIMENT.parents[1]
DEFAULT_LABELS = WORKSPACE / "Data/nhan_de_xuat_size3/bang_nhan_size3.csv"
DEFAULT_CASES = WORKSPACE / "Code/outputs/ostovar_pilot/experiment_cases.csv"
DEFAULT_RUN = (
    EXPERIMENT
    / "artifacts/official/ostovar_atomic_noise_0_b200_algorithm_1_2_tau_sensitivity"
)
DEFAULT_OUTPUT = EXPERIMENT / "ground_truth/ostovar_size3_atomic_object_ground_truth_v1.csv"
NOISE_PERCENT = {"0": 0.0, "5": 2.5, "10": 5.0}


ROLE_TO_FIELD = {
    "thêm": "activities_added",
    "xóa": "activities_deleted",
    "di chuyển": "activities_moved",
    "đổi tỷ trọng": "activities_reweighted",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def json_list(values: list[str]) -> str:
    return json.dumps(sorted(set(values)), ensure_ascii=False)


def public_case_id(filename: str, drift_sequence: str, noise_setting: str) -> str:
    private_key = (
        f"ostovar::{filename}::{drift_sequence}"
        if noise_setting == "0"
        else f"ostovar::{noise_setting}::{filename}::{drift_sequence}"
    )
    return "case_" + hashlib.sha256(private_key.encode()).hexdigest()[:16]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", type=Path, default=DEFAULT_LABELS)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--run-root", type=Path, default=DEFAULT_RUN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--noise-setting", choices=sorted(NOISE_PERCENT), default="0",
                        help="0=clean, 5=native 2.5%%, 10=native 5%%")
    args = parser.parse_args()

    proposed = read_csv(args.labels)
    case_rows = read_csv(args.cases)
    selected_atomic = {
        (row["change_pattern"], row["drift_sequence"]): row
        for row in case_rows
        if row["level"] == "Atomic"
        and float(row.get("noise_pct", 0)) == NOISE_PERCENT[args.noise_setting]
    }

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in proposed:
        grouped[(row["pattern"], row["diem_drift"])].append(row)

    output: list[dict[str, str]] = []
    errors: list[str] = []
    for key in sorted(grouped):
        pattern, drift_sequence = key
        source_rows = grouped[key]
        case = selected_atomic.get(key)
        if case is None:
            errors.append(f"Không tìm thấy case cho {key}")
            continue
        case_id = public_case_id(case["filename"], drift_sequence, args.noise_setting)
        map_path = args.run_root / "private_label_maps" / f"{case_id}.json"
        if not map_path.exists():
            errors.append(f"Thiếu label map: {map_path}")
            continue
        mapping: dict[str, str] = json.loads(map_path.read_text(encoding="utf-8"))

        roles_real: dict[str, list[str]] = {field: [] for field in ROLE_TO_FIELD.values()}
        details: list[str] = []
        for row in source_rows:
            role = row["VAI_TRO"].strip()
            if role not in ROLE_TO_FIELD:
                errors.append(f"Vai trò không hỗ trợ trong {key}: {role!r}")
                continue
            objects = [value.strip() for value in row["DOI_TUONG"].split(",") if value.strip()]
            roles_real[ROLE_TO_FIELD[role]].extend(objects)
            if row.get("chi_tiet", "").strip():
                details.append(row["chi_tiet"].strip())

        missing = sorted({a for values in roles_real.values() for a in values if a not in mapping})
        if missing:
            errors.append(f"{case_id}: activity không có trong label map: {missing}")
            continue

        roles_anon = {
            field: [mapping[value] for value in values]
            for field, values in roles_real.items()
        }
        affected_real = [value for values in roles_real.values() for value in values]
        affected_anon = [value for values in roles_anon.values() for value in values]
        role_pairs_real = [
            {"object": value, "role": role}
            for role, field in ROLE_TO_FIELD.items()
            for value in roles_real[field]
        ]
        role_pairs_anon = [
            {"object": value, "role": role}
            for role, field in ROLE_TO_FIELD.items()
            for value in roles_anon[field]
        ]
        active_roles = [role for role, field in ROLE_TO_FIELD.items() if roles_real[field]]
        operation_class = active_roles[0] if len(active_roles) == 1 else "+".join(active_roles)

        output.append({
            "case_id": case_id,
            "source_filename": case["filename"],
            "change_pattern": pattern,
            "pattern_code": source_rows[0]["ma_pattern"],
            "drift_sequence": drift_sequence,
            "noise_setting": args.noise_setting,
            "native_noise_percent": str(NOISE_PERCENT[args.noise_setting]),
            "transition_start_trace": case["ground_truth_trace"],
            "detected_change_peak": source_rows[0]["moc_drift"],
            "stable_before_window": source_rows[0]["cua_so_truoc"],
            "stable_after_window": source_rows[0]["cua_so_sau"],
            "operation_class": operation_class,
            "affected_activities_real": json_list(affected_real),
            "affected_activities_anon": json_list(affected_anon),
            "activities_added_real": json_list(roles_real["activities_added"]),
            "activities_added_anon": json_list(roles_anon["activities_added"]),
            "activities_deleted_real": json_list(roles_real["activities_deleted"]),
            "activities_deleted_anon": json_list(roles_anon["activities_deleted"]),
            "activities_moved_real": json_list(roles_real["activities_moved"]),
            "activities_moved_anon": json_list(roles_anon["activities_moved"]),
            "activities_reweighted_real": json_list(roles_real["activities_reweighted"]),
            "activities_reweighted_anon": json_list(roles_anon["activities_reweighted"]),
            "object_role_pairs_real": json.dumps(role_pairs_real, ensure_ascii=False),
            "object_role_pairs_anon": json.dumps(role_pairs_anon, ensure_ascii=False),
            "activity_label_map_real_to_anon": json.dumps(mapping, ensure_ascii=False, sort_keys=True),
            "label_details": " | ".join(details),
            "label_status": "da_anh_xa_cho_run_cho_xac_nhan",
            "annotation_source": str(args.labels.relative_to(WORKSPACE)),
        })

    if errors:
        raise SystemExit("\n".join(errors))
    if len(output) != 26:
        raise SystemExit(f"Expected 26 cases, produced {len(output)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {len(output)} cases to {args.output}")


if __name__ == "__main__":
    main()
