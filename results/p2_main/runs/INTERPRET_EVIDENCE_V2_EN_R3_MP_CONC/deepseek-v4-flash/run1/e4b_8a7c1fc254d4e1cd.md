### Observed differences

- Resource allocation: In the later window, for activities A01, A03, A10, A13, A14, A17, and A22, the distribution of resources changed. Previously common resources (e.g., User_46, User_3, User_35, User_37) had shares of about 5–8% in the earlier window; in the later window these shares dropped to near zero or below the top-10, while other resources (e.g., User_39, User_4, User_41, User_42) increased. For example, for A01, User_39 rose from about 4.5% to 9%, and for A10 the "OTHER" share rose from about 14% to 52%. [ASSIGN001, ASSIGN002, ASSIGN003, ASSIGN004, ASSIGN005, ASSIGN006, ASSIGN007]
- Timing: The elapsed time between completion of A09 and A04 increased: mean from about 0.017 to 0.032 hours (about doubled), median from 0.016 to 0.020 hours, and standard deviation from 0.005 to 0.116 hours. The number of such transitions fell from 132 to 105. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in resource allocation for several activities. In the later window, the set of resources performing activities A01, A03, A10, A13, A14, A17, and A22 shifted: some previously common resources were used less (e.g., User_46, User_3, User_35, User_37), while others (e.g., User_39, User_4, User_41, User_42) were used more, and the overall assignment became more spread across resources (higher "OTHER" share). This is supported by seven resource-allocation items, far exceeding the 0.007 expected by chance, and the pattern is consistent across these activities. A competing explanation that cannot be ruled out is a change in the available resource pool or user re-labelling, but the redistribution itself is directly observed.

Other differences: The time between A09 and A04 increased, with the mean roughly doubling and much higher variability. This is a separate timing change, supported by one item that also far exceeds its chance expectation (0.015). No control-flow differences were observed.