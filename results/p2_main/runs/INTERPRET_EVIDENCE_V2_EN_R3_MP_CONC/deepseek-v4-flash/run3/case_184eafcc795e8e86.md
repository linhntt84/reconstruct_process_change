### Observed differences

- In the earlier window, activities A01 and A02 were absent from all 200 traces; in the later window they appear in all 200 traces, each exactly once per trace. [OCC001, OCC002]
- In the earlier window, A01 had no observed outgoing transitions; in the later window A01 always leads to A04. [DIR001]
- In the earlier window, A12 had no observed outgoing transitions; in the later window A12 always leads to A02. [DIR003]
- The successors of A06 changed: before, about half went to A13 and half to A04; after, about half go to A01 and half to A13, with no A04. [DIR002]
- The successors of A13 changed: before, about half went to A04 and half to A06; after, about half go to A06 and half to A01, with no A04. [DIR004]
- In the earlier window, A01 and A02 did not co-occur with any other activity; in the later window they co-occur with all other activities, with A01 before A02, A01 before A04 in about half the traces (interleaved in the rest), A06 and A13 before A01, and A12 before A02. [REL001–REL009]
- The relative positions of A04, A06, A13, and A12 shifted slightly earlier (mean position decreased by about 0.04–0.08), while A01 appears around 73% of the trace length and A02 at the end (position 1.0). [POS001–POS006]
- The gap between A06 and A04, and between A13 and A04, increased: before, about 20% of traces had them one step apart; after, none did, with the distribution shifted to 2–5 steps. [LAG001, LAG003] Similarly, the gap between A06 and A12, and A13 and A12, no longer has 2-step gaps, shifting to 3–5 steps. [LAG002, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports a change in which two new activities, A01 and A02, were added to the process. A01 is inserted between A06/A13 and A04, and A02 is added as a final step after A12. This is directly shown by the appearance of A01 and A02 in every trace, the new outgoing edges A01→A04 and A12→A02, the redirection of A06 and A13 from A04 to A01, and the co-occurrence and ordering relations. The number of qualifying evidence items (25) far exceeds the 0.19 expected by chance, so the change is not a sampling artifact. A competing explanation that A01 and A02 existed before but were never observed is unlikely given they appear in all 200 later traces, but cannot be fully excluded.

Other differences: The positions of A04, A06, A13, and A12 shifted slightly earlier, and the lag distributions between A06/A13 and A04/A12 increased, consistent with the insertion of A01 and A02. These are part of the same structural change.