### Observed differences

- A03 occurred in all 200 traces before and in none after; A07 occurred in none before and in all 200 traces after. [OCC001, OCC002]
- A04's outgoing transition changed from A01 in 99% of cases (and A03 in 1%) to A07 in 100% of cases; A07's outgoing transition, absent before, is A01 in 100% of cases after. [DIR002, DIR003]
- A02's mean position moved from 0.215 to 0.0 (first event); A04's mean position moved from 0.746 to 0.5; A07 appears at mean position 0.75. [POS001, POS003, POS004]
- A03 and A04 co-occurred in all traces before, with A03 before A04 in 98.5% of traces; after, A03 is absent and A04 precedes A07 in all traces. [REL005, REL007]
- The lag between A04 and A01 changed from 1 step in 99% of traces to 2 steps in 100% of traces. [LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow structure: the earlier path A03 → A02 → A04 → A01 (with A03 also branching to A05/A06) was replaced by A02 → A04 → A07 → A01. A03 disappeared entirely, A07 was introduced as a new step between A04 and A01, and A04's successor changed from A01 to A07. This is directly shown by the complete disappearance of A03, the appearance of A07 in every trace, the successor changes for A04 and A07, and the increased lag between A04 and A01. The screening comparison (19 items vs 0.13 expected by chance) rules out random fluctuation. A competing explanation that the two windows simply contain different process variants is unlikely because every trace in each window shows the same pattern, but the evidence cannot exclude that the change was gradual or that other unobserved activities are involved.

Other differences: The outgoing transitions from A03 to A05 and A06 (about 5% each) disappear along with A03. [DIR001]