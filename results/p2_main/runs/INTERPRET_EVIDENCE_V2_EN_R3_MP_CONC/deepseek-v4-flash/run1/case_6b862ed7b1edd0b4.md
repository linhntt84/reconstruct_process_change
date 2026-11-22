### Observed differences

- A06 participation rose from about 24% to 73% of traces, and its mean occurrences per trace from 0.25 to 0.76. [OCC001]
- A08 participation fell from 20% to 7.5% of traces. [OCC002]
- A19, A20 and A25 participation rose from about 48% to nearly 100% of traces. [OCC003, OCC004, OCC005]
- A06's outgoing transitions changed: before it went to many activities (A15 21%, A47 15%, A45 13%), after it goes to A16 in 88% of its transitions. [DIR001]
- A15's outgoing transitions: before to A16 94%, after to A16 58% and to A06 40%. [DIR003]
- A41's outgoing transitions: before to A26 45% and A19 37%, after to A19 96%. [DIR006]
- Many pairs among A06, A14, A15, A16, A19, A20, A25, A26, A41 now co-occur in nearly all traces (e.g., A14-A19 from 48% to 99.5%, A06-A19 from 13% to 72.5%) with fixed orders. [REL004, REL009, REL018, REL020, REL021, REL022, REL023, REL024, REL025, REL026]
- A06's position shifted earlier (mean relative position from 0.50 to 0.25). [POS001]
- A06 now immediately precedes A16 in 97% of co-occurrences (before 18% at lag 1). [LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports a change in control flow: a set of activities (A06, A14, A15, A16, A19, A20, A25, A26, A41) now almost always co-occur in a fixed order, with A06 inserted early and A08 becoming rare. Specifically, A06's participation increased from about 24% to 73%, and it now precedes A16, A19, A20, A25, A26, and A41; A15 now often leads to A06 instead of A16; A41 now leads to A19 instead of A26. A08's participation dropped from 20% to 7.5%. The large number of qualified items (62 vs 0.84 expected) and the consistency across OCC, DIR, REL, POS, and LAG make a chance explanation unlikely. The exact order among the later activities (A19, A20, A25, A26, A41) is not fully resolved, and some LAG items have low support (e.g., A15-A26 after support 1). A competing explanation is that the change reflects a shift in the frequency of existing variants rather than a new structure, but the appearance of new edges (A15→A06, A06→A16) and the near-universal co-occurrence of previously optional activities point to a structural change.

Other differences: A08 decreased, A06 increased, and A19/A20/A25 became near-universal; these are part of the same overall shift.