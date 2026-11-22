### Observed differences

- A08 became more frequent and moved earlier: its share of traces rose from about 13% to 30%, and its mean relative position fell from about 0.49 to 0.34. [OCC001, POS001]
- A08's outgoing transitions changed from a broad set of successors to mainly A19 (about 38%), A20 (29%) and A25 (21%). [DIR001]
- A19, A20 and A25 now lead almost exclusively to A26 (100%, 96% and 97% of their outgoing transitions respectively), whereas before they led to A28 and A32. [DIR002, DIR003, DIR004]
- A45's outgoing transitions changed from mostly A26 (about 92%) to A08 (25%), A19 (23%), A20 (26%) and A25 (23%). [DIR007]
- A27 now goes almost exclusively to A28 (about 98%) instead of to A19/A20/A25/A28, and A28 now goes almost exclusively to A32 (99%) instead of to A19/A20/A25/A32. [DIR005, DIR006]
- Order relations reversed: A08 now appears before A26, A27, A28 and A32 in most traces (co-occurrence rose from 13% to 30%, with A08 before them in about 27% of traces), whereas before it was roughly equally before/after. [REL001–REL004]
- A19, A20 and A25 now appear before A26 and A27 (about 29–35% of traces), whereas before they appeared after them (about 30–36% of traces). [REL005–REL010]
- Lag distances shifted: A08 and A26 are now typically 2 steps apart (was 1, 4 or 5); A19 and A26 are now 1 step apart (was 4); A45 and A26 are now 2–3 steps apart (was 1). [LAG002, LAG007, LAG014]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the control-flow order changed: A08 now appears earlier and more often, and it precedes A19/A20/A25, which in turn precede A26; previously A19/A20/A25 followed A26, and A45 led directly to A26. This is directly shown by the reversal of order relations (REL005–REL010), the new successor patterns (DIR001–DIR004, DIR007), the shift in A08's position and frequency (OCC001, POS001), and the lag changes (LAG002, LAG007, LAG014). The number of qualifying items (40) far exceeds the 0.72 expected by chance, so the overall pattern is not a sampling artefact.

Other differences: A27 and A28 now have more deterministic successors (A27→A28, A28→A32), which may be part of the same restructuring but is not required for the main hypothesis. A limitation is that some lag items rest on very few observations (e.g., LAG001 before support 1, LAG008 after support 1), but the core order changes are supported by high-support REL and DIR items.