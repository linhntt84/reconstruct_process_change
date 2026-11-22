### Observed differences

- Participation did not change: A15, A17, A18, A19, A20 and A21 each appear in about 200 of 200 traces in both windows, and every analysed pair of them co-occurs in all traces in both windows, so no activity was added, removed or made optional. [POS001, POS003, POS004, POS006, REL001, REL004, REL008]

- In the earlier window, routing was dispersed and orders were mixed: from A15 about 62 in 100 outgoing transitions went to A18 with the rest split over A19, A20 and A21; from A18 about 53 in 100 went straight to A27; from A26 transitions split evenly between A19 and A17. A19 preceded A18 in about 88 in 100 traces and preceded A15 in about 75 in 100, while A15/A21, A17/A19 and A18/A20 occurred in both orders in roughly equal shares, i.e. with no fixed order. [DIR001, DIR003, DIR007, REL006, REL001, REL003, REL004, REL007]

- In the later window, each of these activities has essentially a single successor, forming one fixed chain A26 → A17 → A15 → A18 → A19 → A21 → A20 → A27, with each transition carrying about 99–100 in 100 of the source activity's observed outgoing transitions. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, DIR007]

- Pairwise orders became strict and partly reversed: A15 now precedes A19 in 199 of 200 traces (before, A19 was first in about 75 in 100); A18 now precedes A19 in 199 of 200 (before reversed in about 88 in 100) and precedes A21 in 199 of 200 (before, A21 was first in about 70 in 100); the previously unordered pairs A15/A21, A17/A19 and A18/A20 are now strictly ordered. [REL001, REL006, REL008, REL003, REL004, REL007]

- Step distances collapsed onto single values matching that chain: A15 reaches A18 within one step in about 99.5 in 100 traces (before 62 in 100, spread over 1–4 steps); A15 reaches A20 at distance 4 in about 99.5 in 100 (before spread over 1–4); the formerly dominant direct A18→A27 succession is gone — A18 now reaches A27 only at distance 4, while A20→A27 is direct in about 99.5 in 100 (before 47 in 100). [LAG001, LAG003, LAG013, LAG020]

- Positions shifted accordingly: A15, A17 and A18 now occur slightly earlier in the trace (mean relative position lower by about 0.03–0.06) and A19, A20 and A21 slightly later (higher by about 0.03–0.06); old orderings such as A19 before A18 (176 of 200 traces earlier) and A21 before A18 (139 of 200) are almost unobserved later. [POS001, POS002, POS003, POS004, POS005, POS006, LAG015, LAG021]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the ordering constraints among A26, A17, A15, A18, A19, A21, A20 and A27 changed: in the earlier window these activities ran in every case but with several alternative successions and mixed or reversed pairwise orders, while in the later window they execute in one fixed sequence, A26 → A17 → A15 → A18 → A19 → A21 → A20 → A27. The change is shown directly by relational evidence (order reversals for A15/A19, A18/A19 and A18/A21, and previously unordered pairs becoming fixed), by step distances collapsing to the single values of one chain, and by successor profiles collapsing to one successor per activity; participation itself is unchanged, so this is a reordering of the same activities, not activities being added, removed or skipped. [REL001, REL006, REL008, LAG001, LAG013, DIR001, DIR003, DIR004, POS001, POS004]

The volume of qualified items (50 control-flow items from 95 tested units, against fewer than 1 expected without any change) is far too large to be explained by sampling variation as a whole, and the items agree on a single structure instead of pointing in different directions. [DIR001, DIR007, LAG001, LAG027]

Limitations: the chain is reconstructed from pairwise relations and per-activity successor profiles rather than read off a model, so the exact placement of A27 after A20 rests on the agreement of several indicators; and the evidence cannot show whether the earlier mixed orders were one process with flexible ordering or a mixture of several fixed variants. [REL003, REL004, LAG005, LAG018, LAG023]

Other differences: none observed — the remaining qualified items (the position shifts and the near-disappearance of previously common ordered pairs such as A19 before A18 and A21 before A18) are part of the same reordering. [POS001, POS004, LAG015, LAG021]