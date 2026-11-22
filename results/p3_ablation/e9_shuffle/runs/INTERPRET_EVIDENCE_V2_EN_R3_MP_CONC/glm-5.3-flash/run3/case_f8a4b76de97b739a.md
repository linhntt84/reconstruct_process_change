### Observed differences

- **A09 is no longer observed.** In the earlier window it ran in about 54 of 100 traces (about 1.5 times per trace, so it sometimes repeated), and about 82 of 100 of its observed outgoing transitions went to A03; in the later window it appears in none of the 200 traces and shows no outgoing transitions. [OCC003, POS004, DIR006]

- **A01 and A02 are newly observed.** Earlier, neither appeared in any trace; in the later window A01 runs in about 59 of 100 traces (about 1.5 times per trace, repeated in about 39 of 100) around the middle of the trace (median relative position about 0.50), and A02 runs in about 87 of 100 traces near the start (median about 0.20). [OCC001, OCC002, POS001, POS002]

- **Flows were rerouted onto the new activities.** A16's observed outgoing transitions went mainly to A09 earlier (about 45 of 100) and now go to A10 (about 45) and A01 (about 43). A13's largest outgoing share moved from A03 (about 31) to A02 (about 35), and A05's from A03 (about 30) to A02 (about 37). A01's outgoing transitions go mainly to A03 (about 83 of 100); A02's go mainly to A12 (about 63) and A03 (about 19). [DIR009, DIR007, DIR003, DIR001, DIR002]

- **A02 brings a new precedence over A12.** Earlier, A12 ran in about 80 of 100 traces while A02 never appeared; in the later window the two co-occur in about 87 of 100 traces and A02 precedes A12 in essentially all of them. A02 also precedes A07 and A08 in about 69 of 100 traces each, while A13 and A05 precede A02 in about 40 and 38 of 100. [REL017, REL014, REL015, REL018, REL013]

- **A14 became near-universal and sometimes repeated.** Its participation rose from about 39 to 89 of 100 traces and its mean occurrences from about 0.4 to 1.7 (repeated in about 42 of 100), at a slightly earlier position (median 1.0 to 0.95); it now co-occurs with A03, A07, A08 and A16 in about 89 of 100 traces, against roughly 28–39 earlier. [OCC004, POS005, REL023, REL027, REL029, REL037]

- **A14 and A17 now alternate with each other.** A14's outgoing transitions go mainly to A17 in the later window (about 68 of 100, earlier mainly A08 at about 56), and A17's go mainly to A14 (about 89, earlier mainly A08 at about 54); the pair co-occurs in about 42 of 100 traces (earlier never) and A17 now repeats in about 19 of 100. A08's outgoing share to A17 fell from about 35 to 7 in 100 (share to A14 rose from about 28 to 65), and A07's share to A17 fell from about 18 to 4 (share to A14 rose from about 19 to 40). [DIR008, DIR010, DIR005, DIR004, REL038, OCC005]

- **Gaps between connected activities widened in event positions.** A07–A14 and A08–A14 pairs lay within two positions of each other in about 92–96 of 100 cases earlier and in about 46–48 later, with the remainder spread over longer gaps; A05–A12 and A13–A12 moved from mostly one position apart to mostly two. These are event-position gaps, not clock times. [LAG002, LAG004, LAG005, LAG001, LAG006]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the process was structurally reconfigured between the windows: A09 — earlier executed in about half of the traces and followed mainly by A03 — is no longer observed, while A01 (mid-trace, followed mainly by A03) and A02 (early, followed mainly by A12) newly appear, with A16 now running into A01 where it previously ran into A09, and A13 and A05 now running into A02 where they previously fed A03 and A12. In the same reconfiguration, A14 became near-universal and sometimes repeated and now alternates with A17, each being the other's dominant successor. [OCC003, DIR006, OCC001, OCC002, DIR001, DIR002, DIR009, DIR007, DIR003, OCC004, DIR008, DIR010, REL038]

This is shown directly rather than inferred from marginal frequencies: the successor profiles of A16, A13, A05, A14 and A17 change their dominant targets, the participation, position and relation indicators agree with one another, and 67 control-flow items qualified against fewer than 1 expected by chance (about 0.76), each difference larger than roughly 995 of 1000 random re-splits, so the volume of differences cannot be explained by sampling variation alone. [DIR009, DIR007, DIR003, DIR008, DIR010, REL017, REL022, OCC003]

An important competing explanation remains: A09 may still execute but was not sampled, since zero participation only establishes that it was not observed in the later 200-trace window, not that it was removed from the process. The items also overlap heavily — the A09 disappearance alone recurs in about a dozen relation items — so they are not independent confirmations, and the evidence contains no time or resource items, so nothing can be said about clock-time timing or resource allocation. [OCC003, REL030, REL032, REL033]

Other differences: A08, A16 and A17 sit slightly earlier in the trace in the later window (median position shifts of roughly 0.03–0.08), and the A16–A17 gap moved from mostly four to mostly five positions apart; these are consistent with the reconfiguration above but do not by themselves show that any activity was moved in clock time. [POS003, POS006, POS007, LAG007]