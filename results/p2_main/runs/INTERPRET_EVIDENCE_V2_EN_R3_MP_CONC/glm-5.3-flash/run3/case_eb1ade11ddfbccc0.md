### Observed differences

- Activity A03 dropped out of execution. In the earlier window it ran exactly once in every trace (200 in 200), usually as the first event (median position 0), and its outgoing transitions went mostly to A02 (about 86 in 100), with small shares to A06, A05, A04 and A01. In the later window A03 does not appear in a single one of the 200 traces. [OCC001, POS002, DIR001]
- Activity A07 appeared. Before, it was not observed at all; in the later window it runs exactly once in every trace (200 in 200), about three quarters of the way through, always after A04 and always before A01. [OCC002, POS004, DIR002, DIR003, REL004, REL007]
- A04 was rerouted: earlier, about 99 in 100 of its outgoing transitions went to A01 (about 1 in 100 to A03); in the later window all of them go to A07, and A07 in turn always leads to A01. The A04→A01 distance grew from one step (in about 199 of 200 traces) to two steps (in all traces), consistent with one activity inserted between them. [DIR002, DIR003, LAG003]
- A03's ties to the rest of the flow dissolved: earlier it co-occurred with A01, A02 and A04 in every trace and preceded them (A03 before A01 in 199 of 200 traces, before A04 in about 197 of 200); in the later window A01 and A02 occur without A03 in all traces. [REL001, REL003, REL005]
- The front of the trace shifted: A02 moved from about a fifth into the trace to the very start, and A04 from about three quarters in to halfway, while the A02→A04 distance stayed at two steps and the A02→A01 distance grew from mostly three to always four steps. [POS001, POS003, LAG001, LAG002]

### Inference

Support level: Supported hypothesis

A specific structural reconfiguration is supported: A03, previously the opening activity executed once in every case, is no longer executed, and A07 now runs as a new step between A04 and A01 — the typical flow changed from A03 → A02 → A04 → A01 to A02 → A04 → A07 → A01. The participation flips are complete (200 of 200 traces to 0, and 0 to 200 of 200); the new edges A04→A07 and A07→A01 are observed directly; the A04→A01 distance grew by exactly one step, as an insertion would produce; and A03's co-occurrence with A01, A02 and A04 fell from every trace to none. This is not a relocation of A03, since A07 sits late in the trace where A03 never did. The volume of qualified items (19 against roughly 0.13 expected without change) means chance sampling cannot account for the evidence as a whole. [OCC001, OCC002, DIR002, DIR003, REL001, REL005, LAG003]

Limitation: zero participation only shows that A03 was not observed, not why — removal from the process and a step now skipped in every case look identical here. Also, because A02 now sits at the very start of traces, a change in what the log captures at the beginning of a case (A03 falling outside the recorded window) cannot be ruled out. [OCC001, POS001]

Other differences: the remaining positional shifts (A02 to the trace start, A04 about a quarter of a trace earlier) and the A02→A01 distance growing from three to four steps fit the same restructuring and were not counted as separate findings. [POS001, POS003, LAG001]