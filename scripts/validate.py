"""Validate published issues, source quartiles and ordering before Pages deploys."""
import json,re
from pathlib import Path
from urllib.parse import urlparse
from paper_identity import identifiers, papers_in, normalize_title
from apply_search_request import parse_request
root=Path(__file__).resolve().parents[1]/'site/data'
index=json.loads((root/'index.json').read_text());dates=set();seen={}
required=('title','titleZh','authors','venue','source','category','evidence','takeaway','theory','data','method','results','relevance','limitations','url')
journal_data=json.loads((root/'journals.json').read_text())
journals={normalize_title(j['name']):j for j in journal_data['journals']}
for issue in sorted(index,key=lambda x:x['date']):
    date=issue['date'];assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',date) and date not in dates;dates.add(date)
    data=json.loads((root/f'{date}.json').read_text());assert data['date']==date and data['title'] and data['summary']
    schema=data.get('schemaVersion',1)
    target=data.get('recommendationTargetPerGroup',10)
    assert type(target) is int and target in (5,10), 'Invalid recommendation target'
    if schema>=2:
        assert [g['id'] for g in data['groups']]==['crossdisciplinary','journals']
        assert all(g['label'] and (0<=len(g['papers'])<=target if schema>=3 else len(g['papers'])==10) for g in data['groups'])
        assert all(p['publicationType']=='journal' for p in data['groups'][1]['papers'])
        searches=data.get('themeSearches') if schema>=3 else data.get('searchLog')
        assert searches and data['searchNote'], 'Missing theme searches'
        for row in searches+data.get('verificationLog',[]):
            assert all(isinstance(row.get(k),str) and row[k].strip() for k in ('platform','query','timeRange','purpose','status'))
    papers=papers_in(data);assert issue['count']==len(papers), 'Index count mismatch'
    if schema>=3 and len(papers)<2*target: assert data.get('shortfallReason'), 'Explain missing papers'
    for p in papers:
        for field in required: assert isinstance(p.get(field),str) and p[field].strip(), (date,field)
        assert urlparse(p['url']).scheme=='https' and isinstance(p['year'],int)
        assert p['evidence'] in ('全文核验','摘要核验','理论综述')
        if schema>=2:
            assert p['abstractZh'] and urlparse(p['abstractSource']).scheme=='https'
            assert p['abstractMode'] in (('full','unavailable') if schema>=3 else ('full','excerpt'))
            if p['abstractMode']=='full': assert p['originalAbstract'] and p.get('abstractLicense')
            elif schema>=3: assert not p.get('originalAbstract') and p.get('abstractUnavailableReason')
            else: assert len(p['originalAbstract'].split())<=25
    if schema>=3:
        assert data.get('journalPolicy') in ('uploaded-jcr-q1-q2','communication-q1-q2-and-social-science','ssci-communication-q1-q2-and-social-science')
        for p in data['groups'][1]['papers']:
            if schema>=4:
                assert p.get('journalEdition')=='SSCI' and p.get('indexSource'), 'ESCI or unverified journal indexing'
            if schema>=4 and p.get('discipline')=='social-science': continue
            j=journals.get(normalize_title(p.get('journalName','')))
            assert j and j['quartile'] in ('Q1','Q2'), 'Journal outside uploaded Q1/Q2 list: '+p['venue']
            assert p['jifQuartile']==j['quartile'] and p['journalEdition']==j['edition'] and p['quartileSource']
    if schema>=4:
        assert data['historyPolicy']=='repeat-allowed'
        assert data.get('searchPlatforms')==['Google Scholar','NBER','SSRN','arXiv']
        assert all(p.get('discoverySource')=='Google Scholar' and p.get('citationSource')=='Google Scholar' for p in data['groups'][1]['papers']), 'Use actual Google Scholar citations'
        recent=data['groups'][0]['papers']; cited=data['groups'][1]['papers']
        assert all(re.fullmatch(r'\d{4}-\d{2}(?:-\d{2})?',p.get('publicationDate','')) and p.get('publicationDateSource') for p in recent)
        assert [p['publicationDate'] for p in recent]==sorted((p['publicationDate'] for p in recent),reverse=True), 'Publication dates out of order'
        assert all(type(p.get('citationCount')) is int and p['citationCount']>=0 and p.get('citationSource') and p.get('citationCheckedAt') and p.get('citationSourceUrl') for p in cited)
        assert [p['citationCount'] for p in cited]==sorted((p['citationCount'] for p in cited),reverse=True), 'Citations out of order'
config=json.loads((root/'search-settings.json').read_text())
assert config['version']==1 and config['owner']=='xiaoxiao-tiger'
for r in config['requests']:
    data={k:r[k] for k in ('effectiveDate','scope','themeKeywords','journalKeywords','excludeTerms','lookbackDays')}
    parse_request('<!-- daily-search-settings:v1 -->\n```json\n'+json.dumps(data)+'\n```')
    assert type(r['requestNumber']) is int and r['savedAt']
print(f'Validated {len(index)} issue(s), journal scope, settings and sorting.')
