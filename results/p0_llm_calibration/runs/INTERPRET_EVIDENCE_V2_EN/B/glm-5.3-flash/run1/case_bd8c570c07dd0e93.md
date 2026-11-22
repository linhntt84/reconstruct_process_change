### Observed differences

- Successors of A20: in the later window, about 98 in 100 of A20's observed outgoing transitions go to A21, and A21 follows A20 at a distance of 1 step in about 98 in 100 cases; in the earlier window, its transitions went to A27 (about 55 in 100) and A28 (about 45), with A21 sitting three steps downstream. [DIR001, LAG001]
- Successors of A23: in the later window, A23's observed outgoing transitions split about evenly between A27 (about 50 in 100) and A28 (about 48), with A24 at about 2 in 100; in the earlier window essentially all went to A24, which then followed A23 at 1 step but now follows at 3 steps. [DIR002, LAG006]
- Execution order reversed: in the earlier window, A27 and A28 each came before A21 and before A23 in every trace containing the pair (100 in 100); in the later window, A21 and A23 each come before A27 and A28 in about 98 in 100, with the old order remaining in about 2 in 100. [REL001, REL002, REL003, REL004]
- Onward routing of the pair: in the later window, A27 and A28 each route about half to the other and half to A24 (about 49 in 100 each), and A24 follows them at only 1–2 steps; in the earlier window they routed mainly on to A21 (about 45–55 in 100) while A24 lay 4–5 steps after them. [DIR003, DIR004, LAG007, LAG008]
- Step distances (event positions, not clock time) shifted coherently: A20→A27 and A20→A28 moved from 1–2 steps to 4–5 steps, A20→A23 from 5 steps to 3, A21→A24 from 3 steps to 5, and A23→A24 from 1 step to 3. [LAG002, LAG003, LAG004, LAG005, LAG006]
- Relative positions moved in the same directions: in the later window A27 and A28 occur later in the trace (mean relative position about 54% versus about 44% of the trace length before), while A21 (about 43% versus 50%) and A23 (about 50% versus 56%) occur earlier. [POS001, POS002, POS003, POS004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the A27/A28 pair changed its place in the sequence: in the earlier window it was executed directly after A20 and before A21, whereas in the later window it is executed after A23 and directly before A24. The relative order of A21 and A23 themselves is unchanged; what differs is where the pair sits relative to them and to A24. [REL001, REL002, REL003, REL004, LAG001, LAG002, LAG005, LAG006, LAG007, LAG008]

- The order reversals are direct relational evidence, appear in about 98 in 100 traces, and point the same way for all four activity pairs; the routing changes match the new order at every junction (A20 now leads to A21, A23 leads into the pair, the pair leads to A24), and the step-distance shifts agree with the same placement. [REL001, REL002, REL003, REL004, DIR001, DIR002, DIR003, DIR004, LAG003, LAG004, LAG007, LAG008]
- The volume of qualifying evidence (18 items against roughly 0.39 expected if nothing had changed, across 78 tested units) cannot be explained by chance as a whole, and every item rests on about 200 observations per window out of 200 traces, so the pattern is not driven by a rare variant seen in one window only. [DIR001, DIR002, DIR003, DIR004, POS001, POS002, POS003, POS004, REL001, REL002, REL003, REL004, LAG001, LAG002, LAG003, LAG004, LAG005, LAG006, LAG007, LAG008]

- The indicators overlap heavily — the DIR, LAG and REL items largely describe the same traces — so the 18 items amount to one coherent difference rather than independent confirmations. [REL001, REL002, LAG003, LAG004]
- The evidence cannot rule out that both orderings already existed as process variants and only their frequencies shifted between the windows: the old order still appears in about 2 in 100 later-window traces, and a shift in the variant mix within finite samples of 200 traces per window cannot be excluded. [REL001, REL002, REL003, REL004]
- All distance and position statements refer to event positions within the trace, not clock time, so no claim about timing is implied. [LAG001, POS001]