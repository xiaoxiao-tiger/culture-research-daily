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
    def test_publish_blocks_duplicate_and_wrong_quartile(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp);shutil.copytree(root/'scripts',target/'scripts');shutil.copytree(root/'site/data',target/'site/data')
            path=target/'site/data/2026-10-03.json';original=json.loads(path.read_text());bad=json.loads(path.read_text());bad['groups'][1]['papers'][0]['journalName']='A journal absent from user list';path.write_text(json.dumps(bad))
            result=subprocess.run([sys.executable,str(target/'scripts/validate.py')],capture_output=True,text=True);self.assertNotEqual(result.returncode,0);self.assertIn('outside uploaded Q1/Q2',result.stderr)
            path.write_text(json.dumps(original));later=json.loads(path.read_text());later['date']='2026-10-04';(target/'site/data/2026-10-04.json').write_text(json.dumps(later));idx=json.loads((target/'site/data/index.json').read_text());idx.append(dict(date='2026-10-04',title=later['title'],count=sum(len(g['papers']) for g in later['groups'])));(target/'site/data/index.json').write_text(json.dumps(idx))
            result=subprocess.run([sys.executable,str(target/'scripts/validate.py')],capture_output=True,text=True);self.assertNotEqual(result.returncode,0);self.assertIn('Repeated paper',result.stderr)
if __name__=='__main__':unittest.main()
