### Observed differences

- In the later window, activities A14, A15, A20, A21, and A22 no longer have A23 as their sole successor; instead they split between A25 and A29 (e.g., A14: about 45% to A25 and 55% to A29; A22: about 68% to A25 and 32% to A29). [DIR001, DIR002, DIR003, DIR004, DIR005]
- A24 and A25, which previously each had a single successor (A25 and A29 respectively), now have multiple successors including A14, A15, A20, A21, A22, and A29 (for A25). [DIR006, DIR007]
- A42, which previously went to A14, A15, A20, A21, and A22, now goes exclusively to A23. [DIR008]
- The relative order of A14, A15, A20, A21, and A22 with respect to A23 (and A24) reversed: before they occurred before A23/A24, now they occur after. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008]
- The positions of A14, A15, A20, A21, and A22 shifted later in the trace (mean position increased by about 0.26–0.29), while A23, A24, and A25 shifted slightly earlier. [POS001, POS002, POS003, POS004, POS005, POS006, POS007, POS008]
- The lag between A24 and A25 increased (from always 1 step to about 49% 1 step and 51% 2 steps), and between A24 and A29 from 2 to 3 steps; A42–A23 lag decreased from 2 to 1. [LAG001, LAG002, LAG003, LAG004]
- The elapsed time between completion of A03–A08 and A09 roughly halved, from about 1 hour to about 0.5 hours (e.g., A03–A09 mean from 1.02h to 0.51h). [TWAIT001, TWAIT002, TWAIT003, TWAIT004, TWAIT005, TWAIT006]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process was reordered: activities A14, A15, A20, A21, and A22 moved from before A23 to after A23, and their successors changed from A23 to A25/A29, while A42 now leads to A23 instead of to those activities. This is directly shown by the reversal in order for all pairs involving these activities (REL001–008), the change in outgoing edges (DIR001–005, DIR008), and the consistent later positions of these activities (POS001–005). The lag changes (LAG001–004) are consistent with this reordering. The evidence is far beyond what chance would produce (28 control-flow items vs. 0.43 expected), so the structural change is well supported. A competing explanation that cannot be fully ruled out is that the activities themselves changed meaning, but the observed pattern of order reversal and successor change is coherent.

Other differences: The elapsed time between A03–A08 and A09 halved, indicating a separate change in timing. [TWAIT001–006]