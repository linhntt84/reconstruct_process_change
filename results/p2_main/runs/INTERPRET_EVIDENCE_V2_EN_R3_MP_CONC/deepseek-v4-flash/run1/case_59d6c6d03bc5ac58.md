### Observed differences

- In the earlier window, activity A01 occurred in about 50% of traces (101 of 200); in the later window it occurred in none. [OCC001, DIR001, POS001]
- Activity A05 did not occur in the earlier window and occurred in about 46% of traces (92 of 200) in the later window. [OCC002, DIR003, POS004]
- Activity A04 was present in about 50% of traces before (99 of 200) and about 46% after (92 of 200), but its outgoing edge changed: before it always led to A02, after it always led to A05. [DIR002]
- Activity A02 was present in all traces in both windows, but its position shifted: before it was always the second event (mean position 1.0), after it is often the first event (mean 0.46, median 0). [POS002]
- The relation between A04 and A02 changed: before A04 always preceded A02 with a lag of one step; after, A04 no longer directly precedes A02, and instead A05 precedes A02 in the same traces. [LAG001, REL004, REL005]
- Before, A01 and A04 were alternatives (never co-occurred); after, A01 is absent and A04 and A05 co-occur in about 46% of traces. [REL001, REL002, REL003, REL005]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in the process: the earlier window had two alternative paths, A01→A02 and A04→A02, each taken in about half of the traces. In the later window, A01 is no longer observed, A05 appears, and the A04 path now goes through A05 before reaching A02, while a substantial share of traces (about 54%) consist of A02 alone. This is directly shown by the disappearance of A01, the appearance of A05, the change of A04's successor from A02 to A05, the new A05→A02 edge, and the shift of A02's position to earlier in the trace. The number of evidence items (15) far exceeds the 0.09 expected by chance, so the overall pattern is not a sampling artefact. A competing explanation that cannot be fully ruled out is that A01 was renamed to A05, but the routing change (A04→A05→A02 instead of A04→A02) and the emergence of A02-only traces indicate a broader restructuring rather than a simple rename.

Other differences: A04's position shifted from a mean of 0.667 to 0.5, consistent with the new path length. [POS003]