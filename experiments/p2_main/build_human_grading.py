#!/usr/bin/env python3
"""P2: workbooks for human grading of LLM explanations (check of the blind Claude extractor).

SUPERSEDED (2026-11-14) by experiments/p4_grading/build_e11b_package.py, which imports the helpers of this
module (MECHANISMS, PATTERNS, build_references). main() is kept for the record and now writes to
results/_superseded/p2_human_grading_v1/ (git-ignored).

Two files, so that graders stay blind to the references and to the automatic extraction:
  results/p2_main/human_grading/<model>_run<k>_GRADING.xlsx  sheets: Huong_dan (instructions), Rubric_r5
      (the extractor rubric, verbatim), Cham (one row per case: explanation text + empty columns with the
      rubric-r5 fields, in random order with a seeded shuffle; grader ids G001...).
  results/p2_main/human_grading/<model>_run<k>_KEY.xlsx      sheet Key: grader id -> case, set, type,
      reference (anonymous codes, as in the explanation), Claude r5 extraction, automatic scores.
Requires openpyxl (Python >= 3.9).
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
OUT = ROOT / "results" / "p2_main"
RUBRIC = ROOT / "e4_multiperspective" / "code" / "EXTRACTION_RUBRIC_E4_R5_EN.md"
SEED = 20261114
PATTERNS = ["SerialRemoval", "ParallelRemoval", "ConditionalRemoval", "SerialMove", "ConditionalMove",
            "ParallelMove", "Swap", "ConditionalToSequence", "ParallelToSequence", "Substitute", "Loop", "Skip",
            "Frequency", "other", "none"]
MECHANISMS = ["fragment_added", "fragment_removed", "fragment_moved", "fragments_swapped", "fragment_substituted",
              "choice_to_sequence", "sequence_to_choice", "parallel_to_sequence", "sequence_to_parallel",
              "became_repeated", "stopped_repeating", "became_optional", "became_mandatory",
              "branch_frequency_changed", "timing_changed", "resource_allocation_changed", "handover_changed",
              "other", "none"]
GRADER_FIELDS = [
    ("support_level", "insufficient / weak / supported / unparsed"),
    ("central_activities", "mã activity của giả thuyết chính, cách nhau dấu phẩy (vd: A03, A07)"),
    ("secondary_activities", "mã activity của thay đổi phụ, riêng biệt"),
    ("mechanism", "một giá trị trong danh sách"),
    ("pattern", "một trong 13 pattern Ostovar, hoặc other/none"),
    ("time_activities", "activity có thời gian thay đổi"),
    ("time_direction", "increase / decrease / mixed / none"),
    ("resource_activities", "activity có phân công tài nguyên thay đổi"),
    ("ghi_chu", "nhận xét tự do (không bắt buộc)"),
]
INSTRUCTIONS = [
    "Mục đích: kiểm tra bộ trích xuất tự động (Claude, rubric r5). Người chấm đọc lời giải thích do LLM viết",
    "và ghi lại các trường giống như bộ trích xuất, theo đúng định nghĩa ở sheet Rubric_r5.",
    "",
    "Cách làm (sheet Cham):",
    "1. Mỗi dòng là một lời giải thích (cột explanation). Thứ tự dòng đã được xáo ngẫu nhiên; mã G001… không",
    "   tiết lộ tập dữ liệu hay đáp án. Không mở file *_KEY.xlsx trước khi chấm xong.",
    "2. Điền các cột màu vàng. Activity ghi bằng mã như trong lời giải thích (A01, A02, …), cách nhau dấu phẩy.",
    "3. support_level lấy từ dòng 'Support level:' ở phần Inference.",
    "4. central_activities: các activity là đối tượng của giả thuyết chính; không ghi activity chỉ làm mốc/bối cảnh.",
    "5. secondary_activities: activity được nói là thay đổi riêng, thêm vào giả thuyết chính (mục 'Other differences').",
    "6. mechanism và pattern: chọn từ danh sách thả xuống; nếu lời giải thích phân vân, lấy cách mà kết luận nghiêng về.",
    "7. time_* và resource_activities: chỉ điền khi lời giải thích nói thời gian / tài nguyên thay đổi.",
    "8. Không cần đánh giá lời giải thích đúng hay sai: chỉ ghi lại điều nó khẳng định. Điểm được tính sau, cùng một",
    "   công thức cho người chấm và cho bộ trích xuất.",
    "",
    "Gợi ý chia việc: có thể chấm một mẫu (ví dụ 100 dòng đầu, vì đã xáo ngẫu nhiên) hoặc chia dòng cho hai người,",
    "trong đó một phần chồng lấn để đo độ đồng thuận giữa người với người.",
]


def reference_text(case: dict, refs: dict) -> str:
    return refs.get(case["case_id"], "")


def build_references(cases: dict) -> dict[str, str]:
    from score_p2 import cdlg_references, e4_cases, ostovar_references
    ost, cdlg, e4 = ostovar_references(), cdlg_references(), e4_cases()
    out = {}
    for cid, c in cases.items():
        lm = json.loads((OUT / "audit" / f"{cid}.json").read_text(encoding="utf-8"))["label_map"]
        code = lambda acts: ", ".join(sorted(lm[a] for a in acts if a in lm))  # noqa: E731
        if c["kind"] == "null" and c["set"] != "e4b" and c["set"] != "e4a":
            out[cid] = "không có thay đổi (cặp null)"
        elif cid in ost:
            pattern, req, opt = ost[cid]
            out[cid] = f"pattern {pattern}; bắt buộc: {code(req)}" + (f"; tùy chọn: {code(opt)}" if opt else "")
        elif c["set"] == "cdlg":
            r = cdlg[cid]
            parts = [f"{role}: {code(json.loads(r[k]))}" for role, k in
                     (("thêm", "activities_added_real"), ("xóa", "activities_deleted_real"),
                      ("di chuyển", "activities_moved_real")) if json.loads(r[k])]
            out[cid] = f"{r['operation_class']}; " + "; ".join(parts)
        elif c["set"] == "e4a":
            r = e4[cid]
            if r["type"] == "N":
                out[cid] = "không tiêm thay đổi (N)"
            else:
                text = f"{r['type']}: thời gian của {code([r['time_target']])} {r['time_direction']}"
                if r["type"] == "M":
                    text += f"; cộng control-flow {r['cf_pattern']} trên {code(json.loads(r['cf_required']))}"
                out[cid] = text
        elif c["set"] == "e4b":
            r = e4[cid]
            out[cid] = "không tiêm thay đổi (N)" if r["type"] == "N" else \
                f"{r['type']}: tài nguyên của {code([r['target']])}" + \
                (f" (nguồn {code([r['source']])})" if r.get("source") else "")
    return out


def autosize(ws, widths: dict[int, int]):
    for col, width in widths.items():
        ws.column_dimensions[ws.cell(row=1, column=col).column_letter].width = width


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--run", default="run1")
    parser.add_argument("--prompt", default="INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC")
    args = parser.parse_args()
    runs = OUT / "runs" / args.prompt / args.model / args.run
    extr = OUT / "extractions_r5" / args.prompt / args.model / args.run
    with (OUT / "cases.csv").open(encoding="utf-8") as handle:
        cases = {r["case_id"]: r for r in csv.DictReader(handle)}
    scores = {}
    score_file = OUT / f"scores_{args.prompt}_{args.model}_{args.run}.csv"
    if score_file.exists():
        with score_file.open(encoding="utf-8") as handle:
            scores = {r["case_id"]: r for r in csv.DictReader(handle)}
    refs = build_references(cases)
    ids = [cid for cid in cases if (runs / f"{cid}.json").exists()
           and json.loads((runs / f"{cid}.json").read_text()).get("status") == "success"]
    random.Random(SEED).shuffle(ids)
    target_dir = OUT.parent / "_superseded" / "p2_human_grading_v1"  # superseded by experiments/p4_grading
    target_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{args.model}_{args.run}"

    # Grading workbook (blind)
    wb = Workbook()
    ws = wb.active
    ws.title = "Huong_dan"
    for i, line in enumerate(INSTRUCTIONS, 1):
        ws.cell(row=i, column=1, value=line)
    ws.column_dimensions["A"].width = 120
    wr = wb.create_sheet("Rubric_r5")
    for i, line in enumerate(RUBRIC.read_text(encoding="utf-8").splitlines(), 1):
        wr.cell(row=i, column=1, value=line)
    wr.column_dimensions["A"].width = 120
    wl = wb.create_sheet("Danh_sach")
    for col, values in enumerate((PATTERNS, MECHANISMS, ["insufficient", "weak", "supported", "unparsed"],
                                  ["increase", "decrease", "mixed", "none"]), 1):
        for row, v in enumerate(values, 1):
            wl.cell(row=row, column=col, value=v)
    wc = wb.create_sheet("Cham")
    header = ["grader_id", "explanation"] + [f for f, _ in GRADER_FIELDS] + ["nguoi_cham"]
    wc.append(header)
    wc.append(["", "(hướng dẫn cột)"] + [h for _, h in GRADER_FIELDS] + ["tên/viết tắt người chấm"])
    yellow = PatternFill("solid", fgColor="FFF2CC")
    for i, cid in enumerate(ids, 1):
        text = json.loads((runs / f"{cid}.json").read_text(encoding="utf-8"))["text"]
        wc.append([f"G{i:03d}", text] + [""] * (len(GRADER_FIELDS) + 1))
    for cell in wc[1]:
        cell.font = Font(bold=True)
    for cell in wc[2]:
        cell.font = Font(italic=True, color="666666")
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    last = len(ids) + 2
    for row in wc.iter_rows(min_row=3, max_row=last):
        row[1].alignment = Alignment(wrap_text=True, vertical="top")
        for cell in row[2:]:
            cell.fill = yellow
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    col = {f: header.index(f) + 1 for f, _ in GRADER_FIELDS}
    for field, ref in (("support_level", "Danh_sach!$C$1:$C$4"), ("mechanism", f"Danh_sach!$B$1:$B${len(MECHANISMS)}"),
                       ("pattern", f"Danh_sach!$A$1:$A${len(PATTERNS)}"), ("time_direction", "Danh_sach!$D$1:$D$4")):
        dv = DataValidation(type="list", formula1=ref, allow_blank=True)
        letter = wc.cell(row=1, column=col[field]).column_letter
        dv.add(f"{letter}3:{letter}{last}")
        wc.add_data_validation(dv)
    autosize(wc, {1: 9, 2: 100, **{c: 18 for c in range(3, len(header) + 1)}})
    wc.freeze_panes = "C3"
    wb.move_sheet("Cham", offset=-3)
    wb.active = 0
    grading = target_dir / f"{stem}_GRADING.xlsx"
    wb.save(grading)

    # Key workbook (references, Claude extraction, automatic scores)
    kb = Workbook()
    ks = kb.active
    ks.title = "Key"
    metric_cols = ["O", "O_main", "MR", "PI", "RTU", "overclaim", "O_F1", "time_detected", "time_direction_ok",
                   "time_false_claim", "target_claimed", "target_main", "n_resource_claims"]
    kh = ["grader_id", "case_id", "set", "kind", "type", "noise_pct", "reference_anon",
          "claude_support_level", "claude_central", "claude_secondary", "claude_mechanism", "claude_pattern",
          "claude_time_activities", "claude_time_direction", "claude_resource_activities"] + metric_cols
    ks.append(kh)
    for i, cid in enumerate(ids, 1):
        c = cases[cid]
        ex_path = extr / f"{cid}.json"
        e = json.loads(ex_path.read_text(encoding="utf-8"))["extraction"] if ex_path.exists() else {}
        s = scores.get(cid, {})
        ks.append([f"G{i:03d}", cid, c["set"], c["kind"], c["type"], c["noise_pct"], refs.get(cid, ""),
                   e.get("support_level", ""), ", ".join(e.get("central_activities", [])),
                   ", ".join(e.get("secondary_activities", [])), e.get("mechanism", ""), e.get("pattern", ""),
                   ", ".join(e.get("time_activities", [])), e.get("time_direction", ""),
                   ", ".join(e.get("resource_activities", []))] + [s.get(m, "") for m in metric_cols])
    for cell in ks[1]:
        cell.font = Font(bold=True)
    autosize(ks, {1: 9, 2: 24, 3: 14, 7: 60, 9: 30, 10: 24})
    ks.freeze_panes = "C2"
    key = target_dir / f"{stem}_KEY.xlsx"
    kb.save(key)
    missing = sum(not (extr / f"{cid}.json").exists() for cid in ids)
    print(f"{len(ids)} explanations -> {grading.relative_to(ROOT)}, {key.relative_to(ROOT)} "
          f"(Claude extraction missing for {missing})")


if __name__ == "__main__":
    main()
