### Observed differences

- In the earlier window, three activities formed an optional block: A19, A20 and A25 each ran in roughly a third of cases (about 37, 31 and 35 in 100 traces). In the later window they are essentially unobserved — 1, 0 and 0 of 200 traces respectively. [OCC001, OCC002, OCC003]
- Before, each of the three led almost exclusively to A26 (about 95 in 100 of their outgoing transitions); in the later window A20 and A25 have no observed outgoing transitions and A19 appears in a single trace. [DIR001, DIR002, DIR004]
- A41's routing flipped: before, about 87 in 100 of its outgoing transitions went to A19, A20 or A25 (roughly 29, 26 and 32 in 100); in the later window about 86 in 100 go directly to A26. [DIR005]
- The A41→A26 distance shortened accordingly: before, A26 followed A41 two steps later in about 85 in 100 cases (three steps in about 15); in the later window it follows one step later in about 86 in 100. [LAG001]
- Relational profiles agree: before, A19, A20 and A25 co-occurred with A26 in about 31–37 in 100 traces and always preceded it, with A41 preceding them; in the later window these co-occurrences are near zero (at most about 0.5 in 100) and A26 appears without any of the three. [REL004, REL005, REL006, REL009, REL010, REL011, REL013, REL014, REL015]
- Minor positional shifts accompany this: A26's median position moved slightly earlier (about 0.38 to 0.36 of trace length) and A41's slightly later (about 0.31 to 0.32), both observed in all traces of both windows. [POS004, POS005]
- Separately, A21's outgoing routing shifted: A24 rose from about 14 to about 35 in 100 of A21's outgoing transitions, while A31 fell from about 54 to about 38, with substantial support in both windows (114 vs 101 traces). [DIR003]

### Inference

Support level: Supported hypothesis

Screening context: 29 control-flow items qualified where about 0.57 would be expected by chance if nothing had changed — roughly 50 times the chance expectation — and every item's difference exceeded about 99.5 in 100 random re-splits of the pooled data, so this set of differences is not what an unchanged process typically produces. [OCC001–LAG001]

Main hypothesis: the optional segment between A41 and A26, in which exactly one of A19, A20 or A25 was executed, was removed or is now bypassed. In the earlier window a case ran A41, then one of the three alternatives, then A26; in the later window A41 is followed directly by A26 in about 86 in 100 of its outgoing transitions, the A41→A26 distance shortened from mostly two steps to one step, and A19, A20 and A25 are no longer observed. The signs are direct and mutually consistent — the participation collapse of the three activities, their replacement in A41's successor profile by a direct edge to A26, and the shortened A41–A26 distance all describe the same structural difference, though they are not independent confirmations. [OCC001, OCC002, OCC003, DIR005, LAG001, REL004, REL009, REL013]

Limitations: the evidence cannot distinguish outright removal from the block having become extremely rare, since zero participation only means the activities were not observed in the later window; the single remaining A19 occurrence (leading to A12) is too weak to locate any residual execution, and it cannot be shown whether the direct A41→A26 edge already existed at a low, unobserved rate before. [OCC001, DIR001, DIR005]

Other differences: A21's routing shares moved toward A24 (about 14 to about 35 in 100 outgoing transitions) at the expense of A31 (about 54 to about 38); this is a redistribution among existing, well-supported successors and is not part of the main hypothesis. [DIR003]