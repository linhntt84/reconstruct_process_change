#!/usr/bin/env python3
"""P4 / E11b: blind human grading of LLM explanations (check of the automatic Claude extractor).

Sample (pre-registered, docs/E11B_HUONG_DAN_CHAM_VI.md): 100 explanations of P2 run 1, 50 per main model
(glm-5.3-flash, deepseek-v4-flash), stratified by set with a fixed quota per model (QUOTA below), drawn with
seed 20261115 among successful outputs. Two graders grade all 100 independently.

Outputs (results/p4_grading/):
  E11b_GRADING_grader1.xlsx, E11b_GRADING_grader2.xlsx   identical blind workbooks (one per grader):
      Cham (one row per explanation, shuffled; ids H001...), Huong_dan, Rubric_r5 (rendered verbatim, as the
      extractor sees it), Rubric_CDLG_roles (r5a, verbatim), Danh_sach (drop-down lists).
  E11b_KEY.xlsx            NOT for graders: id -> case, model, set, reference, Claude extraction.
  e11b_sample.csv          the sample (id, case_id, model, set, kind, type).
Requires openpyxl (Python >= 3.9).
"""
from __future__ import annotations

import csv
import json
import random
import shutil
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(ROOT / "e4_multiperspective" / "code"))
import extract_e4  # noqa: E402
from build_human_grading import MECHANISMS, PATTERNS, build_references  # noqa: E402

P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p4_grading"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"
MODELS = ["glm-5.3-flash", "deepseek-v4-flash"]
SEED = 20261115
# per model: (set, kind) -> number of explanations; 50 per model
QUOTA = {("ostovar3", "drift"): 10, ("ostovar5", "drift"): 8, ("cdlg", "drift"): 12,
         ("e4a", "drift"): 6, ("e4b", "drift"): 6,
         ("null_ostovar3", "null"): 2, ("null_ostovar5", "null"): 2, ("null_cdlg", "null"): 2,
         ("e4a", "null"): 1, ("e4b", "null"): 1}
CLASSES = ["only_added", "only_deleted", "only_moved", "deleted_and_added", "added_and_moved",
           "deleted_and_moved", "other", "unclear"]

# Guide columns (added 2026-11-15 at the author's request, before any grading): two plain-language questions that
# lead to the pattern, so that graders without a process-mining background need not know the 13 Ostovar pattern
# names. They restate the pattern definitions of rubric r5 (sheet Rubric_r5) and add nothing to them. The workbook
# computes a suggested pattern from the two answers (pattern_goi_y); the grader enters the final pattern. If the
# pattern cell is left empty, score_e11b.py uses the suggestion (guide_pattern below). Option 10 resolves a gap of
# the rubric (the pattern of a time- or resource-only hypothesis) with the convention of the Claude extractor in P2
# (timing_changed / resource_allocation_changed -> pattern none in 165/165 E4 extractions).
GUIDE_Q1 = [
    "1 thêm hoặc bỏ một đoạn",
    "2 thay một đoạn bằng đoạn khác",
    "3 hai đoạn đổi chỗ cho nhau",
    "4 chuyển một đoạn sang vị trí khác",
    "5 đoạn bắt đầu lặp / thôi lặp",
    "6 đoạn thành có thể bỏ qua / thành bắt buộc lại",
    "7 song song thành tuần tự (hoặc ngược lại)",
    "8 lựa chọn thành tuần tự (hoặc ngược lại)",
    "9 cấu trúc giữ nguyên, chỉ tần suất các nhánh đổi",
    "10 chỉ thời gian hoặc tài nguyên thay đổi, control-flow không đổi",
    "11 thay đổi control-flow khác (không thuộc 1-9)",
    "12 không có giả thuyết (insufficient)",
]
GUIDE_Q2 = [
    "a tuần tự (không có nhánh)",
    "b nhánh song song (AND)",
    "c nhánh lựa chọn (XOR)",
    "d không áp dụng",
]
_BY_STRUCTURE = {"1": ("SerialRemoval", "ParallelRemoval", "ConditionalRemoval"),
                 "4": ("SerialMove", "ParallelMove", "ConditionalMove")}
