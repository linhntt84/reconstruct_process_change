### Observed differences

- Before, A19, A20 and A25 were executed in every trace (participation 100 in 100, about one occurrence per trace). In the later window each of the three appears in only about 53 in 100 traces [OCC004, OCC005, OCC006].
- The three change as one group: before, each pair among them co-occurred in every trace; in the later window each pair co-occurs in about 53 in 100 traces, and neither member of the pair appears at all in about 47 in 100 traces — the group is either executed together or skipped together [REL008, REL009, REL014, REL019].
- The group's internal order and its links to neighbours are preserved: A19 still precedes A20 and A25 in essentially all traces where they co-occur, A25 still leads to A20 in about 98 in 100 of its outgoing transitions, and A20 still leads to A26 in about 96 in 100 [REL008, REL009, REL014, DIR003, DIR004].
- A41's outgoing transitions changed: before it led to A19 in about 96 in 100 transitions; in the later window it leads to A19 in about 50 in 100 and directly to A26 in about 44 in 100, matching the cases where the group is skipped [DIR005].
- A26, A41, A46 and A47 continue to appear in every trace in both windows [POS002, POS003, POS004, DIR005, DIR006].
- A02 became rarer: it appeared in about 29 in 100 traces before and about 9 in 100 after; when present, it sits earlier in the trace (mean relative position about 0.90 vs about 0.51) and its outgoing transitions shifted from mostly A47 (about 85 in 100) to a spread over many activities; A46 now leads to A02 in under 1 in 100 of its transitions, down from about 25 in 100. Only 17 after-window traces contain A02, so these details rest on few observations [OCC001, POS001, DIR001, DIR006].
- A04 and A06 became slightly more common, from about 5 to about 12 in 100 traces and from about 4 to about 13 in 100 traces respectively, on small counts (9→24 and 8→25 traces) [OCC002, OCC003].

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the activity group A19, A25, A20 became optional: previously executed in every case in the fixed sequence A41 → A19 → A25 → A20 → A26, in the later window it is executed in only about half of the cases and skipped in the rest, while A41 and A26 remain in every case and A41 now connects directly to A26 when the group is skipped [OCC004, OCC005, OCC006, REL008, REL014, REL015, DIR005].

Supporting signs: the participation drop is large and consistent across all three activities (100 to about 53 in 100), the group is skipped as a unit (pairwise co-occurrence falls to exactly the group's participation, with "neither" rising to about 47 in 100), the internal order and the A25→A20 and A20→A26 links are preserved, and the screening produced 38 qualifying control-flow items where fewer than 1 would be expected without a change, so the pattern as a whole is unlikely under random re-splitting [OCC004, OCC005, OCC006, REL008, REL009, REL014, REL019, DIR003, DIR004].

Limitations: the indicators show window-level behaviour, so the evidence cannot show what determines whether a case skips the group — for example a routing choice tied to case attributes versus a mix of case types — and the changes around A02 rest on few after-window observations [OCC001, POS001, DIR001].

Other differences: A02 appears in far fewer traces (about 29 to about 9 in 100) and, when present, occurs earlier and is rarely reached from A46 anymore; A04 and A06 appear slightly more often (about 5 to 12 and about 4 to 13 in 100 traces) [OCC001, POS001, DIR001, DIR006, OCC002, OCC003].