### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces); in the later window it occurs in all 200 traces, exactly once per trace, at a nearly fixed relative position of about 0.83 of the trace. [OCC001, POS001]
- In the later window, A01's only observed outgoing transition goes to A03 (100% of cases); earlier, A01 had no observed transitions because it did not occur. [DIR001]
- Earlier, A05 led to A03 in about 48 in 100 of its observed outgoing transitions and to A07 in about 52 in 100; in the later window the transition to A03 has disappeared, and A05 leads to A01 in about 47 in 100 and to A07 in about 53 in 100. [DIR002]
- Earlier, A07 led to A03 in about 52 in 100 and to A05 in about 48 in 100; in the later window A07 leads to A01 in about 53 in 100 and to A05 in about 47 in 100. [DIR003]
- Earlier, A03, A05 and A07 each occurred without A01 in every trace; in the later window A01 co-occurs with each of them in every trace, always after A05 and A07 and always before A03. [REL001, REL002, REL003]
- The step distance from A05 to A03 grew from 1–2 steps (roughly 48/52) to 2–3 steps (roughly 47/53), and from A07 to A03 from 1–2 steps (roughly 52/48) to 2–3 steps (roughly 53/47) — one extra step on each route, with shares matching the rerouting above. [LAG001, LAG002]
- A05 and A07 now sit slightly earlier in the trace (mean relative position about 0.70 before versus about 0.58–0.59 after), consistent with one extra step being added after them. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new activity, A01, was inserted as a mandatory step immediately before A03: earlier, A05 and A07 reached A03 directly (or after one bounce between A05 and A07), whereas in the later window both reach A03 only through A01, which occurs exactly once in every trace. [DIR001, DIR002, DIR003, OCC001]

The insertion is shown directly and consistently: the direct transitions A05→A03 and A07→A03 disappeared while new transitions to A01 appeared with matching shares; A01 co-occurs with A03, A05 and A07 in all later traces in the order A05/A07 → A01 → A03; and the step distance from A05/A07 to A03 increased by exactly one. [DIR002, DIR003, REL001, REL002, REL003, LAG001, LAG002] The fixed single occurrence and position of A01, together with the slight earlier relative position of A05 and A07, fit the same insertion rather than a separate change. [OCC001, POS001, POS002, POS003] Twelve control-flow items qualified against about 0.06 expected if nothing had changed, so chance sampling cannot account for the ensemble of differences. [screening]

Limitation: zero participation in the earlier window only establishes that A01 was not observed there, so a very rare pre-existing occurrence of A01 cannot be ruled out; the bounce between A05 and A07 itself continued at similar shares, so the surrounding structure appears otherwise unchanged. [OCC001, DIR002, DIR003]