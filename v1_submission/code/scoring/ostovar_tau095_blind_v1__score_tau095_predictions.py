#!/usr/bin/env python3
"""Score the 26 uniform-evidence-tau=0.95 blind predictions.

Scoring policy v2 uses affected-object recovery as a hard gate.  A mechanism
or pattern receives no credit when it is attached to the wrong fragment.
Partial object credit requires at least two thirds of the reference affected
set (2/3 for ordinary three-activity fragments and 4/6 for a six-activity
reference).

The blind grader's ``predicted_objects`` field is explanatory text rather than
a machine-readable list.  It may name entry/exit anchors, the opposite branch,
or another relational counterpart after the affected fragment.  Such context
is not a false positive.  Only an out-of-reference activity that the grader
explicitly labels as an additional ``main/central object`` (or groups into the
main moved fragment) is treated as an incorrect central claim.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASTAR_PATH = ROOT / "localization/astar_regions_tau095_evidence_v1.csv"
JOBS = [
    (
        ROOT / "grader_outputs/ostovar_tau095_blind_26_predictions.csv",
        ROOT / "internal_after_grading/private_tau095_blind_key_26.csv",
        ROOT / "scored_results/tau095_scored_policy_v2.csv",
    ),
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
    # A swap and a move both recover the broad relative-order/relocation
    # mechanism.  Confusing the two earns MR=1 but only PI=0.5.
    "Swap": "fragment_move",
    "Loop": "loop",
    "Skip": "skip",
    "Frequency": "frequency",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def normalized_pattern(value: str) -> str:
    return re.sub(r"\s*\(.*", "", value).strip()


def object_mentions(value: str) -> set[str]:
    """Return every anonymized activity explicitly named by the blind judge."""
    return set(re.findall(r"A\d{2}", value))


def explicit_central_claims(value: str) -> set[str]:
    """Extract activities explicitly promoted to an additional central object.

    The proposed-method grading files distinguish ordinary relational context
    (``mốc``, ``điểm vào/ra``, ``phần còn lại``) from genuine competing
    hypotheses with phrases such as ``A06 ... đối tượng trung tâm``.  The
    latter must count as a central false positive; the former must not.
    """
    claims: set[str] = set()
    lowered = value.lower()

    # Current blind outputs phrase the extra hypothesis as
    # ``Axx được LLM nêu/đặt/gộp ...``.  Inspect the containing clause so
    # that an ordinary ``thay đổi kèm theo`` is not promoted to a main object.
    for match in re.finditer(r"\b(A\d{2})\s+được\s+LLM\s+(?:nêu|đặt|gộp)", value, re.I):
        clause_end = value.find(";", match.start())
        if clause_end < 0:
            clause_end = len(value)
        clause = lowered[match.start():clause_end]
        if any(marker in clause for marker in (
            "đối tượng chính",
            "đối tượng trung tâm",
            "gộp vào nhóm",
        )):
            claims.add(match.group(1).upper())

    # Also support the rubric's direct form: ``Đối tượng trung tâm là ...``.
    for match in re.finditer(
        r"(?:đối tượng (?:chính|trung tâm)(?: thứ \w+)?\s+(?:là|:))"
        r"([^.;]+)",
        value,
        re.I,
    ):
        claims.update(re.findall(r"A\d{2}", match.group(1), re.I))
    return {code.upper() for code in claims}


def partial_object_threshold(reference_size: int) -> int:
    """Smallest integer covering at least two thirds of the reference set."""
    return (2 * reference_size + 2) // 3


def explicit_direction_conflict(predicted: str, key: dict[str, str]) -> bool:
    """Detect only directions explicitly encoded in the blind prediction."""
    added = set(json.loads(key["activities_added_anon"]))
    deleted = set(json.loads(key["activities_deleted_anon"]))
    lowered = predicted.lower()
    return bool((added and "chiều xóa" in lowered) or (deleted and "chiều thêm" in lowered))


def score(prediction_path: Path, key_path: Path) -> list[dict[str, str]]:
    predictions = {row["grading_id"]: row for row in read_rows(prediction_path)}
    keys = read_rows(key_path)
    regions = {
        row["grading_id"]: set(json.loads(row["localized_a_star_anon"]))
        for row in read_rows(ASTAR_PATH)
    }
    if set(predictions) != {row["grading_id"] for row in keys}:
        raise SystemExit(f"Blind-ID mismatch between {prediction_path} and {key_path}")

    output: list[dict[str, str]] = []
    for key in keys:
        grading_id = key["grading_id"]
        prediction = predictions[grading_id]
        affected = set(json.loads(key["affected_activities_anon"]))
        localized = regions[grading_id]
        tp, fp, fn = localized & affected, localized - affected, affected - localized
        precision = len(tp) / len(localized) if localized else 0.0
        recall = len(tp) / len(affected) if affected else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

        predicted_pattern = normalized_pattern(prediction["predicted_pattern"])
        pattern_exact = predicted_pattern == key["change_pattern"]
        mentions = object_mentions(prediction["predicted_objects"])
        explicit_central = explicit_central_claims(prediction["predicted_objects"])
        correct = affected & mentions
        missing = affected - mentions
        incorrect = explicit_central - affected
        # This is the scored central set: recovered reference objects plus only
        # those non-reference objects explicitly asserted as central.  Anchors
        # and relational counterparts remain visible in all_object_mentions.
        predicted_central = correct | incorrect
        threshold = partial_object_threshold(len(affected))

        if correct == affected and not incorrect:
            object_score = 1.0
            object_note = "Nhận diện đủ affected-object set, không có object trung tâm sai."
        elif len(correct) >= threshold:
            object_score = 0.5
            object_note = (
                f"Đúng {len(correct)}/{len(affected)} affected object, đạt ngưỡng "
                f"hai phần ba; còn thiếu/thừa object trung tâm."
            )
        else:
            object_score = 0.0
            object_note = (
                f"Chỉ đúng {len(correct)}/{len(affected)} affected object, dưới ngưỡng "
                f"{threshold}/{len(affected)}."
            )

        direction_conflict = explicit_direction_conflict(prediction["predicted_pattern"], key)
        same_family = (
            predicted_pattern in PATTERN_FAMILIES
            and key["change_pattern"] in PATTERN_FAMILIES
            and PATTERN_FAMILIES[predicted_pattern] == PATTERN_FAMILIES[key["change_pattern"]]
        )
        if direction_conflict:
            raw_mr = raw_pi = 0.0
            mechanism_note = "Pattern ghi chiều thay đổi trái với vai trò object trong ground truth."
        elif pattern_exact:
            raw_mr = raw_pi = 1.0
            mechanism_note = "Đúng cơ chế và đúng pattern chuẩn."
        elif same_family:
            raw_mr, raw_pi = 1.0, 0.5
            mechanism_note = "Đúng họ cơ chế nhưng nhầm biến thể cấu trúc trong cùng họ pattern."
        else:
            raw_mr = raw_pi = 0.0
            mechanism_note = "Pattern dự đoán thuộc cơ chế khác với ground truth."

        mr = min(object_score, raw_mr)
        pi = min(object_score, mr, raw_pi)
        mr_note = f"{object_note} {mechanism_note}"
        pi_note = (
            "PI bị chặn bởi object gate và MR; "
            f"O={object_score:g}, MR_raw={raw_mr:g}, PI_raw={raw_pi:g}."
        )

        output.append({
            "grading_id": grading_id,
            "case_id": key["case_id"],
            "native_noise_percent": key["native_noise_percent"],
            "reference_pattern": key["change_pattern"],
            "predicted_pattern": prediction["predicted_pattern"],
            "affected_activities_anon": json.dumps(sorted(affected), ensure_ascii=False),
            "localized_a_star_anon": json.dumps(sorted(localized), ensure_ascii=False),
            "localization_tp": json.dumps(sorted(tp), ensure_ascii=False),
            "localization_fp": json.dumps(sorted(fp), ensure_ascii=False),
            "localization_fn": json.dumps(sorted(fn), ensure_ascii=False),
            "localization_precision": f"{precision:.6f}",
            "localization_recall": f"{recall:.6f}",
            "localization_f1": f"{f1:.6f}",
            "predicted_objects": prediction["predicted_objects"],
            "all_object_mentions_anon": json.dumps(sorted(mentions), ensure_ascii=False),
            "predicted_central_objects_anon": json.dumps(sorted(predicted_central), ensure_ascii=False),
            "correct_objects": json.dumps(sorted(correct), ensure_ascii=False),
            "missing_objects": json.dumps(sorted(missing), ensure_ascii=False),
            "incorrect_central_objects": json.dumps(sorted(incorrect), ensure_ascii=False),
            "partial_object_threshold": str(threshold),
            "OBJECT": f"{object_score:g}",
            "OBJECT_note": object_note,
            "MR_raw": f"{raw_mr:g}",
            "MR": f"{mr:g}",
            "MR_note": mr_note,
            "PI_raw": f"{raw_pi:g}",
            "PI": f"{pi:g}",
            "PI_note": pi_note,
            "pattern_exact": str(pattern_exact).lower(),
            "prediction_note": prediction["prediction_note"],
        })
    return output


def aggregate(label: str, rows: list[dict[str, str]]) -> dict[str, str]:
    tp = sum(len(json.loads(row["localization_tp"])) for row in rows)
    fp = sum(len(json.loads(row["localization_fp"])) for row in rows)
    fn = sum(len(json.loads(row["localization_fn"])) for row in rows)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    loc_f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    mean = lambda field: sum(float(row[field]) for row in rows) / len(rows)
    return {
        "noise_percent": label,
        "n": str(len(rows)),
        "micro_localization_precision": f"{precision:.6f}",
        "micro_localization_recall": f"{recall:.6f}",
        "micro_localization_f1": f"{loc_f1:.6f}",
        "macro_localization_precision": f"{mean('localization_precision'):.6f}",
        "macro_localization_recall": f"{mean('localization_recall'):.6f}",
        "macro_localization_f1": f"{mean('localization_f1'):.6f}",
        "mean_OBJECT": f"{mean('OBJECT'):.6f}",
        "mean_MR": f"{mean('MR'):.6f}",
        "mean_PI": f"{mean('PI'):.6f}",
        "pattern_exact_count": str(sum(row["pattern_exact"] == "true" for row in rows)),
    }


def main() -> None:
    all_rows: list[dict[str, str]] = []
    for prediction_path, key_path, output_path in JOBS:
        rows = score(prediction_path, key_path)
        write_rows(output_path, rows)
        all_rows.extend(rows)
        print(f"Wrote {len(rows)} rows to {output_path.relative_to(ROOT)}")
    summary = [aggregate("0.0", all_rows)]
    summary_path = ROOT / "scored_results/summary_policy_v2.csv"
    write_rows(summary_path, summary)
    print(f"Wrote {len(summary)} rows to {summary_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
