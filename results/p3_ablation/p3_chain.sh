#!/bin/zsh
# P3 (author approved 2026-11-14: all 1,044 GLM calls + Claude extraction). Design: docs/P3_ABLATION_PLAN_VI.md
# Restarted 2026-11-14 with --stream (transport only): non-streaming calls hit the gateway 120 s cut (HTTP 524) on 34/178 E9 cases.
cd "."
PY=<local-path>
R=experiments/p3_ablation/run_p3.py
L=results/p3_ablation
M=glm-5.3-flash
gen() { for i in 1 2 3; do $PY $R $1 generate --model $M --workers 6 --stream >> $L/generate_$1.log 2>&1; done; }
for e in e9_shuffle e3b_v2en e5_no_occ e5_no_dir e5_no_pos e5_no_rel e5_no_lag e5_no_time e5_no_cf; do gen $e; done
while pgrep -f "build_p3_cases.py --exp e8_labels" >/dev/null; do sleep 30; done
for e in e8_labels e3_noselect; do gen $e; done
$PY $R e8_labels map-labels > $L/map_labels_e8.log 2>&1
echo "GEN_DONE $(date)" >> $L/p3_chain.log
for e in e9_shuffle e3b_v2en e5_no_occ e5_no_dir e5_no_pos e5_no_rel e5_no_lag e5_no_time e5_no_cf e8_labels e3_noselect; do
  $PY $R $e extract >> $L/extract_$e.log 2>&1
done
for e in e9_shuffle e3_noselect; do $PY $R $e roles >> $L/roles_$e.log 2>&1; done
for e in e9_shuffle e3b_v2en e5_no_occ e5_no_dir e5_no_pos e5_no_rel e5_no_lag e5_no_time e5_no_cf e8_labels e3_noselect; do
  echo "== $e" >> $L/scores_summary.log; $PY $R $e score >> $L/scores_summary.log 2>&1
done
echo "P3_DONE $(date)" >> $L/scores_summary.log
