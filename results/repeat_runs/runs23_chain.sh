#!/bin/zsh
# Runs 2 and 3 (author 2026-11-15: "chỗ nào cần chạy 2-3 run thì cứ chạy", three runs in total).
# Scope: P2 main for glm-5.3-flash and deepseek-v4-flash (528 cases each) and every P3 ablation (glm, 1,044 cases).
# Not repeated: rule baseline (deterministic), Qwen E6 (robustness check, 1 run, ~9 min per case).
# Same prompt, settings and evidence as run 1; transport --stream for all calls (transport only, no effect on the
# request; avoids the gateway 120 s cut). Generation: GLM and DeepSeek in parallel; Claude extraction follows each
# finished unit in a fixed order (flags in $F).
cd "."
PY=<local-path>
L=results/repeat_runs
F=$L/flags
mkdir -p $F
P2RUNS=results/p2_main/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC
R3=experiments/p3_ablation/run_p3.py
EXPS=(e9_shuffle e3b_v2en e5_no_occ e5_no_dir e5_no_pos e5_no_rel e5_no_lag e5_no_time e5_no_cf e8_labels e3_noselect)

p2gen() { for i in 1 2 3; do $PY experiments/p2_main/run_p2.py generate --model $1 --run-index $2 --workers $3 --stream >> $L/gen_p2_$1_run$2.log 2>&1; done; touch $F/p2_$1_run$2; }
p3gen() { for i in 1 2 3; do $PY $R3 $1 generate --model glm-5.3-flash --run-index $2 --workers 6 --stream >> $L/gen_p3_$1_run$2.log 2>&1; done
          [ $1 = e8_labels ] && $PY $R3 e8_labels map-labels --run-index $2 >> $L/map_labels_e8_run$2.log 2>&1
          touch $F/p3_$1_run$2; }
waitflag() { while [ ! -f $F/$1 ]; do sleep 60; done; }

# generation
( for k in 2 3; do p2gen glm-5.3-flash $k 6; done
  for k in 2 3; do for e in $EXPS; do p3gen $e $k; done; done ) &
( for k in 2 3; do p2gen deepseek-v4-flash $k 4; done ) &

# extraction (Claude, Team plan quota; run_p2 waits when the limit is hit)
for k in 2 3; do
  for m in glm-5.3-flash deepseek-v4-flash; do
    waitflag p2_${m}_run$k
    $PY experiments/p2_main/run_p2.py extract --runs $P2RUNS/$m/run$k >> $L/extract_p2_${m}_run$k.log 2>&1
    $PY experiments/p2_main/cdlg_roles.py extract --runs $P2RUNS/$m/run$k >> $L/roles_p2_${m}_run$k.log 2>&1
  done
done
for k in 2 3; do
  for e in $EXPS; do
    waitflag p3_${e}_run$k
    $PY $R3 $e extract --run-index $k >> $L/extract_p3_${e}_run$k.log 2>&1
    case $e in e9_shuffle|e3_noselect) $PY $R3 $e roles --run-index $k >> $L/roles_p3_${e}_run$k.log 2>&1;; esac
  done
done
wait

# scoring (no API)
for k in 2 3; do
  for m in glm-5.3-flash deepseek-v4-flash; do
    echo "== P2 $m run$k" >> $L/scores_summary.log
    $PY experiments/p2_main/score_p2.py --runs $P2RUNS/$m/run$k >> $L/scores_summary.log 2>&1
    $PY experiments/p2_main/cdlg_roles.py score --runs $P2RUNS/$m/run$k >> $L/scores_summary.log 2>&1
  done
  for e in $EXPS; do
    echo "== P3 $e run$k" >> $L/scores_summary.log
    $PY $R3 $e score --run-index $k >> $L/scores_summary.log 2>&1
  done
done
echo "RUNS23_DONE $(date)" >> $L/scores_summary.log
