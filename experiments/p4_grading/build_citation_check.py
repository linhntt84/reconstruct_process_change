#!/usr/bin/env python3
"""P4: manual check that cited evidence supports the claim it is attached to (R1 #6, R4 #3d). No API calls.

Citation validity (the cited IDs exist in the input) says nothing about whether the cited items support the
sentence. Here a human reads claim units with their cited items and judges the support.

Sample (fixed seed): P2 run 1, glm-5.3-flash and deepseek-v4-flash; 6 explanations per drift set (ostovar3,
ostovar5, cdlg, e4a, e4b; 3 per model), 30 explanations. From each: 2 bullets of "Observed differences" and 1 unit
of "Inference", drawn at random among the units that cite at least one evidence ID. A unit is one bullet, or one
paragraph of the inference.

Output: results/p4_grading/citation_check/CITATION_CHECK.xlsx (for the grader, no model or case names) and
citation_check_key.csv (unit -> case, model, set).
"""
from __future__ import annotations

import csv
import json
import random
import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p4_grading" / "citation_check"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"
MODELS = ("glm-5.3-flash", "deepseek-v4-flash")
SETS = ("ostovar3", "ostovar5", "cdlg", "e4a", "e4b")
SEED = 20261117
ID_RE = re.compile(r"\b(?:OCC|DIR|POS|REL|LAG|TWAIT|ASSIGN|CONC|HAND)\d{3}\b")
JUDGEMENTS = ["1 hỗ trợ đầy đủ", "2 hỗ trợ một phần", "3 không hỗ trợ", "4 không đánh giá được"]
FAMILY_VI = {"CF_OCC": "tần suất xuất hiện", "CF_DIR": "activity kế tiếp (routing)", "CF_POS": "vị trí trong trace",
             "CF_REL": "quan hệ giữa hai activity", "CF_LAG": "khoảng cách (số event) giữa hai activity",
             "T_WAIT": "thời gian chờ", "O_ASSIGN": "phân công resource", "O_CONC": "độ tập trung resource"}


def units(text: str) -> dict:
    """Split an explanation into citing units per section (bullets, or paragraphs)."""
    out = {"observed": [], "inference": []}
    section = None
    for block in re.split(r"\n\s*\n", text):
        head = block.strip().lower()
        if head.startswith("### observed"):
            section = "observed"
            block = block.split("\n", 1)[1] if "\n" in block else ""
        elif head.startswith("### inference"):
            section = "inference"
            block = block.split("\n", 1)[1] if "\n" in block else ""
        if section is None:
            continue
        parts, current = [], []
        for line in block.splitlines():
            if line.lstrip().startswith(("- ", "* ")) and current:
                parts.append(" ".join(current))
                current = []
            current.append(line.strip())
        if current:
            parts.append(" ".join(current))
        for p in parts:
            p = p.strip()
            if p and ID_RE.search(p) and not p.lower().startswith("support level"):
                out[section].append(p.lstrip("-* ").strip())
    return out


def fmt(v):
    if isinstance(v, float) and v.is_integer() and abs(v) > 1:
        return str(int(v))
    return f"{v:.2f}" if isinstance(v, float) else str(v)


def render(item: dict) -> str:
    unit = item["analysis_unit"]
    name = unit.get("value") or " → ".join(unit.get("values", [])) or json.dumps(unit)
    lines = [f"[{item['id']}] {FAMILY_VI.get(item['indicator'], item['indicator'])} — {name}"]
    before, after = item.get("components_before", {}), item.get("components_after", {})
    keys = list(dict.fromkeys(list(before) + list(after)))
    if item["indicator"] in ("CF_DIR", "O_ASSIGN"):  # long profiles: largest components only
        keys = sorted(keys, key=lambda k: -max(abs(before.get(k, 0) or 0), abs(after.get(k, 0) or 0)))[:6]
    lines.append("  trước: " + "; ".join(f"{k}={fmt(before[k]) if k in before else '–'}" for k in keys))
    lines.append("  sau:   " + "; ".join(f"{k}={fmt(after[k]) if k in after else '–'}" for k in keys))
    sup = item.get("support", {})
    if sup:
        lines.append(f"  số quan sát: trước {sup.get('before')}, sau {sup.get('after')}")
    return "\n".join(lines)


