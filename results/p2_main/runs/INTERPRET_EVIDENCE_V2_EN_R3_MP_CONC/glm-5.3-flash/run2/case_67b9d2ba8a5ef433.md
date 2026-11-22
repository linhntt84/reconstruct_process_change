### Observed differences

- Activity A01 did not appear in the earlier window (0 of 200 traces) but is executed exactly once in every case in the later window (200 of 200 traces, mean 1.0 occurrence per trace), at a median event position of about 0.83, i.e. roughly 83% of the way through the trace. [OCC001, POS001]
- In the earlier window, A05 and A07 each passed on to A03 in roughly half of their observed outgoing transitions (A05: to A07 about 52 in 100 and to A03 about 48 in 100; A07: to A03 about 52 in 100 and to A05 about 48 in 100). In the later window, those transitions to A03 are replaced by transitions to A01 (A05: to A01 about 47 in 100 and to A07 about 53 in 100; A07: to A01 about 53 in 100 and to A05 about 47 in 100). [DIR002, DIR003]
- In the later window, A01's only observed outgoing transition leads to A03 (100 in 100), and A01 precedes A03 in every case; in the earlier window, A03 always occurred without A01. [DIR001, REL001]
- A05 and A07 now co-occur with A01 and precede it in 100 in 100 later-window cases, whereas they never co-occurred with A01 in the earlier window. [REL002, REL003]
- The step distance from A05 and A07 to A03 grew by about one step: A05 reached A03 within 1–2 steps before versus 2–3 steps after, and A07 within 1–2 steps before versus 2–3 steps after. [LAG001, LAG002]
- A05 and A07 now sit slightly earlier relative to trace length (mean event position about 0.70 before versus about 0.58 after). [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 now executes once in every case between the A05/A07 stage and A03: cases that previously moved from A05 or A07 directly on to A03 now reach A03 through A01, which is in turn always followed by A03. The placement is shown directly by the outgoing-transition profiles of A05 and A07 and by the relation items (A01 before A03 always; A05 and A07 before A01 always), and the one-step increase in the A05/A07-to-A03 distances is consistent with A01 sitting in between. Twelve evidence items qualified against an expectation of about 0.06 items without change, far beyond what an unchanged process typically produces, and each difference is larger than in about 995 of 1000 random re-splits of the pooled traces. Limitations: zero participation in the earlier window strictly means only that A01 was not observed there, so the evidence cannot distinguish a genuinely new activity from an optional one that simply never occurred before; and the routing into A01 (about 47 and 53 in 100 from A05 and A07 respectively) is observed only as outgoing-transition shares, so the exact path through the A05–A07 loop into A01 is inferred rather than traced case by case. [OCC001, DIR001, DIR002, DIR003, REL001, REL002, REL003, LAG001, LAG002]

Other differences: none beyond the above; the small shifts in the A05–A07 shares (about 1 in 100) are minor and consistent with the same structure. [DIR002, DIR003]