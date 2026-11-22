### Observed differences

- In the earlier window, every trace contained A21, A22, and A23 in that order (A21 before A22, A22 before A23). [OCC001, REL001, REL007]
- In the later window, A22 appears in about 57% of traces (down from 100%), and five new activities A27, A28, A33, A34, A35 each appear in about 44% of traces (up from 0%). [OCC001, OCC002–OCC006]
- A21's outgoing transitions changed: before, it always went to A22; after, it goes to A22 in about 57% of cases and to each of the five new activities in about 7–10% of cases. [DIR001]
- The new activities are not in a fixed order; for pairs among them, both orders occur in similar proportions (e.g., A27 before A28 in 23.5% and A28 before A27 in 20% of traces). [REL018–REL027]
- The time between activities A39 and A41 increased from a mean of about 1.0 hour to about 2.0 hours. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that a new alternative branch was introduced between A21 and A23. In the earlier window, the process consistently followed A21 → A22 → A23. In the later window, about 44% of traces instead follow A21 to one of A27, A28, A33, A34, or A35, which then lead to A23 (often through each other in flexible order), while the remaining about 56% still use A22. This is directly shown by the drop in A22 participation, the appearance of the five new activities, and the redistribution of A21's outgoing edges. The large number of control-flow items (45 vs 0.49 expected by chance) makes it unlikely that this is a sampling artifact. A competing explanation that cannot be fully ruled out is that these activities existed before but were extremely rare; however, their complete absence in 200 prior traces makes this unlikely.

Other differences: The timing between A39 and A41 roughly doubled (mean from 1.0 to 2.0 hours), which is a separate change in timing. [TWAIT001]