#!/usr/bin/env python3
"""Score the 182 blind localization-baseline predictions (policy v3).

The semantic predictions are joined to the private key only after grading.
MR/PI follows the frozen compatibility policy used by
``github-ostovar_object_aware_v1/scripts/score_predictions.py`` except that
partial object credit now requires both object precision and object recall to
reach two thirds.  This prevents a prediction containing the reference set
plus many additional central objects from receiving partial credit.  Region
precision/recall/F1 is computed independently against the manually mapped
affected-object ground truth, not against the algorithmic A* used to size the
random regions.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import statistics
from collections import defaultdict
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
PREDICTIONS = PACKAGE / "grader_outputs/blind_all_batches_graded_baseline.csv"
PRIVATE_KEY = PACKAGE / "internal_after_grading/private_localization_blind_key_182.csv"
SELECTION_AUDIT = PACKAGE / "provenance/selection_audit.csv"
RUN_AUDIT = PACKAGE / "provenance/run_audit_182.csv"
OFFICIAL = WORKSPACE / "Experiments/IEEE_ACCESS/artifacts/official/ostovar_localization_ablation_v1"
OUTPUT_DIR = PACKAGE / "results"

CONDITION_DIRS = {
    "NO_LOCALIZATION": "all",
    "OUTSIDE_A_STAR": "outside",
    **{f"RANDOM_REGION_R{i}": f"random_matched_r{i}" for i in range(1, 6)},
}
CONDITION_ORDER = [
    "NO_LOCALIZATION",
    "OUTSIDE_A_STAR",
    *[f"RANDOM_REGION_R{i}" for i in range(1, 6)],
]

PATTERN_FAMILIES = {
    "SerialRemoval": "fragment_removal",
    "ParallelRemoval": "fragment_removal",
    "ConditionalRemoval": "fragment_removal",
    "SerialMove": "fragment_move",
    "ConditionalMove": "fragment_move",
    "ParallelMove": "fragment_move",
    "ConditionalToSequence": "relation_to_sequence",
    "ParallelToSequence": "relation_to_sequence",
    "Substitute": "substitute",
    # Swap and move share the broad relative-order/relocation mechanism.
    "Swap": "fragment_move",
    "Loop": "loop",
    "Skip": "skip",
    "Frequency": "frequency",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def f1(precision: float, recall: float) -> float:
    return 2 * precision * recall / (precision + recall) if precision + recall else 0.0


def normalized_pattern(value: str) -> str:
    return re.sub(r"\s*\(.*", "", value).strip()


def central_objects(value: str) -> set[str]:
    return set(re.findall(r"A\d{2}", value.split(";", 1)[0]))


def partial_object_threshold(reference_size: int) -> int:
    return (2 * reference_size + 2) // 3


def explicit_direction_conflict(predicted: str, key: dict[str, str]) -> bool:
    added = set(json.loads(key["activities_added_anon"]))
    deleted = set(json.loads(key["activities_deleted_anon"]))
    lowered = predicted.lower()
    return bool((added and "chiều xóa" in lowered) or (deleted and "chiều thêm" in lowered))


def mean(rows: list[dict[str, object]], field: str) -> float:
    return sum(float(row[field]) for row in rows) / len(rows)


def score_rows() -> list[dict[str, object]]:
    predictions = {row["grading_id"]: row for row in read_rows(PREDICTIONS)}
    keys = read_rows(PRIVATE_KEY)
    selection = {
        (row["case_id"], row["condition"]): row for row in read_rows(SELECTION_AUDIT)
    }
    runs = {(row["case_id"], row["condition"]): row for row in read_rows(RUN_AUDIT)}
    key_ids = {row["grading_id"] for row in keys}
    if set(predictions) != key_ids:
        raise SystemExit("Blind-ID mismatch between predictions and private key")
    if len(keys) != 182:
        raise SystemExit(f"Expected 182 key rows, found {len(keys)}")

    output: list[dict[str, object]] = []
    for key in keys:
        grading_id = key["grading_id"]
        case_id = key["case_id"]
        condition = key["condition"]
        prediction = predictions[grading_id]
        if sha256_text(prediction["llm_explanation_full"]) != key["explanation_sha256"]:
            raise SystemExit(f"Explanation hash mismatch for {grading_id}")

        affected = set(json.loads(key["affected_activities_anon"]))
        evidence_path = (
            OFFICIAL / CONDITION_DIRS[condition] / "evidence/tau_mixed" / f"{case_id}.json"
        )
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        selected = set(evidence["activity_region"]["selected_activities"])
        tp, fp, fn = selected & affected, selected - affected, affected - selected
        region_precision = len(tp) / len(selected) if selected else 0.0
        region_recall = len(tp) / len(affected) if affected else 0.0
        region_f1 = f1(region_precision, region_recall)

        predicted_pattern = normalized_pattern(prediction["predicted_pattern"])
        pattern_exact = predicted_pattern == key["change_pattern"]

        central = central_objects(prediction["predicted_objects"])
        correct = affected & central
        missing = affected - central
        incorrect = central - affected
        threshold = partial_object_threshold(len(affected))
        object_precision = len(correct) / len(central) if central else 0.0
        object_recall = len(correct) / len(affected) if affected else 0.0
        if central == affected:
            object_score = 1.0
            object_note = "Khớp chính xác affected-object set."
        elif object_precision >= 2 / 3 and object_recall >= 2 / 3:
            object_score = 0.5
            object_note = (
                f"Object precision={object_precision:.3f} và recall={object_recall:.3f}, "
                "đều đạt ngưỡng hai phần ba; còn thiếu/thừa object trung tâm."
            )
        else:
            object_score = 0.0
            object_note = (
                f"Object precision={object_precision:.3f}, recall={object_recall:.3f}; "
                "ít nhất một đại lượng dưới ngưỡng hai phần ba."
            )

        direction_conflict = explicit_direction_conflict(prediction["predicted_pattern"], key)
        same_family = (
            predicted_pattern in PATTERN_FAMILIES
            and key["change_pattern"] in PATTERN_FAMILIES
            and PATTERN_FAMILIES[predicted_pattern] == PATTERN_FAMILIES[key["change_pattern"]]
        )
        if direction_conflict:
            raw_mr = raw_pi = 0.0
            mechanism_note = "Chiều dự đoán trái với vai trò object trong ground truth."
        elif pattern_exact:
            raw_mr = raw_pi = 1.0
            mechanism_note = "Đúng cơ chế và pattern."
        elif same_family:
            raw_mr, raw_pi = 1.0, 0.5
            mechanism_note = "Đúng họ cơ chế nhưng nhầm biến thể cấu trúc."
        else:
            raw_mr = raw_pi = 0.0
            mechanism_note = "Pattern dự đoán thuộc cơ chế khác."

        mr = min(object_score, raw_mr)
        pi = min(object_score, mr, raw_pi)
        mr_note = f"{object_note} {mechanism_note}"
        pi_note = (
            f"Object-gated: O={object_score:g}, MR_raw={raw_mr:g}, PI_raw={raw_pi:g}."
        )

        run = runs[(case_id, condition)]
        sel = selection[(case_id, condition)]
        output.append({
            "grading_id": grading_id,
            "case_id": case_id,
            "condition": condition,
            "reference_pattern": key["change_pattern"],
            "predicted_pattern": prediction["predicted_pattern"],
            "pattern_exact": str(pattern_exact).lower(),
            "affected_activities_anon": json.dumps(sorted(affected), ensure_ascii=False),
            "selected_region_anon": json.dumps(sorted(selected), ensure_ascii=False),
            "region_tp": json.dumps(sorted(tp), ensure_ascii=False),
            "region_fp": json.dumps(sorted(fp), ensure_ascii=False),
            "region_fn": json.dumps(sorted(fn), ensure_ascii=False),
            "region_precision": f"{region_precision:.6f}",
            "region_recall": f"{region_recall:.6f}",
            "region_f1": f"{region_f1:.6f}",
            "predicted_objects": prediction["predicted_objects"],
            "predicted_central_objects_anon": json.dumps(sorted(central), ensure_ascii=False),
            "correct_objects": json.dumps(sorted(correct), ensure_ascii=False),
            "missing_objects": json.dumps(sorted(missing), ensure_ascii=False),
            "incorrect_central_objects": json.dumps(sorted(incorrect), ensure_ascii=False),
            "partial_object_threshold": threshold,
            "object_precision": f"{object_precision:.6f}",
            "object_recall": f"{object_recall:.6f}",
            "OBJECT": f"{object_score:g}",
            "OBJECT_note": object_note,
            "MR_raw": f"{raw_mr:g}",
            "MR": f"{mr:g}",
            "MR_note": mr_note,
            "PI_raw": f"{raw_pi:g}",
            "PI": f"{pi:g}",
            "PI_note": pi_note,
            "evidence_items": int(sel["evidence_items"]),
            "estimated_evidence_tokens": int(sel["estimated_evidence_tokens"]),
            "prompt_tokens": int(run["prompt_tokens"]),
            "completion_tokens": int(run["completion_tokens"]),
            "total_tokens": int(run["total_tokens"]),
            "prediction_note": prediction["prediction_note"],
        })
    return output


def summarize(condition: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tp = sum(len(json.loads(str(row["region_tp"]))) for row in rows)
    fp = sum(len(json.loads(str(row["region_fp"]))) for row in rows)
    fn = sum(len(json.loads(str(row["region_fn"]))) for row in rows)
    micro_precision = tp / (tp + fp) if tp + fp else 0.0
    micro_recall = tp / (tp + fn) if tp + fn else 0.0
    return {
        "condition": condition,
        "n": len(rows),
        "macro_region_precision": f"{mean(rows, 'region_precision'):.6f}",
        "macro_region_recall": f"{mean(rows, 'region_recall'):.6f}",
        "macro_region_f1": f"{mean(rows, 'region_f1'):.6f}",
        "micro_region_precision": f"{micro_precision:.6f}",
        "micro_region_recall": f"{micro_recall:.6f}",
        "micro_region_f1": f"{f1(micro_precision, micro_recall):.6f}",
        "mean_OBJECT": f"{mean(rows, 'OBJECT'):.6f}",
        "mean_MR": f"{mean(rows, 'MR'):.6f}",
        "mean_PI": f"{mean(rows, 'PI'):.6f}",
        "pattern_exact_rate": f"{sum(row['pattern_exact'] == 'true' for row in rows) / len(rows):.6f}",
        "MR_1_count": sum(float(row["MR"]) == 1 for row in rows),
        "PI_1_count": sum(float(row["PI"]) == 1 for row in rows),
        "mean_evidence_items": f"{mean(rows, 'evidence_items'):.3f}",
        "mean_estimated_evidence_tokens": f"{mean(rows, 'estimated_evidence_tokens'):.3f}",
        "mean_prompt_tokens": f"{mean(rows, 'prompt_tokens'):.3f}",
        "mean_completion_tokens": f"{mean(rows, 'completion_tokens'):.3f}",
        "mean_total_tokens": f"{mean(rows, 'total_tokens'):.3f}",
    }


def write_markdown(
    summary: list[dict[str, object]], by_pattern: list[dict[str, object]]
) -> None:
    lookup = {row["condition"]: row for row in summary}
    no_loc = lookup["NO_LOCALIZATION"]
    random_row = lookup["RANDOM_POOLED_5x26"]
    random_conditions = [lookup[f"RANDOM_REGION_R{i}"] for i in range(1, 6)]
    random_pi_sd = statistics.stdev(float(row["mean_PI"]) for row in random_conditions)
    random_exact_sd = statistics.stdev(
        float(row["pattern_exact_rate"]) for row in random_conditions
    )
    token_reduction = 1 - float(random_row["mean_total_tokens"]) / float(no_loc["mean_total_tokens"])
    lines = [
        "# Tổng hợp chấm mù 182 baseline Ostovar",
        "",
        f"- Nguồn dự đoán: `{PREDICTIONS.name}` (SHA-256: `{sha256_file(PREDICTIONS)}`).",
        "- Thiết kế: 26 case × 7 điều kiện = 182 lời giải thích.",
        "- Năm random region được báo riêng và gộp thành 130 lượt ở hàng `RANDOM_POOLED_5x26`.",
        "- MR/PI dùng object gate v3: cả object precision và object recall phải đạt tối thiểu hai phần ba mới được 0.5.",
        "",
        "## Kết quả theo điều kiện",
        "",
        "| Điều kiện | n | P vùng (macro) | R vùng (macro) | F1 vùng (macro) | Object | MR | PI | Pattern exact | Evidence items | Total tokens |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| {row['condition']} | {row['n']} | "
            f"{float(row['macro_region_precision']):.3f} | "
            f"{float(row['macro_region_recall']):.3f} | "
            f"{float(row['macro_region_f1']):.3f} | "
            f"{float(row['mean_OBJECT']):.3f} | {float(row['mean_MR']):.3f} | "
            f"{float(row['mean_PI']):.3f} | "
            f"{float(row['pattern_exact_rate']):.3f} | "
            f"{float(row['mean_evidence_items']):.1f} | "
            f"{float(row['mean_total_tokens']):.0f} |"
        )
    lines += [
        "",
        "## Kết quả gộp theo pattern",
        "",
        "| Pattern | n | Object | MR | PI | Pattern exact |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in by_pattern:
        lines.append(
            f"| {row['reference_pattern']} | {row['n']} | "
            f"{float(row['mean_OBJECT']):.3f} | {float(row['mean_MR']):.3f} | "
            f"{float(row['mean_PI']):.3f} | "
            f"{float(row['pattern_exact_rate']):.3f} |"
        )
    lines += [
        "",
        "## Diễn giải kiểm toán",
        "",
        f"Random region giảm trung bình {token_reduction:.1%} tổng token so với `NO_LOCALIZATION`, "
        f"trong khi PI thay đổi từ {float(no_loc['mean_PI']):.3f} xuống "
        f"{float(random_row['mean_PI']):.3f}. Trên năm seed, PI trung bình là "
        f"{float(random_row['mean_PI']):.3f} ± {random_pi_sd:.3f} và pattern-exact rate là "
        f"{float(random_row['pattern_exact_rate']):.3f} ± {random_exact_sd:.3f} (sample SD giữa các seed).",
        "",
        "Không được diễn giải các hàng random/outside như phép loại bỏ hoàn toàn evidence về affected activities. "
        "Trong implementation tạo 182 baseline này, activity region chỉ gate `CF_POS`, `CF_REL` và `CF_LAG`; "
        "`CF_OCC` và `CF_DIR` vẫn được tính trên toàn bộ activity universe. Vì vậy một region có overlap thấp với "
        "ground truth vẫn có thể cung cấp đủ occurrence/directly-follows evidence để LLM gọi đúng object hoặc pattern.",
        "",
        "Object gate chỉ đọc phần object trung tâm trước dấu `;`; activity ghi `context only` không được tính. "
        "Điểm 1 yêu cầu tập object trung tâm khớp chính xác. Điểm 0.5 yêu cầu cả object precision và "
        "object recall đạt tối thiểu hai phần ba; nếu một trong hai dưới ngưỡng thì MR=PI=0 dù tên pattern có đúng.",
        "",
    ]
    (OUTPUT_DIR / "SUMMARY_BASELINES_182_POLICY_V3.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def main() -> None:
    rows = score_rows()
    write_rows(OUTPUT_DIR / "blind_baselines_182_scored_policy_v3.csv", rows)
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["condition"])].append(row)
    summary = [summarize(condition, grouped[condition]) for condition in CONDITION_ORDER]
    random_rows = [row for row in rows if str(row["condition"]).startswith("RANDOM_REGION_")]
    summary.append(summarize("RANDOM_POOLED_5x26", random_rows))
    write_rows(OUTPUT_DIR / "blind_baselines_182_summary_by_condition_policy_v3.csv", summary)
    by_pattern: list[dict[str, object]] = []
    for pattern in sorted({str(row["reference_pattern"]) for row in rows}):
        pattern_rows = [row for row in rows if row["reference_pattern"] == pattern]
        by_pattern.append({
            "reference_pattern": pattern,
            "n": len(pattern_rows),
            "mean_OBJECT": f"{mean(pattern_rows, 'OBJECT'):.6f}",
            "mean_MR": f"{mean(pattern_rows, 'MR'):.6f}",
            "mean_PI": f"{mean(pattern_rows, 'PI'):.6f}",
            "pattern_exact_rate": f"{sum(row['pattern_exact'] == 'true' for row in pattern_rows) / len(pattern_rows):.6f}",
        })
    write_rows(OUTPUT_DIR / "blind_baselines_182_summary_by_pattern_policy_v3.csv", by_pattern)
    write_markdown(summary, by_pattern)
    print(f"Scored rows: {len(rows)}")
    print(f"Wrote: {OUTPUT_DIR / 'blind_baselines_182_scored_policy_v3.csv'}")
    print(f"Wrote: {OUTPUT_DIR / 'blind_baselines_182_summary_by_condition_policy_v3.csv'}")
    print(f"Wrote: {OUTPUT_DIR / 'blind_baselines_182_summary_by_pattern_policy_v3.csv'}")
    print(f"Wrote: {OUTPUT_DIR / 'SUMMARY_BASELINES_182_POLICY_V3.md'}")


if __name__ == "__main__":
    main()
