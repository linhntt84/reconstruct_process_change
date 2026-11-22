### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces); in the later window it executes exactly once in every trace (200 of 200, mean 1.0 occurrence per trace, no repetitions within a trace). [OCC001]
- The relationship between A01 and A04 changed completely: earlier, the two never shared a trace (A04 appeared without A01 in 100% of traces); in the later window they co-occur in 100% of traces, always with A04 before A01. [REL001]
- In the later window, all observed outgoing transitions of A04 lead to A01; in the earlier window, no outgoing transitions of A04 were observed at all, which is consistent with A04 ending the trace. [DIR001]
- A04's mean relative position moved from 1.0 (the final position in every earlier trace) to 0.75 (about three-quarters through the trace), while A01 occupies relative position 1.0 (the final position) in every later trace — a pattern consistent with A01 being appended directly after A04. [POS001, POS002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a step A01 was introduced after A04, or that a step at that point became mandatory. In the earlier window, cases ended with A04: A04 occurred in all 200 traces at the final relative position, A01 was never observed, and A04 had no observed successor. In the later window, every case executes A01 exactly once directly after A04: all of A04's observed outgoing flow goes to A01, A04 precedes A01 in every trace, and A04's relative position shifts from the end of the trace to about three-quarters through while A01 takes the final position. [OCC001, DIR001, POS001, POS002, REL001]

This pattern is unlikely to be sampling noise: 5 evidence items qualified where about 0.02 would be expected for an unchanged process, and each difference exceeds about 199 of 200 random re-splits of the pooled data. The five items nevertheless all describe one underlying difference and are not independent confirmations. An important competing explanation remains: A01 may have existed before but been executed too rarely to appear in 200 traces, so "newly added" cannot be distinguished from "previously rare, now universal"; the evidence also covers only these activities and says nothing about the rest of the process. [OCC001, DIR001, POS001, POS002, REL001]