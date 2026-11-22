### Observed differences

- In the later window, activity A01 appears in all 200 traces (mean 1.0 per trace) whereas it was absent in the earlier window; it occurs early (mean position 0.29). [OCC001, POS001]
- Activity A09, present in 45% of earlier traces (90 of 200) and at the end (mean position 0.998), is absent in the later window. [OCC002, POS006]
- A02's outgoing transitions shift: in the earlier window 86.5% went to A04; in the later window 54% go to A01 and 44% to A04. [DIR002]
- A04's outgoing transitions shift: in the earlier window the main successors were A07 (37%), A10 (24%), A03 (20%), A05 (15%); in the later window A01 becomes the most frequent successor (39%), with A07 (23%), A10 (17%), A05 (10%), A03 (8%). [DIR003]
- A01 now co-occurs with A02, A03, A04, A06, A07, A10 in most traces, whereas before these activities occurred without A01; A01 precedes A03, A06, A07, A10 in the large majority of co-occurrences, while with A04 the order is mixed (55% A01 before A04, 45% A04 before A01). [REL001, REL002, REL003, REL004, REL005, REL007]
- A09 no longer co-occurs with A02, A03, A04, A06, A10; in the earlier window it co-occurred with them in 45% of traces, in the later window it is absent. [REL008, REL009, REL010, REL011, REL013]
- The distance (in event positions) between A02 and several later activities increases: e.g., A02–A03 lag of 4 steps rises from 0% to 46%, A02–A04 lag of 2 steps rises from 10% to 47%, A02–A10 lag of 4 steps rises from 0% to 47%. [LAG001, LAG002, LAG005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new early activity A01 was introduced into the process, and activity A09 was removed. In the earlier window A01 did not occur at all, while in the later window it occurs in every trace and is positioned early; A09 occurred in 45% of earlier traces at the end and disappears completely. The routing changes are consistent: A02 and A04 now frequently lead to A01, and A01 is followed by most other activities. The increased lags between A02/A04 and later activities reflect the insertion of A01 before them. The screening comparison (34 control-flow items vs 0.28 expected by chance) rules out chance as an overall explanation.

Other differences: The order between A01 and A04 is not fixed (both orders occur in similar proportions), and A06 becomes very rare in the later window (only 3 traces vs 90 before), though this is a minor effect. A competing explanation that cannot be fully ruled out is that A01 existed but was unobserved in the earlier window; however, its appearance in 100% of later traces and the systematic routing changes make this unlikely.