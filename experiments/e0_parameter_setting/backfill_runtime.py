#!/usr/bin/env python3
"""Backfill runtime_log.csv for sweeps started before per-run timing was added.

Start time is the OS process start (ps lstart); end time is the newest cache file.
Per-task seconds were not recorded for these runs, so sum_task_seconds is empty.
"""
import argparse
import csv
from datetime import datetime
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "results/e0_parameter_setting"

parser = argparse.ArgumentParser()
parser.add_argument("--run-dir", required=True, help="e.g. cache/tuning/w200_b100")
parser.add_argument("--start", required=True, help="ISO time, e.g. 2026-11-11T11:30:22+07:00")
parser.add_argument("--workers", type=int, required=True)
parser.add_argument("--cache-root", help="directory containing the original cache (mtimes are lost when copying)")
parser.add_argument("--hardware", default="Apple M4, 10 cores, Python 3.12.10")
args = parser.parse_args()

parser_dir = Path(args.cache_root) if args.cache_root else OUT
files = list((parser_dir / args.run_dir).glob("*.json"))
start = datetime.fromisoformat(args.start)
end = datetime.fromtimestamp(max(f.stat().st_mtime for f in files)).astimezone()
mode, cfg = Path(args.run_dir).parts[-2:]
window, bs = cfg.split("_")[0][1:], cfg.split("_")[1][1:]
row = {"run": cfg, "mode": mode, "window": window, "B_S": bs,
       "localization_grid": "current only" if "curloc" in cfg else "4x4", "tasks": len(files),
       "computed": len(files), "workers": args.workers, "start": start.isoformat(timespec="seconds"),
       "end": end.isoformat(timespec="seconds"), "wall_seconds": round((end - start).total_seconds(), 1),
       "sum_task_seconds": "", "hardware": args.hardware,
       "source": "backfilled: process start + newest cache file mtime"}
path = OUT / "runtime_log.csv"
new = not path.exists()
with path.open("a", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(row))
    if new:
        writer.writeheader()
    writer.writerow(row)
print(row)
