### Observed differences

- In the earlier window, activity A01 never occurred (0% of traces); in the later window it occurs in all 200 traces, exactly once per trace. [OCC001]
- In the earlier window, A05's outgoing transitions all went to A06; in the later window they all go to A01. [DIR002]
- In the earlier window, A01 had no outgoing transitions (since it was absent); in the later window all its outgoing transitions go to A06. [DIR001]
- The relative position of A05 moved earlier (from 0.5 to 0.4 of the trace), and A06 moved later (from 0.75 to 0.8); A01 appears at position 0.6. [POS002, POS003, POS001]
- In the earlier window, A05 and A06 co-occurred in all traces with A06 immediately after A05 (lag 1); in the later window they still co-occur but with A06 two steps after A05 (lag 2). [LAG001]
- In the earlier window, A01 did not co-occur with A05 or A06; in the later window A05 occurs before A01 and A01 before A06 in all traces. [REL001, REL002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new activity A01 was inserted between A05 and A06, changing the sequence from A05 → A06 to A05 → A01 → A06. The insertion is complete: A01 appears in every trace, all outgoing edges of A05 now lead to A01, and all outgoing edges of A01 lead to A06. The positional shifts (A05 earlier, A06 later) and the increase in lag between A05 and A06 from 1 to 2 are exactly what this insertion predicts. The screening expected only 0.04 items by chance, but 9 items were found, so the overall difference is not a sampling artefact. No competing explanation is plausible given the direct successor and lag evidence. A limitation is that the evidence is based on 200 traces per window, but the change is uniform across all traces.