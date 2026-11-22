### Observed differences

- In the earlier window, work on the six offer-handling activities — A01, A03, A13, A14, A17 and A22 — was spread thinly across many resources: on each activity the ten most frequent named resources held only about 3–10 in 100 assignments each, and a long tail of further resources accounted for roughly 37–52 in 100. In the later window, assignments concentrate on a smaller set of resources — on A22, User_61 rises from about 4 in 100 to about 14 in 100 and User_55 from none observed to about 13 in 100 — while the long-tail share falls to roughly 30–41 in 100. [ASSIGN001, ASSIGN002, ASSIGN003, ASSIGN004, ASSIGN005, ASSIGN006]
- A24 changed most sharply. In the earlier window, validation was spread over 21 distinct resources, with the most frequent one performing about 22 in 100 validations (95 of 200 traces). In the later window, every observed validation (83 of 200 traces) was assigned to the single resource User_107, and the concentration index rose from about 0.09 to 1.0. [ASSIGN007, CONC001]
- All eight differences are far larger than random re-splits produce: each exceeds about 99.9% of 2,000 reference comparisons. [ASSIGN001, ASSIGN002, ASSIGN003, ASSIGN004, ASSIGN005, ASSIGN006, ASSIGN007, CONC001]
- Screening qualified eight resource items where only 0.005 would be expected by chance in that family; no control-flow or timing items qualified (0 against 0.17 and 0.015 expected). [screening]

### Inference

Support level: Supported hypothesis

The evidence supports a reallocation of work toward fewer resources. Across the offer-handling activities (A01, A03, A13, A14, A17, A22), assignments moved from a diffuse distribution, with roughly half of the work in a long tail of resources, to a small set of resources including User_61 and User_55; in the extreme case, A24, previously shared by about 21 resources, became assigned exclusively to User_107. [ASSIGN001, ASSIGN002, ASSIGN003, ASSIGN004, ASSIGN005, ASSIGN006, ASSIGN007, CONC001]

Supporting signs: the resource family produced eight qualifying items against a chance expectation of 0.005, far beyond what an unchanged process typically yields; the two indicator types agree in direction, with the assignment profiles redistributing toward the same resources and the concentration index for validation rising in step with its single-resource profile; and every difference is unusual for random re-splits. [ASSIGN007, CONC001, screening]

Limitations: ASSIGN007 and CONC001 describe the same validation behaviour, so they corroborate but do not independently confirm it. The evidence shows allocation shares, not assignment rules, and cannot distinguish a deliberate reassignment from a change in which resources were available, nor establish whether the validation concentration and the broader redistribution are one coordinated change or two separate ones. Resource codes are anonymous, so no roles or teams can be inferred. [ASSIGN007, CONC001]

Other differences: none — no control-flow or timing items qualified at the configured thresholds. [screening]