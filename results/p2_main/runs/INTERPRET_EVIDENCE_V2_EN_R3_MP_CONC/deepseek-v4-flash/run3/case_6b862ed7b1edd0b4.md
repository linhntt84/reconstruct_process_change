### Observed differences

- In the later window, activity A06 appears in about 73% of traces (up from about 24%), with mean occurrences per trace rising from 0.25 to 0.76, and it occurs earlier in the trace (median position from 0.39 to 0.21). [OCC001, POS001]
- Activities A19, A20, and A25 appear in about 99.5% of traces (up from about 48%), with mean occurrences near 1.0. [OCC003, OCC004, OCC005]
- Activity A08 appears in about 7.5% of traces (down from 20%). [OCC002]
- The outgoing transitions of A06 changed: it now goes to A16 in about 88% of its transitions (up from 8%), while its previous many alternatives (A15, A47, A45, etc.) almost disappeared. [DIR001]
- A15 now goes to A06 in about 40% of its transitions (up from 1%), and to A16 in about 58% (down from 94%). [DIR003]
- A41 now goes to A19 in about 96% of its transitions (up from 37%), and to A26 in about 0.5% (down from 45%). [DIR006]
- The co-occurrence of A06 with A14, A15, A16, A19, A20, A25, A26, and A41 increased from about 24% (or 13% for A19/A20/A25) to about 73% (or 72.5%). [REL001-REL008]
- The co-occurrence of A14, A15, A16 with A19, A20, A25 increased from about 47-48% to about 99.5%. [REL009-REL017]
- The order became more fixed: A14 before A19/A20/A25 in about 98% of traces (up from 46-47%); A41 before A19/A20/A25 in about 97% (up from 47%); A25 before A20 in about 97.5% (up from 46.5%). [REL009-REL011, REL021-REL022, REL026]
- A06 now typically appears immediately before A16 (lag 1 in 97% of the pairs, up from 18%), and about 4-5 steps before A19/A25. [LAG002, LAG003, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process changed so that a set of activities (A06, A19, A20, A25, A26, A41, A16, A14, A15) are now executed in almost every case, with A06 becoming much more frequent and earlier, and A08 becoming less frequent. The routing among these activities also changed: A06 now typically leads to A16, A15 now often leads to A06, and A41 now typically leads to A19. The order among these activities became more fixed, with A14 before A19/A20/A25, A41 before A19/A20/A25, and A25 before A20. This is supported by the large number of evidence items (62 vs 0.84 expected by chance) and the consistency across OCC, DIR, REL, and LAG indicators. A competing explanation that the differences are due to random sampling is unlikely given the magnitude and consistency, but the exact sequence of all activities is not fully determined because some pairs show interleaving (e.g., A15 with A19/A20/A25).

Other differences: A08 decreased in participation from 20% to 7.5%. [OCC002] Also, A26's position shifted slightly later (mean from 0.41 to 0.44). [POS002]