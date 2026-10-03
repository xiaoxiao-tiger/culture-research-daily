"""Validate issue contracts before publishing; no external dependencies."""
import json, re
from pathlib import Path
from urllib.parse import urlparse
root = Path(__file__).resolve().parents[1] / 'site/data'
index = json.loads((root / 'index.json').read_text())
dates = set()
required = ('title','titleZh','authors','venue','source','category','evidence','takeaway','theory','data','method','results','relevance','limitations','url')
for issue in index:
    date = issue['date']
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', date), date
    assert date not in dates, 'Duplicate date'
    dates.add(date)
    data = json.loads((root / f'{date}.json').read_text())
    assert data['date'] == date and data['title'] and data['summary']
    modern = data.get('schemaVersion') == 2
    if modern:
        groups = data['groups']
        assert [g['id'] for g in groups] == ['crossdisciplinary', 'journals']
        assert all(len(g['papers']) == 10 and g['label'] for g in groups)
        assert data['searchLog'] and data['searchNote']
        for row in data['searchLog']:
            assert all(isinstance(row.get(k), str) and row[k].strip() for k in ('platform','query','timeRange','purpose','status'))
        assert all(p['publicationType'] == 'journal' for p in groups[1]['papers'])
        papers = [p for g in groups for p in g['papers']]
    else:
        papers = data['papers']
        assert 1 <= len(papers) <= 10
    assert issue['count'] == len(papers), 'Index count mismatch'
    seen = set()
    for p in papers:
        for field in required:
            assert isinstance(p.get(field), str) and p[field].strip(), (date, field)
        assert urlparse(p['url']).scheme == 'https'
        key = p.get('doi') or p['title'].casefold()
        assert key not in seen, 'Duplicate paper'
        seen.add(key)
        assert isinstance(p['year'], int)
        assert p['evidence'] in ('全文核验','摘要核验','理论综述')
        if modern:
            assert all(isinstance(p.get(k), str) and p[k].strip() for k in ('originalAbstract','abstractZh','abstractSource'))
            assert urlparse(p['abstractSource']).scheme == 'https'
            assert p['abstractMode'] in ('full','excerpt')
            if p['abstractMode'] == 'full':
                assert p.get('abstractLicense'), 'Full abstract needs explicit permission'
            else:
                assert len(p['originalAbstract'].split()) <= 25, 'Excerpt exceeds quote limit'
print(f'Validated {len(index)} issue(s).')
