### Observed differences

- In the later window, activity A01 appears in about 60% of traces (119/200) with a mean of 0.60 occurrences per trace; it was completely absent in the earlier window (0/200). [OCC001, POS001]
- A01 is positioned early: its median relative position is about 0.17 (early in the trace). [POS001]
- A01 has outgoing transitions to A03, A04, A07, and A10 in the later window; these transitions did not exist before. [DIR001]
- A03's outgoing transitions were redistributed: before, A03 went to A07 (29%), A10 (45%), A04 (26%); after, it goes to A10 (39%), A01 (34%), A07 (12%), A04 (15%). A01 is a new successor, while A07 and A04 shares drop. [DIR002]
- A10's outgoing transitions similarly: before to A03 (55%), A07 (20%), A04 (25%); after to A01 (39%), A04 (15%), A03 (29%), A07 (17%). [DIR003]
- A01 co-occurs with A03, A04, A07, A10 in the later window (about 60% for A03 and A10, 32% for A04, 28% for A07); before, A01 was absent and these activities occurred alone. [REL001, REL002, REL003, REL004]
- A01 always precedes A04 and A07 when they co-occur (A_before_B 100% of co-occurrences), but with A03 and A10 both orders occur (A_before_B 43% and 43% respectively, B_before_A 57% and 57%). [REL001, REL002, REL003, REL004]
- The distance between A03 and A04, A03 and A07, and A10 and A04 increased: before, they were 1–2 steps apart; after, a third of the cases are 3 steps apart. [LAG001, LAG002, LAG005]
- The distance between A03 and A10 increased from always 1 step to 2 steps in about 29–36% of cases. [LAG003, LAG004]
- A04 and A07 shifted later in the trace: A04's mean position from 0.22 to 0.31, A07's from 0.57 to 0.68. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new activity A01 was added to the process, occurring in about 60% of traces, typically early, before A04 and A07, and with mixed order relative to A03 and A10. This insertion pushes A04, A07, and A10 to later positions. The evidence is direct: A01 appears only in the later window, has outgoing transitions to the other activities, co-occurs with them, and precedes A04/A07 consistently. The screening comparison (17 items vs 0.19 expected) rules out chance as a whole. A competing explanation that A01 existed but was unobserved before is unlikely given its high frequency and the systematic changes in positions and lags.

Other differences: The order between A01 and A03/A10 is not fixed; both orders occur, so A01 is not strictly a new first step for all cases. The increased lag between A03 and A10 suggests A01 may be inserted between them in some cases, but this is part of the same insertion effect. No time or resource changes were reported.