_FIXED = {"2": "Substitute", "3": "Swap", "5": "Loop", "6": "Skip", "7": "ParallelToSequence",
          "8": "ConditionalToSequence", "9": "Frequency", "10": "none", "11": "other",
          "12": "none"}


def guide_pattern(q1: str, q2: str) -> str:
    """Pattern implied by the two guide answers ("" if they do not determine one)."""
    k1, k2 = (q1 or "").split(" ")[0], (q2 or "").split(" ")[0]
    if k1 in _FIXED:
        return _FIXED[k1]
    if k1 in _BY_STRUCTURE and k2 in ("a", "b", "c"):
        return _BY_STRUCTURE[k1]["abc".index(k2)]
    return ""


def guide_table() -> list[tuple[str, str]]:
    """Lookup rows "Q1|Q2" -> suggested pattern for the workbook formula (Q2 may be blank)."""
    rows = []
    for q1 in GUIDE_Q1:
        for q2 in GUIDE_Q2 + [""]:
            rows.append((f"{q1}|{q2}", guide_pattern(q1, q2) or "(trả lời câu 2: a, b hoặc c)"))
    return rows


GUIDE_TEXT = """DẪN DẮT CHỌN PATTERN (cột dan_loai_thay_doi, dan_cau_truc, pattern_goi_y)

Bạn không cần thuộc tên 13 pattern. Đọc giả thuyết CHÍNH trong phần Inference, rồi trả lời hai câu:

Câu 1 (dan_loai_thay_doi): lời giải thích nói điều gì đã xảy ra với đoạn quy trình bị đổi?
  1 thêm hoặc bỏ một đoạn: activity xuất hiện mới hoặc biến mất hẳn.
  2 thay một đoạn bằng đoạn khác: activity cũ biến mất, activity mới xuất hiện ở đúng chỗ đó.
  3 hai đoạn đổi chỗ cho nhau: X trước Y thành Y trước X, cả hai cùng đổi vị trí.
  4 chuyển một đoạn sang vị trí khác: chỉ MỘT đoạn đổi vị trí, phần còn lại giữ thứ tự.
  5 đoạn bắt đầu lặp / thôi lặp: activity giờ lặp lại nhiều lần trong một case (hoặc ngược lại).
  6 đoạn thành có thể bỏ qua / bắt buộc lại: activity vẫn còn, nhưng có case giờ đi tắt qua nó (hoặc ngược lại).
  7 song song thành tuần tự (hoặc ngược lại): các activity trước chạy song song, thứ tự tùy ý, giờ theo một thứ tự
    cố định (hoặc ngược lại). Không activity nào bị thêm, bỏ hay chuyển chỗ.
  8 lựa chọn thành tuần tự (hoặc ngược lại): trước chỉ làm một trong hai nhánh, giờ làm cả hai nối tiếp (hoặc ngược lại).
  9 cấu trúc giữ nguyên, chỉ tần suất đổi: vẫn các nhánh đó, nhưng tỷ lệ case đi mỗi nhánh thay đổi.
  10 chỉ thời gian hoặc tài nguyên thay đổi: thứ tự và cấu trúc các bước không đổi (pattern = none; ghi phần thời gian
     / tài nguyên vào các cột time_* và resource_activities).
  11 thay đổi control-flow khác: có thay đổi về thứ tự hay cấu trúc nhưng không khớp loại 1-9 (pattern = other).
  12 không có giả thuyết: support level Insufficient và không nêu thay đổi cụ thể (pattern = none).

Nếu lời giải thích nêu CẢ thay đổi control-flow LẪN thay đổi thời gian/tài nguyên, trả lời câu 1 theo phần
control-flow (1-9 hoặc 11).

Câu 2 (dan_cau_truc): CHỈ cần khi câu 1 là 1 hoặc 4. Đoạn đó được thêm/bỏ hoặc chuyển ở đâu?
  a tuần tự: trong một chuỗi các bước nối tiếp nhau.
  b nhánh song song (AND): thành một nhánh chạy song song với nhánh khác, hoặc chuyển vào/ra một vùng song song.
  c nhánh lựa chọn (XOR): thành một nhánh mà chỉ một số case đi qua, hoặc chuyển vào/ra một vùng lựa chọn.
  d không áp dụng: dùng khi câu 1 không phải 1 hoặc 4.

Cột pattern_goi_y tự hiện pattern tương ứng. Hãy chép nó vào cột pattern (hoặc chọn pattern khác nếu bạn chắc chắn
lời giải thích nói khác). Nếu để trống cột pattern, khi tính toán sẽ dùng pattern gợi ý.

Bảng tương ứng:
  1 + a -> SerialRemoval        1 + b -> ParallelRemoval      1 + c -> ConditionalRemoval
  4 + a -> SerialMove           4 + b -> ParallelMove         4 + c -> ConditionalMove
  2 -> Substitute   3 -> Swap   5 -> Loop   6 -> Skip   7 -> ParallelToSequence   8 -> ConditionalToSequence
  9 -> Frequency    10 -> none    11 -> other    12 -> none

Các cặp hay nhầm:
  - Chuyển (4) hay đổi chỗ (3)? Nếu lời giải thích nói chỉ một đoạn dời đi, chọn 4. Nếu nói hai đoạn hoán đổi vị trí
    cho nhau, chọn 3. Nếu lời giải thích tự nói không phân biệt được, chọn cách mà kết luận nghiêng về, và ghi vào
    alternative_pattern cách còn lại nếu nó được coi là ngang khả năng.
  - Chuyển vào/ra nhánh song song (4 + b) hay song song thành tuần tự (7)? Nếu một activity cụ thể đổi vị trí, chọn 4.
    Nếu không có activity nào đổi chỗ, chỉ quan hệ giữa chúng đổi từ song song sang nối tiếp, chọn 7.
  - Bỏ qua được (6) hay thêm/bỏ một nhánh lựa chọn (1 + c)? Nếu activity vẫn còn trong quy trình nhưng giờ có thể
    bị nhảy qua, chọn 6. Nếu cả một nhánh với activity của nó xuất hiện hoặc biến mất, chọn 1 + c.
  - Chỉ tần suất (9) hay bỏ qua được (6)? Nếu activity trước đây đã có lúc bị bỏ qua và chỉ tỷ lệ thay đổi, chọn 9.
    Nếu trước đây luôn bắt buộc mà giờ có thể bỏ qua, chọn 6.
"""

