# E12: CDLG-specific parameter selection (no LLM)

Tuning: 288 changes / 100 no-change pairs; evaluation: 99 / 50.
Feasible configurations on CDLG tuning: 80 of 320; frozen v2 feasible: False.

| Config | tau | tau_loc | eps_loc | eps_rel | Split | A* recall | |A*| | Coverage | Full cov. | Median |E*| | Null |E*| | Null nonempty |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| frozen v2 (Ostovar tuning) | 0.995 | 0.995 | 0.1 | 0.2 | tuning | 0.927 | 5.5 | 0.973 | 0.931 | 16.0 | 0.11 | 0.09 |
| frozen v2 (Ostovar tuning) | 0.995 | 0.995 | 0.1 | 0.2 | evaluation | 0.942 | 5.6 | 0.979 | 0.939 | 17 | 0.12 | 0.06 |
| selected on CDLG tuning | 0.995 | 0.995 | 0.05 | 0.2 | tuning | 0.961 | 6.1 | 0.981 | 0.944 | 18.0 | 0.12 | 0.1 |
| selected on CDLG tuning | 0.995 | 0.995 | 0.05 | 0.2 | evaluation | 0.977 | 6.3 | 0.985 | 0.96 | 20 | 0.12 | 0.06 |
| max recall on CDLG tuning | 0.9 | 0.95 | 0.05 | 0.15 | tuning | 0.966 | 6.5 | 0.985 | 0.965 | 25.0 | 2.41 | 0.46 |
| max recall on CDLG tuning | 0.9 | 0.95 | 0.05 | 0.15 | evaluation | 0.979 | 6.7 | 0.992 | 0.98 | 27 | 2.18 | 0.54 |
