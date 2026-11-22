#!/bin/zsh
# E3-full on CDLG (author 2026-11-16): both selection stages off, cdlg + null_cdlg (150 cases), glm-5.3-flash,
# runs 1-3, transport --stream. Then Claude extraction (r5, r5a for CDLG drift) and scoring.
cd "."
PY=<local-path>
R3=experiments/p3_ablation/run_p3.py
L=results/p3_ablation/e3_full/logs
mkdir -p $L
for k in 1 2 3; do
  for i in 1 2 3; do $PY $R3 e3_full generate --model glm-5.3-flash --run-index $k --workers 6 --stream >> $L/gen_run$k.log 2>&1; done
done
for k in 1 2 3; do
  $PY $R3 e3_full extract --run-index $k >> $L/extract_run$k.log 2>&1
  $PY $R3 e3_full roles --run-index $k >> $L/roles_run$k.log 2>&1
  echo "== e3_full run$k" >> $L/scores_summary.log
  $PY $R3 e3_full score --run-index $k >> $L/scores_summary.log 2>&1
done
echo "E3FULL_DONE $(date)" >> $L/scores_summary.log
