### Observed differences

- In the earlier window, A21, A22 and A23 each executed exactly once in every trace (200 of 200); in the later window each appears in only about 1 in 200 traces. [OCC004, OCC005, OCC006]
- A14, A15 and A16, not observed at all in the earlier window, now execute in about 30, 33 and 37 in 100 traces respectively (60, 65 and 74 of 200), once per trace when present. [OCC001, OCC002, OCC003]
- The three later-window activities are mutually exclusive alternatives: no trace contains two of them, and together they cover about 199 in 200 later traces. [REL001, REL002, REL010]
- Routing moved with them: A14, A15 and A16 are each followed by A24 in all of their executions, and A39's outgoing transitions shifted from roughly one-third each to A21/A22/A23 to roughly one-third each to A14/A15/A16. [DIR001, DIR002, DIR003, DIR007]
- Order relations agree: earlier, A39 always preceded A21/A22/A23 and A21 always preceded A24; later, A39 precedes A14/A15/A16, which precede A24 in essentially all co-occurrences. [REL027, REL028, REL006, REL007, REL014, REL015, REL021, REL022]
- The distance from A39 to A24 fell from 4 positions in all earlier traces to 2 positions in about 99.5 in 100 later traces; A24's mean position moved earlier (about 0.43 to 0.39 of the trace) and A39's slightly later (about 0.31 to 0.33), while A24, A39 and A40 still appear in every trace. [LAG010, POS007, POS008, POS009]
- A41's participation rose from about 59 in 100 traces to about 69 in 100, and it now often co-occurs with A14/A15/A16, usually after them. [REL030, REL009, REL017, REL024]
- Apparent routing and lag changes among A21, A22 and A23 themselves (for example, A21 leading only to A22) rest on the single later trace that still contains them and are weak. [DIR004, DIR005, DIR006, LAG001, LAG005, LAG006]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the segment executed between A39 and A24 was restructured: the earlier pattern, in which A21, A22 and A23 each ran once per trace in varying order, gave way in the later window to exactly one of three alternatives — A14, A15 or A16 — running after A39 and immediately before A24. [OCC004, OCC005, OCC006, OCC001, OCC002, OCC003, REL025, REL027, REL028]

The support is direct and consistent: A39's successor distribution moved from the old block to the three alternatives with nearly the same one-third shares, each alternative leads to A24, the alternatives never co-occur, and the A39-to-A24 distance shrank from 4 to 2 positions — occurrence, routing, relational and lag evidence all point to the same placement. [DIR007, DIR001, DIR002, DIR003, REL001, REL010, LAG010]

Limitations remain: with 200 traces per window, variant frequencies can differ without any change, and because A14/A15/A16 were entirely absent from the earlier sample, a pre-existing very rare variant that later became frequent cannot be fully excluded — although participation swings from 100 in 100 to 1 in 100 and from 0 to 60–74 of 200 traces are far larger than typical random re-splits produce. The single later trace still containing A21/A22/A23 shows the old block persists at very low frequency rather than being provably removed, and the routing/lag items about those activities rest on that one trace. A41's increase (about 59 to 69 in 100) is observed but the evidence does not establish whether it belongs to the same change, and several indicators summarise the same traces, so their agreement is not independent confirmation. [OCC004, OCC001, DIR004, LAG001, REL030, REL009]