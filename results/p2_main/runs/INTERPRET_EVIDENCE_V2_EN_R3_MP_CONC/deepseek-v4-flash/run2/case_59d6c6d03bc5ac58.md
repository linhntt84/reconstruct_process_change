### Observed differences

- In the earlier window, about 50 in 100 traces started with A01 and then went to A02; the other about 50 started with A04 and then went to A02. A02 was always present, always as the second event. [OCC001, DIR001, DIR002, REL001, REL002, POS002]
- In the later window, A01 no longer occurs; A05 appears in about 46 in 100 traces. A04 now goes to A05 instead of directly to A02, and A05 then goes to A02, so the sequence A04→A05→A02 replaces A04→A02. [OCC001, OCC002, DIR002, DIR003, REL004, REL005, LAG001]
- In the later window, about 54 in 100 traces contain only A02 (no A04 or A05), whereas earlier every trace had either A01 or A04 before A02. [REL002, REL003, REL004, REL005]
- A02's position changed from always second to sometimes first (about half the traces) and sometimes second. [POS002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the process changed from having two alternative start activities (A01 or A04) both followed by A02, to having either A02 alone or a sequence A04→A05→A02. Specifically, A01 was removed, A05 was introduced, and A04 now leads to A05 before A02. This is directly shown by the disappearance of A01, the appearance of A05, the change in A04's successor from A02 to A05, the new A05→A02 edge, and the increase in the gap between A04 and A02 from one to two steps. The number of evidence items (15) far exceeds the chance expectation (0.09), so the overall pattern is unlikely to be a random artefact.

Other differences: The share of traces with a start activity decreased from 100% to 46%, so A02 now sometimes occurs alone. This is a separate change in participation, not part of the main hypothesis.

A competing explanation that cannot be fully ruled out is that the observed differences reflect a rare variant that happened to appear in the later window, but the consistency and volume of evidence make this unlikely.