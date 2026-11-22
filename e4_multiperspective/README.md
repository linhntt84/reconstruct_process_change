# E4 — Multi-perspective changes (time, resource)

| Folder | Content |
|---|---|
| `code/e4_common.py` | shared helpers (reading logs with timestamps and resources) |
| `code/pipeline_mp.py`, `code/config_time.json`, `code/config_org.json` | pipeline v2 extended with the temporal (TWAIT) and resource-allocation families (control flow calls `pcr.pipeline.build_evidence` unchanged) and their frozen parameters; earlier candidate configurations are kept as `config_*_v*.json` |
| `code/e4a_time_injection/` | Ostovar-Time: timing changes injected into Ostovar logs (README inside) |
| `code/e4b_resource_injection/` | BPI17-Resource: resource changes (reassignment, handover, concentration) injected into BPI Challenge 2017 |
| `code/prompts/` | interpretation prompts; `INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC.md` is the frozen prompt of every reported run; `.diff` files show the changes between versions |
| `code/EXTRACTION_RUBRIC_E4_R*_EN.md`, `code/extract_e4.py` | extraction rubrics and the blind extractor (rubric r5 used in the main runs) |
| `results/e4a_time_injection/`, `results/e4b_resource_injection/` | cases (`cases.csv` = references), evidence, runs, extractions and scores |

The E4 code imports `src/pcr/` and does not modify it. Run every command from the repository root, e.g.
`python e4_multiperspective/code/e4a_time_injection/build_e4a.py`.
