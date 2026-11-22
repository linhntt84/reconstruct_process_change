### Observed differences

- In the later window, activities A16, A17, and A18 appear in about 25% of traces, down from about 75% in the earlier window; activities A19, A20, and A21 appear in about 75% of traces, up from about 25%. [OCC001–OCC006]
- The outgoing transitions of A15 shifted: in the earlier window, about 75% of its successors were A16/A17/A18 (roughly 26%, 23%, and 26% respectively) and about 25% were A19/A20/A21; in the later window, about 75% are A19/A20/A21 (roughly 25%, 22%, and 29%) and about 25% are A16/A17/A18 (each about 8–9%). [DIR001]
- Co-occurrence patterns changed accordingly: A15 co-occurs with A16/A17/A18 in about 25% of traces (down from 75%), and with A19/A20/A21 in about 75% (up from 25%). [REL001–REL006]
- The activities A16–A18 now rarely co-occur with each other (about 25% of traces, down from 75%) and mostly appear without each other; A19–A21 now co-occur with each other in about 75% of traces (up from 25%). [REL007, REL008, REL013, REL022, REL023, REL025]
- A25, which previously co-occurred with A16–A18 in about 75% of traces, now co-occurs with A19–A21 in about 75% of traces. [REL012, REL017, REL021, REL024, REL026, REL027]
- The lag between A15 and A19 shifted: in the earlier window, A19 followed A15 within one step in about 54% of cases; in the later window, that share dropped to about 33%, while a three-step lag rose from 20% to 39%. [LAG001]
- The elapsed time between completion of A10 and A11 increased from a mean of about 1.0 hour to about 2.0 hours (median from 0.99 to 1.99 hours). [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process changed from executing one set of activities (A16, A17, A18) after A15 to executing an alternative set (A19, A20, A21) after A15. In the later window, A15's successors are predominantly A19–A21, and these activities now co-occur with each other and with A25, while A16–A18 have become rare and no longer co-occur with each other or with A25. The lag change for A15–A19 is consistent with A19 now being part of the main path. The large number of control-flow items (35 vs 0.53 expected by chance) rules out random sampling variation.

Other differences: The timing between A10 and A11 doubled (mean and median from about 1 hour to about 2 hours), indicating a separate change in timing. [TWAIT001]

A competing explanation that cannot be fully ruled out is that the observed change reflects a replacement of one set of activities by another (e.g., relabelling) rather than a shift in routing between existing alternatives, but the direct evidence of successor and co-occurrence changes supports the branch-switch interpretation.