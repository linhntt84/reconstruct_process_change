### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces); in the later window it occurs exactly once in 119 of 200 traces (about 60 in 100 cases), with no repetitions within a trace. [OCC001]
- In the later window, A01's observed outgoing transitions lead to A03 (about 32 in 100), A10 (about 27), A04 (about 23) and A07 (about 18); in the earlier window A01 had no observed outgoing transitions. [DIR001]
- The successor mixes of A03 and A10 changed accordingly. Earlier, A03 led mostly to A10 (about 45 in 100), A07 (about 29) and A04 (about 26); later, about 34 in 100 of its outgoing transitions go to A01, while those to A07 and A04 shrink to about 12 and 15. Earlier, A10 led mostly to A03 (about 55), A04 (about 25) and A07 (about 20); later, about 39 in 100 go to A01. [DIR002, DIR007]
- A04 and A07 became tied to A01: earlier, A04 appeared without A01 in about 29 in 100 traces and A07 without A01 in about 28; in the later window this never happens, and A01 runs before A04 in about 32 in 100 traces and before A07 in about 28. A01 itself never appears without A03 and without A10 in the later window. [REL002, REL003, REL001, REL004]
- A01 and A03 (likewise A01 and A10) went from never running in the same trace (A03 without A01 in about 56 in 100 traces) to running together in about 60 in 100 traces, in both orders (A01 first about 26, A03/A10 first about 34), so no fixed order separates them. [REL001, REL004]
- Activities after the new step sit later in the trace: A04's median relative position moved from about 0.22 to 0.33, A07's from 0.50 to 0.75, and A10's from 0 to about 0.13, while A01 itself sits early (median about 0.17). [POS001, POS003, POS004, POS005]
- Distances between consecutive activities stretched: A03→A04 was 1–2 steps apart before and is now spread over 1–3 steps, with 3 steps the largest share (about 38 in 100); the same holds for A03→A07, A10→A04 and A10→A07. A03→A10 and A10→A03, previously always adjacent, now show a one-step gap in roughly 30 in 100 cases. [LAG001, LAG002, LAG005, LAG006, LAG003, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 was inserted into the control flow between the A03/A10 region and the activities that follow it. In the earlier window A01 was never observed; in the later window it runs once in about 60 in 100 traces, A03 and A10 now lead to it in roughly a third of their outgoing transitions, and it leads on to A03, A10, A04 and A07. As a result, A04 and A07 no longer occur unless A01 ran before them, and the downstream activities (A04, A07, A10, A03) appear about one position later, with A03/A10-to-successor distances stretching from 1–2 steps to up to 3. [OCC001, DIR001, DIR002, DIR007, REL002, REL003, POS003, POS004, LAG001, LAG002]

This hypothesis is supported directly and consistently: the occurrence, successor, relational, positional and distance indicators all describe the same insertion rather than independent phenomena, and the core items show differences larger than in about 995 of 1000 random re-splits of the pooled traces. [REL001, REL004, POS001, POS005, LAG003, LAG004]

The evidence cannot show whether A01 is a genuinely new activity or one that previously went unobserved, since zero participation only means it did not appear in the earlier sample; nor is the placement uniform, because direct A03→A04 and A03→A07 transitions still occur in a minority of cases, so A01's exact position varies from trace to trace. [OCC001, DIR002, LAG001]

Other differences: A13 occurs slightly less often (31 vs 27 of 200 traces) and A09's successor share shifted mildly from A13 (about 54 in 100) toward A14 (about 51); A07's exits moved slightly from A06 toward A05. These differences are small and within the range that random re-splits of an unchanged process produce. [OCC013, DIR006, DIR004]