import json,sys,tempfile,unittest,subprocess,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'scripts'))
from reading_plan import rotation,core_request,apply_core
from apply_search_request import parse_request
class ReadingPlan(unittest.TestCase):
 def test_rotation_is_independent_and_repeats(self):
  plan=json.loads((root/'site/data/reading-plan.json').read_text())
  self.assertEqual(rotation(plan,'2026-10-16','communication')['id'],'joc')
  self.assertEqual(rotation(plan,'2026-10-22','communication')['id'],'sms')
  self.assertEqual(rotation(plan,'2026-10-23','communication')['id'],'joc')
  self.assertEqual(rotation(plan,'2026-10-22','general')['id'],'pnas')
 def test_core_request_owner_and_idempotence(self):
  payload={'papers':[dict(title='Example',url='https://doi.org/10.1/example',doi='10.1/example',topicIds=['culture'],note='')]}
  body='<!-- daily-core-papers:v1 -->\n```json\n'+json.dumps(payload)+'\n```'
  self.assertEqual(core_request(body),payload)
  with tempfile.TemporaryDirectory() as tmp:
   path=Path(tmp)/'core.json';path.write_text(json.dumps(dict(version=1,owner='owner',requests=[])))
   with self.assertRaises(AssertionError):apply_core(body,4,'now','owner','other','owner',path)
   for _ in range(2):apply_core(body,4,'now','owner','owner','owner',path)
   self.assertEqual(len(json.loads(path.read_text())['requests']),1)
  payload['papers'][0]['url']='javascript:alert(1)'
  with self.assertRaises(AssertionError):core_request('<!-- daily-core-papers:v1 -->\n```json\n'+json.dumps(payload)+'\n```')
 def test_topic_request_preserves_legacy(self):
  data=dict(effectiveDate='2026-10-16',scope='once',themeKeywords='x',journalKeywords='y',excludeTerms='',lookbackDays=30)
  def parse():return parse_request('<!-- daily-search-settings:v1 -->\n```json\n'+json.dumps(data)+'\n```')
  self.assertNotIn('topicIds',parse());data['topicIds']=['sycophancy'];self.assertEqual(parse()['topicIds'],['sycophancy'])
  data['topicIds']=['leader']
  with self.assertRaises(AssertionError):parse()
 def test_schema6_collection_and_history(self):
  with tempfile.TemporaryDirectory() as tmp:
   target=Path(tmp);shutil.copytree(root/'scripts',target/'scripts');shutil.copytree(root/'site/data',target/'site/data');data=target/'site/data'
   old=json.loads((data/'2026-10-15.json').read_text());old.update(date='2026-10-16',schemaVersion=6,shortfallReason='Fixture access limitation',periodicalChecks=[dict(platform='publisher',query='https://example.org',timeRange='today',purpose='browse',status='partial')])
   cross=old['groups'][0];cross['target']=5;cross['papers']=[p for p in cross['papers'] if p.get('selectionBucket')=='latest'][:3]+[p for p in cross['papers'] if p.get('selectionBucket')=='cited'][:2];cross['selectionBuckets'][0]['target']=3;cross['selectionBuckets'][1]['target']=2;cross['latestSourceExceptions']='fixture source blocked'
   cross['sourceCoverage']=[dict(database=db,status='included' if any(p['sourceDatabase']==db for p in cross['papers']) else 'unavailable',reason='fixture') for db in ['NBER','SSRN','arXiv']]
   old['groups'][1]['journalPriorityNote']='fixture communication unavailable'
   old['groups']+= [dict(id='communication-issue',label='传播学整期',unit='issue',target=0,sortBy='issue',papers=[],collection=dict(journalId='joc',journalName='Journal of Communication',kind='online-first',title='Online First',url='https://example.org/issue',checkedAt='2026-10-16',complete=False,toc=[])),dict(id='general-science',label='综合期刊',target=1,sortBy='publicationDate',rotationJournalId='pnas',papers=[])]
   for g in old['groups']:
    for p in g['papers']:p.update(topicIds=['culture'],readingUse='理论框架',researchConnection='fixture',readingPriority='normal',priorityReason='fixture')
   (data/'index.json').write_text(json.dumps([dict(date='2026-10-16',title='fixture',count=7)]));(data/'recommended.json').write_text(json.dumps(dict(version=1,records=[])))
   path=data/'2026-10-16.json'
   def check(error=None):
    path.write_text(json.dumps(old));result=subprocess.run([sys.executable,str(target/'scripts/validate.py')],capture_output=True,text=True)
    if error:self.assertNotEqual(result.returncode,0);self.assertIn(error,result.stderr)
    else:self.assertEqual(result.returncode,0,result.stderr)
   check();old['groups'][3]['rotationJournalId']='science';check('Wrong general journal');old['groups'][3]['rotationJournalId']='pnas'
   old['groups'][2]['collection']['toc']=[dict(title='not decoded',url='https://example.org',articleType='research',status='new')];check('Collection directory mismatch')
if __name__=='__main__':unittest.main()
