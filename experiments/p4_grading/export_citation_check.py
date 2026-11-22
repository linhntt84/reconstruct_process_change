#!/usr/bin/env python3
"""Citation-support check (Section VII-E): export the completed blind sheet with its key as one English CSV.

build_citation_check.py drew 90 statements (60 observations, 30 inferences) from 30 explanations with a fixed seed
and wrote a sheet without model or case names (CITATION_CHECK.xlsx) plus a separate key. One author rated every
statement against the content of the items it cites:
  1 fully supported   every numerical claim and direction in the statement is visible in the cited items,
                      for the right activity and the right direction
  2 partly supported  the main point holds, but one detail is not in the cited items, a number clearly differs,
                      or a cited ID is unrelated to the statement
  3 not supported     the main point is not in the cited items or contradicts them
  4 cannot be judged  the statement is too generic or the displayed evidence is insufficient
  numeric_mismatch    "yes" if at least one number in the statement does not match the cited items
Inputs: results/p4_grading/returned/CITATION_CHECK_author.xlsx, results/p4_grading/citation_check/citation_check_key.csv
Output: results/p4_grading/citation_check_results.csv and a summary printed to stdout. No API calls.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
P4 = ROOT / "results" / "p4_grading"
TYPES = {"quan sát": "observation", "suy luận": "inference"}
YES_NO = {"co": "yes", "có": "yes", "khong": "no", "không": "no"}


def main():
    with (P4 / "citation_check" / "citation_check_key.csv").open(encoding="utf-8") as handle:
        key = {r["row"]: r for r in csv.DictReader(handle)}
    sheet = openpyxl.load_workbook(P4 / "returned" / "CITATION_CHECK_author.xlsx", data_only=True)["Ra_soat"]
    rows = []
    for r in sheet.iter_rows(min_row=2, values_only=True):
        if not r[0]:
            continue
        k = key[r[0]]
        rows.append({"row": r[0], "explanation": r[1], "case_id": k["case_id"], "model": k["model"], "set": k["set"],
                     "statement_type": TYPES.get(r[2], r[2]), "statement": r[3], "cited_ids": r[4],
                     "nonexistent_ids": r[6] or "", "rating": r[7],
                     "numeric_mismatch": YES_NO.get(str(r[8]).strip().lower(), r[8])})
    with (P4 / "citation_check_results.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} statements from {len({r['explanation'] for r in rows})} explanations")
    print("by type:", dict(Counter(r["statement_type"] for r in rows)))
    print("by model:", dict(Counter(r["model"] for r in rows)))
    print("rating:", dict(Counter(r["rating"] for r in rows)))
    print("numeric mismatch:", dict(Counter(r["numeric_mismatch"] for r in rows)))
    print("nonexistent IDs:", sum(bool(r["nonexistent_ids"]) for r in rows))


if __name__ == "__main__":
    main()
