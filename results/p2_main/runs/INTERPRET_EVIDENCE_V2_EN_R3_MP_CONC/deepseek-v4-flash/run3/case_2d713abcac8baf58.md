### Observed differences

- In the earlier window, activities A19, A20 and A21 each occurred in about 30–36% of traces (70, 60 and 72 of 200 traces respectively) and were mutually exclusive alternatives (co-occurrence below 1%). In the later window, each occurs in at most 1% of traces (2, 1 and 1 of 200). [OCC001, OCC002, OCC003, REL001, REL002, REL008]
- Activities A26, A27 and A28 were absent in the earlier window (0 of 200 traces). In the later window, each occurs in all 200 traces, with a mean of about 1.0 occurrences per trace. [OCC004, OCC005, OCC006]
- Activity A44's outgoing transitions changed: before it led mainly to A19 (30.5%), A21 (30%) and A20 (24.5%); after it leads mainly to A26 (31.3%), A27 (27.4%) and A28 (26.4%). [DIR007]
- Activity A29 was preceded by A19, A20 or A21 in about 30–36% of traces before; after, it is preceded by A26, A27 or A28 in about 98–99% of traces, and the old activities are almost absent. [REL006, REL012, REL017, REL021, REL024, REL026]
- The lag between A44 and A29 shifted: before, 83.5% of traces had a lag of 2 steps and 16% a lag of 3; after, 81.6% have a lag of 4 and 18.4% a lag of 5. [LAG001]
- A26, A27 and A28 now co-occur with each other in all traces, with no fixed order (about half in each order). [REL019, REL020, REL023]
- A29's position shifted slightly later (mean from 0.40 to 0.44 of the trace). [POS007]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change: the process moved from a branch where one of A19, A20 or A21 was executed (each in about a third of traces) to a mandatory block of activities A26, A27 and A28, which are now executed in every trace and in no fixed order. A44 now leads to the new block instead of the old alternatives, and A29 still follows, now after the new block, which is consistent with the increased lag from A44 to A29. The number of qualifying items (48) far exceeds the 0.65 expected by chance, and the changes are directly observed in occurrence, routing, relations and lag. A competing explanation that the old activities were simply renamed is unlikely because the new activities co-occur with each other while the old ones were alternatives, and the new block is mandatory whereas the old ones were optional.

Other differences: A29's position shifted slightly later, and the new activities are executed together without a fixed order.