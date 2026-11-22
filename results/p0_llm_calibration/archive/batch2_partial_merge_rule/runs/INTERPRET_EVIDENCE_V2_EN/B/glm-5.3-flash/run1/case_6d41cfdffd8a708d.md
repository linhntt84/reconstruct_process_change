### Observed differences

- In the later window, A14, A15, A20 and A21 are almost never executed: each took part in roughly 23–26 in 100 traces before (46–52 of 200 traces) but in at most about 1 in 100 afterwards (0–2 of 200). [OCC001, OCC002, OCC003, OCC004]
- Before, these four were mutually exclusive alternatives whose participation shares sum to about 100 in 100 traces, so exactly one of them ran in almost every before-window trace; afterwards about 99 in 100 traces contain none of them. [OCC001, OCC002, OCC003, OCC004, REL001, REL008, REL012]
- Whenever one of the four ran, it always ran together with A23, A24 and A25, positioned after A23 and before A25 — placing the block between them. [REL004, REL006, REL009, REL011, REL013, REL015, REL016, REL018]
- Routing concentrated on the direct path: A23 previously led to A24 in about 50 in 100 of its outgoing transitions and to one of the four activities in the other half, and now leads to A24 in about 995 in 100; A24 previously led to A25 in about 50 in 100 and to the four activities otherwise, and now leads to A25 in about 99 in 100. [DIR005, DIR006]
- The A23-to-A25 path shortened by one step: A23 is now followed by A24 at distance 1 in about 995 in 100 cases (about half before), A24 is followed by A25 at distance 1 in about 99 in 100 cases (about half before), and A23 reaches A25 in 2 steps in about 985 in 100 cases instead of 3 steps in essentially all cases. [LAG005, LAG007, LAG006]
- A25 still occurs in every trace in both windows, at a slightly earlier relative position (mean about 0.56 before, 0.55 after). [POS005]
- The after-window successor, position and lag profiles of the four activities themselves rest on 0–2 observations each and carry little weight on their own. [DIR001, DIR002, DIR003, DIR004, POS001, POS002, POS003, POS004, LAG001, LAG002, LAG003, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the block of four alternative activities A14, A15, A20 and A21 — of which exactly one was executed in almost every before-window trace, between A23/A24 and A25 — is no longer executed in the later window, leaving the direct sequence A23 → A24 → A25. This is a possibility supported by the evidence, not a confirmed modification. [OCC001, OCC002, OCC003, OCC004, DIR005, DIR006, LAG005, LAG006, LAG007]

Supporting signs: the participation collapse (from about 50 of 200 traces per activity down to 0–2) is far beyond what sampling variation between 200-trace windows would produce, and each difference here exceeds the differences seen in about 199 of 200 random re-splits of the pooled traces; the routing and distance changes were observed directly on all 200 traces per window and match exactly what not executing one intermediate step between A23 and A25 would produce; grouped into distinct differences (the block's near-disappearance, and the tightening of the A23–A25 path in routing and distance), the evidence clearly exceeds the 0.43 items expected for an unchanged process. [OCC001, OCC002, OCC003, OCC004, DIR005, DIR006, LAG005, LAG006, LAG007]

Limitations: the evidence cannot distinguish a genuine removal of this branch from a shift in the mix of trace variants, in which the later window happens to contain only cases that never took the optional block; the after-window behaviour of the four activities themselves rests on 0–2 observations; and distances are measured in event positions, so the shortening is in steps, not clock time. [DIR001, DIR002, DIR003, DIR004, LAG001, LAG002, LAG003, LAG004, LAG005, LAG006, LAG007]