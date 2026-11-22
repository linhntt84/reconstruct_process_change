### Observed differences

- In the later window, A10 appears in about 25% of traces (down from 71%), and its mean occurrences per trace dropped from 0.78 to 0.29. [OCC005]
- In the later window, activities A30, A31, A36, A37, A38 each occur on average about 3 times per trace (up from about 1), and they repeat in about two-thirds of traces, whereas before they almost never repeated. [OCC006, OCC007, OCC008, OCC009, OCC010]
- In the later window, A10's outgoing transitions are redistributed: before about 89% went to A45, after only about 14% go to A45, with many other successors appearing. [DIR004]
- In the later window, the fixed order among the activities A14, A15, A30, A31, A36, A37, A38, A46, A47 is largely lost: for example, A14 before A30 occurred in 97.5% of traces before but only 33% after, with the rest becoming interleaved or repeated; similar changes appear for many pairs. [REL014, REL015, REL016, REL017, REL018, REL019, REL020, REL021, REL022, REL023, REL029, REL030, REL031, REL032, REL033, REL034, REL035, REL036, REL037, REL040, REL041, REL042, REL043, REL044, REL047, REL048, REL050, REL053, REL054, REL055, REL058, REL059, REL062, REL063]
- In the later window, the lag between A10 and A47 shifted from mostly 3 steps to mostly 1 step. [LAG001]
- In the later window, A10's position in the trace moved earlier (mean from 0.85 to 0.48). [POS001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the process changed from a fixed sequential execution of a set of activities (A14, A15, A30, A31, A36, A37, A38, A46, A47) with A10 as a common preceding step, to a process where A10 is less common and those activities are repeated and interleaved without a fixed order. This is supported by the large drop in A10 participation, the increase in repetition of the later activities, the replacement of fixed orders by interleaving in many REL pairs, the shift in lag distributions, and the earlier position of A10. The number of qualifying items (114) far exceeds the 1.2 expected by chance, so the overall difference is not a sampling artefact. A competing explanation that cannot be fully ruled out is that the change reflects a different case mix or a new variant rather than a modification of the same process, but the consistency across many activity pairs makes that less likely.

Other differences: Activities A02, A04, A06, A08 increased in participation from about 5–9% to about 18–26% of traces. [OCC001, OCC002, OCC003, OCC004]