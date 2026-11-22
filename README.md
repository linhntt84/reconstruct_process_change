# Reconstructing Hidden Process Transformations with LLMs from Selected Quantitative Evidence

Code, prompts, rubrics, references and all model outputs for the revised IEEE Access manuscript
(Access-2026-49367). The material of the originally submitted version is kept unchanged in
[`v1_submission/`](v1_submission/) (git tag `v1-submission`).

The pipeline compares two windows of an event log before and after a change point, keeps only the
behavioural differences that are statistically qualified (localization, screening, permutation reference),
and gives this evidence to an LLM, which writes an explanation of the change. The explanations are read by
a blind extractor and scored deterministically against references.

## What is included

| Material | Location |
|---|---|
| Pipeline (evidence construction, Algorithms 1 and 2, indicators) | [`src/pcr/`](src/pcr/), parameters in [`configs/pipeline_v2.json`](configs/pipeline_v2.json) |
| Time and resource extension (TWAIT, resource-allocation families) | [`e4_multiperspective/code/`](e4_multiperspective/code/) |
| Interpretation prompt used for every reported run | [`e4_multiperspective/code/prompts/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC.md`](e4_multiperspective/code/prompts/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC.md) (earlier versions and diffs in the same folder and in [`prompts/`](prompts/)) |
| LLM request settings | [`configs/llm_generation.json`](configs/llm_generation.json) |
| Extraction rubrics (standalone) | [`prompts/EXTRACTION_RUBRIC_V2_EN.md`](prompts/EXTRACTION_RUBRIC_V2_EN.md), [`experiments/p2_main/EXTRACTION_RUBRIC_CDLG_ROLES_EN.md`](experiments/p2_main/EXTRACTION_RUBRIC_CDLG_ROLES_EN.md), [`e4_multiperspective/code/EXTRACTION_RUBRIC_E4_R5_EN.md`](e4_multiperspective/code/EXTRACTION_RUBRIC_E4_R5_EN.md), vocabulary-free variant [`results/p4_grading/e10_vocab_free/rubric_e10.md`](results/p4_grading/e10_vocab_free/rubric_e10.md) |
| References | [`data/references/`](data/references/) (see [`data/README.md`](data/README.md)); time/resource references in `e4_multiperspective/results/*/cases.csv` |
| Evidence sent to the LLMs | `results/p2_main/evidence/<case_id>.json` (+ `audit/` with label maps and intermediate statistics) |
| Explanations (full API records) | `results/p2_main/runs/<prompt>/<model>/run<k>/<case_id>.{json,md}` |
| Extractions | `results/p2_main/extractions_r5/…`, `results/p2_main/extractions_r5a_cdlg/…` (CDLG roles) |
| Per-case scores | `results/p2_main/scores_*.csv` |
| Ablations, BPI 2017, multi-perspective logs | `results/p3_ablation/<variant>/`, `results/p6_bpi2017/`, `e4_multiperspective/results/` (same structure) |
| Baselines | ProDrift: [`experiments/e1_prodrift/`](experiments/e1_prodrift/), `results/e1_prodrift/`; rule-based interpreter: [`experiments/e2_rule_baseline/`](experiments/e2_rule_baseline/) (`rule-engine-v1` folders under `runs/`) |
| Human grading and extractor checks | `results/p4_grading/` (graders anonymized as GraderA / GraderB) |
| Citation-support check (90 statements, ratings and key) | `results/p4_grading/citation_check_results.csv`; sampling in `experiments/p4_grading/build_citation_check.py`, rating scale in `export_citation_check.py` (the completed rating sheet itself is not included) |
| Aggregates, statistics and figures | `results/p5_stats/` |

Every API record stores the model identifier returned by the provider, request settings, timestamps, token
usage, the SHA-256 of the prompt and of the evidence, and the full response including the reasoning
content. The gateway URL is replaced by a placeholder.

## Evaluation sets

