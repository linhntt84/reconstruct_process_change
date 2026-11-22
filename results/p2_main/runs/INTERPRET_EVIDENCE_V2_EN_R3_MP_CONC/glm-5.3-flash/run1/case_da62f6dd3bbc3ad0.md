### Observed differences

- Earlier, of the observed outgoing transitions from A38, about 53 in 100 went to A14 and about 47 in 100 went directly to A23; in the later window, every observed outgoing transition from A38 goes to A14 [DIR001].
- A14 and A15 each ran in about 53 in 100 traces earlier (exactly once per trace when present); in the later window both run exactly once in every trace [OCC001, OCC002].
- Earlier, A23 ran without A14 and without A15 in about 48 in 100 traces; in the later window A23 always co-occurs with A14 and A15 and always follows them, and A38 always precedes A14 and A15 [REL005, REL010, REL001, REL006, REL011].
- The A38–A23 gap was one step in about 48 in 100 traces earlier and 4–5 steps apart otherwise; in the later window it is always 4–5 steps apart, with the 4-step and 5-step shares (about 48 and 53 in 100) matching the A22 and A20+A21 route shares [LAG001, OCC005, OCC003].
- A20 and A21 rose from about 33 to about 53 in 100 traces and A22 from about 20 to about 48 in 100; in both windows A20 and A21 never occur together with A22, and the three participations sum to A14's, so a choice between an A20+A21 route and an A22 route persists [OCC003, OCC004, OCC005, REL012, REL013].
- Minor: A23's median event position moved slightly later (about 0.41 to 0.45 of trace length) and A38's slightly earlier (about 0.32 to 0.29); these are event positions, not clock times [POS001, POS002].

### Inference

Support level: Supported hypothesis

The 24 flagged control-flow items are many times the roughly 0.42 expected without a change for the 85 tested units, so chance cannot account for the ensemble, and every item's difference exceeds about 995 in 1000 random re-splits of the pooled traces [OCC001, DIR001, REL001, LAG001].

The evidence supports the possibility that the direct route from A38 to A23 is no longer taken: in the later window every case runs A38, then A14, then either A20 together with A21 or A22, then A15, and finally A23, whereas earlier about 47 in 100 cases went from A38 straight to A23, skipping A14, A15, A20, A21 and A22 — A14 and A15 changed from optional to mandatory, and A23 is now always reached after them. The successor change at A38 is observed directly, A23 moved from often running without A14/A15 to always following them, A38 now always precedes A14/A15, the A38–A23 gap grew from one step to 4–5 steps, and all participation changes fit this structure [DIR001, REL005, REL010, REL006, REL011, LAG001, OCC001, OCC002, OCC003, OCC004, OCC005].

Limitations: non-observation of the direct route in the later window shows only that it does not appear in these 200 traces, so a rarely used remaining bypass cannot be excluded; the always-joint execution of A20 and A21 is inferred from participation arithmetic, since no relational item covers that pair [OCC003, OCC004, OCC005, REL012, REL013].

Other differences: within the now-mandatory branch, the A22 route's share appears to have grown from about 37 to about 47 in 100 branch cases (A22 in 39 vs 95 traces; A20/A21 in 66 vs 105), but these counts are moderate and a sampling explanation cannot be ruled out; the small positional shifts of A23 and A38 are consistent with the structural change but add little independent weight, and many items describe the same traces rather than independent confirmations [OCC003, OCC004, OCC005, REL012, REL013, POS001, POS002].