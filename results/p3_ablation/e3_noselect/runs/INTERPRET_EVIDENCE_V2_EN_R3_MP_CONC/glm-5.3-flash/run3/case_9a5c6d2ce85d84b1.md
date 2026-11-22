### Observed differences

- Activity A01 was absent from the earlier window — it appears in 0 of 200 traces — while in the later window it occurs exactly once in every trace (200 of 200), with no repetitions. [OCC001]
- The relationship between A01 and A04 changed fundamentally: earlier, A04 appeared in traces without A01 in 100% of cases and the two never co-occurred; in the later window they co-occur in every trace, always in the fixed order A04 before A01. The pair went from never being executed together to always being executed together. [REL001]
- A04's successors changed: in the earlier window no outgoing transition from A04 was observed (consistent with it holding the final position, mean position 1.0, in every trace), while in the later window every observed outgoing transition of A04 leads directly to A01. [DIR001, POS002]
- Positions shifted accordingly: A01 sits at the final position (mean position 1.0) in every later trace, and A04's mean position moved from 1.0 to 0.75, i.e. about a quarter of the trace earlier. These are event positions, not clock times. [POS001, POS002]
- Each of these differences is larger than in about 995 of 1,000 random re-splits of the pooled data, so none looks like ordinary sampling variation between two windows of this size. [OCC001, DIR001, POS001, POS002, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a mandatory final step, A01, was appended after A04: in the earlier window cases ended with A04, which occupied the last position in every trace with no observed successor, while in the later window every case ends with A04 followed by A01, with A01 running exactly once per case. This is shown directly by the relational evidence (co-occurrence of A01 and A04 rising from 0% to 100% of traces, always with A04 first), by A04's outgoing transitions (all now leading to A01 after none were observed earlier), and by A01's participation rising from 0 to 200 of 200 traces. The five evidence items describe one underlying difference rather than independent confirmations of it. [OCC001, DIR001, POS001, POS002, REL001]

Limitations: the evidence cannot distinguish a genuinely new activity from one that existed earlier but was so rare it never appeared in the 200 earlier traces; it covers only A01 and A04, so any further changes elsewhere in the trace would not be visible; and positions are event positions, so no statement about clock-time timing is possible. [OCC001, POS001, POS002]