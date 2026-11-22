### Observed differences

- Activities A19, A20 and A25 were not observed in any of the 200 earlier traces. In the later window each occurs at most once per trace: A19 in about 37 in 100 traces, A25 in about 34, A20 in about 29. [OCC001, OCC002, OCC003]
- The three are mutually exclusive alternatives: the pairs A19–A20, A19–A25 and A20–A25 practically never occur in the same trace (co-occurrence at most about 0.5 in 100), and in the later window about 99 in 100 traces contain exactly one of them. [REL001, REL002, REL007, OCC001, OCC002, OCC003]
- Earlier, about 93 in 100 of A41's outgoing transitions went directly to A26; in the later window that direct step has nearly disappeared (about 1 in 100) and about 92 in 100 go to one of the three activities (A19 about 34, A25 about 31, A20 about 27). [DIR004]
- Each of the three activities is followed almost always by A26 (about 96–98 in 100 of their outgoing transitions). [DIR001, DIR002, DIR003]
- The step distance from A41 to A26 grew: earlier the pair occurred within one step in about 94 in 100 cases; later within two steps in about 90 in 100, and within one step in only about 1 in 100. [LAG002]
- The new activities sit at about one third of the trace (mean relative position about 0.36), always after A41 and before A26 and before A31; A26's mean position moved slightly later (about 0.37 to 0.39). [REL003, REL006, REL008, REL010, REL011, REL014, POS001, POS002, POS003, POS004]
- Other differences: the gap between A31 and A35 shifted from mostly one step (about 55 in 100) to mostly two steps (about 62 in 100), A31's mean position moved slightly later (about 0.69 to 0.71), and A35 appeared in about 54 in 100 traces earlier versus about 48 later. [LAG001, POS005, REL005, REL013]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a stage of three mutually exclusive activities — A19, A20 and A25 — runs between A41 and A26: earlier, cases passed from A41 directly to A26 (about 93 in 100 of A41's outgoing transitions, within one step in about 94 in 100 cases), whereas later A41 leads to exactly one of the three (roughly 34, 31 and 27 times in 100 respectively), which then leads almost always to A26, making the A41–A26 distance two steps. This is shown directly by the successor change at A41, the outgoing edges from the three activities to A26, the shifted step distance, and their consistent placement after A41 and before A26 and A31; screening flagged 28 control-flow items where fewer than one would be expected without a change, so the pattern as a whole is not what a stable process typically produces. [DIR004, DIR001, DIR002, DIR003, LAG002, OCC001, OCC002, OCC003, REL001, REL002, REL007, REL003, REL006, REL008, REL011, REL014, POS001, POS002, POS003]

The main limitation is that zero participation in the earlier window only shows the activities were not observed there: a pre-existing but very rare alternative that later became frequent cannot be ruled out with 200 traces per window. Many items also describe the same underlying insertion (for example the several relations of A19), so they are not independent confirmations. [OCC001, OCC002, OCC003]

Other differences: the A31–A35 step distance shifted from mostly one step to mostly two, and A31 sits slightly later; the evidence does not show which behaviour, if any, now lies between them. [LAG001, POS005]