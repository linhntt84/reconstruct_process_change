### Observed differences

- Activity A02 became much more frequent: it appears in about 15% of traces before and 65% after, and its mean position moved from about 0.53 to 0.20 (earlier in the trace). [OCC001, POS001]
- Activities A06 and A10 became less frequent: A06 fell from about 22% to 5% of traces, A10 from about 17% to 6%. [OCC002, OCC003]
- A02's outgoing behaviour changed: before it led to many different activities (A16, A46, A22, etc.), after it leads to A15 in about 87% of its transitions. [DIR001]
- A14's outgoing behaviour changed: before it led mostly to A15 (about 84%), after it leads mostly to A02 (about 60%) and A15 (about 37%). [DIR004]
- A19, A21 and A24 changed their main successor from A30 to A25 (e.g., A19: A30 in 97% before, A25 in 98% after). [DIR005, DIR007, DIR010]
- A29's main successors changed from A21/A19/A24 to A20/A23/A22; A40's main successors changed from A22/A20/A23 to A19/A21/A24. [DIR011, DIR012]
- Order relations changed: A02 now precedes many activities it previously followed or was interleaved with (e.g., A02 before A20: 7.5% before, 58.5% after; A02 before A15: 1% before, 33% after). [REL004, REL002]
- A19, A21 and A24 moved from after to before A20/A22/A23 (e.g., A19 before A20: 0% before, 42.5% after; A21 before A22: 0.5% before, 28% after). [REL015, REL024]
- The order between A20/A22/A23 and A25/A29 reversed: before, A20 preceded A25 in about 99% of traces; after, A25 precedes A20 in about 98%. [REL022, REL029, REL032]
- A29 and A30 moved from being 2 steps apart to 4 steps apart. [LAG019]

### Inference

Support level: Supported hypothesis

The evidence supports a change in which activity A02 became a much more frequent and earlier step, and the ordering of several activities changed: A19, A21 and A24 moved earlier relative to A20/A22/A23, and the order between A20/A22/A23 and A25/A29 reversed. These changes are directly shown by participation, position, successor and order-relation indicators, and the number of qualifying items (87) far exceeds the 1 expected by chance for the control-flow family. [OCC001, POS001, DIR001, DIR004, REL004, REL015, REL022, REL029, REL032, screening.by_family.control_flow]

Other differences: A06 and A10 became less frequent; A14's main successor shifted from A15 to A02; A29 and A40 changed their successor sets; A29 and A30 moved further apart. [OCC002, OCC003, DIR004, DIR011, DIR012, LAG019]

A competing explanation that cannot be fully ruled out is that some of the order changes are driven by the large increase in A02 participation, which may have pulled other activities into new relative positions without a separate reordering of those activities. However, the reversal between A20/A22/A23 and A25/A29 is independent of A02 and is based on full support in both windows. [REL022, REL029, REL032]