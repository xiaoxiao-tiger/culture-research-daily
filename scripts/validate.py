"""Check daily selection, source coverage, journal indexing and historical identities."""
import json,re
from pathlib import Path
from urllib.parse import urlparse
from paper_identity import identifiers,papers_in,normalize_title
from apply_search_request import parse_request
root=Path(__file__).resolve().parents[1]/'site/data'
index=json.loads((root/'index.json').read_text());dates=set();seen={}
ledger_path=root/'recommended.json'
ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else {'version':1,'records':[]}
assert ledger['version']==1 and isinstance(ledger['records'],list)
required=('title','titleZh','authors','venue','source','category','evidence','takeaway','theory','data','method','results','relevance','limitations','url')
journals={normalize_title(j['name']):j for j in json.loads((root/'journals.json').read_text())['journals']}
for issue in sorted(index,key=lambda x:x['date']):
    date=issue['date'];assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',date) and date not in dates;dates.add(date)
    data=json.loads((root/f'{date}.json').read_text());assert data['date']==date and data['title'] and data['summary']
    assert data['schemaVersion']==5 and data['historyPolicy']=='exclude-recommended'
    assert data['journalPolicy']=='ssci-communication-q1-q2-and-social-science'
    assert data['searchPlatforms']==['Google Scholar','NBER','SSRN','arXiv']
    groups=data['groups'];assert [g['id'] for g in groups]==['crossdisciplinary','journals']
    assert all(g['label'] and g['target']==target and 0<=len(g['papers'])<=target for g,target in zip(groups,[10,5]))
    assert [g['sortBy'] for g in groups]==['split','citationCount']
    other=groups[0]['papers'];latest=[p for p in other if p.get('selectionBucket')=='latest'];popular=[p for p in other if p.get('selectionBucket')=='cited']
    assert len(latest)<=5 and len(popular)<=5 and latest+popular==other, 'Invalid 5+5 split'
    assert [b['id'] for b in groups[0]['selectionBuckets']]==['latest','cited']
    assert data['themeSearches'] and data['searchNote']
    for row in data['themeSearches']+data.get('verificationLog',[]):
        assert all(isinstance(row.get(k),str) and row[k].strip() for k in ('platform','query','timeRange','purpose','status'))
    papers=papers_in(data);assert issue['count']==len(papers), 'Index count mismatch'
    if len(papers)<15:assert data.get('shortfallReason'), 'Explain missing papers'
    for p in papers:
        for field in required:assert isinstance(p.get(field),str) and p[field].strip(), (date,field)
        assert urlparse(p['url']).scheme=='https' and isinstance(p['year'],int)
        assert p['evidence'] in ('全文核验','摘要核验','理论综述')
        assert p['abstractZh'] and urlparse(p['abstractSource']).scheme=='https'
        assert p['abstractMode'] in ('full','unavailable')
        if p['abstractMode']=='full':assert p['originalAbstract'] and p.get('abstractLicense')
        else:assert not p.get('originalAbstract') and p.get('abstractUnavailableReason')
        for identity in identifiers(p):
            assert identity not in seen, 'Repeated paper: '+p['title']
            assert not any(identity in entry['identifiers'] and entry['date']<date for entry in ledger['records']), 'Previously recommended paper: '+p['title']
            seen[identity]=date
    for group in groups[:1]:
        assert all(p.get('sourceDatabase') in ('NBER','SSRN','arXiv') for p in group['papers'])
        coverage={c['database']:c for c in group['sourceCoverage']}
        assert set(coverage)=={'NBER','SSRN','arXiv'}, 'Missing source coverage'
        for db,c in coverage.items():
            included=any(p['sourceDatabase']==db for p in group['papers'])
            assert c['status']==('included' if included else 'unavailable'), 'Incorrect source coverage'
            if not included:assert c.get('reason'), 'Explain missing database'
    recent=latest
    assert all(re.fullmatch(r'\d{4}-\d{2}(?:-\d{2})?',p.get('publicationDate','')) and p.get('publicationDateSource') for p in recent)
    assert [p['publicationDate'] for p in recent]==sorted((p['publicationDate'] for p in recent),reverse=True), 'Publication dates out of order'
    for cited in [popular,groups[1]['papers']]:
        assert all(type(p.get('citationCount')) is int and p['citationCount']>=0 and p.get('citationSource')=='Google Scholar' and p.get('citationCheckedAt') and urlparse(p.get('citationSourceUrl','')).scheme=='https' for p in cited), 'Use actual Google Scholar citations'
        assert [p['citationCount'] for p in cited]==sorted((p['citationCount'] for p in cited),reverse=True), 'Citations out of order'
    for p in groups[1]['papers']:
        assert p['publicationType']=='journal' and p.get('discoverySource')=='Google Scholar'
        assert p.get('journalEdition')=='SSCI' and p.get('indexSource'), 'ESCI or unverified journal indexing'
        assert p.get('discipline') in ('communication','social-science')
        if p['discipline']=='communication':
            j=journals.get(normalize_title(p.get('journalName','')))
            assert j and j['edition']=='SSCI' and j['quartile'] in ('Q1','Q2'), 'Journal outside uploaded Q1/Q2 list'
            assert p['jifQuartile']==j['quartile'] and p['quartileSource']
config=json.loads((root/'search-settings.json').read_text())
assert config['version']==1 and config['owner']=='xiaoxiao-tiger'
for r in config['requests']:
    data={k:r[k] for k in ('effectiveDate','scope','themeKeywords','journalKeywords','excludeTerms','lookbackDays')}
    parse_request('<!-- daily-search-settings:v1 -->\n```json\n'+json.dumps(data)+'\n```')
    assert type(r['requestNumber']) is int and r['savedAt']
print(f'Validated {len(index)} issue(s), history, source coverage, journal scope and sorting.')
