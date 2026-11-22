#!/bin/zsh
# P2 follow-up (author: run everything automatically, 2026-11-14): CDLG roles (r5a) for DeepSeek and the
# rule ablation, then, after the r5 chain, scoring of every method and grading workbooks.
cd "."
P=results/p2_main
RUNS=$P/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC
RULE=$P/runs/RULE_BASELINE_V2/rule-engine-v1/run1
python3 experiments/p2_main/cdlg_roles.py extract --runs $RUNS/deepseek-v4-flash/run1 > $P/extract_cdlg_roles_deepseek_run1.log 2>&1
python3 experiments/p2_main/cdlg_roles.py extract --runs $RULE > $P/extract_cdlg_roles_rule_run1.log 2>&1
while ! grep -q CHAIN_DONE $P/batch1_chain.log; do sleep 120; done
for R in $RUNS/glm-5.3-flash/run1 $RUNS/deepseek-v4-flash/run1 $RULE; do
  <local-path> experiments/p2_main/score_p2.py --runs $R
  python3 experiments/p2_main/cdlg_roles.py score --runs $R
done > $P/scores_summary.log 2>&1
<local-path> experiments/p2_main/build_human_grading.py --model glm-5.3-flash >> $P/scores_summary.log 2>&1
<local-path> experiments/p2_main/build_human_grading.py --model deepseek-v4-flash >> $P/scores_summary.log 2>&1
echo FOLLOWUP_DONE >> $P/scores_summary.log
