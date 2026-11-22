### Observed differences

- In the earlier window, A19, A20 and A25 each ran in roughly a third of the cases — about 37, 31 and 35 in 100 traces respectively — and almost never together (co-occurrence about 1 in 100 or less), so they behaved as mutually exclusive alternatives. In the later window they are essentially unobserved: A19 appears in 1 of 200 traces, A20 and A25 in none. [OCC001, OCC002, OCC003, REL001, REL003, REL008]
- Earlier, each of the three led almost exclusively to A26 — about 95, 97 and 96 in 100 of their observed outgoing transitions. In the later window, A20 and A25 have no observed outgoing transitions, and A19's single occurrence goes to A12 instead. [DIR001, DIR002, DIR004]
- A41's routing changed markedly: earlier, about 87 in 100 of its outgoing transitions went to A19 (about 29), A20 (about 26) or A25 (about 32), and none went directly to A26; in the later window, about 86 in 100 go directly to A26. [DIR005]
- The relation items match this picture: A41 previously co-occurred with each of the three in about 31–37 in 100 traces, always with A41 first, and each of the three preceded A26 or A31 in about 30–36 in 100 traces; in the later window, A26, A31 and A41 occur without any of the three in essentially every trace. [REL004, REL005, REL006, REL009, REL010, REL011, REL013, REL014, REL015]
- A26 and A41 still occur in every trace in both windows. A26's mean event position moved slightly earlier (about 0.39 to 0.37 of the trace) and A41's slightly later (about 0.32 to 0.33); these are positions among events, not clock times. [POS004, POS005]
- Downstream, A19, A20 and A25 no longer precede A24 (about 16–17 in 100 traces before, effectively zero after), and A24 now typically appears without them (about 56 in 100 traces, up from about 33). [REL002, REL007, REL012]
- Separately, A21's outgoing mix shifted: A24's share rose from about 14% to 35% while A31's fell from about 54% to 38%, on similar numbers of observed transitions (114 before, 101 after). [DIR003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the alternative block formed by A19, A20 and A25, which sat between A41 and A26, is no longer executed: in the earlier window about one case in three ran exactly one of the three, reached from A41 and followed by A26, while in the later window the three are unobserved and A41 leads directly to A26 in about 86 in 100 of its transitions, with A26 and A31 now running without them. This is unlikely to be a sampling artefact: 28 control-flow items qualified where roughly 0.55 would be expected without a change, and the occurrence, direction and relation items all describe one coherent bypass rather than unrelated fluctuations. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR004, DIR005, REL004, REL009, REL013]

Limitations: zero participation only means the activities were not observed, so the evidence cannot distinguish removing the block from it becoming optional and skipped in every observed case; the single remaining A19 trace routing to A12 rests on one observation. Several items describe the same traces, so they are not independent confirmations. A competing explanation the evidence cannot rule out is that the three activities still run at a very low rate below what these windows can detect. [OCC001, DIR001]

Other differences: A21's successor shares shifted towards A24 and away from A31 — a redistribution among transitions A21 already had, not part of the bypass above. [DIR003]