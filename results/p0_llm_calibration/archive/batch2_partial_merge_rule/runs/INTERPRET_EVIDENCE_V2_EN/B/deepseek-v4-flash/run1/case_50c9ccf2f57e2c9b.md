### Observed differences

- In the later window, activity A06 appears in about 31% of traces (up from about 11%), with mean occurrences per trace rising from 0.105 to 0.33. [OCC002]
- Activity A04 appears less often: participation fell from about 11% to 4%. [OCC001]
- A06 occurs later in traces: its median relative position moved from about 0.51 to 0.90. [POS001]
- A06's outgoing routing became concentrated: before, its top successor A44 took about 25% of transitions; after, A44 takes about 85%. [DIR001]
- Several activities changed their successors: A21 now goes to A30 in about 52% of transitions (previously 0%), A22 to A30 in about 55% (previously 0%), A23 to A30 in about 50% (down from 98%), and A24 to A30 in about 39% (down from 99%). A23 and A24 also now go to A21/A22 in substantial shares. [DIR002, DIR003, DIR004, DIR005]
- A29's successors shifted from A21/A22 (about 49% each) to A23/A24 (about 27% and 25%), while still going to A21/A22 in about 24% and 21%. [DIR006]
- A43 now goes to A06 in about 38% of transitions (previously about 3%), while its share to A44 fell from about 89% to 60%. [DIR007]
- A06 co-occurs more with A29, A30, A43 and A44; in particular, A29 before A06 rose from about 5% to 28%, A30 before A06 from 5% to 27%, A43 before A06 from 3.5% to 22%, and A06 before A44 from 5% to 24%. [REL001, REL002, REL003, REL004]
- A22 and A24 co-occur less (30% to 19%), and the order reversed: A22 before A24 fell from 30% to 8%, while A24 before A22 rose from 0% to 10%. [REL005]
- Lag distributions shifted for many pairs, e.g., A21–A30 and A22–A30 now often have lag 1 (about 52% and 55%, previously 0%), while A23–A30 and A24–A30 now often have lag 2 (about 48% and 61%, previously near 0%). [LAG002, LAG004, LAG006, LAG007, LAG008, LAG009, LAG010, LAG011]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in routing and ordering: in the later window, A06 is executed more often and later, frequently after A29, A30 or A43 and before A44, while several activities (A21, A22, A23, A24) now route to A30 instead of to each other, and A29 routes to A23/A24 instead of A21/A22. These changes are directly shown by successor distributions, co-occurrence relations, and lag shifts, and they involve multiple distinct activities. The main limitation is that A30's own outgoing behaviour is not observed, so the full shape of the new path cannot be characterised; also, some individual lag items rest on few observations (e.g., A23–A22 had only 1 supporting trace before), but the overall pattern is consistent across many indicators. Sampling differences in variant frequencies are unlikely to explain the breadth of these coordinated changes.