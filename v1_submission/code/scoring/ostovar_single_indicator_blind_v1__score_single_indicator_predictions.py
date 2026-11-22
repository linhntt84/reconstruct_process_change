#!/usr/bin/env python3
"""Score the 130 answer-blind single-indicator predictions (policy v3).

Each of the 26 Ostovar cases appears once under OCC, DIR, POS, REL, and LAG.
The Claude extraction is joined to the private key only after grading.  Object
credit is symmetric: a partial score requires both object precision and object
recall to reach two thirds.  MR and PI are capped by that object score.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
PREDICTIONS = PACKAGE / "grader_outputs/blind_all_batches_single_predictions.csv"
PRIVATE_KEY = PACKAGE / "internal_after_grading/private_blind_key.csv"
RUN_AUDIT = PACKAGE / "provenance/run_audit.csv"
EVIDENCE_ROOT = (
    WORKSPACE
    / "Experiments/IEEE_ACCESS/artifacts/api/"
    "ostovar_atomic_b200_algorithm_1_2_per_indicator_v1/evidence"
)
OUTPUT_DIR = PACKAGE / "scored_results"

CONDITION_ORDER = ["OCC_ONLY", "DIR_ONLY", "POS_ONLY", "REL_ONLY", "LAG_ONLY"]
EVIDENCE_DIR = {
    "OCC_ONLY": "OCC",
    "DIR_ONLY": "DIR",
    "POS_ONLY": "POS",
    "REL_ONLY": "REL",
    "LAG_ONLY": "LAG",
}

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


def normalized_pattern(value: str) -> str:
    return re.sub(r"\s*\(.*", "", value).strip()


def central_objects(value: str) -> set[str]:
    """Read central activities while excluding the rubric's context-only tail."""
    central_text = re.split(
        r";\s*context\s+only\s*:", value, maxsplit=1, flags=re.I
    )[0]
    return {code.upper() for code in re.findall(r"A\d{2}", central_text, re.I)}


def explicit_direction_conflict(predicted: str, key: dict[str, str]) -> bool:
    added = set(json.loads(key["activities_added_anon"]))
    deleted = set(json.loads(key["activities_deleted_anon"]))
    lowered = predicted.lower()
    return bool(
        (added and re.search(r"chiều\s*:\s*xóa|chiều xóa", lowered))
        or (deleted and re.search(r"chiều\s*:\s*thêm|chiều thêm", lowered))
    )


def mean(rows: list[dict[str, object]], field: str) -> float:
    return sum(float(row[field]) for row in rows) / len(rows)