FIELDS = [  # (column, short instruction); rubric r5 fields used by the scores, then CDLG r5a fields
    ("support_level", "insufficient / weak / supported / unparsed"),
    ("central_activities", "mã activity của giả thuyết chính, cách nhau dấu phẩy (vd: A03, A07)"),
    ("secondary_activities", "activity được nói là thay đổi riêng, thêm vào giả thuyết chính"),
    ("mechanism", "chọn trong danh sách"),
    ("dan_loai_thay_doi", "DẪN DẮT câu 1: điều gì xảy ra với đoạn bị đổi? (xem sheet Dan_dat_pattern)"),
    ("dan_cau_truc", "DẪN DẮT câu 2: chỉ khi câu 1 là 1 hoặc 4; còn lại chọn d"),
    ("pattern_goi_y", "TỰ TÍNH từ hai câu trên, không cần điền"),
    ("pattern", "chép pattern_goi_y, hoặc chọn khác nếu chắc chắn (13 pattern, other, none)"),
    ("alternative_pattern", "chỉ khi lời giải thích coi một cách đọc khác là ngang khả năng; nếu không: none"),
    ("alternative_activities", "activity của cách đọc thay thế (để trống nếu none)"),
    ("perspectives", "control_flow, time, resource (có thể nhiều, cách nhau dấu phẩy); trống nếu mechanism = none"),
    ("time_activities", "activity có thời gian thay đổi"),
    ("time_direction", "increase / decrease / mixed / none"),
    ("resource_activities", "activity có phân công / bàn giao tài nguyên thay đổi"),
    ("cdlg_objects", "CHỈ dòng có cdlg = có: mọi activity được nói là thay đổi (chính + phụ)"),
    ("cdlg_role_pairs", "CHỈ dòng cdlg = có: A03:added, A05:moved, ... (added / deleted / moved)"),
    ("cdlg_operation_class", "CHỈ dòng cdlg = có: chọn trong danh sách"),
    ("cdlg_quote", "CHỈ dòng cdlg = có: chép nguyên văn một câu nêu thay đổi chính"),
    ("ghi_chu", "nhận xét, chỗ phân vân (không bắt buộc)"),
]
INSTRUCTIONS = """HƯỚNG DẪN CHẤM E11b (tóm tắt; bản đầy đủ: docs/E11B_HUONG_DAN_CHAM_VI.md)

Mục đích: kiểm tra bộ trích xuất tự động (Claude, rubric r5). Bạn đọc lời giải thích do một LLM viết và ghi lại
những gì lời giải thích KHẲNG ĐỊNH, theo đúng định nghĩa trường ở sheet Rubric_r5 (và Rubric_CDLG_roles cho các
dòng CDLG). Bạn KHÔNG đánh giá lời giải thích đúng hay sai, và không cần biết đáp án.

Quy tắc:
1. Chấm độc lập. Không trao đổi với người chấm kia về từng dòng cho đến khi cả hai đã nộp file.
2. Không mở file KEY, không xem kết quả của Claude hay dữ liệu gốc. Chỉ dùng chính lời giải thích.
3. Thứ tự dòng đã xáo ngẫu nhiên; mã H001… không tiết lộ mô hình, tập dữ liệu hay đáp án.
4. Điền các ô màu vàng. Activity ghi bằng mã như trong lời giải thích (A01, A02, …), cách nhau dấu phẩy.
   Ô để trống = danh sách rỗng. Các cột có danh sách thả xuống: chỉ chọn giá trị trong danh sách.
5. support_level: lấy từ dòng "Support level:" trong phần Inference.
6. central_activities: activity là đối tượng của giả thuyết chính. Không ghi activity chỉ làm mốc, đứng trước/sau,
   hoặc bối cảnh không đổi. Nếu kết luận là Insufficient: để trống, trừ khi vẫn nêu một activity cụ thể đã đổi.
7. secondary_activities: activity được nói là thay đổi riêng, thêm vào giả thuyết chính (thường ở "Other differences").
8. mechanism / pattern: thay đổi chính mà lời giải thích đề xuất. Nếu phân vân giữa các khả năng, lấy khả năng
   mà kết luận nghiêng về, ghi lý do vào ghi_chu. Insufficient → mechanism = none, pattern = none.
   Để chọn pattern, trả lời hai cột dẫn dắt (dan_loai_thay_doi, dan_cau_truc) theo sheet Dan_dat_pattern; cột
   pattern_goi_y tự hiện pattern tương ứng, chép nó sang cột pattern.
9. alternative_*: chỉ khi lời giải thích nói rõ một cách mô tả khác của CÙNG khác biệt là ngang khả năng.
   Giải thích cạnh tranh bị bác bỏ hoặc "ít khả năng hơn" thì không tính. Không có → alternative_pattern = none.
10. time_* và resource_activities: chỉ điền khi lời giải thích nói thời gian / tài nguyên thay đổi.
11. Các cột cdlg_*: chỉ điền ở dòng có cột cdlg = "có" (định nghĩa ở sheet Rubric_CDLG_roles). Dòng khác để trống.
12. Ghi tên/viết tắt của bạn ở ô B1 của sheet Cham. Khi xong, lưu file và gửi lại nguyên file .xlsx.

Thời gian ước tính: 3–5 phút mỗi dòng, khoảng 6–8 giờ cho 100 dòng; có thể chia nhiều buổi.
""".splitlines()


