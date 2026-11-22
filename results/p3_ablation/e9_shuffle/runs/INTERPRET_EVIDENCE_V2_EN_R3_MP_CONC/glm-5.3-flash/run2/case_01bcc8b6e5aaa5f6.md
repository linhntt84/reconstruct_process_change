### Observed differences

- In the earlier window, A02 was executed exactly once in every trace (200 in 200 traces, one occurrence each) and very early, at about 5% of the trace length. In the later window, A02 was not observed in any of the 200 traces. [OCC001, POS001]
- Earlier, A02 co-occurred with A03 in every trace and ran before it in about 89 in 100 traces (A03 first in the remainder); it likewise co-occurred with A04 in every trace and ran first in about 88 in 100. In the later window, A02 never co-occurs with either activity: A03 appears without A02 in all traces, and A04 does the same. [REL001, REL002]
- A02's outgoing transitions, previously dominated by A03 (about 48 in 100) and A04 (about 42 in 100) with small shares to A06, A05 and A07, show an empty profile in the later window because A02 no longer occurs. [DIR001]
- The activities that used to follow A02 now sit earlier in the trace: A03's mean relative position fell from about 0.27 to 0.18, and A04's from about 0.29 to 0.15 (A04's median fell from 0.33 to 0). [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A02, previously a mandatory early step executed once per case before both A03 and A04, is no longer executed in the later window, while A03 and A04 continue to run in every case, now without A02 and at earlier relative positions. Seven control-flow items qualified against roughly 0.07 expected for an unchanged process, far beyond what chance would produce, and the picture is direct and consistent: A02's participation fell from 100% to 0%, its co-occurrence with A03 and A04 fell from 100% to 0% with both now appearing alone in every trace, its outgoing profile emptied, and the position shifts of A03 and A04 match the loss of an early predecessor. [OCC001, POS001, DIR001, REL001, REL002, POS002, POS003]

Limitations: the agreeing items largely reflect one underlying trace behaviour (A02's disappearance) rather than independent confirmations, and zero participation strictly means only that A02 was not observed in the later sample. A competing explanation the evidence cannot rule out is that A02 still occurs but was missed by sampling, or that its work is now carried out by an activity outside the tested set. [OCC001, POS001]