### Observed differences

- Activity A01 was not observed in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200, mean 1.0 occurrence per trace, no repetitions). [OCC001]
- In the later window, A01 always sits at the final position of the trace (relative position 1.0 in every case); it had no position in the earlier window because it never occurred. [POS001]
- Activity A04 is present in every trace in both windows, but its position shifted: it sat at the end of the trace in the earlier window (relative position 1.0 in all 200 traces) and at about three-quarters of the trace in the later window (0.75 in all 200 traces, with no spread). [POS002]
- In the earlier window, no outgoing transitions of A04 were observed, which fits A04 ending the trace; in the later window, all 200 observed outgoing transitions of A04 lead to A01. [DIR001]
- Taken together: in the earlier window, 200 of 200 traces contained A04 without A01; in the later window, 200 of 200 contain both activities, always in the order A04 before A01. [REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, every case executes a step A01 after A04, so that A04 — previously the closing step of the trace — is now systematically followed by A01 as the final step. The signs are direct and mutually consistent: A01's participation rose from 0 to 200 of 200 traces with exactly one occurrence per case; the A01–A04 relation changed from "A04 only" in all earlier traces to co-occurrence with A04 first in all later traces; A04's entire observed outgoing flow now leads to A01; and the positions match, with A04 moving from the end to about three-quarters of the trace while A01 takes the end position. [OCC001, REL001, DIR001, POS001, POS002]

The volume of qualifying evidence also far exceeds what an unchanged process typically produces: 5 control-flow items qualified where roughly 0.02 (about 1 in 50) were expected by chance, and all five items describe this one underlying difference, so they should be read as a single coherent signal rather than independent confirmations. [OCC001, DIR001, POS001, POS002, REL001]

An important competing explanation remains: zero participation in the earlier window only means A01 was not observed there, so a step that was too rare to appear in 200 traces and later became universal is indistinguishable from a genuinely added step. Likewise, the empty outgoing profile of A04 in the earlier window is consistent with, but does not prove, that A04 had no successor before. [OCC001, DIR001]