def rendered_r5() -> str:
    saved = extract_e4.RUBRIC_R4
    extract_e4.RUBRIC_R4 = extract_e4.RUBRIC_R5
    try:
        return extract_e4.system_prompt_r4("main")
    finally:
        extract_e4.RUBRIC_R4 = saved


def draw_sample() -> list[dict]:
    with (P2 / "cases.csv").open(encoding="utf-8") as handle:
        cases = list(csv.DictReader(handle))
    rng, sample = random.Random(SEED), []
    for model in MODELS:
        runs = P2 / "runs" / PROMPT / model / "run1"
        ok = [c for c in cases if (runs / f"{c['case_id']}.json").exists()
              and json.loads((runs / f"{c['case_id']}.json").read_text()).get("status") == "success"]
        for (set_, kind), n in QUOTA.items():
            pool = sorted((c for c in ok if c["set"] == set_ and c["kind"] == kind), key=lambda c: c["case_id"])
            for c in rng.sample(pool, n):
                sample.append({**c, "model": model})
    rng.shuffle(sample)
    for i, s in enumerate(sample, 1):
        s["hid"] = f"H{i:03d}"
    return sample


def text_sheet(wb, title: str, text: str):
    ws = wb.create_sheet(title)
    for i, line in enumerate(text.splitlines(), 1):
        ws.cell(row=i, column=1, value=line)
    ws.column_dimensions["A"].width = 120


