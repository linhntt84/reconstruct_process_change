### Observed differences

- In the later window, activities A20, A21, A30, A31, A32, which were present in about 99–100% of traces in the earlier window, are present in at most 1.5% of traces (A30 1.5%, A32 1.5%, A20 0.5%, A21 0.5%, A31 0.5%). [OCC003, OCC004, OCC009, OCC010, OCC011]
- In the later window, activities A22, A23, A24, A25, A19, A04 appear or increase: A22 from 0% to 21%, A23 from 1.5% to 24.5%, A24 from 0% to 16%, A25 from 0.5% to 23%, A19 from 0.5% to 17.5%, A04 from 10.5% to 33.5%. [OCC001, OCC002, OCC005, OCC006, OCC007, OCC008]
- The successors of the new activities point to A33: A22, A23, A24, A19 all lead to A33 in the later window (A22 100%, A23 92%, A24 97%, A19 89%), while the old activities A20, A21, A30, A31, A32 had successors among themselves and A33 in the earlier window. [DIR003, DIR006, DIR007, DIR008, DIR004, DIR005, DIR009, DIR010, DIR011]
- A48's successors changed from the old set (A20, A21, A30, A31, A32) to the new set (A25, A22, A19, A23, A24) in the later window. [DIR012]
- Co-occurrence of A15 and A16 with the old activities dropped from ~99.5% to ~0.5–1.5%, while co-occurrence with the new activities (A22, A23, A25) rose from ~0–1.5% to ~21–24.5%. [REL015, REL016, REL020, REL021, REL022, REL023, REL024, REL028, REL029, REL030, REL017, REL018, REL019, REL025, REL026, REL027]
- The order between the old activities and A33 changed: in the earlier window A20, A21, A30, A31, A32 almost always preceded A33 (A_before_B ~0.98), in the later window these activities are absent and A33 is present alone. [REL048, REL057, REL085, REL088, REL090]
- A04 now co-occurs with A15, A16, A33, A48 in about 33.5% of traces, up from 10.5%, and its position moved earlier (mean from 0.49 to 0.28). [OCC001, POS001, REL001, REL002, REL013, REL014]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the process changed from a variant that always executed a set of activities (A20, A21, A30, A31, A32) to a variant that instead executes a different set (A22, A23, A24, A25, A19, A04), while the core activities A15, A16, A33, A48 remain. The change is directly shown by the near-total disappearance of the old activities, the appearance of the new ones, and the corresponding shifts in successors (e.g., A48 now leads to the new activities) and co-occurrence (A15/A16 now co-occur with the new activities instead of the old ones). The large number of qualifying items (158 vs 1.22 expected by chance) rules out random sampling as an explanation.

Other differences: A04 and A19 also increased in participation and moved earlier in the trace; A33 moved slightly earlier and A48 slightly later, consistent with the new activities being inserted before them. The evidence cannot rule out that the old activities are still possible but simply not used in the later window, or that the two windows represent different case types rather than a temporal change.