### Observed differences

- Three activities ran in about half of all cases before but are almost absent afterwards: A32, A33 and A38 each appeared in roughly 97–98 of 200 traces before, and in only 1 of 200 traces (about 0.5%) in the later window. [OCC005, OCC006, OCC007]
- A27 moved the opposite way: from about 52% of traces (103 of 200) to virtually all of them (199 of 200), with about one execution per trace. Before, A27 and the trio A32/A33/A38 never shared a trace — they were strict alternatives; in the later window A27 co-occurs with A14, A15, A26 and A28 in about 995 of 1,000 traces, typically after A14 or A26 and before A28. [OCC004, REL022, REL023, REL024, REL009, REL013, REL017, REL021]
- A26's outgoing flow consolidated on A27: about 50% of its outgoing transitions led to A27 before (with A38, A33 and A32 taking most of the rest), versus about 98% in the later window. [DIR006]
- A04 became far less frequent: present in about 68% of traces before (136 of 200) versus about 22% after (43 of 200). A14 now continues to A15 in about 82% of its occurrences (before about 36%) instead of to A04 (before about 63%, now about 10%), and A14 runs without A04 in about 79% of traces, up from 32%. [OCC002, DIR004, REL001]
- A04's own routing spread out: the share of its outgoing transitions leading to A15 fell from about 90% to about 48%, distributed instead across many activities. [DIR002]
- Spacing shifted consistently with these routing changes: A28 now follows A26 at a distance of two steps in about 95% of cases (before, the distance split roughly evenly between two and four steps), and A15 immediately follows A14 in about 47% of cases (before about 19%). [LAG003, LAG002]
- Two low-frequency activities became more common: A08 from 5% to about 21% of traces, A02 from 5% to 15%. [OCC003, OCC001]

### Inference

Support level: Supported hypothesis

Fifty-six control-flow items qualified, against roughly 0.74 expected if nothing had changed, so the volume of flagged behaviour cannot be explained by random re-splits of a stable process. [OCC001–OCC007, DIR001–DIR009, REL001–REL030, LAG001–LAG010]

The evidence supports the hypothesis of a structural change in which the alternative block formed by A32, A33 and A38 is no longer executed while A27 became part of virtually every case. Before, each case ran either A27 (about 52% of cases) or the trio A32/A33/A38 together (about 49%), never both; in the later window the trio is essentially unobserved, A27 runs in about 995 of 1,000 cases, and A26 leads to A27 in nearly all of its outgoing transitions. The pattern is direct and consistent across participation, co-occurrence, routing and spacing indicators. [OCC004, OCC005, OCC006, OCC007, DIR006, REL021, REL022, REL025, REL028, LAG003]

Limitations: zero participation only means these activities were not observed in the later sample, so removal versus extreme rarity cannot be distinguished; several items re-describe the same trace behaviour and are not independent confirmations; and the routing and spacing profiles of A32, A33 and A38 in the later window rest on a single trace each. A competing explanation the evidence cannot rule out is that the later window simply contains a different mix of case variants rather than a changed process definition. [DIR007, DIR008, DIR009, LAG004–LAG010]

Other differences: A04 was largely bypassed — A14 now proceeds directly to A15 rather than through A04, whose participation fell from about 68% to about 22%; whether this belongs to the same restructuring or is an independent change cannot be determined. A08 and A02 also became more frequent (about 5% to about 21%, and 5% to 15% of traces), though on small bases of 10–41 traces per window. [OCC002, DIR004, REL001, REL002, OCC003, OCC001]