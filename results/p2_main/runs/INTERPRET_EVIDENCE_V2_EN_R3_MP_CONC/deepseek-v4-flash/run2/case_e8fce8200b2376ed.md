### Observed differences

- In the later window, activities A07, A15, A16, and A17 appear that were completely absent in the earlier window: A07 in about 48% of traces, A15 in 39%, A16 in 70%, A17 in 33% (earlier: 0% for all). [OCC002, OCC004, OCC005, OCC006]
- A05 becomes more repetitive: mean occurrences per trace rise from about 1.9 to 4.0, while the share of traces containing it falls from 48% to 39%. [OCC001]
- A18 changes from a mean of 1.8 occurrences per trace to 0.9, but its trace participation rises from 40% to 48%. [OCC007]
- Routing changes are widespread: A05's successors shift from A13/A09/A14 to A02/A13; A08's successors shift from A05/A04 to A07/A04; A10's successors shift from A03/A10/A02 to A16/A15; A12's successors shift from A18/A08 to A08/A05; A18's successors shift from A02 to A14/A17. [DIR001, DIR003, DIR004, DIR005, DIR009]
- New outgoing edges appear for the new activities: A07→A18, A15→A10, A16→A03/A02, A17→A09. [DIR002, DIR006, DIR007, DIR008]
- Many activity pairs that never co-occurred before now co-occur, often with interleaved or repeated order. For example, A02–A07 co-occurrence goes from 0% to 48% (interleaved 45%), A03–A07 from 0% to 48%, A05–A16 from 0% to 35%. [REL001, REL005, REL011]
- Position shifts: A05 moves earlier (mean relative position from 0.63 to 0.46), A18 moves later (0.42 to 0.64). [POS002, POS007]
- Lags between activities change, e.g., A02–A05 lag shifts from mostly 3/5 steps to 2/4 steps; A08–A05 lag shifts from 1/3/5 to 4. [LAG001, LAG008]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow structure of the process: activities A07, A15, A16, and A17 were added (or became active) in the later window, and the routing among existing activities changed accordingly, with A05 becoming more repetitive and A18 moving later in the trace. This is directly shown by the appearance of these activities, their new outgoing edges, and the many new co-occurrence relations with existing activities. The screening shows 92 control-flow items against 0.6 expected by chance, so the overall difference is far beyond what a stable process would produce. The main competing explanation—that the earlier window simply missed these activities by sampling—is unlikely given their complete absence in 200 traces and the large number of consistent changes. A limitation is that the exact nature of the change (e.g., a new branch, a parallel path, or a reordering) cannot be determined from these indicators alone.