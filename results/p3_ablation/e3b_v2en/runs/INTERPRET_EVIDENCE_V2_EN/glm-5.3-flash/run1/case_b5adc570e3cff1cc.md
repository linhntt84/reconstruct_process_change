### Observed differences

- The three alternative activities A14, A15 and A20 keep their overall frequency but run much earlier: each appears in about 31–38 in 100 traces in both windows (their shares together amount to about one execution per trace), while their mean position moves from about 60% to about 32% of the trace length in the later window. [POS001, POS002, POS003]
- Routing around these three activities changed completely in the later window: A40, previously always followed by A21, is now always followed by one of A14/A15/A20 (about one third each); A14/A15/A20, previously split roughly half to A23 and half to A27, now always lead to A21; and A22 and A23 no longer route into the fragment (A22 now always goes to A23, before about 48 in 100; A23 now always goes to A27, before about 53 in 100). [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006]
- Distances along the remaining chain tighten: A22→A23 and A23→A27 are now always adjacent, where before roughly half of each pair had one activity in between, and A22→A27 shortens from three steps to two. [LAG001, LAG002, LAG003]
- The distance from A40 to A21 grows from one step to two, consistent with one of the three activities now sitting between them. [LAG004, DIR006]
- Order relations flip completely: before, A21 and A22 preceded A14/A15/A20 in every trace containing both; in the later window the fragment precedes A21 and A22 in every such trace. [REL001, REL002, REL003, REL004, REL005, REL006]
- A10 and A11 still occur in every trace but repeat less often: about 1.9 occurrences per trace before versus about 1.6 in the later window, with repeats in about 47 versus 38 in 100 traces. [OCC001, OCC002]
- A21, A22 and A23 occur at slightly later relative positions in the later window (mean position up by about 0.01–0.03). [POS004, POS005, POS006]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the optional three-way fragment A14/A15/A20 was relocated: in the earlier window it executed late, inserted after A22 or A23 and before A27, whereas in the later window it executes early, between A40 and A21; in addition, A10 and A11 repeat less often. [REL001, DIR006, POS001, LAG004, OCC001]

- The order flip is observed directly rather than inferred from frequencies alone: A21 and A22 precede the fragment in 100% of joint occurrences before and in 0% in the later window. [REL001, REL002, REL003, REL004, REL005, REL006]
- Successor sets change exactly as a relocation implies: A40 switches from always A21 to always the fragment, the fragment switches from A23/A27 to always A21, and A22/A23 drop their transitions into the fragment. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006]
- Adjacency and distance changes corroborate the new placement, and the fragment's participation is essentially unchanged (about one execution per trace in both windows), so this is a change of placement rather than of frequency. [LAG001, LAG002, LAG003, LAG004, POS001, POS002, POS003]
- With 24 qualifying items against roughly 0.4 expected for an unchanged process, the pattern as a whole is far beyond what random re-splits produce, and every item's difference exceeds about 995 of 1000 reference comparisons. [OCC001, DIR001, POS001, REL001, LAG001]

Limitations: the main competing explanation is a drastic shift in the mix of pre-existing process variants; the complete 0%→100% order flip at essentially unchanged participation across 200-trace windows makes this implausible but cannot fully exclude it. [REL001, POS001] The reduced repetition of A10 and A11 is not linked to the fragment by any relational evidence in this set and may be an independent change in a repeating part or a sampling difference in how often that part iterates. [OCC001, OCC002] Positions are event positions, so the change concerns order within traces, not clock timing. [POS001, POS004]