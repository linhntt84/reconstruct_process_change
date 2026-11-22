### Observed differences

- In the earlier window the process branched after A15/A26: A27 ran in about 52 in 100 traces, while A32, A33 and A38 each ran in about 49 in 100 and always as a group (co-occurring in roughly 48–49 in 100 traces, in no fixed order among themselves); A27 never co-occurred with any of the three. In the later window, A27 runs in 199 of 200 traces — exactly once per trace — and each of A32, A33 and A38 appears in only about 1 in 200 traces. [OCC004, OCC005, OCC006, OCC007, REL022, REL023, REL024, REL028, REL029, REL030]

- In the later window A27 keeps its place in the sequence: it follows A14, A15 and A26 in about 97–99 in 100 traces and precedes A28 in about 97 in 100, much as before; A26's outgoing transitions now lead to A27 in about 98 in 100 cases versus about 50 in 100 before, when the remainder went to A32, A33 and A38. [REL009, REL013, REL017, REL021, DIR006]

- The A26-to-A28 distance collapsed: before, the pair sat two steps apart in about 49 in 100 traces and four steps apart in about 46 in 100; in the later window they are two steps apart in about 95 in 100, consistent with the intermediate branch no longer running. [LAG003]

- A04 is now largely skipped: it appeared in about 68 in 100 traces before and about 22 in 100 after. Before, A14 led to A04 in about 63 in 100 of its outgoing transitions and A04 preceded A26/A28 in about 62–64 in 100 traces; in the later window A14 leads directly to A15 in about 82 in 100 of its outgoing transitions (A04 only about 10 in 100), and the A14-to-A15 gap is one step in about 47 in 100 observed pairs versus about 19 before. When A04 still runs, its occurrences sit later in the trace (mean event position about 0.21 before versus about 0.40 after). [OCC002, REL001, REL003, REL005, DIR004, LAG002, POS001]

- A02 and A08 occur more often (about 5 to 15 in 100 traces for A02; about 5 to 21 in 100 for A08) with broadly changed successor profiles; these rest on only 10–40 outgoing transitions per window and are weakly supported. [OCC001, OCC003, DIR001, DIR003]

- A14 and A28, present in every trace in both windows, show only small shifts in mean event position (about 0.01–0.02). [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the mid-process routing changed: the alternative branch formed by A32, A33 and A38 — previously executed together in about half of the cases as the alternative to A27 — is no longer executed, while A27 has become the standard path, running once in nearly every trace in the same slot between A15/A26 and A28; in the same region A04 became largely skippable, so A14 typically flows straight to A15 and A26. The screening produced 62 qualifying items in the control-flow family where fewer than 1 would be expected without change, and each item's difference exceeds about 995 in 1000 random re-splits; the participation changes are measured on roughly 200 traces per window (A27 103→199 traces; A32/A33/A38 97–98→1 each; A04 136→43), and relational evidence agrees — A26's successors shifted to A27, A14's to A15, the A26-to-A28 distance collapsed to two steps, and A27 kept its relative order — though many relation items restate the same structural shift rather than independent confirmations. The evidence cannot rule out that the two windows simply sample different case mixes (for example a subpopulation that never executed the branch) rather than a modified process, and the residual occurrences of A32, A33 and A38 rest on a single trace each, so their after-window profiles are weakly supported. [OCC002, OCC004, OCC005, OCC006, OCC007, REL009, REL013, REL017, REL021, REL022, REL023, REL024, DIR004, DIR006, LAG003]

Other differences: A02 and A08 appear in more traces with changed successor profiles, but the samples behind them are small (10–40 outgoing transitions per window); A14 and A28 show only minor position drift. [OCC001, OCC003, DIR001, DIR003, POS002, POS003]