def build_grading(sample: list[dict], target: Path):
    wb = Workbook()
    wc = wb.active
    wc.title = "Cham"
    header = ["id", "cdlg", "explanation"] + [f for f, _ in FIELDS]
    wc.append(["Người chấm:", "", "(ghi tên/viết tắt vào ô B1)"])
    wc.append(header)
    wc.append(["", "", "(hướng dẫn cột)"] + [h for _, h in FIELDS])
    for s in sample:
        text = json.loads((P2 / "runs" / PROMPT / s["model"] / "run1" / f"{s['case_id']}.json")
                          .read_text(encoding="utf-8"))["text"]
        wc.append([s["hid"], "có" if s["set"] == "cdlg" else "", text] + [""] * len(FIELDS))
    yellow, grey = PatternFill("solid", fgColor="FFF2CC"), PatternFill("solid", fgColor="EEEEEE")
    wc["B1"].fill = yellow
    for cell in wc[2]:
        cell.font = Font(bold=True)
    for cell in wc[3]:
        cell.font = Font(italic=True, color="666666")
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    last = len(sample) + 3
    col = {f: header.index(f) + 1 for f, _ in FIELDS}
    for row in wc.iter_rows(min_row=4, max_row=last):
        row[2].alignment = Alignment(wrap_text=True, vertical="top")
        is_cdlg = row[1].value == "có"
        for f, _ in FIELDS:
            cell = row[col[f] - 1]
            cell.fill = grey if (f.startswith("cdlg_") and not is_cdlg) or f == "pattern_goi_y" else yellow
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        r, q1, q2 = row[0].row, wc.cell(row=2, column=col["dan_loai_thay_doi"]).column_letter, \
            wc.cell(row=2, column=col["dan_cau_truc"]).column_letter
        row[col["pattern_goi_y"] - 1].value = (
            f'=IF({q1}{r}="","",IFERROR(VLOOKUP({q1}{r}&"|"&{q2}{r},Danh_sach!$G$1:$H${len(guide_table())},2,FALSE),""))')
    lists = {"support_level": "Danh_sach!$C$1:$C$4", "mechanism": f"Danh_sach!$B$1:$B${len(MECHANISMS)}",
             "pattern": f"Danh_sach!$A$1:$A${len(PATTERNS)}", "alternative_pattern": f"Danh_sach!$A$1:$A${len(PATTERNS)}",
             "time_direction": "Danh_sach!$D$1:$D$4", "cdlg_operation_class": f"Danh_sach!$E$1:$E${len(CLASSES)}",
             "dan_loai_thay_doi": f"Danh_sach!$I$1:$I${len(GUIDE_Q1)}",
             "dan_cau_truc": f"Danh_sach!$J$1:$J${len(GUIDE_Q2)}"}
    for field, ref in lists.items():
        dv = DataValidation(type="list", formula1=ref, allow_blank=True)
        letter = wc.cell(row=2, column=col[field]).column_letter
        dv.add(f"{letter}4:{letter}{last}")
        wc.add_data_validation(dv)
    for c in range(1, len(header) + 1):
        wc.column_dimensions[wc.cell(row=2, column=c).column_letter].width = {1: 7, 2: 6, 3: 100}.get(c, 18)
    wc.freeze_panes = "D4"
    text_sheet(wb, "Huong_dan", "\n".join(INSTRUCTIONS))
    text_sheet(wb, "Dan_dat_pattern", GUIDE_TEXT)
    text_sheet(wb, "Rubric_r5", rendered_r5())
    text_sheet(wb, "Rubric_CDLG_roles",
               (ROOT / "experiments" / "p2_main" / "EXTRACTION_RUBRIC_CDLG_ROLES_EN.md").read_text(encoding="utf-8"))
    wl = wb.create_sheet("Danh_sach")
    for c, values in enumerate((PATTERNS, MECHANISMS, ["insufficient", "weak", "supported", "unparsed"],
                                ["increase", "decrease", "mixed", "none"], CLASSES), 1):
        for r, v in enumerate(values, 1):
            wl.cell(row=r, column=c, value=v)
    for r, (key, pattern) in enumerate(guide_table(), 1):
        wl.cell(row=r, column=7, value=key)
        wl.cell(row=r, column=8, value=pattern)
    for c, values in ((9, GUIDE_Q1), (10, GUIDE_Q2)):
        for r, v in enumerate(values, 1):
            wl.cell(row=r, column=c, value=v)
    wb.save(target)


