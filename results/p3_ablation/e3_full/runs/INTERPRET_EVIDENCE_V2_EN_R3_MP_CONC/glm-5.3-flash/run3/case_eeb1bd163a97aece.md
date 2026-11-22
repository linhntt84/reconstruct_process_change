### Observed differences

- Activity A01 did not occur at all in the earlier window (0 of 200 traces); in the later window it occurs in every trace, exactly once per case [OCC001].
- In the later window, A01 always sits at the same relative position, 0.6 of the way through the trace; before, it had no observed position [POS001].
- The handover around A05 changed: before, every observed outgoing transition of A05 led to A06, and A06 followed A05 immediately (1 step apart); after, every outgoing transition of A05 leads to A01, every outgoing transition of A01 leads to A06, and A05–A06 are now 2 steps apart [DIR001, DIR002, LAG006].
- A01's order relative to every other activity is consistent: in the later window it co-occurs with A02, A03, A04, A05 and A06 in all 200 traces, always after A02, A04 and A05 and always before A03 and A06; before, it co-occurred with none of them [REL001, REL002, REL003, REL004, REL005].
- Every measured activity pair spanning A01's new position moved exactly one step further apart: A02→A03 from 4 to 5, A02→A06 from 3 to 4, A04→A03 from 3 to 4, A04→A06 from 2 to 3, A05→A03 from 2 to 3, A05→A06 from 1 to 2 [LAG001, LAG002, LAG003, LAG004, LAG005, LAG006].
- Relative positions shifted accordingly: A04 from 0.25 to 0.2, A05 from 0.5 to 0.4, A06 from 0.75 to 0.8 [POS002, POS003, POS004].
- Every item rests on all 200 traces per window (for A01, 0 before vs 200 after), and each difference is larger than in about 199 of 200 random re-splits of the pooled data [OCC001, DIR001, DIR002, POS001, POS002, POS003, POS004, REL001, REL002, REL003, REL004, REL005, LAG001, LAG002, LAG003, LAG004, LAG005, LAG006].

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 now runs exactly once per case between A05 and A06, whereas it did not appear in the earlier window: before, cases passed from A05 directly to A06; after, A05 always hands over to A01 and A01 always leads to A06, with A01 fixed at relative position 0.6 [OCC001, DIR001, DIR002, POS001, LAG006]. The placement is corroborated from several independent angles: A01 co-occurs with all five other activities in a fixed order (after A02, A04 and A05; before A03 and A06), every measured pair spanning the new position is exactly one step further apart, and the small position shifts of A04, A05 and A06 match a trace that is one event longer — all consistent with one extra step added between A05 and A06 while the relative order of the other activities is preserved [REL001, REL002, REL003, REL004, REL005, LAG001, LAG002, LAG003, LAG004, LAG005, POS002, POS003, POS004].

Limitations: zero participation only means A01 was not observed in the earlier window, so the evidence cannot distinguish a newly added activity from one that was simply not executed or recorded before; with 200 traces per window and full participation afterwards, a sampling explanation is unlikely but cannot be fully excluded [OCC001]. The end-to-end sequence (for example, the placement of A02 and A03 relative to A04 and A05) is inferred from pairwise lags and positions rather than observed directly [LAG001, LAG003].

Other differences: none — the spacing and position shifts for A02–A06 follow from A01 running between A05 and A06 and are not independent changes [LAG001, LAG002, LAG003, LAG004, LAG005, LAG006, POS002, POS003, POS004].