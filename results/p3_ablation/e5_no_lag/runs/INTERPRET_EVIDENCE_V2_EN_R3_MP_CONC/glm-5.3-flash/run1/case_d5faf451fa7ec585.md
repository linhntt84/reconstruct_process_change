### Observed differences

- In the earlier window, A14, A15 and A20 were mutually exclusive alternatives that together appeared in every trace: A14 in about 32 in 100 traces, A15 in about 28, A20 in about 40, with no trace containing two of them. In the later window, none of the three is observed at all (0 of 200 traces, zero occurrences). [OCC001, OCC002, OCC003, REL001, REL002, REL006]
- The routing around this block changed accordingly. Before, about 45 in 100 of A22's observed outgoing transitions went to one of A14, A20 or A15 (about 14, 21 and 11 in 100 respectively) and the remainder went directly to A23; in the later window, A22 leads to A23 in every observed transition. Before, A23 led to A24 in about 46 in 100 of its outgoing transitions and to A14, A20 or A15 in about 54; in the later window, A23 leads to A24 in every observed transition. The three alternative activities show no outgoing transitions in the later window. [DIR001, DIR002, DIR003, DIR004, DIR005]
- Pairwise relations confirm this. Before, each of A14, A15 and A20 always co-occurred with A22 (A22 first) and with A24 (the alternative activity first), and stood in a mixed order with A23; in the later window, every pair involving one of the three is either "only the other activity" (100 in 100 traces) or "neither". [REL003, REL004, REL005, REL007, REL008, REL009, REL010, REL011, REL012]
- Event positions show only small shifts: A22's mean relative position moved from about 0.46 to 0.47 and A24's from about 0.57 to 0.55, while A14, A15 and A20 have no position observations in the later window. [POS001, POS002, POS003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the alternative block of A14, A15 and A20 is no longer executed in the later window. Earlier, exactly one of the three ran in each trace between A22 and A24 — directly after A22 in about 45 in 100 traces and after A23 in about 55 in 100 — whereas in the later window every observed trace passes from A22 directly to A23 and from A23 directly to A24, and none of the three activities appears. [OCC001, OCC002, OCC003, DIR004, DIR005, REL003, REL005, REL012]

The screening context supports this reading: 25 control-flow items qualified, many times the roughly 0.37 expected by chance in an unchanged process, and every item's difference exceeded about 199 of 200 random re-splits. The disappearance is shown directly (64, 56 and 80 traces contained the activities before versus 0 afterwards) and consistently across occurrence, direction, relation and position indicators, all describing one underlying behaviour: the bypass of the block via A22 → A23 → A24. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, POS001, POS002, POS003]

Limitations: zero participation in the later window means only that the activities were not observed in these 200 traces, so a residual execution rate too low to observe cannot be ruled out; and because all items come from control-flow indicators over the same traces, they are not independent confirmations. [OCC001, OCC002, OCC003]

Other differences: none beyond the small position shifts of A22 and A24 noted above, which are consistent with the same change. [POS004, POS005]