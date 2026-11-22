### Observed differences

- **A10 is no longer observed.** In the earlier window it appeared in about 44 in 100 traces (88 of 200), typically in the first half of the trace; in the later window it appears in 0 of 200 traces, and no outgoing transitions from A10 are observed (earlier, about 82 in 100 of them led to A12 and about 10 to A04) [OCC001, POS001, DIR003].
- **A04 now leads directly to A12.** Earlier, about 55 in 100 of A04's observed outgoing transitions went to A10 and only about 10 to A12; in the later window A10 is no longer a successor of A04 and about 73 in 100 go to A12, while A04's other successors keep similar small shares [DIR002].
- **The A04–A12 distance shortened.** Earlier the pair was most often two steps apart (about 56 in 100 observed pairs, with about 23 in 100 three steps apart); in the later window it is most often directly consecutive (about 75 in 100) [LAG001].
- **Co-occurrence with A10 collapsed.** Earlier, A04 and A10 always appeared together (about 44 in 100 traces) and A12 always appeared together with A10, with A10 first; in the later window A04 and A12 each appear without A10 in about 58 in 100 traces and never with it [REL001, REL002].
- **A03 and A11 were rerouted away from A10.** A03 earlier led to A10 (about 60%) or A02 (about 40%), later to A04 and A12 (about 50% each); A11 earlier led to A02 (about 60%) or A10 (about 40%), later to A04 (about 78%) or A12 (about 22%). Both rest on very few observations (5–10 outgoing transitions per window) [DIR001, DIR004].

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A10 was dropped from the flow between A04 and A12. Earlier, A04 led mostly into A10 (about 55 in 100 of its outgoing transitions) and A10 led on to A12 (about 82 in 100), so A04 and A12 were typically two steps apart; in the later window A10 is not observed in any of 200 traces (down from 88), A04 leads directly to A12 in about 73 in 100 of its outgoing transitions, and the A04–A12 distance is typically one step. The change is visible directly in the occurrence, successor and distance indicators, agrees across all nine qualified control-flow items, and each difference is larger than in about 995 of 1000 random re-splits; nine items also far exceed the roughly 0.15 expected without change, so sampling noise alone cannot account for the set [OCC001, DIR002, DIR003, LAG001, REL001, REL002, POS001].

Limitations: zero participation only shows that A10 was not observed in the later sample, so a residual rare execution of A10 cannot be ruled out; the hypothesis is about observed behaviour, not a confirmed modification [OCC001].

Other differences: A04 and A12 now each appear in about 58 in 100 traces, up from about 44 in 100; and A03 and A11, which earlier led mostly to A10, now lead to A04 and/or A12 — consistent with the same rerouting of traffic around A10, but based on only 5–10 outgoing transitions each, so this side of the change is weakly supported [REL001, REL002, DIR001, DIR004].