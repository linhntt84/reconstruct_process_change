### Observed differences

- For activities A01, A03, A17, and A22, the distribution of assignments changed. In the earlier window, assignments were spread across many users, with a large share going to a long tail of other users (about 54% for A01, 54% for A03, 55% for A17, 42% for A22). In the later window, that tail shrank (to about 45%, 44%, 45%, 32% respectively), and a few users gained larger shares, e.g., User_40 rose from 0% to about 8–13% across these activities, User_3 from 0% to about 8–11%, and User_49 from about 3–4% to 6–7%. [ASSIGN001, ASSIGN002, ASSIGN003, ASSIGN004]
- For activities A16 and A24, the elapsed time between consecutive completions (TWAIT) decreased. The mean fell from about 76 hours to about 44 hours, and the median from about 93 hours to about 45 hours. The number of observed intervals increased from 48 to 57. [TWAIT001]
- No control-flow differences were observed at the configured thresholds.

### Inference

Support level: Supported hypothesis

The evidence supports a change in resource allocation: activities A01, A03, A17, and A22 are now more concentrated on a few resources (e.g., User_40, User_3, User_49) and less on a long tail of other users. This is supported by four consistent assignment items across these activities, with the share of the long tail dropping by about 10 percentage points and the named users gaining shares. The screening expectation for resource items was 0.005, and four items were observed, far exceeding chance.

Other differences: The elapsed time between completions of activities A16 and A24 decreased substantially (mean from about 76 to 44 hours, median from about 93 to 45 hours). This is a single time item but its empirical strength is very high and the expected count was 0.019, so it is also unlikely to be due to chance. No control-flow changes were observed.

A competing explanation that cannot be ruled out is that the resource change and the timing change are independent, but both are supported by the evidence.