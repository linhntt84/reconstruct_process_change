# E2 — Rule-based interpretation baseline under the same extraction protocol

Question answered: *is the LLM needed, or do simple rules over the same evidence do as well?*
(R1, R3, R4, R7: the version-1 rule baseline was scored with a different protocol and could
not be compared with the LLM.)

## What is compared
- Same evidence documents the LLM receives (pipeline v2, `llm_payload`).
- Interpretation by deterministic rules instead of an LLM.
- Same blind extractor (Claude via `claude -p`), same rubric, same references and metrics
  (`experiments/p0_llm_calibration/run_extraction.py`, `score.py`).

## Files
| File | Content |
|---|---|
| `engine_v1.py` | Rule engine of the submitted study, copied verbatim (SHA-256 `32ff5b7d…5023f7`). Rules R01–R08: appearance/removal (OCC+DIR), repetition (OCC), exclusive ↔ sequence and mixed ↔ fixed order (REL), movement (POS+REL+DIR), order reversal (REL), optionality and participation frequency (OCC). Thresholds unchanged. |
| `run_rule_baseline.py` | v2 wrapper: (1) screening with the principle of the LLM prompt, fixed before scoring: `n_items <= max(2, 3 × items_expected_without_change)` → "Insufficient evidence"; (2) the LLM output frame (Observed differences / Inference / Support level). Writes records in the LLM record format. |
| `pilot_cases_r3_sample.txt` | Development pilot: the 50 tuning cases of the prompt-R3 check. |

## Run
```
python experiments/e2_rule_baseline/run_rule_baseline.py            # all tuning cases (config B)
python experiments/p0_llm_calibration/run_extraction.py \
       --runs results/p0_llm_calibration/runs/RULE_BASELINE_V2/B \
       --case-list experiments/e2_rule_baseline/pilot_cases_r3_sample.txt
python experiments/p0_llm_calibration/score.py
```
The evaluation-set run (P2) uses the frozen evidence of each evaluation set via `--evidence-dir`.

## Notes
- The engine never sees source case ids, references or dataset names.
- The rules do not cover every pattern (e.g. no rule for moves into/out of a parallel branch);
  this is part of what the comparison measures, and the rules were not extended after seeing
  results.
