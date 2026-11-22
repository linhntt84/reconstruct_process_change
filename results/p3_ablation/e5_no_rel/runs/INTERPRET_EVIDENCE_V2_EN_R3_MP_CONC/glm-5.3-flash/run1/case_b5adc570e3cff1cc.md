### Observed differences

- In the earlier window, routing in the A22–A23–A27 segment was variable: A22 led to A23 in about 48 in 100 of its observed outgoing transitions and to one of A14/A15/A20 in the rest; A23 led to A27 in about 53 in 100 and to one of A14/A15/A20 otherwise; and A14/A15/A20 split their outgoing transitions roughly equally between A23 and A27. In the later window, A22 always led to A23, A23 always led to A27, and A14/A15/A20 no longer appeared as successors in this segment; the A22→A27 distance shortened from 3 steps in essentially all cases to 2 steps, and the A22→A23 and A23→A27 gaps, previously 1 or 2 steps, became fixed at 1. [DIR001, DIR002, DIR003, DIR004, DIR005, LAG001, LAG002, LAG003]

- The block A14/A15/A20 still accounted for essentially one execution per trace in both windows (about 38, 32 and 31 in 100 traces earlier; about 34, 35 and 32 in 100 later), but its position moved from roughly 60% to roughly 32% of the trace's event positions. [POS001, POS002, POS003]

- The A40→A21 transition was rewired: earlier, A40 always led directly to A21 (adjacent, gap 1); in the later window, A40 led to A14, A15 or A20 in roughly equal thirds (about 31–35 in 100 each), and each of these always led to A21, so A21 followed A40 with one activity in between (gap 2). [DIR006, DIR001, DIR002, DIR003, LAG004]

- The anchor activities kept their places almost unchanged: A21 sat at about 0.33 of the trace earlier and 0.35 later, A22 at 0.56 versus 0.59, and A23 at 0.61 versus 0.62. [POS004, POS005, POS006]

- A10 and A11 still occurred in every trace but repeated less often: about 1.9 occurrences per trace earlier versus about 1.6 later, with traces containing repeats down from about 47 to 38 in 100. [OCC001, OCC002]

### Inference

Support level: Supported hypothesis

The evidence supports a structural rewiring in which the block A14/A15/A20 — exactly one of the three executing per case — was relocated from the A22→A23→A27 segment to the transition from A40 to A21. In the earlier window the block acted as a detour that made both A22→A23 and A23→A27 conditional (about half of the transitions through each went via the block); in the later window A22→A23→A27 runs as a fixed chain, and A40 reaches A21 only through the block. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, LAG001, LAG002, LAG003, LAG004, POS001, POS002, POS003]

This goes beyond chance and is internally consistent: 18 items qualified against only 0.36 expected without change in the control-flow family, so the volume alone cannot be explained by random re-splits; the successor profiles changed from mixed to single targets on substantial supports (61–76 observed outgoing transitions for the block activities before, 63–69 after, and all 200 traces for A22, A23 and A40); and the lag and position changes match the rewiring quantitatively — A22→A27 gap 3→2, A40→A21 gap 1→2, block position about 0.60→0.32 while A21, A22 and A23 shifted only 0.01–0.03 later — with every item's difference exceeding about 99.5 in 100 random reference splits. [DIR001, DIR004, LAG002, LAG004, POS001, POS004]

Limitations: the evidence cannot distinguish one relocation of the block from a removal from the later segment combined with a separate insertion before A21, and rare transitions unobserved in these 200-trace samples cannot be excluded; positions are event positions, not clock times. [DIR001, LAG004, POS001]

Other differences: A10 and A11 repeat less often per trace (about 1.9 versus 1.6 occurrences; traces with repeats down from about 47 to 38 in 100) while still appearing in every trace; this repetition change is not explained by the relocation hypothesis. [OCC001, OCC002]