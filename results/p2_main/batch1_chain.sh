#!/bin/zsh
# P2: GLM retries, DeepSeek generation (+ retries), rule baseline, Claude r5 extraction (author request 2026-11-14).
cd "."
P=results/p2_main
RUNS=$P/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC
( for i in 1 2 3; do python3 experiments/p2_main/run_p2.py generate --model glm-5.3-flash --workers 2 >> $P/generate_glm_run1_retry.log 2>&1; done ) & GLMPID=$!
( python3 experiments/p2_main/run_p2.py generate --model deepseek-v4-flash --workers 3 > $P/generate_deepseek_run1.log 2>&1
  for i in 1 2 3; do python3 experiments/p2_main/run_p2.py generate --model deepseek-v4-flash --workers 2 >> $P/generate_deepseek_run1_retry.log 2>&1; done
  touch $P/.deepseek_done ) & DSPID=$!
python3 experiments/e2_rule_baseline/run_rule_baseline.py --evidence-dir $P/evidence --out $P/runs/RULE_BASELINE_V2/rule-engine-v1/run1 > $P/rule_baseline.log 2>&1
wait $GLMPID
python3 experiments/p2_main/run_p2.py extract --runs $RUNS/glm-5.3-flash/run1 >> $P/extract_glm_run1.log 2>&1
python3 experiments/p2_main/run_p2.py extract --runs $P/runs/RULE_BASELINE_V2/rule-engine-v1/run1 >> $P/extract_rule_run1.log 2>&1
while [ ! -f $P/.deepseek_done ]; do sleep 120; done
python3 experiments/p2_main/run_p2.py extract --runs $RUNS/deepseek-v4-flash/run1 >> $P/extract_deepseek_run1.log 2>&1
echo CHAIN_DONE