def build_key(sample: list[dict], target: Path):
    refs = build_references({s["case_id"]: s for s in sample})
    kb = Workbook()
    ks = kb.active
    ks.title = "Key"
    ks.append(["id", "case_id", "model", "set", "kind", "type", "noise_pct", "reference_anon",
               "claude_r5_json", "claude_r5a_json"])
    for s in sample:
        rel = Path(PROMPT) / s["model"] / "run1" / f"{s['case_id']}.json"
        r5 = P2 / "extractions_r5" / rel
        r5a = P2 / "extractions_r5a_cdlg" / rel
        ks.append([s["hid"], s["case_id"], s["model"], s["set"], s["kind"], s["type"], s["noise_pct"],
                   refs.get(s["case_id"], ""),
                   json.dumps(json.loads(r5.read_text())["extraction"], ensure_ascii=False) if r5.exists() else "",
                   json.dumps(json.loads(r5a.read_text())["extraction"], ensure_ascii=False) if r5a.exists() else ""])
    for cell in ks[1]:
        cell.font = Font(bold=True)
    kb.save(target)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sample = draw_sample()
    with (OUT / "e11b_sample.csv").open("w", encoding="utf-8", newline="") as handle:
        w = csv.writer(handle)
        w.writerow(["id", "case_id", "model", "set", "kind", "type", "noise_pct"])
        for s in sorted(sample, key=lambda s: s["hid"]):
            w.writerow([s["hid"], s["case_id"], s["model"], s["set"], s["kind"], s["type"], s["noise_pct"]])
    first = OUT / "E11b_GRADING_grader1.xlsx"
    build_grading(sample, first)
    shutil.copyfile(first, OUT / "E11b_GRADING_grader2.xlsx")
    build_key(sample, OUT / "E11b_KEY.xlsx")
    print(f"{len(sample)} explanations ({sum(s['set'] == 'cdlg' for s in sample)} CDLG) -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
