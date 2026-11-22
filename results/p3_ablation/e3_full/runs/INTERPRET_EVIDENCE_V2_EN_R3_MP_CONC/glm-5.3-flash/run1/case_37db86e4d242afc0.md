### Observed differences

- **A01 disappears.** In the earlier window A01 appears exactly once in every one of the 200 traces, very early in the case (median position 0.2), and its only observed successor is A07. In the later window A01 is not observed in any of the 200 traces. [OCC001, POS001, DIR001]
- **A03 appears in A01's place.** In the earlier window A03 is not observed at all; in the later window it appears once in every trace, at the same early position (median 0.2), always preceded by A02 and always followed by A07. A02's outgoing transitions switch from 100% A01 before to 100% A03 after. [OCC002, POS002, DIR002, DIR003, REL002, REL008, REL014]
- **A06 is a new final activity.** Before, A06 is never observed; in the later window it occurs in about 47 in 100 traces, always as the last event, after A07 and A05, and never in the same trace as A08. [OCC003, POS005, REL020, REL021, REL013]
- **The ending behaviour changed.** Before, A05 led to A08 in about half the traces (101 of 200) and was itself the final event in the remaining traces. In the later window A05 always has a successor: A06 in about 47 in 100 of its outgoing transitions and A08 in about 53 in 100, so traces that previously ended at A05 now continue to A06. [DIR004, POS004, REL021]
- **The middle of the process is stable.** A04, A05 and A07 occur in all traces in both windows at the same median positions; their positions only become constant (e.g., A04 always at 0.6 later, versus 0.6–0.75 before), which is consistent with all traces now having the same length. [POS003, POS004, POS006]
- **A08 participation is essentially unchanged** (about 50 in 100 traces before, about 54 in 100 after); this small difference has an empirical strength of 0.40, i.e., within what random re-splits of unchanged data produce. [OCC004, REL010]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change with two parts. First, A01 was replaced by A03: A03 took over A01's position between A02 and A07 (A02 → A03 → A07 instead of A02 → A01 → A07), with A01 absent and A03 present in every later-window trace. Second, a new final activity A06 was introduced after A05: in about 47 in 100 later-window traces the sequence now runs A05 → A06 as the last event, occupying the slot where traces previously ended directly after A05; A06 and A08 act as mutually exclusive alternatives after A05, while the A08 share stays roughly the same. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, POS001, POS002, POS005, REL021]

The rewiring is shown directly by relational and directional evidence rather than by participation counts alone: A03 inherits A01's predecessor, successor and position, and A06's placement (after A05 and A07, last position, never co-occurring with A08) is observed directly. The many REL items are consistent with this but largely reflect the same two underlying differences, so they are not independent confirmations. [DIR002, DIR003, DIR004, POS002, POS005, REL008, REL014, REL020, REL021]

Limitations: the evidence is control-flow only and provides no screening expectation to compare the item count against; it also cannot rule out that the two windows sample different process variants or segments rather than a single change at a point in time. [OCC001, OCC002]

Other differences: A08 participation rose slightly from about 50 to about 54 in 100 traces; the difference is small and empirically unremarkable (strength 0.40), so it is consistent with sampling noise rather than a behavioural change. [OCC004, REL010, REL017, REL019, REL022]