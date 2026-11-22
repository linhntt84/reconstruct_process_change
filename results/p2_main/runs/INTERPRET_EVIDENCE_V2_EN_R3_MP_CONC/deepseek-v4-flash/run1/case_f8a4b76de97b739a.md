### Observed differences

- In the later window, A09 is no longer observed: before it appeared in about 54% of traces (mean 1.54 per trace), after it appears in none. [OCC003, POS004, DIR006]
- A01 and A02 appear in the later window: A01 in about 59% of traces (mean 1.545), A02 in about 87% of traces (mean 0.865); both were absent before. [OCC001, OCC002, POS001, POS002]
- A14 becomes much more frequent: participation rises from about 39% to 89% of traces, and mean occurrences per trace from 0.385 to 1.73. [OCC004, POS005]
- The routing around A14 changes: A08's outgoing transitions to A14 rise from about 28% to 65%, while its transitions to A17 fall from 35% to 7%; A17's outgoing transitions to A14 rise from 0 to about 89%. [DIR005, DIR010]
- A14 and A17, which were mutually exclusive before (cooccurrence 0), now co-occur in about 42% of traces, often interleaved. [REL038]
- A08 and A14, and A07 and A14, now co-occur in about 89% of traces (before about 39%). [REL029, REL027]
- The distance between several activity pairs increases: e.g., A08 and A17 are now typically 2–5 steps apart instead of 1 step; A07 and A17 similarly. [LAG005, LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process changed from a path that included A09 to a path that includes A01 and A02, with A14 becoming a central activity that now co-occurs with A17, A08, and A07, whereas before A14 and A17 were alternatives. Specifically, A09 was removed, A01 and A02 were added, and the routing shifted so that A08 and A17 now lead to A14 instead of to each other. The large number of consistent control-flow items (67 vs. 0.76 expected by chance) makes a sampling artefact unlikely.

Other differences: A17's position moved slightly earlier (mean from 0.93 to 0.86), and the gaps between several activity pairs increased, consistent with the reordering of the path. A competing explanation that cannot be fully ruled out is that A09 was simply not sampled in the later window, but the consistency of its disappearance across occurrence, position, and relation indicators makes this unlikely.