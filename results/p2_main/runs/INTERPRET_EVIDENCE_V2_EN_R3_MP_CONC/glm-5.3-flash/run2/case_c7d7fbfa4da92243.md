### Observed differences

- Activity A10 was a regular step in the earlier window — it appeared in about 44 in 100 traces (88 of 200), typically in the first third of the trace by event position — and it is not observed in any of the 200 later traces. [OCC001, POS001]
- Before, the flow ran through A10 as a chain: A04 led to A10 in about 55 in 100 of A04's observed outgoing transitions, and A10 led on to A12 in about 82 in 100 of its outgoing transitions. In the later window, A04 no longer leads to A10 at all; about 73 in 100 of its outgoing transitions now go straight to A12, up from about 10 in 100 before. [DIR002, DIR003]
- The A04→A12 succession became immediate: before, A12 typically followed A04 two steps later (about 56 in 100 of observed pairs, consistent with A10 sitting in between) and only about 11 in 100 followed directly; in the later window about 75 in 100 follow within one step. [LAG001]
- The co-occurrence pattern flipped accordingly: before, A04 and A10 appeared together in about 44 in 100 traces (A04 was never seen without A10) and A10 always preceded A12 when they co-occurred; in the later window A04 appears without A10 in about 58 in 100 traces and A12 appears without A10 in about 58 in 100, with no co-occurrence of either pair. A04 itself now runs in about 58 in 100 traces, up from about 44 in 100. [REL001, REL002]
- The outgoing flows of A03 and A11 also moved away from A10 (and A02) toward A04 and A12, but these profiles rest on only about 5 outgoing transitions before and 9–10 after, so they are weakly grounded. [DIR001, DIR004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the A10 step between A04 and A12 was dropped: traces that previously ran A04 → A10 → A12 now pass from A04 directly to A12, and A10 is no longer executed. This is shown directly — A10 falls from about 44 in 100 traces to 0 of 200, A04's outgoing transitions shift from A10 (about 55 in 100) to A12 (about 73 in 100), and the A04→A12 distance collapses from typically two steps to one — and consistently, with nine qualifying control-flow items against roughly 0.15 expected if nothing had changed, all describing this same difference. [OCC001, POS001, DIR002, DIR003, LAG001, REL001, REL002]

The evidence cannot fully rule out that A10 still exists in the process but was simply not executed in the later window; given 0 of 200 traces after about 44 in 100 before, this is unlikely but not logically excluded. Whether other predecessors of A10 (such as A03 and A11) rerouted in the same way rests on very few observations and remains uncertain. [OCC001, DIR001, DIR004]

Other differences: the direction profiles for A03 and A11 changed as described above; they are consistent with the same rerouting away from A10 but add little weight on their own. [DIR001, DIR004]