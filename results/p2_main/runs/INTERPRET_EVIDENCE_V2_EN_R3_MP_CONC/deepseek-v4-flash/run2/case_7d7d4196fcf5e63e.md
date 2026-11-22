### Observed differences

- A02 changed from appearing in about half of traces (48.5%) to every trace, with mean occurrences rising from 1.0 to 1.77 and its median position moving from about 0.51 to 0.0 (start of the trace). [OCC002, POS002]
- A02's outgoing transitions shifted from 100% to A01 to about 57% to A04 and 43% to A03. [DIR001]
- A08 changed from appearing in every trace (mean 2.0) to 45% of traces (mean 0.77), and its median position moved from 0.10 to 0.50 (later in the trace). [OCC005, POS004]
- A08's outgoing transitions shifted from 50% A03 / 50% A04 to 100% A02. [DIR004]
- A06's outgoing transitions shifted from about 51% A02 / 49% A07 to 53% A08 / 47% A07, while A06 participation dropped from 48.5% to 29%. [DIR003, OCC003]
- A01 participation dropped from 48.5% to 30.5% and its position moved earlier (mean 0.58 to 0.37). [OCC001, POS001]
- A02 and A04 now co-occur in all traces (was 48.5%), with A02 before A04 in 55% and interleaved in 45%. [REL006]
- A02 and A01 now co-occur less (48.5% to 30.5%), with A02 occurring alone in 69.5% of traces. [REL001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow structure: A02 has become an early, mandatory activity that is followed by A03 or A04 instead of A01, while A08, previously present in all traces and followed by A03/A04, now occurs less often and is followed by A02, creating a new loop A06 → A08 → A02 → A03/A04. This is directly shown by the routing changes (DIR001, DIR004, DIR003), the participation and position shifts (OCC002, OCC005, POS002, POS004), and the co-occurrence change between A02 and A04 (REL006). The number of qualifying items (64) far exceeds the 0.36 expected by chance, so the overall pattern is not a sampling artefact.

Other differences: A01, A06, and A07 decreased in participation; A01 moved earlier; A08 moved later; A03 now sometimes leads to A01. These are not part of the main hypothesis.

A competing explanation that cannot be fully ruled out is that the observed differences reflect a shift in case mix or variant frequencies rather than a true structural modification, but the direct successor changes and the strong co-occurrence pattern make a structural change the most plausible interpretation.