### Observed differences

- In the earlier window, A19, A20 and A25 each ran in roughly a third of cases (about 37, 31 and 35 in 100 traces); in the later window they have practically disappeared — A20 and A25 were not observed at all, and A19 appeared in only 1 of 200 traces. [OCC001, OCC002, OCC003]
- Earlier, the three rarely occurred together (co-occurrence about 1 in 100 traces for each pair), so a case typically contained one of them as a single intermediate step. [REL001, REL003, REL008]
- Earlier, each of the three led almost exclusively to A26 (about 94–97 in 100 of their observed outgoing transitions); in the later window A20 and A25 show no observed outgoing transitions at all. [DIR001, DIR002, DIR004]
- A41's routing changed: earlier about 29, 32 and 26 in 100 of its observed outgoing transitions went to A19, A25 and A20 respectively, with none going directly to A26; in the later window about 86 in 100 go directly to A26. [DIR005]
- The A41–A26 distance shortened accordingly: earlier A26 followed A41 two positions later in about 85 in 100 cases (three positions in about 15); in the later window it immediately follows A41 in about 86 in 100 cases. [LAG001]
- Consequently, A26, A31 and A41 — which earlier co-occurred with one of the three activities in about 31–37 in 100 traces — now occur without them in essentially every trace (about 99–100 in 100). [REL004, REL005, REL006, REL009, REL010, REL011, REL013, REL014, REL015]
- Separately, the outgoing shares of A21 shifted: A24 rose from about 14 to about 35 in 100 of A21's observed outgoing transitions, while A31 fell from about 54 to about 38 and A23 from about 29 to about 25. [DIR003]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the three activities A19, A20 and A25, which earlier executed as intermediate steps between A41 and A26, are no longer executed, so that A41 now passes control directly to A26. Earlier, about 87 in 100 of A41's outgoing transitions led to one of the trio, each of which led almost exclusively onward to A26, and A26 followed A41 two steps later in about 85 in 100 cases; in the later window A41 leads directly to A26 in about 86 in 100 of its outgoing transitions and the distance has collapsed to a single step. [DIR005, LAG001, DIR001, DIR002, DIR004]

The signs are direct and consistent across occurrence, direction, relation and lag indicators: the trio's participation fell from 62–73 traces each to 0–1 traces, and A26, A31 and A41 now occur without the trio in essentially all traces. Screening flagged 24 control-flow items where fewer than one would qualify by chance, so the pattern as a whole cannot be a sampling artefact; and because the trio is nearly absent in the later window rather than merely taken less often, this indicates activities being removed or no longer reached, not a re-sharing of frequencies between surviving paths. [OCC001, OCC002, OCC003, REL004, REL009, REL013]

Limitations: the evidence cannot distinguish a full removal of A19, A20 and A25 from a drastic reduction that leaves them unobserved in this 200-trace sample, and the single later occurrence of A19 (one outgoing transition to A12) is too thin to characterise any new successor. It also remains possible that the direct A41–A26 handover is only the dominant rather than the only routing, since about 14 in 100 of A41's later outgoing transitions go elsewhere. [DIR001, DIR005]

Other differences: the redistribution of A21's outgoing shares towards A24 and away from A31 and A23, described above, is a separate routing shift that this hypothesis does not cover. [DIR003]