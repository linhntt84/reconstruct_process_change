### Observed differences

- In the later window, each activity's outgoing transitions become almost deterministic: A15 goes to A18 in about 99.5% of cases (previously 62% to A18, with the rest split among A19, A20, A21); A17 goes to A15 in 99.5% (previously 56%); A18 goes to A19 in 99.5% (previously 53% to A27 and smaller shares to A19, A20, A21); A19 goes to A21 in 99.5% (previously 55.5% to A21, 27.5% to A17, etc.); A20 goes to A27 in 99.5% (previously 47% to A27, 22% to A18, etc.); A21 goes to A20 in 100% (previously 65.5% to A20, 14% to A15, etc.); A26 goes to A17 in 100% (previously 50% to A19, 50% to A17). [DIR001-DIR007]

- The order between activity pairs becomes fixed: for example, A15 precedes A19 in 99.5% of traces after vs 25.5% before; A15 precedes A20 in 100% vs 69% before; A15 precedes A21 in 100% vs 49.5% before; A17 precedes A19 in 100% vs 50% before; A18 precedes A19 in 99.5% vs 12% before; A18 precedes A20 in 99.5% vs 47% before; A18 precedes A21 in 99.5% vs 30.5% before. [REL001-REL008]

- The distance between activities becomes concentrated at a single value: e.g., A15 and A18 are adjacent (lag 1) in 99.5% after vs 62% before; A15 and A19 are two steps apart in 100% after (vs 52.9% at lag 1 and 47.1% at lag 2 before); A15 and A20 are four steps apart in 99.5% after (vs spread over lags 1-4 before); A17 and A15 are adjacent in 99.5% after vs 56% before; A17 and A18 are two steps apart in 99.5% after vs spread before; A18 and A21 are two steps apart in 100% after vs 60.7% at lag 1 and 39.3% at lag 2 before. [LAG001, LAG002, LAG003, LAG006, LAG007, LAG012, etc.]

- The relative positions of activities shift: A15, A17, A18 occur earlier (mean position decreases by about 0.05, 0.02, 0.06 respectively), while A19, A20, A21 occur later (mean position increases by about 0.06, 0.03, 0.04 respectively). [POS001-POS006]

Together, these indicate that in the later window the process follows a strict linear sequence: A26 → A17 → A15 → A18 → A19 → A21 → A20 → A27, whereas before there were multiple branches and mixed orders.

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the process changed from a flexible, branching order to a fixed sequential order among activities A26, A17, A15, A18, A19, A21, A20, and A27. In the later window, each activity has a single dominant successor, the ordering between pairs is fixed, and the distances between activities are concentrated at specific values, all consistent with a single linear path. The position shifts are also consistent with this reordering. The number of evidence items (50) far exceeds the 0.47 expected by chance, and the pattern is highly consistent across DIR, REL, LAG, and POS indicators. A competing explanation of random sampling variation is ruled out by the magnitude and consistency of the differences. A limitation is that some LAG items have very low support in the later window (e.g., pairs involving A19 and A18, A20 and A18, A21 and A18), but these are not needed to establish the main sequence, which is supported by items with full support in both windows.

Other differences: The relative positions of activities shift as described, but this is part of the same reordering. No other independent differences are apparent.