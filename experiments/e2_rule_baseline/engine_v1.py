"""Deterministic, evidence-only interpretation baseline (exploratory v1).

No ground truth, dataset identity, case name, LLM response, or scorer input is used.
Patterns are hypotheses inferred from finite-window evidence, not proven edits.
"""
from dataclasses import asdict, dataclass
import math

VERSION = 'evidence-rules-v1'

@dataclass(frozen=True)
class Config:
    absent: float = .02
    present: float = .20
    strong: float = .80
    delta: float = .10
    stable: float = .05
    mixed_order: float = .20
    max_observations: int = 5

    def validate(self):
        assert 0 <= self.absent < self.present < self.strong <= 1
        assert 0 < self.stable < self.delta <= 1
        assert 0 < self.mixed_order < .5
        assert self.max_observations >= 1


def number(mapping, key):
    """Missing components are unknown, never implicit zeros."""
    value = mapping.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Invalid numerical component: '+key)
    return float(value)


def unit(e):
    u = e['analysis_unit']
    return tuple(u['values']) if 'values' in u else (u['value'],)


def interpret(evidence, config=None):
    c = config or Config(); c.validate()
    items = sorted(evidence, key=lambda e: e['id'])
    ids = [e['id'] for e in items]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate evidence IDs')
    for e in items:
        if not isinstance(e['id'], str) or not unit(e):
            raise ValueError('Malformed evidence item')
        for side in ('components_before', 'components_after'):
            for key in e[side]: number(e[side], key)
    groups = {}
    for e in items: groups.setdefault(e['indicator'], []).append(e)
    claims = []
    def emit(rule, mechanism, pattern, activities, support, text, direction='changed'):
        claims.append(dict(rule_id=rule, mechanism=mechanism, pattern=pattern,
                           activities=sorted(set(activities)), evidence_ids=sorted(set(support)),
                           direction=direction, status='hypothesis', explanation=text))
    def incident(activity):
        matches = []
        for e in groups.get('CF_DIR', []):
            b,a=e['components_before'],e['components_after']
            # Absent bins of a supplied DIR distribution have zero mass.
            for target in sorted(set(b)|set(a)):
                if activity in (unit(e)[0],target) and abs(a.get(target,0)-b.get(target,0)) >= c.delta:
                    matches.append(e['id']);break
        return matches
    excluded = set(); occ_by_activity={}
    for e in groups.get('CF_OCC', []):
        x=unit(e)[0];b=e['components_before'];a=e['components_after']
        pb,pa=number(b,'trace_participation'),number(a,'trace_participation')
        rb,ra=number(b,'recurrence_support'),number(a,'recurrence_support')
        mb,ma=number(b,'mean_occurrences_per_trace'),number(a,'mean_occurrences_per_trace')
        occ_by_activity[x]=(e,pb,pa)
        if pb is None or pa is None:continue
        links=incident(x)
        if links and ((pb<=c.absent and pa>=c.present) or (pa<=c.absent and pb>=c.present)):
            added=pa>pb;excluded.add(x)
            emit('R01_OCC_DIR_APPEARANCE','insertion' if added else 'removal',None,[x],[e['id']]+links,
                 f'{x} is consistent with {"insertion" if added else "removal"}: trace participation changes from {pb:.3f} to {pa:.3f}, with corroborating changes in incident directly-follows distributions. The structural subtype is undetermined.',
                 'added' if added else 'removed')
        elif None not in (rb,ra,mb,ma) and abs(ra-rb)>=c.delta and (ma-mb)*(ra-rb)>0:
            excluded.add(x)
            emit('R02_OCC_REPETITION','repetition','Loop',[x],[e['id']],
                 f'Repetition of {x} {"increases" if ra>rb else "decreases"}: recurrence support changes from {rb:.3f} to {ra:.3f} and mean occurrences from {mb:.3f} to {ma:.3f}. This is consistent with a loop-related change.',
                 'increased' if ra>rb else 'decreased')
    # Infer observable pair-state transitions. Both orders in traces do not prove concurrency.
    reversals=[]
    for e in groups.get('CF_REL', []):
        pair=unit(e)
        if len(pair)!=2:raise ValueError('REL requires two activities')
        if set(pair)&excluded:continue
        states=[]
        for side in ('components_before','components_after'):
            d=e[side];v=[number(d,k) for k in ('cooccurrence','A_only','B_only','A_before_B','B_before_A','interleaved_or_repeated')]
            co,ao,bo,ab,ba,repeat=v
            state='unknown'
            if None not in v:
                if co<=c.absent and ao>=c.present and bo>=c.present: state='exclusive'
                elif co>=c.strong and repeat<=c.stable:
                    if ab/co>=c.strong:state='forward'
                    elif ba/co>=c.strong:state='backward'
                    elif min(ab,ba)/co>=c.mixed_order:state='mixed_order'
            states.append(state)
        before,after=states
        if before==after or 'unknown' in states:continue
        x,y=pair
        if before in ('forward','backward') and after in ('forward','backward'):
            reversals.append(e)
        elif 'exclusive' in states and any(v in ('forward','backward') for v in states):
            emit('R03_REL_EXCLUSIVE_SEQUENCE','relation_change','ConditionalToSequence',pair,[e['id']],
                 f'{x} and {y} change from {before} behavior to {after} behavior, consistent with a conditional/sequential relation change.',
                 'to_sequence' if before=='exclusive' else 'to_conditional')
        elif 'mixed_order' in states and any(v in ('forward','backward') for v in states):
            emit('R04_REL_MIXED_SEQUENCE','relation_change','ParallelToSequence',pair,[e['id']],
                 f'{x} and {y} change from {before} behavior to {after} behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency.',
                 'to_sequence' if before=='mixed_order' else 'to_mixed_order')
    # Movement needs positional displacement, changed ordering, and DIR corroboration.
    covered_reversals=set()
    for e in groups.get('CF_POS', []):
        x=unit(e)[0]
        if x in excluded:continue
        b,a=e['components_before'],e['components_after']
        sb,sa=number(b,'support'),number(a,'support');mb,ma=number(b,'mean'),number(a,'mean')
        rel=[r for r in reversals if x in unit(r)];links=incident(x)
        if None not in (sb,sa,mb,ma) and min(sb,sa)>=c.present and abs(sa-sb)<=c.stable and abs(ma-mb)>=c.delta and rel and links:
            covered_reversals.update(r['id'] for r in rel);excluded.add(x)
            support=[e['id']]+links+[r['id'] for r in rel]
            # LAG corroborates displacement but does not establish direction or a specific pattern.
            for lag in groups.get('CF_LAG', []):
                change=number(lag,'observed_change')
                if x in unit(lag) and change is not None and change>=c.delta:support.append(lag['id'])
            emit('R05_POS_REL_DIR_MOVE','movement',None,[x],support,
                 f'{x} may have moved: mean normalized position changes from {mb:.3f} to {ma:.3f}, with stable presence, reversed ordering and changed directly-follows distributions. The evidence does not distinguish movement of {x} from movement of its surrounding fragment, or determine the structural subtype.')
    for e in reversals:
        if e['id'] not in covered_reversals:
            x,y=unit(e)
            emit('R06_REL_ORDER_REVERSAL','reordering',None,[x,y],[e['id']],
                 f'The order of {x} and {y} reverses. The evidence does not determine which activity moved or whether this is a swap.')
    structural={x for cl in claims for x in cl['activities']}
    for x,(e,pb,pa) in sorted(occ_by_activity.items()):
        if x in structural or pb is None or pa is None:continue
        b,a=e['components_before'],e['components_after'];rb,ra=number(b,'recurrence_support'),number(a,'recurrence_support')
        if min(pb,pa)>=c.present and abs(pa-pb)>=c.delta and None not in (rb,ra) and max(rb,ra)<=c.stable:
            # Distinguish a transition between mandatory-like and optional-like participation.
            optional=(max(pb,pa)>=1-c.absent and min(pb,pa)<=1-c.present)
            emit('R07_OCC_OPTIONALITY' if optional else 'R08_OCC_FREQUENCY',
                 'optionality' if optional else 'frequency', 'Skip' if optional else 'Frequency',
                 [x],[e['id']],
                 f'Participation of {x} changes from {pb:.3f} to {pa:.3f} without substantial recurrence. '+
                 ('This is consistent with changed optionality; a particular skip edge is not established.' if optional else 'This supports a participation-frequency change; the branch structure is undetermined.'),
                 'increased' if pa>pb else 'decreased')
    # Deterministic observation fallback; this is not promoted to a mechanism claim.
    observations=[]
    for e in items:
        changes=[]
        b,a=e['components_before'],e['components_after']
        for key in sorted(set(b)&set(a)):
            if a[key]!=b[key]:changes.append((abs(a[key]-b[key]),key,b[key],a[key]))
        if changes:
            _,key,old,new=max(changes,key=lambda v:(v[0],v[1]))
            observations.append(dict(evidence_id=e['id'],text=f'{", ".join(unit(e))}: {key} changes from {old:.3f} to {new:.3f}.'))
    observations=observations[:c.max_observations]
    mechanisms=sorted({cl['mechanism'] for cl in claims});patterns=sorted({cl['pattern'] for cl in claims if cl['pattern']})
    lines=['### Reconstructed change']
    for cl in claims:lines.append('- '+cl['explanation']+' ['+', '.join(cl['evidence_ids'])+']')
    if not claims:lines.append('The supplied evidence is insufficient for these rules to identify a change mechanism.')
    if observations:
        lines.extend(['','### Evidence observations'])
        lines.extend('- '+o['text']+' ['+o['evidence_id']+']' for o in observations)
    lines.extend(['','### Limitations','Rule matches are hypotheses based on qualified evidence, not proof of the generating process edit. Missing evidence is unknown. Multiple matches may reflect one underlying change; they are not automatically distinct edits.'])
    return dict(version=VERSION,config=asdict(c),status='hypotheses' if claims else 'abstained',
                predicted_objects=sorted({x for cl in claims for x in cl['activities']}),
                predicted_mechanisms=mechanisms,predicted_patterns=patterns,claims=claims,
                observations=observations,explanation='\n'.join(lines)+'\n')
