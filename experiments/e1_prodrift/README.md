# E1 — ProDrift 2.5 baseline (Ostovar and CDLG)

Non-LLM state-of-the-art baseline: ProDrift 2.5 (Ostovar et al.), event-based detection +
fragment-based characterization, unmodified.

## Requirements
- Java 8+ (tested with OpenJDK 17.0.17).
- `ProDrift2.5.jar` (SHA-256 `700f20f9…50e59c0`), path in `PRODRIFT_JAR`
  (default: `../ProDrift2.5/ProDrift2.5.jar` next to the repository).
- Ostovar logs (`PCR_OSTOVAR_FULL`) and CDLG zips (`PCR_CDLG`), see `data/README.md`.
- Heap via `PRODRIFT_XMX` (default 6g).

## Scripts (run from the repository root)

| Step | Script | Output |
|---|---|---|
| 1 | `run_prodrift.py [--dataset ostovar\|cdlg\|files]` — runs ProDrift; stops the JVM (which does not exit by itself) after the final console line | `results/e1_prodrift/raw/<group>/<log>/` |
| 2 | `make_window_logs.py --cdlg-isolated` — one log per evaluated CDLG change, cut between the neighbouring official change points (± 50 traces) | `results/e1_prodrift/window_logs/cdlg_isolated/` (not in Git) |
| 3 | `parse_prodrift.py` — detections (event index → trace position) and statements | `results/e1_prodrift/detections.{csv,jsonl}` |
| 4 | `score_prodrift.py` — Ostovar, same metrics as the pipeline | `results/e1_prodrift/scores.csv` |
| 5 | `score_prodrift_cdlg.py [--isolated]` — CDLG, version-1 CDLG metrics | `results/e1_prodrift/scores_cdlg[_isolated].csv` |

```
python experiments/e1_prodrift/run_prodrift.py --workers 4
python experiments/e1_prodrift/make_window_logs.py --cdlg-isolated
PRODRIFT_XMX=8g python experiments/e1_prodrift/run_prodrift.py --dataset files \
       --files-dir results/e1_prodrift/window_logs/cdlg_isolated --workers 3
python experiments/e1_prodrift/parse_prodrift.py
python experiments/e1_prodrift/score_prodrift.py
python experiments/e1_prodrift/score_prodrift_cdlg.py --isolated
```

`make_window_logs.py` without `--cdlg-isolated` builds the 400-trace L−/L+ logs used to show
that ProDrift cannot characterize inputs of the pipeline's size (kept for transparency).

ProDrift needs no tuning, so running it on the evaluation sets leaks nothing into pipeline v2.
