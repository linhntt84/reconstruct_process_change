### Observed differences

- In the later window, A01 occurs exactly once in every trace (200 of 200), while in the earlier window it was not observed at all (0 of 200). A05 shows the mirror image: exactly once in every earlier trace (200 of 200, never repeated) and absent from all later traces. [OCC001, OCC002]
- Both activities occupy one fixed event position when they occur: mean position 0.5 with no spread, identical for A05 in the earlier window and A01 in the later window. [POS001, POS002]
- The link to A03 is preserved: earlier, A05 was always followed by A03; in the later window, A01 is always followed by A03, and A03 itself runs in every trace in both windows. [DIR003, DIR001, REL002, REL007]
- Predecessors re-route from A05 to A01 with nearly unchanged shares: A02's outgoing transitions led to A05 in about 72 of 100 cases earlier and lead to A01 in about 75 of 100 later; A07's led to A05 in about 71 of 100 and lead to A01 in about 66 of 100; A06's led to A05 in about 29 of 100 and lead to A01 in about 30 of 100. [DIR002, DIR005, DIR004]
- A01 also inherits A05's co-occurrence pattern: earlier, A06 always co-occurred with A05 and always preceded it; later, A06 always co-occurs with A01 and always precedes it. A02 co-occurred with A05 in 47 of 100 traces (always before it) and now co-occurs with A01 in 50 of 100 (always before it); A07 shows the same pattern (53 of 100 earlier, 50 of 100 later, always before). [REL004, REL008, REL006, REL009, REL001, REL005]
- The rest of the skeleton is unchanged: A06 appears in every trace in both windows, A02 and A07 remain optional predecessors in roughly half of the traces, and the side branches A06→A02, A06→A07, A02→A06 and A07→A06 persist with similar shares (for example A02→A06 at about 28 of 100 earlier versus 25 of 100 later). [REL004, REL001, REL005, DIR002, DIR004, DIR005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 has taken over the position A05 held earlier, with A05 no longer executed: in the earlier window every trace ran A06, then optionally A02 (47 of 100 traces) or A07 (53 of 100), then A05 and finally A03; in the later window the same flow runs with A01 in A05's place — always after A06, after A02 or A07 in about half of the traces, and always before A03. The support is direct and consistent rather than merely frequency-based: A01 inherits all of A05's relations (with A06, A02, A07 and A03) at nearly the same strengths, appears at A05's exact former event position, and the two participations swap completely (0 versus 200 of 200 traces in both directions). [OCC001, OCC002, POS001, POS002, DIR001, DIR002, DIR003, DIR004, DIR005, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009]

The volume of flagged evidence also exceeds what an unchanged process typically produces: 18 control-flow items qualified where about 0.13 would be expected by chance, and each item's difference exceeds about 995 of 1000 random re-splits of the pooled data. [screening]

What the evidence cannot rule out is that this is one substitution rather than two independent changes (A05 removed and A01 inserted at the same point), or simply a relabelling of the activity — these look behaviourally identical here. Strictly, A05's absence in the later window means only that it was not observed in those 200 traces, so a residual very rare use of A05 cannot be excluded.

Other differences: only minor shifts accompany the swap — A02 appears in 47 of 100 traces earlier versus 50 of 100 later, A07 in 53 versus 50, and A07 routes to the swapped activity in about 71 of 100 earlier versus 66 of 100 later; these are small enough that sampling variation between the two windows cannot be excluded. [REL001, REL005, DIR002, DIR005]