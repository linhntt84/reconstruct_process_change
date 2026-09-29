#!/usr/bin/env python3
"""Summarize Attempt 2 scores without manually inspecting grader predictions."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
SCORED = PACKAGE / "scored_results/deepseek_noise2p5_attempt2_scored_policy_v2.csv"
BASE_SUMMARY = PACKAGE / "scored_results/deepseek_noise2p5_attempt2_summary_policy_v2.csv"
SUMMARY_RTU = PACKAGE / "scored_results/deepseek_noise2p5_attempt2_summary_with_rtu_policy_v2.csv"
BY_PATTERN = PACKAGE / "scored_results/deepseek_noise2p5_attempt2_by_pattern_policy_v2.csv"
REPORT = PACKAGE / "RESULT_SUMMARY.md"
RUN_SUMMARY = PACKAGE / "provenance/run_summary.json"
COMPARISON = PACKAGE / "scored_results/attempt1_attempt2_comparison.csv"
ATTEMPT1 = PACKAGE.parent / "model2_deepseek_ostovar_noise_2p5_blind_v1"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def mean(rows, field):
    return sum(float(row[field]) for row in rows) / len(rows)


def rtu(rows):
    return sum(float(row["PI"]) == 1.0 for row in rows) / len(rows)


def main() -> None:
    rows = read_csv(SCORED)
    summary = read_csv(BASE_SUMMARY)[0]
    summary["RTU"] = f"{rtu(rows):.6f}"
    summary["RTU_count"] = str(sum(float(row["PI"]) == 1.0 for row in rows))
    write_csv(SUMMARY_RTU, [summary])

    pattern_rows = []
    for pattern in sorted({row["reference_pattern"] for row in rows}):
        group = [row for row in rows if row["reference_pattern"] == pattern]
        pattern_rows.append({
            "change_pattern": pattern,
            "n": len(group),
            "mean_OBJECT": f"{mean(group, 'OBJECT'):.6f}",
            "mean_MR": f"{mean(group, 'MR'):.6f}",
            "mean_PI": f"{mean(group, 'PI'):.6f}",
            "RTU": f"{rtu(group):.6f}",
            "RTU_count": sum(float(row["PI"]) == 1.0 for row in group),
        })
    write_csv(BY_PATTERN, pattern_rows)

    distribution = {
        field: Counter(row[field] for row in rows) for field in ("OBJECT", "MR", "PI")
    }
    usage = json.loads(RUN_SUMMARY.read_text(encoding="utf-8"))
    attempt1_auto = read_csv(
        ATTEMPT1 / "scored_results/deepseek_noise2p5_scored_policy_v2.csv"
    )
    attempt1_adj = read_csv(
        ATTEMPT1 / "scored_results/deepseek_noise2p5_scored_adjudicated_v1.csv"
    )
    attempt1_usage = json.loads(
        (ATTEMPT1 / "provenance/run_summary.json").read_text(encoding="utf-8")
    )
    comparison = []
    for label, source_rows, token_usage, selected in (
        ("attempt1_automated_policy_v2", attempt1_auto, attempt1_usage, "no"),
        ("attempt1_manual_adjudication_v1", attempt1_adj, attempt1_usage, "no"),
        ("attempt2_automated_policy_v2", rows, usage, "yes"),
    ):
        comparison.append({
            "result": label,
            "selected_for_current_paper": selected,
            "n": len(source_rows),
            "mean_OBJECT": f"{mean(source_rows, 'OBJECT'):.6f}",
            "mean_MR": f"{mean(source_rows, 'MR'):.6f}",
            "mean_PI": f"{mean(source_rows, 'PI'):.6f}",
            "RTU": f"{rtu(source_rows):.6f}",
            "RTU_count": sum(float(row["PI"]) == 1.0 for row in source_rows),
            "prompt_tokens": token_usage["prompt_tokens"],
            "completion_tokens": token_usage["completion_tokens"],
            "reasoning_tokens": token_usage["reasoning_tokens"],
            "total_tokens": token_usage["total_tokens"],
            "mean_total_tokens": f"{token_usage['total_tokens'] / len(source_rows):.6f}",
        })
    write_csv(COMPARISON, comparison)
    lines = [
        "# Tổng hợp chấm mù: DeepSeek-V4, Ostovar 2.5%, Attempt 2",
        "",
        "## Kết quả",
        "",
        "| n | Micro P(A*) | Micro R(A*) | Micro F1(A*) | O | MR | PI | RTU |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
        (
            f"| {summary['n']} | {float(summary['micro_localization_precision']):.3f} | "
            f"{float(summary['micro_localization_recall']):.3f} | "
            f"{float(summary['micro_localization_f1']):.3f} | "
            f"{float(summary['mean_OBJECT']):.3f} | {float(summary['mean_MR']):.3f} | "
            f"{float(summary['mean_PI']):.3f} | {float(summary['RTU']):.3f} |"
        ),
        "",
        "Phân bố điểm:",
        "",
        f"- O: 1 = {distribution['OBJECT'].get('1', 0)}; 0.5 = {distribution['OBJECT'].get('0.5', 0)}; 0 = {distribution['OBJECT'].get('0', 0)}.",
        f"- MR: 1 = {distribution['MR'].get('1', 0)}; 0.5 = {distribution['MR'].get('0.5', 0)}; 0 = {distribution['MR'].get('0', 0)}.",
        f"- PI: 1 = {distribution['PI'].get('1', 0)}; 0.5 = {distribution['PI'].get('0.5', 0)}; 0 = {distribution['PI'].get('0', 0)}.",
        f"- RTU: {summary['RTU_count']}/{summary['n']} ca.",
        "",
        "## Token usage",
        "",
        f"- Prompt: {usage['prompt_tokens']:,}.",
        f"- Completion (đã gồm reasoning): {usage['completion_tokens']:,}.",
        f"- Reasoning subset: {usage['reasoning_tokens']:,}.",
        f"- Total: {usage['total_tokens']:,}.",
        f"- Mean total/case: {usage['total_tokens'] / len(rows):,.2f}.",
        "",
        "## So sánh hai attempt",
        "",
        "| Result | O | MR | PI | RTU | Mean total tokens/case | Selected |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in comparison:
        lines.append(
            f"| {row['result']} | {float(row['mean_OBJECT']):.3f} | "
            f"{float(row['mean_MR']):.3f} | {float(row['mean_PI']):.3f} | "
            f"{float(row['RTU']):.3f} | {float(row['mean_total_tokens']):,.2f} | "
            f"{row['selected_for_current_paper']} |"
        )
    lines.extend([
        "",
        "## Theo pattern",
        "",
        "| Pattern | n | O | MR | PI | RTU |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    for row in pattern_rows:
        lines.append(
            f"| {row['change_pattern']} | {row['n']} | {float(row['mean_OBJECT']):.3f} | "
            f"{float(row['mean_MR']):.3f} | {float(row['mean_PI']):.3f} | "
            f"{float(row['RTU']):.3f} |"
        )
    lines.extend([
        "", "## Provenance", "",
        "- Điểm được tạo hoàn toàn bằng `score_predictions.py` theo policy v2.",
        "- Không có hiệu chỉnh thủ công trong bảng này.",
        "- `RTU` là tỷ lệ ca có `PI = 1`.",
    ])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {SUMMARY_RTU}")
    print(f"Wrote {BY_PATTERN}")
    print(f"Wrote {COMPARISON}")
    print(f"Wrote {REPORT}")


if __name__ == "__main__":
    main()
