### Observed differences

- In the earlier window, every trace contained the same fixed chain: A05 was always followed by A06, and A06 was always followed by A01. A05 sat at about one-sixth of the trace, A06 at one-third, and A01 at one-half, with A01 two steps after A05. [DIR001, DIR002, REL001, REL002, POS001, POS002, POS003, LAG001]
- In the later window, A06 is no longer observed at all: 0 of 200 traces contain it, down from all 200 (mean occurrences per trace fell from 1.0 to 0.0). [OCC001, POS003]
- In the later window, A05 leads directly to A01: all of A05's outgoing flow goes to A01, whereas before it went entirely to A06; A06's outgoing edge to A01 is likewise unobserved. [DIR001, DIR002]
- A01 and A05 now appear without A06 in essentially all traces: the "A01/A05 without the partner" relation rose from 0 to about 100 in 100 cases, while co-occurrence of A06 with each of them fell from about 100 in 100 to 0. [REL001, REL002]
- The step gap between A05 and A01 narrowed from 2 steps in all traces to 1 step in all traces. [LAG001]
- A01's mean position moved earlier (0.5 to 0.4) and A05's moved slightly later (about 0.17 to 0.2), consistent with each trace containing one event fewer than before. [POS001, POS002]
- Every item's difference exceeds what is seen in roughly 99.5 of 100 random re-splits of the pooled data, and 9 items qualified in total where only about 0.04 would be expected if nothing had changed. [DIR001, DIR002, OCC001, POS001, POS002, POS003, REL001, REL002, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A06 was bypassed: traces that previously executed A05 → A06 → A01 now execute A05 → A01 directly, with A06 no longer executed. The rewiring is shown directly in the routing — A05's outgoing flow moved wholly from A06 to A01 — and is corroborated consistently by A06's disappearance from all 200 later traces, the loss of co-occurrence between A06 and both A01 and A05, and the narrowing of the A05→A01 gap from two steps to one. With 9 items qualified against an expectation of about 0.04 without change, chance sampling cannot account for the pattern as a whole. [DIR001, DIR002, OCC001, REL001, REL002, LAG001, POS003]

Limitations: zero participation shows only that A06 was not observed in the later window, not that it cannot occur; the evidence cannot distinguish complete removal from A06 becoming an optional step that was skipped in all 200 later traces, nor rule out that A06 was replaced rather than simply dropped. The position shifts of A01 and A05 are consequences of the same shortening of the trace, not separate changes. [OCC001, POS001, POS002]

Other differences: none — all items describe the same rewiring around A06.