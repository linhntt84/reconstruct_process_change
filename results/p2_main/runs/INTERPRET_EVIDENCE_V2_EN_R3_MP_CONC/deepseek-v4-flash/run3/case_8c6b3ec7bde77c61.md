### Observed differences

- In the earlier window, activities A20, A21, A30, A31, and A32 were present in about 99–100% of traces (e.g., A20 0.995, A21 0.995, A30 0.995, A31 0.995, A32 0.995). In the later window, each of these appears in at most 1.5% of traces (A20 0.005, A21 0.005, A30 0.015, A31 0.005, A32 0.015). [OCC003, OCC004, OCC009, OCC010, OCC011]
- Conversely, activities A19, A22, A23, A24, and A25 were rare or absent in the earlier window (A19 0.005, A22 0, A23 0.015, A24 0, A25 0.005) and appear in the later window in 16–24.5% of traces (A19 0.175, A22 0.21, A23 0.245, A24 0.16, A25 0.23). [OCC002, OCC005, OCC006, OCC007, OCC008]
- A04 increased from 10.5% to 33.5% of traces. [OCC001]
- A33 and A48 remain present in all traces in both windows (co-occurrence with A15, A16, and each other stays at 1.0). [REL013, REL014, REL048, REL049]
- The old activities A20, A21, A30, A31, A32 were heavily interconnected: they co-occurred with each other and with A15, A16, A33, A48 in about 99% of traces in the earlier window (e.g., A20–A21 0.995, A20–A30 0.995, A21–A31 0.995). In the later window, these co-occurrences drop to near zero (e.g., A20–A21 0.005, A20–A30 0.005, A21–A31 0.005). [REL040, REL045, REL046, REL054, REL055, REL083, REL087]
- The new activities A19, A22, A23, A24, A25 now co-occur with A15, A16, A33, and A48 in moderate shares (e.g., A22–A15 0.21, A23–A15 0.245, A25–A15 0.23, A22–A33 0.21, A23–A33 0.245, A25–A33 0.23). [REL017, REL018, REL019, REL065, REL072, REL081]
- A04 now often precedes A16: in the later window, A04–A16 co-occurrence is 0.335 and A_before_B is 0.145, while in the earlier window co-occurrence was 0.105 and A_before_B 0.02. [REL002, LAG001]
- A15 and A16 remain present in all traces, but their mean position shifts slightly later (A15 from 0.174 to 0.194, A16 from 0.204 to 0.226). [POS002, POS003]

### Inference

Support level: Supported hypothesis

The process changed from a stable core of activities A20, A21, A30, A31, and A32 that were executed in nearly all traces to a new set of activities A19, A22, A23, A24, and A25 that are now executed in a substantial share of traces, while A33 and A48 remain always present. The evidence is direct and consistent: occurrence, co-occurrence, and successor relations all shift in the same direction, and the number of qualifying items (158) far exceeds the 1.22 expected by chance, so the overall pattern is not a sampling artifact. The new activities appear in only 16–24% of traces, so they are not universal, and the old activities are almost absent, indicating a replacement of a near-universal set by a partial set. A competing explanation that cannot be ruled out is a change in case mix (different types of cases) rather than a change in the process itself.

Other differences: A04 increased from 10.5% to 33.5% and now often immediately precedes A16. A15 and A16 remain always present but shift slightly later in the trace.