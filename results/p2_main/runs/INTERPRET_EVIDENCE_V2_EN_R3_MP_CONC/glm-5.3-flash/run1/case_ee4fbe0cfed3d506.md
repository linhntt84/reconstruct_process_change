### Observed differences

- Before, the mid-process activities A33, A34, A35, A37, A38 and A39–A43 each ran exactly once in every case (participation 100 in 100 traces, about 1.0 occurrences per trace). In the later window, A33, A34, A35, A37 and A38 each appear in only about 46–48 in 100 traces, and A39–A43 each in about 55 in 100, still at most once per case. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, OCC007, OCC008, OCC009, OCC010]

- The two groups became mutually exclusive. Before, an early-group and a late-group activity co-occurred in 100 in 100 traces (for example, A33 before A39 in about 99 in 100). In the later window, such cross-group pairs co-occur in at most about 3 in 100 traces; roughly 45 in 100 traces contain only the early group and about 53 in 100 only the late group. [REL025, REL029, REL033, REL037, REL040, REL044, REL046, REL050, REL051, REL055]

- Each group still moves as one unit: within the early group, pairs such as A33–A34 co-occur in about 46 in 100 traces with neither present in about 52 in 100; within the late group, pairs such as A39–A40 co-occur in about 55 in 100 with neither in about 45 in 100. Order inside each group remains unfixed (both orders in similar shares) in both windows. [REL021, REL024, REL030, REL038, REL045, REL056, REL059, REL065]

- The frame around the segment is unchanged: A30 and A31 still occur in every trace in both windows, A30 still precedes the group activities in about 97–99 of 100 co-occurrences, and the group activities still precede A31 in about 95 or more of 100. [REL001, REL006, REL010, REL011, REL016, REL020]

- Handovers follow the same pattern. Before, about 99 in 100 of A30's observed outgoing transitions went to early-group activities; in the later window, about 44 in 100 go to the early group and about 53 in 100 to the late group. A33, A34 and A38 now pass directly to A31 in about 21–25 of 100 of their observed outgoing transitions (not observed among them before), while their transitions to late-group activities (about 18–21 in 100 combined before) are no longer observed. [DIR001, DIR002, DIR003, DIR004]

- Event positions and step distances point the same way: A30's mean relative position moved from about 0.55 to 0.64, early-group activities from about 0.62–0.63 to 0.72–0.73, and late-group activities from about 0.75–0.76 to 0.71–0.72; cross-group pairs within five steps collapsed (A33→A41: 121 supporting cases before, 1 after) while early-group→A31 pairs within five steps appeared (A33→A31: 1 before, 88 after). Most distance items rest on only 1–3 observations in one window, and positions are event indices, not clock times. [POS001, POS002, POS003, POS004, POS005, POS006, POS007, POS008, POS009, POS010, LAG004, LAG005, LAG006]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that, in the later window, every case executes exactly one of two mid-process blocks that previously always ran in sequence — the early block (A33, A34, A35, A37, A38) in about 46 in 100 cases, or the late block (A39, A40, A41, A42, A43) in about 53 in 100 — whereas before, both blocks ran in every case (single-block traces: 0 in 200). A30 and A31 still frame every case, the order A30 → block → A31 is preserved whenever a block runs, and internal block order stays unfixed. Because one-block behaviour was essentially absent before, this is a participation change (the blocks became skippable, mutually exclusive alternatives), not a re-weighting of pre-existing paths. [OCC001, OCC006, REL001, REL011, REL021, REL025, REL056, DIR001, DIR002]

Supporting signs: the control-flow screening qualified 112 items where about 1.28 would be expected without any change, so the pattern as a whole is not what an unchanged process typically produces; participation, co-occurrence and handover evidence all describe the same underlying difference directly, though they are not independent confirmations of one another. [OCC001, REL025, DIR001, DIR002]

Limitations: the evidence cannot show what determines which block a case receives, since case attributes are not part of the data; a changed mix of cases entering the process therefore cannot be ruled out as an alternative to a new routing decision, and the step-distance items add little because of their very low support in one window. [LAG005, LAG006]

Other differences: a few new, low-share outgoing transitions appear in the later window — from A30 to A05, A06, A09 and A14, and from A33, A34 and A38 to A08, A13, A24, A36, A45, A49 and A51 — each about 1 in 100 of the source's observed outgoing transitions. [DIR001, DIR002, DIR003, DIR004]