### Observed differences

- In the earlier window, A01 never appears (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200), always at the same event position, about 60% of the way through the trace. [OCC001, POS001]
- In the earlier window, A05's only observed outgoing transition led to A06, and the two activities were consecutive events (lag 1) in all 200 traces. In the later window, A05's outgoing flow leads entirely to A01 instead of A06, and A05 and A06 are now separated by exactly one intervening event (lag 2). [DIR002, LAG001]
- In the later window, A01's only observed outgoing transition is to A06; A01 co-occurs with A05 in every trace with A05 executed first, and with A06 in every trace with A01 executed first. Before, A05 and A06 each occurred without A01 in all traces. [DIR001, REL001, REL002]
- The mean event positions of the neighbouring activities shifted slightly: A05 from 0.5 to 0.4 and A06 from 0.75 to 0.8, the pattern expected on a normalised position scale when one event is inserted between them. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports that A01 was inserted between A05 and A06: traces that previously executed A05 immediately followed by A06 now execute A05, then A01, then A06, in essentially every case. The placement is shown directly by the rewiring of A05's outgoing transition from A06 to A01 and A01's transition to A06, by the fixed order relations (A05 before A01 and A01 before A06 in all 200 later traces), and by the A05–A06 gap growing from one event to two while A01 appears exactly in between. All nine qualifying items describe this single difference, screening produced 9 items where about 0.04 would be expected by chance without a change, each difference is larger than in about 995 of 1,000 random re-splits, and the 200-of-200 versus 0-of-200 participation rules out a rare variant appearing in one window only. [OCC001, DIR001, DIR002, POS001, REL001, REL002, LAG001]

The evidence cannot distinguish a genuinely new step from a pre-existing optional step that was simply never executed in the earlier sample, since zero participation only means A01 was not observed before; the characterisation is also limited to the neighbourhood of A05, A01 and A06. [OCC001, POS001]

Other differences: none — the small position shifts of A05 and A06 are part of the same insertion. [POS002, POS003]