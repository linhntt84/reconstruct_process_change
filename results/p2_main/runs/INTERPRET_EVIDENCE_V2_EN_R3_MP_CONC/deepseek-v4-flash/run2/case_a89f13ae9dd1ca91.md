### Observed differences

- In the earlier window, activities A21, A22, and A23 occurred in every trace (100% participation); in the later window they occur in about 0.5% of traces (1 trace each). [OCC004, OCC005, OCC006]
- In the earlier window, activities A14, A15, and A16 did not occur at all; in the later window they occur in about 30%, 33%, and 37% of traces respectively. [OCC001, OCC002, OCC003]
- The outgoing transitions of A39 changed: before, it led to A21, A22, and A23 (about 35%, 31%, and 35% of its transitions); after, it leads to A14, A15, and A16 (about 30%, 33%, and 37%). [DIR007]
- A14, A15, and A16 each lead to A24 in the later window (100% of their transitions), and they appear before A24 in the same traces. [DIR001, DIR002, DIR003, REL006, REL014, REL021]
- In the earlier window, A21, A22, and A23 were followed by A24 (with varying lags); in the later window these activities are essentially absent, so those paths are gone. [REL027, REL032, REL036, LAG002, LAG003, LAG006]
- A14, A15, and A16 never co-occur with each other; they are alternatives. [REL001, REL002, REL010]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process replaced a set of activities (A21, A22, A23) with a new set (A14, A15, A16) in the same position: A39 now leads to one of A14/A15/A16, which then leads to A24, whereas before A39 led to one of A21/A22/A23, which then led to A24. This is directly shown by the occurrence changes, the successor changes from A39, and the relational order (A39 before A14/A15/A16 before A24). The number of evidence items (71) far exceeds the 0.64 expected by chance, so the overall difference is not a sampling artifact. A competing explanation that cannot be fully ruled out is that the new activities are a rare variant that happened to appear in the later window, but their consistent appearance in about a third of traces and the complete disappearance of the old activities make this unlikely.

Other differences: The position of A24 shifted slightly earlier (mean position from about 0.43 to 0.39), and A39 shifted slightly later (mean from 0.31 to 0.33), but these are small and likely secondary to the main replacement. [POS007, POS008]