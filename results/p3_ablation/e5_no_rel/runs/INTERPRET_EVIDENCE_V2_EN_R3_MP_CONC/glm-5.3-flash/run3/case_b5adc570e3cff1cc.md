### Observed differences

- The alternative activities A14, A15 and A20 together appear in essentially every trace in both windows (about 38, 32 and 31 in 100 traces before; about 34, 35 and 32 after — the three shares sum to roughly all traces in each window), consistent with exactly one of the three executing per case. In the earlier window they sat at about 60% of the trace (mean positions 0.60–0.61); in the later window they sit at about 31–32%. [POS001, POS002, POS003]

- In the earlier window, A14, A15 and A20 each led either to A23 or to A27 (A14 about 50/50, A15 about 56/44, A20 about 52/48 across their observed outgoing transitions); in the later window, all three lead only to A21. [DIR001, DIR002, DIR003]

- In the earlier window, A22 led to A23 in about 48 of 100 observed outgoing transitions and to one of A14/A15/A20 in the remainder, while A23 led to A27 in about 53 of 100 and to one of A14/A15/A20 in the remainder; in the later window, A22 leads only to A23 and A23 only to A27. [DIR004, DIR005]

- In the earlier window, A40 was always followed by A21; in the later window it is followed by A15 in about 35 of 100 outgoing transitions, A14 in about 34 and A20 in about 32. [DIR006]

- The adjacency gaps match: in the earlier window A22 was immediately followed by A23 in about 48 of 100 traces and A23 immediately by A27 in about 53 (otherwise one of A14/A15/A20 lay in between), and A22 reached A27 at a gap of 3 in every trace; in the later window A22→A23 and A23→A27 are adjacent in every trace, A22→A27 has a gap of 2 in every trace, and A40→A21 changed from adjacent in every trace to a gap of 2 in every trace. [LAG001, LAG002, LAG003, LAG004]

- A21, A22 and A23 each shifted slightly later in the trace (mean positions up by about 0.01–0.03), consistent with one event having been inserted ahead of them. [POS004, POS005, POS006]

- A10 and A11 still occur in every trace, but repeat less in the later window: about 1.9 occurrences per trace before versus about 1.6 after, with a repeat within the same trace in about 47 of 100 traces before versus about 38 after. [OCC001, OCC002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the alternative block A14/A15/A20 — one of which executes per case — is now placed at a different point of the process. In the earlier window it executed between A22 and A27, in either order relative to A23 (before A23 in about 53 of 100 traces, after it in about 47); in the later window it executes between A40 and A21, while A22, A23 and A27 form a fixed, directly connected sequence. The block's participation is essentially unchanged across the windows, so the evidence points to a change of placement rather than a change in how often the block runs. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, LAG001, LAG002, LAG003, LAG004, POS001, POS002, POS003]

The hypothesis is shown directly and consistently rather than through a single indicator: the successor profiles of A22, A23, A40, A14, A15 and A20 all changed exactly as a relocation predicts, the four gap distributions moved the same way, and the block's mean position fell by about 0.28–0.29 while A21, A22 and A23 moved only slightly later. Screening also found 18 qualifying control-flow items where about 0.36 would be expected without a change, many times the chance level, so the ensemble is not what random re-splits typically produce. [DIR001, DIR006, LAG001, LAG004, POS001, POS003, POS004, screening]

Limitations: positions are event positions, so "earlier" means earlier in the sequence, not earlier in clock time. The main competing explanation the evidence cannot rule out is a simultaneous change in how often the block executes per case: the items record how many traces contain each of A14, A15 and A20 but not their occurrence counts within a trace. [POS001, POS002, POS003]

Other differences: A10 and A11 repeat less often in the later window (about 1.9 versus about 1.6 occurrences per trace; within-trace repetition in about 47 versus about 38 of 100 traces) while still occurring in every trace. No relational item connects this repetition change to the relocated block, so it is reported separately from the main hypothesis. [OCC001, OCC002]