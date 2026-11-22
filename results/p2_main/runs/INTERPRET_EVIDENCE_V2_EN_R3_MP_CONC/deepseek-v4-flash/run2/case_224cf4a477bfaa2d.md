### Observed differences

- In the later window, activity A01 appears in every trace (100% vs 0% before), while A09 disappears (0% vs 45% before). [OCC001, OCC002]
- A02's outgoing transitions shift: before, about 87% went to A04; after, about 54% go to A01 and 44% to A04. [DIR002]
- A04's outgoing transitions also shift: before, A07 (37%), A10 (24%), A03 (20%), A05 (15%); after, A01 (39%), A07 (23%), A10 (17%), A03 (8%), A05 (10%). [DIR003]
- A06's outgoing transitions: before all to A09; after to A01 (67%) and A04 (33%). [DIR004]
- A01 appears early (mean position ~0.29) and precedes A03, A04, A06, A07, A10 in most cases; A09 was last (position ~1.0) and is gone. [POS001, POS006, REL002-REL007, REL013]
- The lag between A02 and later activities (A03, A04, A06, A07, A10) increases by about one step, consistent with A01 inserted between them. [LAG001-LAG005]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change: a new activity A01 is added early in the process (after A02) and becomes mandatory, while A09 is removed. The routing from A02 and A04 changes to include A01. Specifically, in the earlier window, A02 led mostly to A04, and A06 led to A09; in the later window, A02 often leads to A01, which then leads to A04 and other activities, and A09 is no longer executed. The evidence is direct: OCC shows A01 appears and A09 disappears; DIR shows new outgoing edges from A01 and changed outgoing from A02, A04, A06; REL shows A01 co-occurs with many activities and precedes them; LAG shows increased distance between A02 and later activities. Limitations: The evidence is all control flow, no time or resource changes. Also, we cannot rule out that A01 existed but was not recorded in the earlier window, but the data show it is now present in all traces.