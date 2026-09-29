#!/usr/bin/env python3
"""Score blind object/role predictions against the frozen private key.

This script is the only scoring implementation for this package. It performs
schema validation, joins by opaque grading ID, applies the two-thirds object
gate, computes MR/PI, and writes both case-level and aggregate results.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
from collections import Counter, defaultdict
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
DEFAULT_PREDICTIONS = (
    WORKSPACE / "Latex/Kết quả thực nghiệm/deepseek-cdlgblind_all_graded.csv"
)
PRIVATE_KEY = PACKAGE / "internal_after_grading/private_blind_key.csv"
GRADER_COPY = PACKAGE / "grader_outputs/deepseek_cdlg_blind_predictions.csv"
SCORED = PACKAGE / "results/deepseek_cdlg_scored_policy_v1.csv"
SUMMARY = PACKAGE / "results/deepseek_cdlg_summary_policy_v1.csv"
BY_PATTERN = PACKAGE / "results/deepseek_cdlg_by_pattern_policy_v1.csv"
SUMMARY_MD = PACKAGE / "results/RESULTS_SUMMARY.md"

ALLOWED_PATTERNS = {
    "only_added",
    "only_deleted",
    "only_moved",
    "deleted_and_added",
    "added_and_moved",
    "deleted_and_moved",
    "other",
    "unclear",
}
ALLOWED_ROLES = {"added", "deleted", "moved"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise SystemExit(f"Refusing to write an empty result: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def parse_objects(value: str, field: str, grading_id: str) -> set[str]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{grading_id}: invalid JSON in {field}: {exc}") from exc
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise SystemExit(f"{grading_id}: {field} must be a JSON string array")
    objects = {item.strip().upper() for item in parsed}
    if any(not (len(item) == 3 and item[0] == "A" and item[1:].isdigit()) for item in objects):
        raise SystemExit(f"{grading_id}: invalid anonymized object in {field}: {sorted(objects)}")
    return objects


def parse_pairs(value: str, grading_id: str) -> set[tuple[str, str]]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise SystemExit(
            f"{grading_id}: invalid JSON in predicted_object_role_pairs: {exc}"
        ) from exc
    if not isinstance(parsed, list):
        raise SystemExit(f"{grading_id}: predicted_object_role_pairs must be a JSON list")
    pairs: set[tuple[str, str]] = set()
    for item in parsed:
        if not isinstance(item, list) or len(item) != 2:
            raise SystemExit(f"{grading_id}: invalid object-role pair: {item!r}")
        obj, role = str(item[0]).strip().upper(), str(item[1]).strip().lower()
        if not (len(obj) == 3 and obj[0] == "A" and obj[1:].isdigit()):
            raise SystemExit(f"{grading_id}: invalid object code in pair: {obj}")
        if role not in ALLOWED_ROLES:
            raise SystemExit(f"{grading_id}: invalid role: {role}")
        pairs.add((obj, role))
    return pairs


def reference_pairs(key: dict[str, str]) -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for field, role in (
        ("activities_added_anon", "added"),
        ("activities_deleted_anon", "deleted"),
        ("activities_moved_anon", "moved"),
    ):
        for obj in json.loads(key[field]):
            pairs.add((str(obj).upper(), role))
    return pairs


def threshold(size: int) -> int:
    return math.ceil(2 * size / 3)


def fmt_set(values: set[str]) -> str:
    return json.dumps(sorted(values), ensure_ascii=False)


def fmt_pairs(values: set[tuple[str, str]]) -> str:
    return json.dumps([list(pair) for pair in sorted(values)], ensure_ascii=False)


def score_row(prediction: dict[str, str], key: dict[str, str]) -> dict[str, object]:
    grading_id = key["grading_id"]
    predicted_objects = parse_objects(
        prediction["predicted_objects"], "predicted_objects", grading_id
    )
    predicted_pairs = parse_pairs(prediction["predicted_object_role_pairs"], grading_id)
    pair_objects = {obj for obj, _ in predicted_pairs}
    if not pair_objects <= predicted_objects:
        raise SystemExit(
            f"{grading_id}: pair objects absent from predicted_objects: "
            f"{sorted(pair_objects - predicted_objects)}"
        )

    predicted_pattern = prediction["predicted_pattern"].strip()
    if predicted_pattern not in ALLOWED_PATTERNS:
        raise SystemExit(f"{grading_id}: unsupported predicted_pattern={predicted_pattern!r}")

    affected = {str(item).upper() for item in json.loads(key["affected_activities_anon"])}
    ref_pairs = reference_pairs(key)
    if affected != {obj for obj, _ in ref_pairs}:
        raise SystemExit(f"{grading_id}: frozen affected set and role pairs disagree")

    correct_objects = predicted_objects & affected
    missing_objects = affected - predicted_objects
    incorrect_objects = predicted_objects - affected
    object_threshold = threshold(len(affected))
    if predicted_objects == affected:
        object_score = 1.0
    elif len(correct_objects) >= object_threshold:
        object_score = 0.5
    else:
        object_score = 0.0

    correct_pairs = predicted_pairs & ref_pairs
    missing_pairs = ref_pairs - predicted_pairs
    incorrect_pairs = predicted_pairs - ref_pairs
    role_threshold = threshold(len(ref_pairs))
    role_coverage = len(correct_pairs) / len(ref_pairs) if ref_pairs else 0.0
    if predicted_pairs == ref_pairs:
        mr_raw = 1.0
    elif len(correct_pairs) >= role_threshold:
        mr_raw = 0.5
    else:
        mr_raw = 0.0

    reference_pattern = key["operation_class"].strip()
    pattern_exact = predicted_pattern == reference_pattern
    quote = prediction["supporting_quote"].strip()
    quote_valid = bool(quote) and quote in prediction["llm_explanation_full"]
    if mr_raw == 1.0 and pattern_exact and quote_valid:
        pi_raw = 1.0
    elif mr_raw >= 0.5 and quote_valid and predicted_pattern != "unclear":
        pi_raw = 0.5
    else:
        pi_raw = 0.0

    mr = min(object_score, mr_raw)
    pi = min(object_score, mr, pi_raw)
    return {
        "grading_id": grading_id,
        "case_id": key["case_id"],
        "subset": (
            "excluded_reference_conflict_20"
            if key["excluded_from_primary_80"].lower() == "true"
            else "primary_reference_consistent_80"
        ),
        "reference_pattern": reference_pattern,
        "predicted_pattern": predicted_pattern,
        "pattern_exact": int(pattern_exact),
        "affected_activities_anon": fmt_set(affected),
        "predicted_objects_anon": fmt_set(predicted_objects),
        "correct_objects": fmt_set(correct_objects),
        "missing_objects": fmt_set(missing_objects),
        "incorrect_objects": fmt_set(incorrect_objects),
        "partial_object_threshold": object_threshold,
        "OBJECT": f"{object_score:g}",
        "reference_object_role_pairs": fmt_pairs(ref_pairs),
        "predicted_object_role_pairs": fmt_pairs(predicted_pairs),
        "correct_object_role_pairs": fmt_pairs(correct_pairs),
        "missing_object_role_pairs": fmt_pairs(missing_pairs),
        "incorrect_object_role_pairs": fmt_pairs(incorrect_pairs),
        "object_role_coverage": f"{role_coverage:.6f}",
        "partial_role_threshold": role_threshold,
        "MR_raw": f"{mr_raw:g}",
        "MR": f"{mr:g}",
        "supporting_quote_valid": int(quote_valid),
        "PI_raw": f"{pi_raw:g}",
        "PI": f"{pi:g}",
        "prediction_note": prediction["prediction_note"],
    }


def aggregate(label: str, rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        raise SystemExit(f"Empty aggregate subset: {label}")

    def mean(field: str) -> float:
        return sum(float(row[field]) for row in rows) / len(rows)

    distribution = Counter((str(row["MR"]), str(row["PI"])) for row in rows)
    return {
        "subset": label,
        "n": len(rows),
        "mean_OBJECT": f"{mean('OBJECT'):.6f}",
        "mean_MR": f"{mean('MR'):.6f}",
        "mean_PI": f"{mean('PI'):.6f}",
        "mean_object_role_coverage": f"{mean('object_role_coverage'):.6f}",
        "exact_object_count": sum(float(row["OBJECT"]) == 1.0 for row in rows),
        "exact_pattern_count": sum(int(row["pattern_exact"]) == 1 for row in rows),
        "full_score_count": sum(
            float(row["OBJECT"]) == float(row["MR"]) == float(row["PI"]) == 1.0
            for row in rows
        ),
        "valid_quote_count": sum(int(row["supporting_quote_valid"]) == 1 for row in rows),
        "MR_PI_distribution": json.dumps(
            {f"{mr}/{pi}": count for (mr, pi), count in sorted(distribution.items())},
            ensure_ascii=False,
            sort_keys=True,
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", type=Path, default=DEFAULT_PREDICTIONS)
    args = parser.parse_args()

    predictions_rows = read_csv(args.predictions)
    key_rows = read_csv(PRIVATE_KEY)
    predictions = {row["grading_id"]: row for row in predictions_rows}
    keys = {row["grading_id"]: row for row in key_rows}
    if len(predictions) != len(predictions_rows):
        raise SystemExit("Duplicate grading_id in prediction file")
    if len(keys) != len(key_rows):
        raise SystemExit("Duplicate grading_id in private key")
    if set(predictions) != set(keys):
        raise SystemExit(
            "Blind-ID mismatch: "
            f"missing predictions={sorted(set(keys) - set(predictions))}; "
            f"unknown predictions={sorted(set(predictions) - set(keys))}"
        )

    scored = [score_row(predictions[key], keys[key]) for key in sorted(keys)]
    primary = [row for row in scored if row["subset"] == "primary_reference_consistent_80"]
    excluded = [row for row in scored if row["subset"] == "excluded_reference_conflict_20"]
    summaries = [
        aggregate("all_valid_outputs", scored),
        aggregate("primary_reference_consistent", primary),
        aggregate("excluded_reference_conflict", excluded),
    ]

    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in scored:
        grouped[(str(row["subset"]), str(row["reference_pattern"]))].append(row)
    pattern_summaries = [
        aggregate(f"{subset}::{pattern}", group)
        for (subset, pattern), group in sorted(grouped.items())
    ]

    GRADER_COPY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(args.predictions, GRADER_COPY)
    write_csv(SCORED, scored)
    write_csv(SUMMARY, summaries)
    write_csv(BY_PATTERN, pattern_summaries)

    primary_by_pattern = [
        row
        for row in pattern_summaries
        if str(row["subset"]).startswith("primary_reference_consistent_80::")
    ]
    markdown = [
        "# Kết quả scoring blind của mô hình thứ hai trên benchmark có kiểm soát",
        "",
        "Kết quả hiện tại là **tạm thời** vì mới có 97/100 output API hợp lệ. ",
        "Trong đó, 78 case thuộc tập reference-consistent chính và 19 case thuộc ",
        "tập conflict dùng cho audit độ nhạy.",
        "",
        "## Tổng hợp",
        "",
        "| Tập đánh giá | n | Object | MR | PI | Object--role coverage | Full score |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        markdown.append(
            f"| {row['subset']} | {row['n']} | {row['mean_OBJECT']} | "
            f"{row['mean_MR']} | {row['mean_PI']} | "
            f"{row['mean_object_role_coverage']} | {row['full_score_count']} |"
        )
    markdown.extend(
        [
            "",
            "## Tập reference-consistent theo pattern",
            "",
            "| Pattern | n | Object | MR | PI | Object--role coverage |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in primary_by_pattern:
        pattern = str(row["subset"]).split("::", 1)[1]
        markdown.append(
            f"| {pattern} | {row['n']} | {row['mean_OBJECT']} | "
            f"{row['mean_MR']} | {row['mean_PI']} | "
            f"{row['mean_object_role_coverage']} |"
        )
    markdown.extend(
        [
            "",
            "## Policy",
            "",
            "Object đạt 1 khi tập affected object khớp đầy đủ, đạt 0.5 khi phục "
            "hồi ít nhất hai phần ba. MR áp cùng ngưỡng cho các cặp object--role. "
            "PI yêu cầu thêm pattern phù hợp và một đoạn trích liền mạch xuất hiện "
            "nguyên văn trong lời giải thích; luôn áp dụng `PI <= MR <= Object`.",
            "",
            "Ba lỗi HTTP 524 không được quy đổi thành điểm 0. Sau khi chạy bù và "
            "chấm blind ba case đó, cần chạy lại chính script này để khóa kết quả "
            "100 case.",
            "",
        ]
    )
    SUMMARY_MD.write_text("\n".join(markdown), encoding="utf-8")

    print(f"Validated and scored {len(scored)} predictions")
    print(f"Primary reference-consistent subset: {len(primary)}")
    print(f"Excluded conflict subset: {len(excluded)}")
    print(f"Scored rows: {SCORED}")
    print(f"Summary: {SUMMARY}")
    print(f"Markdown summary: {SUMMARY_MD}")
    for row in summaries:
        print(
            f"{row['subset']}: n={row['n']}, O={row['mean_OBJECT']}, "
            f"MR={row['mean_MR']}, PI={row['mean_PI']}, "
            f"coverage={row['mean_object_role_coverage']}"
        )


if __name__ == "__main__":
    main()
