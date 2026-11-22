### Observed differences

- In the later window, the allocation of work to resources changed for activities A01, A03, A10, A13, A14, A17 and A22. Previously common resources (e.g., User_46, User_3, User_35, User_37) decreased or disappeared, while others (e.g., User_39, User_4, User_41, User_42) increased. For most of these activities the share of work done by "OTHER" resources also rose, e.g., for A10 from about 14% to 52%, indicating a more spread distribution. [ASSIGN001, ASSIGN002, ASSIGN003, ASSIGN004, ASSIGN005, ASSIGN006, ASSIGN007]
- The elapsed time between completion of A09 and completion of A04 increased: the mean rose from about 0.017 hours to 0.032 hours (roughly doubled), the median from 0.016 to 0.020 hours, and the standard deviation from 0.005 to 0.116 hours, showing much higher variability. The number of such transitions fell from 132 to 105. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in resource allocation for several activities (A01, A03, A10, A13, A14, A17, A22): the set of resources performing these activities shifted away from a previously dominant group toward a different group, and the work became more spread across resources. This is supported by seven ASSIGN items, far exceeding the chance expectation of 0.007 for the resource family. The change is consistent across all seven activities, with the same direction of shift (decrease for User_46, User_3, User_35, User_37; increase for User_39, User_4, User_41, User_42). The support is strong, with each activity observed in at least 133 traces per window.

Other differences: The time between A09 and A04 increased and became more variable, as shown by TWAIT001. This is a separate timing change, not part of the resource-allocation hypothesis.

A competing explanation that cannot be fully ruled out is that the observed resource shift reflects a change in case mix or in the availability of specific resources rather than a deliberate reallocation policy. However, the consistency across many activities makes a chance explanation very unlikely.