### Observed differences

- In the later window, activity A14 appears in about 47% of traces (up from 23%) and A15 in about 53% (up from 21.5%). [OCC001, OCC002]
- The outgoing transitions of A35 changed: before, about 56% went to A20, 23% to A14, and 21% to A15; after, none go to A20, about 47% go to A14 and 53% to A15. [DIR001]
- A14 and A15 are mutually exclusive: before, about 56% of traces had neither; after, every trace has exactly one of them (47% A14 only, 53% A15 only, 0% both). [REL001]
- The distance between A35 and A20 shifted: before, about 56% were 1 step apart and 44% were 2 steps apart; after, all are 2 steps apart. [LAG001]
- A14 before A20 increased from 23% to 47% of traces; A15 before A20 increased from 21.5% to 53%. [REL002, REL005]
- A35 before A14 increased from 23% to 47%; A35 before A15 increased from 21.5% to 53%. [REL003, REL006]
- A15 and A18 co-occurrence increased from 8.5% to 21%, with A15 alone increasing and A18 alone decreasing. [REL004]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that, in the later window, the process routes A35 to either A14 or A15 (mutually exclusive alternatives) and then to A20, instead of sometimes going directly from A35 to A20. This is directly shown by the disappearance of the A35→A20 edge, the increase in A35→A14 and A35→A15, the increase in A14→A20 and A15→A20, and the shift in the A35–A20 distance from 1 to 2 steps. The mutual exclusivity of A14 and A15 indicates a choice between them. The number of evidence items (10) far exceeds the 0.34 expected by chance, and the items are consistent across directional, relational, and lag indicators. A competing explanation of mere sampling variation in variant frequencies is unlikely given the size and coherence of the changes, though the evidence cannot rule out that some other unobserved mechanism produces the same trace pattern.