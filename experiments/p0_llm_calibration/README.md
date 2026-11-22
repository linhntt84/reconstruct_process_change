# P0-C — LLM calibration on the tuning split

Purpose: before freezing pipeline v2, check on held-out tuning data (Ostovar sizes 2, 4;
156 drift cases, 78 no-change pairs) that
1. the English prompt V2 declares "Insufficient evidence" on no-change pairs and still
   recovers the changed activities on drift cases;
2. the selected thresholds (config B) do not hurt the LLM result compared with config A
   (pre-registered: keep B unless mean O on tuning drift cases is more than 0.05 below A);
3. the blind extraction rubric V2 is unambiguous enough (spot checks by the authors).

Steps (scripts in this folder):

| Step | Script | Cost |
|---|---|---|
| 1 | `build_cases.py --config B` / `--config A`: v2 evidence per case (`results/.../evidence/<config>/`) | local |
| 2 | `run_generation.py --config B --model glm-5.3-flash --run-index 1` | **paid API** (gateway), keys from `.env` |
| 3 | `run_extraction.py --runs results/p0_llm_calibration/runs/INTERPRET_EVIDENCE_V2_EN/B` | Claude subscription via `claude -p`; waits at usage limits, never uses extra usage |
| 4 | `score.py --variant main` | local |

Generation and extraction never see case ids of the source, references, dataset names or
whether a case is a drift or a no-change pair. Request settings: `configs/llm_generation.json`
(temperature 0, top_p 0.9, thinking enabled, as in version 1).
