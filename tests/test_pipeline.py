import json,os,sys,tempfile,unittest,subprocess,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'scripts'))
from apply_search_request import apply,parse_request
class Pipeline(unittest.TestCase):
    def test_owner_only_and_scope_validation(self):
        payload=dict(effectiveDate='2026-10-04',scope='once',themeKeywords='LLM sycophancy',journalKeywords='news consumption',excludeTerms='',lookbackDays=30)
        body='<!-- daily-search-settings:v1 -->\n```json\n'+json.dumps(payload)+'\n```'
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'settings.json';path.write_text(json.dumps(dict(owner='xiaoxiao-tiger',requests=[])))
            with self.assertRaises(AssertionError):apply(body,1,'2026-10-03T00:00:00Z','xiaoxiao-tiger','stranger','xiaoxiao-tiger',path)
            self.assertEqual(json.loads(path.read_text())['requests'],[])
            apply(body,1,'2026-10-03T00:00:00Z','xiaoxiao-tiger','xiaoxiao-tiger','xiaoxiao-tiger',path)
            self.assertEqual(json.loads(path.read_text())['requests'][0]['themeKeywords'],'LLM sycophancy')
            payload['scope']='unknown'
            with self.assertRaises(AssertionError):parse_request('<!-- daily-search-settings:v1 -->\n```json\n'+json.dumps(payload)+'\n```')
    def test_selection_history_and_coverage(self):
        def paper(title,db=None,count=10,bucket=None):
            p={k:'fixture' for k in ('titleZh','authors','venue','source','category','takeaway','theory','data','method','results','relevance','limitations','abstractZh')}
            p.update(title=title,url='https://example.org/'+title,year=2026,evidence='摘要核验',publicationType='working-paper',abstractMode='unavailable',originalAbstract='',abstractUnavailableReason='fixture',abstractSource='https://example.org/abstract',publicationDate='2026-09-01',publicationDateSource='https://example.org/date',citationCount=count,citationSource='Google Scholar',citationCheckedAt='2026-10-04',citationSourceUrl='https://scholar.google.com/scholar?q='+title)
            if db:p.update(sourceDatabase=db,selectionBucket=bucket)
            else:p.update(publicationType='journal',discoverySource='Google Scholar',discipline='social-science',journalEdition='SSCI',indexSource='https://example.org/index')
            return p
        other=[paper('latest'+str(i),db,bucket='latest') for i,db in enumerate(['NBER','SSRN','arXiv'])]+[paper('cited'+str(i),db,count=100-i,bucket='cited') for i,db in enumerate(['NBER','SSRN','arXiv'])]
        issue=dict(date='2026-10-04',title='fixture',summary='fixture',schemaVersion=5,historyPolicy='exclude-recommended',journalPolicy='ssci-communication-q1-q2-and-social-science',searchPlatforms=['Google Scholar','NBER','SSRN','arXiv'],searchNote='fixture',themeSearches=[dict(platform='fixture',query='fixture',timeRange='fixture',purpose='fixture',status='fixture')],shortfallReason='fixture missing candidates',groups=[dict(id='crossdisciplinary',label='其他研究',target=10,sortBy='split',selectionBuckets=[dict(id='latest'),dict(id='cited')],sourceCoverage=[dict(database=db,status='included') for db in ['NBER','SSRN','arXiv']],papers=other),dict(id='journals',label='传播学与社会科学',target=5,sortBy='citationCount',papers=[paper('journalA',count=50),paper('journalB',count=20)])])
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp);shutil.copytree(root/'scripts',target/'scripts');shutil.copytree(root/'site/data',target/'site/data');data=target/'site/data';path=data/'2026-10-04.json'
            (data/'index.json').write_text(json.dumps([dict(date=issue['date'],title=issue['title'],count=8)]))
            def check(value,expected=None,records=None):
                path.write_text(json.dumps(value));(data/'recommended.json').write_text(json.dumps(dict(version=1,records=records or [])))
                result=subprocess.run([sys.executable,str(target/'scripts/validate.py')],capture_output=True,text=True)
                if expected:self.assertNotEqual(result.returncode,0);self.assertIn(expected,result.stderr)
                else:self.assertEqual(result.returncode,0,result.stderr)
            check(issue)
            bad=json.loads(json.dumps(issue));bad['groups'][1]['papers'][0]['journalEdition']='ESCI';check(bad,'ESCI or unverified')
            bad=json.loads(json.dumps(issue));bad['groups'][0]['papers'][3]['title']='latest0';check(bad,'Repeated paper')
            old=dict(date='2026-10-01',title='previous version',identifiers=['title:latest0']);check(issue,'Previously recommended',records=[old])
            own=dict(old,date='2026-10-04');check(issue,records=[own])
            bad=json.loads(json.dumps(issue));bad['groups'][0]['papers'][0]['publicationDate']='2026-08-01';check(bad,'Publication dates out of order')
            bad=json.loads(json.dumps(issue));bad['groups'][0]['papers'][3]['citationCount']=1;check(bad,'Citations out of order')
            bad=json.loads(json.dumps(issue));bad['groups'][0]['sourceCoverage'][0]['status']='unavailable';check(bad,'Incorrect source coverage')
            bad=json.loads(json.dumps(issue))
            for p in bad['groups'][0]['papers']:
                if p['sourceDatabase']=='arXiv':p['sourceDatabase']='NBER'
            bad['groups'][0]['sourceCoverage'][2]=dict(database='arXiv',status='unavailable');check(bad,'Explain missing database')
            bad['groups'][0]['sourceCoverage'][2]['reason']='No eligible unseen candidates';check(bad)
            check(issue,records=[dict(date='2026-09-01',title='archived',identifiers=['title:archived'])])
            for _ in range(2):
                result=subprocess.run([sys.executable,str(target/'scripts/rebuild_registry.py')],capture_output=True,text=True);self.assertEqual(result.returncode,0,result.stderr)
            ledger=json.loads((data/'recommended.json').read_text());self.assertEqual(len(ledger['records']),9);self.assertEqual(ledger['records'][0]['title'],'archived')
if __name__=='__main__':unittest.main()
