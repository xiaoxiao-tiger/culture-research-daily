"""Explicit, evidence-bearing access fallback validation; never bypass challenges."""
from datetime import date

def fallback_enabled(day):
    return date.fromisoformat(day) >= date(2026, 11, 1)

def validate_fallback(value, day):
    assert fallback_enabled(day), 'Fallback not authorized for historical issues'
    assert isinstance(value, dict)
    assert all(isinstance(value.get(k), str) and value[k].strip()
               for k in ('reason', 'channel', 'checkedAt')), 'Document actual access fallback'
    date.fromisoformat(value['checkedAt'][:10])

def validate_unverified(p):
    assert p.get('citationStatus') == 'unverified' and p.get('citationNote'), 'Explain unverified citations'
    assert all(p.get(k) is None for k in ('citationCount', 'citationSource', 'citationSourceUrl', 'citationCheckedAt')), 'Do not rank unverified citations'

def validate_rotation_fallback(group, plan, day):
    from reading_plan import rotation
    scheduled = rotation(plan, day, 'general')['id']
    assert group['rotationJournalId'] == scheduled, 'Wrong general journal rotation: preserve scheduled rotation'
    selected = group.get('selectedJournalId', scheduled)
    if selected == scheduled:
        assert not group.get('rotationFallback'), 'No replacement without a changed journal'
        return
    assert fallback_enabled(day) and group['papers'], 'Invalid general journal replacement'
    f = group.get('rotationFallback', {})
    assert f.get('reason') and f.get('checkedAt') and f.get('attempts'), 'Explain rotation fallback'
    date.fromisoformat(f['checkedAt'][:10])
    ids = [j['id'] for j in plan['rotations']['general']]
    assert selected in ids
    start = ids.index(scheduled)
    expected = (ids[start:] + ids[:start])
    attempts = f['attempts']
    assert 2 <= len(attempts) <= len(ids)
    assert [a['journalId'] for a in attempts] == expected[:len(attempts)], 'Try journals in configured order'
    assert all(a.get('reason') and a['status'] in ('blocked', 'no-candidate') for a in attempts[:-1])
    assert attempts[0]['status'] == 'blocked', 'Replacement requires actual access failure'
    assert attempts[-1]['status'] == 'selected' and attempts[-1]['journalId'] == selected
