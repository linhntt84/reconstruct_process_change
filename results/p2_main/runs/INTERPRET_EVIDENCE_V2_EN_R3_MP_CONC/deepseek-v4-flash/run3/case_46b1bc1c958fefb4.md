### Observed differences

- In the later window, activity A01 appears in about 50% of traces (101 of 200) and activity A02 disappears (from 46% to 0%). [OCC001, OCC002]
- A01's outgoing transitions are observed only in the later window, while A02's outgoing transitions are observed only in the earlier window. [DIR001, DIR002]
- A01 and A02 never co-occur; before only A02 was present, after only A01. [REL001]
- A01 now co-occurs with A03 in about half the traces (50.5%), with mixed order (A01 before A03 in 5%, A03 before A01 in 20%, interleaved in 25.5%); before A03 was always present and A02 co-occurred with A03 in 46% of traces. [REL002, REL004]
- A01 and A06 now co-occur in about 25% of traces, whereas before A06 was present without A01 (53% alone). [REL003, REL005]
- A03's outgoing routing changed: A01 becomes a successor (8% of transitions), A02 disappears as successor, A10 increases (from 32% to 37%) and A11 decreases (from 24% to 19%). [DIR003]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process replaced activity A02 with activity A01 in about half of the cases. In the earlier window, A02 was executed in 46% of traces and A03 was always present; in the later window, A01 is executed in 50.5% of traces, A02 is absent, and A03 remains always present. A01's appearance is accompanied by new outgoing transitions from A03 to A01 and by co-occurrence of A01 with A03 and A06. The main limitation is that we cannot tell whether A01 is a renamed A02 or a genuinely different activity, but the behavioural swap is clear.

Other differences: A03's outgoing distribution shifted (A10 increased, A11 decreased) and A01 and A06 now co-occur, which may be part of the same change or independent.