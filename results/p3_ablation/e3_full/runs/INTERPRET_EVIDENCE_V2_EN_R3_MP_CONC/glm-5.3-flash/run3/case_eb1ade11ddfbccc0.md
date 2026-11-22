### Observed differences

- Activity A03 was executed exactly once in every trace in the earlier window (200 of 200 traces), typically as the first event and before A02 (about 86 in 100 traces); in the later window it does not appear at all (0 of 200). [OCC001, POS003, REL005]
- Activity A07 was absent from the earlier window (0 of 200) and is executed exactly once in every trace in the later window (200 of 200), placed between A04 and the closing A01 (median position about three quarters through the trace). [OCC004, POS007, REL015, REL004]
- Typical traces ran A03 → A02 → (A05 or A06) → A04 → A01 in the earlier window and A02 → (A05 or A06) → A04 → A07 → A01 in the later one: A02 moved from about a quarter into the trace to the first event, A05/A06 from the midpoint to about one quarter, and A04 from three quarters to the midpoint, while A01 remained the final event throughout. [POS002, POS005, POS006, POS004, POS001, DIR002]
- The handover after A04 changed: before, about 99 in 100 of A04's outgoing transitions led to A01 (about 1 in 100 to A03); in the later window A04 always leads to A07, which in turn always leads to A01. [DIR004, DIR007]
- Distances to the closing A01 grew by one step: A04→A01 went from the immediately following event to two events later, A05/A06→A01 from two to three events, and A02→A01 from three–four to four events. [LAG005, LAG006, LAG008, LAG001]
- The edges into A03 disappeared with the activity: A02 had led to A03 in about 10 in 100 of its outgoing transitions, with rare further edges from A05, A06, A04 and A01; in the later window A02 leads only to A05 and A06, and A05/A06 lead only to A04. [DIR002, DIR003, DIR005, DIR006]
- A05 and A06 remain mutually exclusive alternatives (they never occur in the same trace in either window), but their shares shifted slightly: A05 appears in about 47 in 100 traces before versus about 53 in 100 after; A06 about 54 versus 48. [OCC002, OCC003, REL016]

### Inference

Support level: Supported hypothesis

The evidence supports a structural reorganisation around A03 and A07: A03, previously executed at the start of every observed case before A02, is no longer executed, while A07, previously unobserved, now executes in every observed case between A04 and the closing A01, so traces run A02 → (A05 or A06) → A04 → A07 → A01 instead of A03 → A02 → (A05 or A06) → A04 → A01. [OCC001, OCC004, DIR003, DIR004, DIR007, POS002, POS007]

The support is direct and consistent: participation of A03 and A07 flips completely between the windows (200 of 200 versus 0 of 200) with empirical strength of about 0.995; the successor of A04 changes from A01 to A07 and A07's successor is A01, showing the insertion point directly; the one-step increase in distance from A02, A05 and A06 to A01 and the positional shifts of A02, A05/A06 and A04 are exactly what removing the leading A03 and inserting A07 before A01 would produce; and the occurrence, direction, position, relation and lag items all describe this same coherent restructuring. [OCC001, OCC004, DIR004, DIR007, LAG001, LAG005, LAG006, LAG008, POS002, POS004, POS005, POS006]

Limitations: zero participation only means A03 was not observed in the later window, not that it was removed from the underlying process, and the evidence cannot establish whether A07 takes over A03's role or is an unrelated addition, since the two occupy different points in the flow; the windows are also finite samples of 200 traces each. [OCC001, OCC004, DIR003, DIR007]

Other differences: the routing shares between the alternatives A05 and A06 moved from roughly 47/53 to 53/47 in A02's outgoing transitions; the difference is small and its empirical strength (about 0.72) is moderate, so a sampling difference without any real change cannot be ruled out. [DIR002, OCC002, OCC003, REL016]