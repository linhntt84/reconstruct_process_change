### Observed differences

- In the earlier window, A14, A15 and A20 each ran in a minority of cases — about 32 in 100, 28 in 100 and 40 in 100 traces respectively — and they never occurred together, so exactly one of the three executed per trace. In the later window, none of the three appears in any of the 200 traces. [OCC001, OCC002, OCC003, REL001, REL002, REL006]
- In the earlier window, A22 split its outgoing flow across A23 (about 55 in 100), A20 (21), A14 (13) and A15 (11), and A23 led on to A24 (about 46 in 100), A20 (19), A14 (19) and A15 (17). In the later window, A22 always leads to A23 and A23 always leads to A24. [DIR001, DIR002, DIR003, DIR004, DIR005]
- The gaps between A22, A23 and A24 closed: A23 followed A22 immediately in about 55 in 100 earlier cases but in 100 in 100 later cases; A24 followed A23 immediately in about 45 in 100 earlier cases and in 100 in 100 later cases; the A22-to-A24 distance moved from always 3 positions to always 2. [LAG001, LAG002, LAG003]
- A22, A23 and A24 still occur in every trace in both windows; A22 now sits slightly later in the trace (mean relative position about 0.46 to 0.47) and A24 slightly earlier (about 0.57 to 0.55). [POS004, POS005, REL003, REL004, REL005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the optional step carried out by one of the three alternative activities A14, A15 and A20 — exactly one of which executed in every earlier case, inserted either between A22 and A23 or between A23 and A24 — is no longer executed in the later window, so that A22, A23 and A24 now follow one another in immediate succession. The signs are direct and mutually consistent: participation of all three activities fell from 28–40 in 100 traces to 0 of 200; their outgoing transitions disappeared while A22 and A23 each kept a single successor; the pairwise distances contracted to immediate succession; and the small position shifts of A22 and A24 point the same way. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG001, LAG002, LAG003, POS004, POS005]

The volume of qualifying evidence also far exceeds what an unchanged process would produce: 28 control-flow items qualified where fewer than one would be expected by chance. [screening]

Limitation: zero participation strictly means only that A14, A15 and A20 were not observed in the later window; with 200 traces and earlier participation of 28–40 in 100, chance non-sampling is implausible but cannot be fully excluded, and the evidence cannot distinguish a removal of these activities from their alternative branch simply never being taken. [OCC001, OCC002, OCC003]