def score_rows() -> list[dict[str, object]]:
    prediction_rows = read_rows(PREDICTIONS)
    key_rows = read_rows(PRIVATE_KEY)
    predictions = {row["grading_id"]: row for row in prediction_rows}
    keys = {row["grading_id"]: row for row in key_rows}
    if len(predictions) != 130 or len(keys) != 130:
        raise SystemExit(
            f"Expected 130 unique predictions and keys; found {len(predictions)} and {len(keys)}"
        )
    if set(predictions) != set(keys):
        raise SystemExit("Blind-ID mismatch between predictions and private key")

    runs = {
        (row["case_id"], row["condition"]): row for row in read_rows(RUN_AUDIT)
    }
    output: list[dict[str, object]] = []
    for grading_id, key in keys.items():
        prediction = predictions[grading_id]
        if sha256_text(prediction["llm_explanation_full"]) != key["explanation_sha256"]:
            raise SystemExit(f"Explanation hash mismatch for {grading_id}")

        case_id = key["case_id"]
        condition = key["condition"]
        affected = set(json.loads(key["affected_activities_anon"]))
        central = central_objects(prediction["predicted_objects"])
        correct = affected & central
        missing = affected - central
        incorrect = central - affected
        object_precision = len(correct) / len(central) if central else 0.0
        object_recall = len(correct) / len(affected) if affected else 0.0

        if central == affected:
            object_score = 1.0
            object_note = "Khớp chính xác affected-object set."
        elif object_precision >= 2 / 3 and object_recall >= 2 / 3:
            object_score = 0.5
            object_note = (
                f"Object precision={object_precision:.3f} và recall={object_recall:.3f}, "
                "đều đạt ngưỡng hai phần ba."
            )
        else:
            object_score = 0.0
            object_note = (
                f"Object precision={object_precision:.3f}, recall={object_recall:.3f}; "
                "ít nhất một đại lượng dưới ngưỡng hai phần ba."
            )

        predicted_pattern = normalized_pattern(prediction["predicted_pattern"])
        reference_pattern = key["change_pattern"]
        pattern_exact = predicted_pattern == reference_pattern
        same_family = (
            predicted_pattern in PATTERN_FAMILIES
            and reference_pattern in PATTERN_FAMILIES
            and PATTERN_FAMILIES[predicted_pattern] == PATTERN_FAMILIES[reference_pattern]
        )
        direction_conflict = explicit_direction_conflict(
            prediction["predicted_pattern"], key
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
        run = runs[(case_id, condition)]
        evidence_path = EVIDENCE_ROOT / EVIDENCE_DIR[condition] / f"{case_id}.json"
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        evidence_items = int(evidence["condition"]["evidence_count"])

        output.append(
            {
                "grading_id": grading_id,
                "case_id": case_id,
                "condition": condition,
                "reference_pattern": reference_pattern,
                "predicted_pattern": prediction["predicted_pattern"],
                "pattern_exact": str(pattern_exact).lower(),
                "affected_activities_anon": json.dumps(
                    sorted(affected), ensure_ascii=False
                ),
                "predicted_objects": prediction["predicted_objects"],
                "predicted_central_objects_anon": json.dumps(
                    sorted(central), ensure_ascii=False
                ),
                "correct_objects": json.dumps(sorted(correct), ensure_ascii=False),
                "missing_objects": json.dumps(sorted(missing), ensure_ascii=False),
                "incorrect_central_objects": json.dumps(
                    sorted(incorrect), ensure_ascii=False
                ),
                "object_precision": f"{object_precision:.6f}",
                "object_recall": f"{object_recall:.6f}",
                "OBJECT": f"{object_score:g}",
                "OBJECT_note": object_note,
                "MR_raw": f"{raw_mr:g}",
                "MR": f"{mr:g}",
                "MR_note": f"{object_note} {mechanism_note}",
                "PI_raw": f"{raw_pi:g}",
                "PI": f"{pi:g}",
                "PI_note": (
                    f"Object-gated: O={object_score:g}, MR_raw={raw_mr:g}, "
                    f"PI_raw={raw_pi:g}."
                ),
                "evidence_items": evidence_items,
                "prompt_tokens": int(run["prompt_tokens"]),
                "completion_tokens": int(run["completion_tokens"]),
                "total_tokens": int(run["total_tokens"]),
                "prediction_note": prediction["prediction_note"],
            }
        )
    return output


def summarize(condition: str, rows: list[dict[str, object]]) -> dict[str, object]:
    exact_count = sum(str(row["pattern_exact"]).lower() == "true" for row in rows)
    return {
        "condition": condition,
        "n": len(rows),
        "mean_evidence_items": f"{mean(rows, 'evidence_items'):.6f}",
        "mean_prompt_tokens": f"{mean(rows, 'prompt_tokens'):.6f}",
        "mean_completion_tokens": f"{mean(rows, 'completion_tokens'):.6f}",
        "mean_total_tokens": f"{mean(rows, 'total_tokens'):.6f}",
        "mean_OBJECT": f"{mean(rows, 'OBJECT'):.6f}",
        "mean_MR": f"{mean(rows, 'MR'):.6f}",
        "mean_PI": f"{mean(rows, 'PI'):.6f}",
        "pattern_exact_count": exact_count,
        "pattern_exact_rate": f"{exact_count / len(rows):.6f}",
    }


def main() -> None:
    rows = score_rows()
    output = OUTPUT_DIR / "single_indicator_scored_policy_v3.csv"
    write_rows(output, rows)

    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_pattern: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["condition"])].append(row)
        by_pattern[(str(row["condition"]), str(row["reference_pattern"]))].append(row)
    summary = [summarize(condition, grouped[condition]) for condition in CONDITION_ORDER]
    summary.append(summarize("ALL_SINGLE_INDICATORS", rows))
    write_rows(OUTPUT_DIR / "single_indicator_summary_policy_v3.csv", summary)

    pattern_summary = [
        {
            "condition": condition,
            "reference_pattern": pattern,
            **{
                key: value
                for key, value in summarize(condition, by_pattern[(condition, pattern)]).items()
                if key != "condition"
            },
        }
        for condition in CONDITION_ORDER
        for pattern in sorted({str(row["reference_pattern"]) for row in rows})
    ]
    write_rows(
        OUTPUT_DIR / "single_indicator_by_pattern_policy_v3.csv", pattern_summary
    )
    print(f"Wrote {len(rows)} scored rows and {len(summary)} summary rows.")


if __name__ == "__main__":
    main()
