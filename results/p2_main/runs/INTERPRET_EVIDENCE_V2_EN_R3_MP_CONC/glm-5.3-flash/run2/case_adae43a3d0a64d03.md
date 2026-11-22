### Observed differences

- In the earlier window, A05 occurred exactly once in every trace (200 of 200) at a fixed event position (mean 0.5, no spread); in the later window it was not observed at all (0 of 200). [OCC002, POS002]
- A01 shows the mirror image: never observed in the earlier window (0 of 200), it occurs exactly once in every trace of the later window (200 of 200), at the same fixed event position A05 previously held. [OCC001, POS001]
- A01 also took over A05's direct relations. Before, A05 was followed by A03 after every occurrence and always preceded by A06; in the later window, A01 is followed by A03 in 100% of traces and preceded by A06 in 100% of traces. [DIR001, DIR003, REL002, REL004, REL007, REL008]
- The optional predecessors carried over with similar shares: before, A02 preceded A05 in about 47% of traces and A07 in about 53% (never both together); in the later window, A02 precedes A01 in about 50% of traces and A07 in about 50%, again never together. [REL001, REL005, REL006, REL009]
- Upstream routing is nearly unchanged: A02 now leads to A01 in about 75% of its outgoing transitions (previously to A05, about 72%) and to A06 in about 25% (previously about 28%); A07 leads to A01 in about 66% (previously to A05, about 71%) and to A06 in about 34% (previously about 29%); A06's split over its three successors stays within a few percentage points. [DIR002, DIR004, DIR005]

### Inference

Support level: Supported hypothesis

In the later window, A01 executes in exactly the role A05 had in the earlier window: the per-trace pattern A06 → (A02 or A07) → A05 → A03, with A05 in all 200 earlier traces, appears as A06 → (A02 or A07) → A01 → A03, with A01 in all 200 later traces. The support is direct and consistent: participation flips between 0% and 100% on 200-trace samples, the event position is identical, A01's only observed successor is A03 (as A05's was), A06 always precedes A01 (as it preceded A05), and A02/A07 each precede it in about half of the traces, matching the earlier 47%/53% split, while upstream routing shares move only a few percentage points. Chance is also implausible as a whole: 18 control-flow items qualified where roughly 0.13 would be expected if nothing had changed, and every item's difference exceeds about 99.5 in 100 random re-splits of the pooled traces. [OCC001, OCC002, POS001, POS002, DIR001, DIR002, DIR003, DIR005, REL001, REL002, REL004, REL005]

The evidence cannot distinguish a genuine substitution of behaviour from a relabelling of the same activity: A01 and A05 never appear in the same window (before, A05 only; after, A01 only), so a renaming would look identical in this data. The few-percentage-point shifts in branch shares could also be ordinary sampling variation between two finite windows. [REL003, DIR002, DIR005]

Other differences: none beyond the change from A05 to A01, apart from minor shifts — A02 appears in about 50% of later traces versus about 47% earlier, A07 in about 50% versus about 53%, and A06's outgoing shares move by a few percentage points; these are small and consistent with sampling noise. [DIR004, REL001, REL005]