### Observed differences

- Activity A01 was absent from the earlier window (0 of 200 traces) and appears in every trace of the later window (200 of 200), exactly once per case, at a stable relative event position of about 0.83 of the trace. [OCC001, POS001]
- In the later window, all observed outgoing transitions of A01 go to A03, and A01 precedes A03 in every trace containing both; earlier, A03 always appeared without A01. [DIR001, REL001]
- Earlier, A05 and A07 both ran in every case in no fixed order (about 52/48 between the two orders), and the later of the two led directly to A03: roughly 48 in 100 of A05's outgoing transitions went to A03, and roughly 52 in 100 of A07's. In the later window these direct transitions to A03 are gone: A05 now leads to A01 in about 47 in 100 of its transitions (A07 taking the rest), and A07 leads to A01 in about 53 in 100 (A05 taking the rest). [DIR003, DIR004, REL004]
- In the later window, A01 co-occurs with A05 and with A07 in every trace, with A05 before A01 and A07 before A01 in all cases; earlier, A05 and A07 always appeared without A01. [REL002, REL003]
- The step distance from A05 to A03 and from A07 to A03 grew by one step: earlier mostly 1–2 steps, later mostly 2–3 steps. [LAG001, LAG002]
- The mean relative positions of A05 and A07 moved earlier, from about 0.70 to about 0.58, consistent with one extra event being inserted after them (these are event positions, not clock times). [POS002, POS003]
- The branch at A04 (about 52/48 between A05 and A07) and the mixed ordering of A05 and A07 stayed essentially unchanged; these differences are well within what random re-splits produce (empirical strength about 0.07). [DIR002, REL004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was added as a new step executed once in every case, inserted between the A05/A07 block and A03. In the earlier window a case ran A04, then A05 and A07 in either order, with the second of the pair passing control directly to A03; in the later window the second of A05/A07 instead leads to A01 (about half of the outgoing transitions in each case), and A01 always hands over to A03. [OCC001, DIR001, DIR003, DIR004, REL001, REL002, REL003, LAG001, LAG002]

Supporting signs: the change is shown directly by occurrence, direction, relation, position and distance indicators that all describe the same insertion; eleven of the thirteen items reach the maximum empirical strength (about 0.995), and the two that do not describe stability rather than a competing change. The one-step increase in the A05/A07-to-A03 distances and the earlier relative positions of A05 and A07 match the insertion of exactly one event after them. [OCC001, DIR003, DIR004, LAG001, LAG002, POS002, POS003]

Limitations: zero participation in the earlier window strictly means only that A01 was not observed there, so an extremely rare pre-existing variant cannot be fully excluded, although 0 occurrences in 200 traces bounds it tightly; the evidence also cannot show whether A01 took over work previously performed outside the observed traces, since no other activity disappeared. [OCC001]

Other differences: none beyond the stable items noted above; the A04 branch split and the A05/A07 mixed order are unchanged within chance variation. [DIR002, REL004]