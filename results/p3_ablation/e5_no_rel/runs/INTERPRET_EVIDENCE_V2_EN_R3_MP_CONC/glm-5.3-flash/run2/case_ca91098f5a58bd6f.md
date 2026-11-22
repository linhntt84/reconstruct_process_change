### Observed differences

- In the earlier window, A14, A15 and A20 each occurred at most once per trace and appeared in roughly a third of traces — about 70, 60 and 70 of 200 traces (35%, 30% and 35%). In the later window, none of the 200 traces contains any of these three activities. [OCC001, OCC002, OCC003]
- In the earlier window, each of A14, A15 and A20 led only to A21 whenever it occurred; in the later window these activities and their outgoing transitions are not observed at all. [DIR001, DIR002, DIR003]
- A36's routing changed completely: in the earlier window its outgoing transitions were split about 35 in 100 to A20, 30 to A15 and 35 to A14, while in the later window A36 leads to A21 in essentially all observed transitions. [DIR004]
- The distance from A36 to A21 shortened: in the earlier window A21 followed A36 two steps later in all cases; in the later window it follows immediately, one step later, in all cases. [LAG001]
- A21 and A36 still occur in every trace in both windows; A21 now sits slightly earlier within traces (mean relative position about 0.39 vs 0.37) and A36 slightly later (about 0.32 vs 0.33), in the direction expected if the intermediate steps between them are gone. [POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the segment between A36 and A21 — where A36 was previously followed by exactly one of A14, A15 or A20, each leading on to A21 — is no longer executed in the later window: A36 now leads directly to A21, and A14, A15 and A20 are not observed anywhere. [DIR004, LAG001, OCC001, OCC002, OCC003]

Supporting signs: the three activities drop from about 30–35 in 100 traces to zero despite solid before-window support; their common predecessor A36 redirects entirely from them to A21; the A36–A21 gap shortens from two steps to one in every case; and the small position shifts of A21 and A36 are consistent with the missing intermediate steps. The screening also found 13 qualifying items where only about 0.34 would be expected by chance across 68 tested units, so a chance explanation of the set as a whole is implausible. [DIR004, LAG001, POS004, POS005, OCC001, OCC002, OCC003]

Limitations: zero participation only means the activities were not observed in the later window, so the evidence cannot distinguish a removal of A14, A15 and A20 from the branch through them simply never being taken. In addition, all items come from the control-flow family and several of them describe the same underlying disappearance of the three activities, so they are not independent confirmations. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003]