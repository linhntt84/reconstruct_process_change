### Observed differences

- In the earlier window, about half of the cases (101 of 200) executed A01, always as the first activity, and every such case was followed by A02; the other half (99 cases) executed A04, also followed by A02. A05 never occurred. [OCC001, OCC002, DIR001, DIR002, REL001, REL002, REL003, REL004, REL005, POS001, POS002, POS003, POS004, LAG001]
- In the later window, A01 is absent (0 of 200), while A05 appears in 92 of 200 cases (46%). [OCC001, OCC002, POS001, POS004]
- A04's successor changed: before, A04 always led to A02; after, A04 always leads to A05, and A05 then leads to A02. [DIR002, DIR003, LAG001]
- A04 and A05 now co-occur in 46% of cases, with A04 before A05; before they never co-occurred. [REL005]
- A02's position changed: before it was always the second event; after, it is the first event in about 54% of cases and later in the remaining 46%. [POS002, REL004]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in the control flow: the process moved from a pattern where each case executed either A01 or A04, followed by A02, to a pattern where A01 is no longer executed, A05 is newly executed, and A04 now precedes A05 which precedes A02, while about half of the cases execute only A02. This is directly shown by the disappearance of A01, the appearance of A05, the change of A04's successor from A02 to A05, the new A05→A02 edge, and the lag change for A04→A02 from 1 to 2. The number of evidence items (15) far exceeds the 0.09 expected by chance, so this is not a sampling artifact.

Other differences: A02's position shifted from always second to sometimes first, consistent with the new structure where A02 can be the only activity. A04's position also shifted slightly.

Limitation: The evidence is based on 200 traces per window; the support for A01 before is 101, but its absence after is clear. No competing explanation is apparent.