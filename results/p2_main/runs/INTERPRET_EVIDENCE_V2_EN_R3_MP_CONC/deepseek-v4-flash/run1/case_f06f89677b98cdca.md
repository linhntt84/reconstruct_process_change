### Observed differences

- Activity A01 was absent in the earlier window and appears in about 48% of traces in the later window, with a mean of 0.475 occurrences per trace; it occurs late in the trace (median relative position about 0.85). [OCC001, POS001]
- In the earlier window, A18's outgoing transitions were spread across many activities (A10 19%, A06 13%, A12 13%, A16 11%, A19 11%, etc.). In the later window, about 65% of A18's transitions go to A01, with all other successors reduced. [DIR004]
- A01 and A18 never co-occurred before; in the later window they co-occur in about 48% of traces, and A18 always precedes A01. [REL001]
- A02's mean occurrences per trace rose from 0.48 to 1.01, and it now repeats in about 26% of traces (recurrence support 0.255) versus none before. [OCC002]
- A08's mean occurrences per trace fell from 0.87 to 0.475, and it no longer repeats (recurrence support dropped from 0.2 to 0). [OCC003]
- A09's outgoing transitions shifted: to A02 increased from 37.5% to 64.9%, to A07 dropped from 16.7% to 0, and to A04 dropped from 24% to 13.8%. [DIR002]
- A14's outgoing transitions shifted: to A08 dropped from 63% to 24.2%, to A06 increased from 4.9% to 21.1%, and to A15 increased from 0 to 18.9%. [DIR003]

### Inference

Support level: Supported hypothesis

The later window shows a new activity A01 that appears in about half of the traces, always after A18, and A18 now predominantly leads to A01 instead of its previous diverse successors. This supports the hypothesis that a new path A18 → A01 was added, replacing or supplementing many of A18's earlier outgoing paths. The evidence is direct: A01 was absent before and present after, A18's outgoing distribution changed from many successors to mostly A01, and A01 and A18 co-occur with A18 before A01. The screening count (9 items vs 0.2 expected by chance) indicates the overall change is not a sampling artefact. A competing explanation that A01 existed but was unobserved in the earlier window is unlikely given 200 traces with zero occurrences and 95 in the later window.

Other differences: A02 now repeats more often, A08 repeats less often, and the routing of A09 and A14 shifted toward A02 and toward A06/A15 respectively. These are separate from the A18–A01 change and are not part of the main hypothesis.