#!/bin/zsh
# E6 (author 2026-11-14): qwen3.8-27b-uncensored, default reasoning (xhigh; "thinking" dropped, rejected by the
# gateway), streaming transport, stratified sample of 150 cases (experiments/p2_main/e6_qwen_sample_cases.txt).
cd "."
P=results/p2_main
M=qwen3.8-27b-uncensored
IDS=($(cat experiments/p2_main/e6_qwen_sample_cases.txt))
for i in 1 2 3 4; do
  python3 experiments/p2_main/run_p2.py generate --model $M --key-env GLM_API_KEY --drop-request thinking --stream \
      --workers 4 --case $IDS >> $P/generate_qwen_run1.log 2>&1
done
R=$P/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC/$M/run1
python3 experiments/p2_main/run_p2.py extract --runs $R >> $P/extract_qwen_run1.log 2>&1
python3 experiments/p2_main/cdlg_roles.py extract --runs $R >> $P/extract_cdlg_roles_qwen_run1.log 2>&1
<local-path> experiments/p2_main/score_p2.py --runs $R > $P/scores_qwen_summary.log 2>&1
python3 experiments/p2_main/cdlg_roles.py score --runs $R >> $P/scores_qwen_summary.log 2>&1
echo QWEN_DONE >> $P/scores_qwen_summary.log
