# E11b: agreement between graders and the Claude extractor

| Pair | n | κ support | κ mechanism | κ pattern | central exact | central Jaccard | κ time_dir | κ CDLG class | CDLG objects exact | scores identical | weighted κ PI |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude – Claude_repeat | 100 | 1.00 | 0.99 | 0.99 | 0.96 | 0.99 | 0.96 | 0.94 | 0.96 | 0.97 | 0.94 |
| Claude – GraderB | 100 | 1.00 | 0.88 | 0.81 | 0.88 | 0.96 | 0.96 | 0.77 | 0.75 | 0.86 | 0.73 |
| Claude – GraderA | 100 | 1.00 | 0.93 | 0.87 | 0.88 | 0.97 | 0.96 | 0.73 | 0.71 | 0.83 | 0.82 |
| Claude_repeat – GraderB | 100 | 1.00 | 0.87 | 0.80 | 0.87 | 0.95 | 0.91 | 0.83 | 0.75 | 0.84 | 0.71 |
| Claude_repeat – GraderA | 100 | 1.00 | 0.92 | 0.86 | 0.87 | 0.96 | 0.91 | 0.68 | 0.71 | 0.82 | 0.79 |
| GraderB – GraderA | 100 | 1.00 | 0.92 | 0.89 | 0.86 | 0.95 | 1.00 | 0.62 | 0.71 | 0.84 | 0.74 |

Scores identical = every metric of the case (see score_e11b.scores) equal under both extractions.
Weighted κ PI over the cases with a PI score (Ostovar, CDLG, E4a drift).
