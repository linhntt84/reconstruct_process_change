### Observed differences

- In the later window, A02 is executed in every trace (100% participation, mean 1.77 per trace) whereas in the earlier window it appeared in about 49% of traces (mean 1.0). [OCC002]
- A08, which was executed in every trace in the earlier window (100%, mean 2.0), drops to 45% participation and 0.77 mean occurrences in the later window. [OCC005]
- A01, A06 and A07 also become less frequent: A01 from 48.5% to 30.5%, A06 from 48.5% to 29%, A07 from 31% to 15%. [OCC001, OCC003, OCC004]
- The routing changes: A02 no longer leads to A01 but to A03/A04; A08 now always leads to A02 instead of A03/A04; A03 now sometimes leads to A01 instead of always A06; A06 now leads to A08 instead of A02 (still A07). [DIR001, DIR004, DIR002, DIR003]
- In the earlier window, A08 was the only activity present in all traces, and all other activities (A01, A02, A03, A04, A06, A07) only occurred in traces that also contained A08. In the later window, A02 is the only activity present in all traces, and all other activities (A01, A03, A04, A06, A07, A08) only occur in traces that also contain A02. [REL004, REL009, REL010, REL011, REL012, REL013, REL001, REL005, REL006, REL007, REL008]
- A01 and A02 occur earlier in the trace in the later window (mean position from 0.58 to 0.37 for A01, from 0.51 to 0.27 for A02), while A08 occurs later (from 0.32 to 0.52). [POS001, POS002, POS004]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process changed from a structure in which A08 was a mandatory activity and all other activities were optional and only executed together with A08, to a structure in which A02 is mandatory and all other activities are optional and only executed together with A02. This is directly shown by the participation changes (A08 from 100% to 45%, A02 from 48.5% to 100%) and by the co-occurrence relations: before, A01, A02, A03, A04, A06, A07 all only occurred with A08; after, A01, A03, A04, A06, A07, A08 all only occur with A02. The routing changes (A02 no longer to A01, A08 now to A02, etc.) are consistent with this reorganisation. The large number of qualifying items (64 vs 0.36 expected by chance) makes a chance explanation unlikely.

Other differences: A01, A06 and A07 become less frequent overall, and A01 and A02 shift to earlier positions while A08 shifts later. These are consistent with the main change but not part of the core hypothesis.

A competing explanation that cannot be fully ruled out is that the process changed in a more complex way, e.g., a new variant replaced the old one, but the observed pattern is strongly consistent with the mandatory-activity switch.