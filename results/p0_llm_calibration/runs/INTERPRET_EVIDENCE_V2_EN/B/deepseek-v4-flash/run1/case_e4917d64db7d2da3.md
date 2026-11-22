### Observed differences

- In the later window, activities A19 and A20 appear in about 48% and 52% of traces respectively, each once per trace, whereas they were absent in the earlier window. [OCC001, OCC002]
- A19 and A20 never occur together; almost every trace contains exactly one of them (neither in about 0.5% of traces). [REL001]
- A26, A27 and A28 remain present in every trace in both windows. [REL002, REL003, REL004, REL005, REL006, REL007]
- The outgoing routing of A26 changed: before, about 98% of its transitions went to A27; after, about 47% go to A27, about 24% to A19 and about 27% to A20. [DIR003]
- The outgoing routing of A27 changed: before, about 99% of its transitions went to A28; after, about 51% go to A28, about 24% to A20 and about 23% to A19. [DIR004]
- A19 and A20 lead to A27 and A28: A19 goes to A27 and A28 about 49% each; A20 goes to A28 about 44% and to A27 about 53%. [DIR001, DIR002]
- A19 and A20 appear around the middle of the trace (mean position about 0.51). [POS001, POS002]
- Ordering: A26 precedes A19/A20 in about half of traces; A19/A20 precede A28 in about half; A19/A20 and A27 appear in both orders. [REL002, REL004, REL005, REL007, REL003, REL006]
- Lags: A26-to-A28 shifted from mostly lag 2 to mostly lag 3; A26-to-A27 and A27-to-A28 shifted from mostly lag 1 to a mix of lag 1 and lag 2. [LAG001, LAG002, LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a new alternative step consisting of either A19 or A20 was inserted into the main path between A26/A27 and A28. A26 and A27 now sometimes route to A19 or A20 instead of directly to A27/A28, and A19/A20 then lead to A27 or A28. A19 and A20 are mutually exclusive and each appears in about half of traces, never together. This is directly shown by occurrence, routing, ordering and lag indicators. A competing explanation that these are only sampling differences in variant frequencies is unlikely given the large number of consistent indicators and the absence of A19/A20 in the earlier window, but the evidence cannot rule out that A19/A20 existed but were unobserved before, nor can it identify the cause of the change.