def main():
    rng = random.Random(SEED)
    with (P2 / "cases.csv").open(encoding="utf-8") as handle:
        cases = [r for r in csv.DictReader(handle) if r["kind"] == "drift" and r["set"] in SETS]
    rows, key = [], []
    n_expl = 0
    for set_ in SETS:
        for model in MODELS:
            pool = [c for c in cases if c["set"] == set_]
            rng.shuffle(pool)
            taken = 0
            for c in pool:
                rec = P2 / "runs" / PROMPT / model / "run1" / f"{c['case_id']}.json"
                if not rec.exists() or json.loads(rec.read_text())["status"] != "success":
                    continue
                u = units(json.loads(rec.read_text())["text"])
                if len(u["observed"]) < 2 or not u["inference"]:
                    continue
                n_expl += 1
                code = f"G{n_expl:02d}"
                evidence = {e["id"]: e for e in
                            json.loads((P2 / "evidence" / f"{c['case_id']}.json").read_text())["evidence"]}
                picks = [("quan sát", t) for t in rng.sample(u["observed"], 2)] + \
                        [("suy luận", rng.choice(u["inference"]))]
                for kind, text in picks:
                    ids = list(dict.fromkeys(ID_RE.findall(text)))
                    missing = [i for i in ids if i not in evidence]
                    shown = [render(evidence[i]) for i in ids if i in evidence]
                    if len(ids) > 8:  # long synthesis lists: show the first 8 items
                        shown = shown[:8] + [f"(và {len(ids) - 8} item khác)"]
                    rid = f"{code}-{len(rows) % 3 + 1}"
                    rows.append([rid, code, kind, text, ", ".join(ids), "\n\n".join(shown),
                                 ", ".join(missing) or "", "", "", ""])
                    key.append({"row": rid, "explanation": code, "case_id": c["case_id"], "model": model,
                                "set": set_, "unit": kind, "n_cited": len(ids)})
                taken += 1
                if taken == 3:
                    break
    OUT.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Ra_soat"
    header = ["ma_dong", "ma_loi_giai_thich", "loai_doan", "doan_van (claim)", "id_trich_dan",
              "noi_dung_evidence_duoc_trich", "id_khong_ton_tai", "danh_gia", "so_lieu_sai (co/khong)", "ghi_chu"]
    ws.append(header)
    for r in rows:
        ws.append(r)
    widths = [9, 10, 10, 70, 18, 80, 12, 22, 14, 40]
    for i, w in enumerate(widths):
        ws.column_dimensions[chr(65 + i)].width = w
    for cell in ws[1]:
        cell.font = Font(bold=True)
    fill = PatternFill("solid", start_color="FFF2CC")
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        for cell in row[7:10]:
            cell.fill = fill
    dv = DataValidation(type="list", formula1='"' + ",".join(JUDGEMENTS) + '"', allow_blank=True)
    dv2 = DataValidation(type="list", formula1='"co,khong"', allow_blank=True)
    ws.add_data_validation(dv)
    ws.add_data_validation(dv2)
    dv.add(f"H2:H{len(rows) + 1}")
    dv2.add(f"I2:I{len(rows) + 1}")
    ws.freeze_panes = "D2"
    g = wb.create_sheet("Huong_dan")
    for line in GUIDE.strip().splitlines():
        g.append([line])
    g.column_dimensions["A"].width = 120
    wb.save(OUT / "CITATION_CHECK.xlsx")
    with (OUT / "citation_check_key.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(key[0]))
        writer.writeheader()
        writer.writerows(key)
    print(f"{n_expl} explanations, {len(rows)} units -> {OUT}")


GUIDE = """
RÀ SOÁT TRÍCH DẪN EVIDENCE (citation support)

Mục đích: kiểm tra xem các evidence mà mô hình trích dẫn [ví dụ OCC001] có thật sự hỗ trợ câu mà nó gắn vào hay không.
Bài cũ chỉ kiểm tra ID có tồn tại (100%), nhưng điều đó không cho biết nội dung có khớp hay không (R1 #6, R4 #3d).

Mỗi dòng gồm một đoạn trong lời giải thích (cột D) và nội dung các evidence được trích dẫn (cột F).
Activity được ẩn danh (A01, A02, ...). Số liệu trong evidence là tỷ lệ (0–1) hoặc trung bình; mô hình thường viết lại
thành "khoảng 48 trên 100". Coi là khớp nếu làm tròn hợp lý.

Cột H — đánh giá:
1 hỗ trợ đầy đủ: mọi khẳng định có số liệu hoặc hướng thay đổi trong đoạn đều thấy được trong evidence được trích,
  đúng activity và đúng chiều (tăng/giảm, trước/sau).
2 hỗ trợ một phần: ý chính đúng, nhưng có một chi tiết không thấy trong evidence được trích, hoặc một số liệu lệch
  rõ, hoặc có ID trích không liên quan đến câu.
3 không hỗ trợ: ý chính không thấy trong evidence được trích, hoặc mâu thuẫn với evidence (sai activity, sai chiều).
4 không đánh giá được: đoạn văn quá chung chung, hoặc evidence hiển thị không đủ để kết luận.

Với đoạn "suy luận": câu thường là một kết luận (ví dụ "A02 bị loại bỏ"). Hỏi: các evidence được trích có cho
thấy điều đó một cách hợp lý không? Không cần evidence chứng minh tuyệt đối; chỉ cần nhất quán và liên quan.

Cột I — so_lieu_sai: ghi "co" nếu có ít nhất một con số trong đoạn không khớp evidence (kể cả khi bạn vẫn chấm 1 hoặc 2).
Cột G — id_khong_ton_tai: điền tự động; nếu có ID ở đây thì mô hình trích một ID không có trong đầu vào.

Ý nghĩa một số trường:
- tần suất: mean_occurrences_per_trace = số lần trung bình mỗi trace; trace_participation = tỷ lệ trace có activity;
  recurrence_support = tỷ lệ trace có activity lặp lại.
- activity kế tiếp: tỷ lệ các lần activity được theo sau trực tiếp bởi từng activity (chỉ hiện 6 thành phần lớn nhất).
- vị trí: vị trí event chuẩn hóa trong trace (0 = đầu, 1 = cuối); mean, median, q25, q75.
- quan hệ hai activity: cooccurrence = cùng trace; A_only / B_only = chỉ một trong hai; A_before_B / B_before_A = thứ
  tự; interleaved_or_repeated = đan xen hoặc lặp.
- khoảng cách: phân bố số event nằm giữa hai activity.
- thời gian chờ: thống kê thời gian (giờ) từ khi xong activity trước đến khi xong activity sau.
- phân công resource: tỷ lệ event của activity do từng resource thực hiện; OTHER = tổng các resource nhỏ.
  Dấu "–" nghĩa là giá trị đó không được liệt kê trong evidence (với resource: nhỏ hơn các resource được liệt kê;
  với activity kế tiếp: không quan sát thấy).
"""

if __name__ == "__main__":
    main()
