### Observed differences

- In the earlier window, every trace contained only activity A04; no other activity was observed. In the later window, every trace contains both A04 and A01, with A01 occurring exactly once per trace. [OCC001, REL001]
- In the earlier window, A04 had no observed outgoing transitions; in the later window, all outgoing transitions of A04 lead to A01. [DIR001]
- In the earlier window, A01 was absent; in the later window, A01 appears in 100% of traces and is positioned at the end of the trace. [OCC001, POS001]
- In the earlier window, A04 was the only activity and thus occupied the sole position; in the later window, A04 occurs before A01 in every trace. [POS002, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change: the process changed from executing only activity A04 to executing A04 followed by A01. In the earlier window, each trace consisted solely of A04; in the later window, each trace consists of A04 then A01, with A01 as the final activity. This is directly shown by the complete appearance of A01 (0% to 100% participation), the new outgoing transition from A04 to A01, the consistent ordering (A04 before A01), and the shift in A04's position relative to the added activity. The number of qualifying evidence items (5) far exceeds the 0.02 expected by chance, and all items point to the same single change. A competing explanation of a rare variant is ruled out by the complete and consistent shift across all 200 traces in each window. No other differences are indicated.