### Observed differences

- In the earlier window, activities A14 and A15 occurred in all 200 traces; in the later window they occur in about 105 traces (52.5%). Activities A20 and A21 dropped from about 50% to about 29% of traces, and A22 from about 50% to about 24%. [OCC001, OCC002, OCC003, OCC004, OCC005]
- The outgoing transitions of A38 changed: before, all 200 transitions went to A14; after, about 52.5% go to A14 and about 47.5% go to A23. [DIR001]
- The lag between A38 and A23 changed: before, A23 always occurred 4 or 5 positions after A38; after, about 47.5% of cases have A23 immediately after A38 (lag 1), and the rest still at lag 4 or 5. [LAG001]
- Co-occurrence of A14 with A23 and with A38 dropped from 100% to 52.5%, with the remaining 47.5% of traces containing A23/A38 but not A14. The same pattern holds for A15, and for A20/A21/A22 with A23/A38. [REL005, REL006, REL010, REL011, REL014, REL015, REL017, REL018, REL019, REL020]
- Waiting times between A28 and A34 decreased from a mean of about 0.91 hours to about 0.45 hours; between A35 and A34 from about 0.20 to about 0.08 hours. [TWAIT001, TWAIT002]
- The waiting time between A38 and A14 increased from about 1.99 to about 3.03 hours, while the number of such transitions fell from 200 to 105. [TWAIT003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in about half of the cases the process now bypasses a group of activities (A14, A15, A20, A21, A22) that were previously always executed between A38 and A23. In those cases, A38 now leads directly to A23 (lag 1) instead of going through the skipped activities. This is directly shown by the successor change (DIR001), the lag change (LAG001), the drop in occurrence of the skipped activities (OCC001–OCC005), and the co-occurrence changes (REL005, REL006, REL010, REL011, REL014, REL015, REL017–REL020). The remaining cases still follow the old path. The number of control-flow evidence items (29) far exceeds the 0.45 expected by chance, so the overall pattern is unlikely to be a sampling artefact.

Other differences: The waiting times between A28–A34 and A35–A34 decreased, and the waiting time between A38 and A14 increased in the remaining cases. These are timing changes independent of the structural bypass. [TWAIT001, TWAIT002, TWAIT003]

A competing explanation that cannot be fully ruled out is that the skipped activities are still present but not observed in the later window due to sampling; however, the direct successor and lag evidence make this unlikely. [DIR001, LAG001]