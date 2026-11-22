### Observed differences

- The block A19 → A25 → A20 was executed in every earlier trace (200 of 200, once per trace, in that fixed order: A19 before A25 and A25 before A20 in about 99 in 100 cases). In the later window, each of the three appears in only about 53 in 100 traces (106–107 of 200), and they disappear together: in about 46–47 in 100 traces none of the three occurs, while traces containing only one or two of them are essentially absent. [OCC004, OCC005, OCC006, REL008, REL009, REL014]

- When the block does run in the later window, its order and placement are unchanged: A41 still precedes all three, and all three still precede A26, A46 and A47, with each of these orderings holding in about 52–53 in 100 traces — exactly the block's participation share, i.e. in all of its appearances. [REL011, REL016, REL020, REL010, REL019, REL015, REL012, REL017, REL021]

- The skip leaves a direct gap: the ordered pair A41 → A26 sat about 4 steps apart in 93 in 100 earlier cases (the block in between), but in the later window it is immediately consecutive in about 44 in 100 cases and 4 steps apart in about 49 in 100 — matching the roughly 47 in 100 traces without the block. [LAG002, OCC004]

- Activities around the block are stable: A41, A26, A46 and A47 still occur in all traces in both windows, their mean positions shift by only about 0.02, and A46 is now almost always immediately before A47 (about 96 in 100 cases, up from about 75). [POS002, POS003, POS004, LAG003]

- A02 became rarer and differently placed: from 58 of 200 traces (about 29%) to 17 of 200 (about 8.5%); when it occurs, its relative position is earlier and much more variable (median about 0.97 of the trace before, about 0.47 after). Before, A02 only ever appeared alongside the block; later it also appears in traces without it. The apparent change in its distance to A47 rests on only 5 later observations. [OCC001, POS001, REL001, LAG001]

- Two rare activities rose modestly: A04 from 9 to 24 of 200 traces (about 5% to 12%) and A06 from 8 to 25 (about 4% to 13%); both rest on few observations. [OCC002, OCC003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, the fixed sub-sequence A19 → A25 → A20 — executed between A41 and the closing activities A26/A46/A47 — is skipped in roughly 47 in 100 cases, whereas it was executed in every earlier case; when it runs, its internal order and its placement in the flow are unchanged, and A41 then reaches A26 directly. The three activities fall out of traces in lockstep (participation 200 → about 106 of 200, no partial occurrences), their orderings towards A41, A26, A46 and A47 are preserved, and the direct A41 → A26 succession appears precisely in the share of traces where the block is absent; the surrounding activities keep full participation and stable positions. Screening supports this reading: 35 control-flow items qualified where fewer than 1 was expected without change, far beyond what an unchanged process produces — though most relation items re-express the same block-level behaviour rather than confirming it independently [OCC004, OCC005, OCC006, REL008, REL009, REL014, LAG002, REL010, REL011].

Limitations: the evidence cannot distinguish a newly introduced skip option from growth of a pre-existing variant without the block that was simply not sampled earlier, and the exact skip share carries sampling error in windows of 200 traces [OCC004, OCC005, OCC006].

Other differences: A02's decline in participation (about 29% to 8.5% of traces) together with its earlier and more variable position, and the modest rises of A04 and A06 (to about 12–13% from about 4–5%), are separate from the main hypothesis; the A04 and A06 changes rest on only 8–9 before-window observations and may be sampling variation of rare variants [OCC001, POS001, OCC002, OCC003].