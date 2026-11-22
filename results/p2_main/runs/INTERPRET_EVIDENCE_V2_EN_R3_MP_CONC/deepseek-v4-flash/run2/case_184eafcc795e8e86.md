### Observed differences

- In the earlier window, activities A01 and A02 did not occur in any of the 200 traces; in the later window, each occurs exactly once in all 200 traces. [OCC001, OCC002]
- In the earlier window, A06 and A13 each split their outgoing transitions between A04 and each other (about 50/50). In the later window, A06 goes to A01 (about 48%) and A13 (52%), and A13 goes to A06 (48%) and A01 (52%); neither goes to A04 anymore. [DIR002, DIR004]
- In the earlier window, A01 and A02 had no outgoing transitions (they were absent). In the later window, A01 always leads to A04, and A12 always leads to A02. [DIR001, DIR003]
- In the earlier window, A12 was always the last activity (position 1.0). In the later window, A02 is always last (position 1.0), and A12 occurs slightly before the end (mean position about 0.94). [POS002, POS005]
- In the earlier window, A01 and A02 never co-occurred with any other activity (they were absent). In the later window, A01 co-occurs with A04, A06, A12, A13 and A02; A02 co-occurs with A04, A06, A12, A13 and A01. The order is: A06 and A13 occur before A01; A01 occurs before A04, A12 and A02; A04, A06, A12 and A13 occur before A02. [REL001-REL009]
- The lag between A06/A13 and A04 shifted: in the earlier window, about 21% of A06-A04 pairs were adjacent (lag 1); in the later window, none are adjacent, and the distance increased to lags 2-5. [LAG001, LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which two new activities, A01 and A02, were added to the process, and the routing was adjusted accordingly. Specifically, A01 was inserted after the A06/A13 loop and before A04/A12, while A02 was added as a new final activity after A12. The routing from A06 and A13 to A04 was replaced by routing to A01, so A04 is now reached from A01 instead of from A06/A13. This is supported by the appearance of A01 and A02 in all later traces, the changed outgoing transitions of A06, A13, A01 and A12, the ordering relations showing A06/A13 before A01, A01 before A04/A12/A02, and A02 last, and the increased lag between A06/A13 and A04. The evidence is consistent and direct, with no competing explanation that fits all these observations. A limitation is that the exact position of A04 relative to A12 is not fully specified, but the main structural change is clear.

Other differences: The relative order between A06 and A13 remains mixed (they go to each other), and A04's position shifted slightly earlier, but these are minor and do not affect the main hypothesis.