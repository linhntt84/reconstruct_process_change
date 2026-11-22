### Observed differences

- In the earlier window, A19, A20 and A25 were not observed in any of the 200 traces. In the later window, A19 appears in about 37 in 100 traces (74 of 200), A25 in about 34 in 100 (68 of 200) and A20 in about 29 in 100 (57 of 200), in each case at most once per trace. [OCC001, OCC002, OCC003]
- The three act as alternatives: in the later window they essentially never occur in the same trace (co-occurrence at most about 1 in 200), and their participation shares sum to about 99 in 100, so almost every later trace contains exactly one of them. [REL001, REL002, REL007]
- A41, which is executed in essentially every trace in both windows, changed its dominant successor: earlier, about 93 in 100 of its outgoing transitions went to A26 (with small shares to A06, A02 and a few others); later, about 34 in 100 go to A19, about 31 to A25 and about 27 to A20, while A26 receives only about 1 in 100. [DIR004]
- The three activities in turn lead almost always to A26: about 96 in 100 of A19's outgoing transitions, 98 in 100 of A20's and 97 in 100 of A25's go to A26. [DIR001, DIR002, DIR003]
- Pairwise orderings match this: in the later window, A41 precedes each of A19, A20 and A25, and each of the three precedes A26, in every trace in which it occurs; earlier, A26 was the only observed successor of A41 and the three activities never appeared. [REL003, REL006, REL008, REL010, REL011, REL014]
- By event position, the three activities sit at about one-third of the trace (mean relative position about 0.36); A26 and A31 still occur in every trace and now appear slightly later (mean position about 0.37 to 0.39 and about 0.69 to 0.71, respectively). [POS001, POS002, POS003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a three-way alternative step sits between A41 and A26 where A41 previously led directly to A26. Earlier, A41 was followed directly by A26 in about 93 in 100 of its outgoing transitions and A19, A20 and A25 did not occur; later, A41 leads to exactly one of A19, A25 or A20 (about 34, 31 and 27 in 100 of its outgoing transitions), that activity then leads almost always to A26, and about 99 in 100 later traces execute exactly one of the three, once, at about one-third of the trace, while A26 remains in every trace. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, REL001, REL003, REL006, REL008, REL011, POS004]

This reading is direct and consistent: the successor profiles and the pairwise orderings show the re-routing directly rather than through a shift in how often existing paths are taken, all 26 qualifying control-flow items fit this one picture (about 46 times the 0.56 items expected by chance over the 112 tested units), and every item's difference exceeds about 199 of 200 random re-splits of the pooled data. [DIR001, DIR002, DIR003, DIR004, REL003, REL006, REL008, REL010, REL011, REL014, screening]

An important competing explanation cannot be ruled out: the earlier window only shows that A19, A20 and A25 did not occur in 200 traces, so it cannot distinguish activities that were newly added from activities that existed earlier but were executed so rarely that none of the 200 earlier traces captured them; the long-run split among the three alternatives may also differ from the observed sample split. [OCC001, OCC002, OCC003]

Other differences: A35 appears in somewhat fewer traces in the later window (about 48 in 100, versus about 54 in 100 earlier), and A19 or A25 now precede A35 in about 20 and 15 in 100 later traces respectively; the three activities also each precede A31 whenever they occur. [REL004, REL005, REL009, REL012, REL013]