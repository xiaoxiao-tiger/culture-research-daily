"""Validate all published issues before Pages deploys; no external dependencies."""
import json, re
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1] / 'site/data'
index = json.loads((root / 'index.json').read_text())
dates = set()
required = ('title', 'titleZh', 'authors', 'venue', 'source', 'category', 'evidence', 'takeaway', 'theory', 'data', 'method', 'results', 'relevance', 'limitations', 'url')
for issue in index:
    date = issue['date']
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', date), date
    assert date not in dates, 'Duplicate date'
    dates.add(date)
    data = json.loads((root / f'{date}.json').read_text())
    assert data['date'] == date and data['title'] and data['summary']
    assert 1 <= len(data['papers']) <= 10
    seen = set()
    for p in data['papers']:
        for field in required:
            assert isinstance(p.get(field), str) and p[field].strip(), (date, field)
        assert urlparse(p['url']).scheme == 'https'
        assert p['title'].casefold() not in seen
        seen.add(p['title'].casefold())
        assert isinstance(p['year'], int)
        assert p['evidence'] in ('全文核验', '摘要核验', '理论综述')
print(f'Validated {len(index)} issue(s).')