| Set | Cases | Source of the reference |
|---|---|---|
| Ostovar, fragment sizes 3 and 5 (0 / 2.5 / 5% noise) | 78 + 78 changes, 78 no-change pairs | fixed rule on the noise-free logs, cross-checked by a projection criterion ([`experiments/e11a_ostovar_references/`](experiments/e11a_ostovar_references/)) |
| CDLG (Kraus and van der Aa) | 99 scored changes, 50 no-change pairs | drift information shipped with each log |
| Ostovar-Time (injected timing changes) | 78 changes, 26 no-change pairs | known from the injection |
| BPI17-Resource (BPI 2017 with injected resource changes) | 30 changes, 10 no-change pairs | known from the injection |
| BPI Challenge 2017 (real) | 4 change points | qualitative |
| Tuning split (Ostovar sizes 2 and 4) | 156 changes | same rule as sizes 3 and 5 |

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
pip install matplotlib openpyxl pandas   # figures, grading sheets, E4b construction
```

Python ≥ 3.10. Raw logs are not redistributed; download them and set the paths as described in
[`data/README.md`](data/README.md). LLM calls need an OpenAI-compatible endpoint and keys:

```bash
cp .env.example .env   # set PCR_LLM_ENDPOINT, GLM_API_KEY, DEEPSEEK_API_KEY
```

The blind extractor runs Claude through the Claude Code CLI (`claude -p`, model `claude-opus-5-5`, no tools,
empty working directory, JSON schema); see [`src/pcr/extract.py`](src/pcr/extract.py).

## Reproducing the results

**Without any API call.** All tables and figures of Section VII are computed from the archived scores:

```bash
python experiments/p5_stats/aggregate_runs.py       # three-run means, SDs, bootstrap CIs, ablation contrasts
python experiments/p5_stats/method_contrasts.py     # LLM vs rule-based vs ProDrift (paired)
python experiments/p5_stats/mcnemar_all.py
python experiments/p5_stats/run_stability.py
python experiments/p5_stats/llm_step_analyses.py    # token usage, retries, dates per run
python experiments/p5_stats/plot_results_v2.py      # Figs. 2-6 -> results/p5_stats/figures/
python experiments/p5_stats/localization_table.py   # localization and qualified-evidence table (Section VII-D)
```

Scores can be recomputed from the archived extractions:

```bash
python experiments/p2_main/score_p2.py --runs results/p2_main/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC/glm-5.3-flash/run1
python experiments/p2_main/cdlg_roles.py score --runs results/p2_main/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC/glm-5.3-flash/run1
```

**Walkthrough for one configuration (GLM, Ostovar fragment size 3, run 1).**

1. *Evidence (no LLM).* Builds the qualified evidence for every evaluation case with the frozen parameters;
   seeds are derived from the case identifier, so the evidence files are reproduced byte for byte
   (compare `evidence_sha256` in `results/p2_main/cases.csv`).
   ```bash
   python experiments/p2_main/build_p2_cases.py --sets ostovar
   ```
2. *Explanation (paid API calls).*
   ```bash
   python experiments/p2_main/run_p2.py generate --model glm-5.3-flash --sets ostovar3 --dry-run   # inspect first
   python experiments/p2_main/run_p2.py generate --model glm-5.3-flash --sets ostovar3
   ```
3. *Blind extraction (Claude).*
   ```bash
   python experiments/p2_main/run_p2.py extract --runs results/p2_main/runs/INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC/glm-5.3-flash/run1 --sets ostovar3
   ```
4. *Scoring and aggregation.* `score_p2.py` as above, then `aggregate_runs.py`.

Reasoning-mode generation is not deterministic, so a new run differs from the archived one in wording;
the archived runs are the ones reported.

## Experiments

| Folder | Content | Paper |
|---|---|---|
| `e0_parameter_setting` | tuning references, parameter grid and one-at-a-time sensitivity on the tuning split | V-C, Appendix B |
| `p0_evidence_v2` | permutation reference, tie rule, variants of evidence qualification | IV |
| `p0_llm_calibration` | prompt and rubric calibration on the tuning split (before the frozen runs) | V-D |
| `e11a_ostovar_references` | Ostovar references for sizes other than 3 | V-B |
| `e12_cdlg_tuning` | check of a CDLG-specific parameter selection (no LLM) | not reported |
| `e1_prodrift` | ProDrift 2.5 baseline | V-E, VII-A |
| `e2_rule_baseline` | rule-based interpreter | V-E, VII-A |
| `p2_main` | main runs: evidence, generation, extraction, scoring | VII-A to VII-C, VII-E |
| `p3_ablation` | ablations (no qualification, family removal, original labels, shuffled order, …) | VII-D |
| `p4_grading` | two human graders vs extractor, repeated and vocabulary-free extraction (Claude) | V-F, VII-E |
| `p5_stats` | aggregation, statistics, figures | VII |
| `p6_bpi2017` | BPI Challenge 2017 | VII-B |
| `e4_multiperspective` | Ostovar-Time and BPI 2017 resource injections | V-A, VII-B |

Some script docstrings refer to internal working notes (`docs/*_VI.md`) that are not part of this
repository; the decisions they record are stated in the paper. The grader instructions generated by
`experiments/p4_grading/build_e11b_package.py` are in Vietnamese, the graders' working language.

## Conventions

- Scripts read inputs and write only to `results/<experiment>/`; references and version-1 material are never modified.
- Scripts that call a paid API say so in their docstring and support `--dry-run` where applicable.
- Activity names are replaced by anonymous codes (A01, A02, …) before any LLM call; label maps are in `audit/`.
