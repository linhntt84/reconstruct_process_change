# E4a: rule-based interpreter with R09_TWAIT (evaluation set, P2 evidence)

| Type | n | time detected [95% CI] | direction correct | false timing claim |
|---|---|---|---|---|
| T_SLOW | 26 | 0.962 [0.885, 1.000] | 0.962 | 0 |
| T_FAST | 26 | 0.923 [0.808, 1.000] | 0.923 | 0 |
| M | 26 | 0.846 [0.692, 0.962] | 0.846 | 0 |
| all drift | 78 | 0.910 [0.846, 0.974] | 0.910 | 0 |
| N | 26 | 0.000 [0.000, 0.000] | 0.000 | 0 |

| LLM | n | LLM time detected | rule | diff [95% CI] | b / c (majority) | McNemar p |
|---|---|---|---|---|---|---|
| GLM | 78 | 0.893 | 0.910 | -0.017 [-0.081, +0.051] | 4 / 4 | 1 |
| DeepSeek | 78 | 0.932 | 0.910 | +0.021 [-0.047, +0.094] | 6 / 3 | 0.51 |

Missed drift cases: 7; T_WAIT items in them: [(0, 0.01), (1, 0.011), (1, 0.011), (1, 0.012), (1, 0.012), (1, 0.019), (1, 0.027)]
