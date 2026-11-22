### Observed differences

- In the earlier window, A04 was executed exactly once in every case (200 of 200 traces, mean 1.0 occurrence per trace) and always as the final step (position 1.0 in all traces). In the later window, A04 does not appear in any of the 200 traces. [OCC001, POS003]
- Before, A02's only observed outgoing transition was to A04 (100% of A02's observed outgoing transitions). In the later window, A02 is the last activity in every trace (position 1.0) and no outgoing transitions from A02 are observed. [DIR001, POS001]
- Before, A04 co-occurred with A01, A02, A03, A05 and A06 in 100% of cases and always ran after each of them. In the later window, co-occurrence with A04 is 0 for all five pairs, and each partner now occurs without A04. [REL001, REL002, REL003, REL004, REL005]
- The remaining activities kept their relative order (A06 before A05 before A03 before A02 in both windows); their positions shifted only by the amounts consistent with each trace becoming one step shorter: A06 from 0.2 to 0.25, A05 from 0.4 to 0.5, A03 from 0.6 to 0.75, A02 from 0.8 to 1.0. These are event positions, not clock times. [POS001, POS002, POS004, POS005]

### Inference

Support level: Supported hypothesis

A specific hypothesis supported by the evidence is that A04, previously the mandatory final step of a fixed sequence that ran A01, then A06, A05, A03 and A02, and closed with A04 in every case, is no longer executed in the later window, leaving the same sequence to end at A02. Before, every trace contained all six activities in this fixed order; in the later window, every trace contains the same five activities in the same relative order, with A04 absent. [OCC001, POS003, DIR001, REL001, REL002, REL003, REL004, REL005]

The signs are direct and mutually consistent: A04's participation fell from 100% to 0% between samples of 200 traces each, the previously unconditional A02→A04 transition disappeared as A02 became the final activity, and all five co-occurrence relations with A04 fell from 100% to 0%, while the surviving activities show no reordering — their position shifts match the shortening of the trace rather than independent moves. Every item's difference also exceeds those of about 199 in 200 random re-splits of the pooled data. A competing explanation the evidence cannot fully rule out is that A04 still occurs but has become so rare that 200 later traces contain no instance; the evidence also cannot show whether the work A04 performed is now done elsewhere. [OCC001, DIR001, REL001, REL002, REL003, REL004, REL005, POS001, POS002, POS004, POS005]