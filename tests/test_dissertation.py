import sys, unittest, json, tempfile, shutil, subprocess
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from paper_identity import papers_in,identifiers

class DissertationTests(unittest.TestCase):
    def test_supplement_is_registered_but_references_are_not(self):
        a={'title':'A','doi':'10.1/a'};b={'title':'B','doi':'10.1/b'}
        data={'groups':[{'papers':[a]}],'dissertation':{'papers':[b],'selectedPapers':['10.1/a','10.1/b'],'topPapers':[{'doi':'10.1/a'}]}}
        self.assertEqual(papers_in(data),[a,b])
        self.assertEqual(papers_in({'papers':[a]}),[a])
    def test_cross_section_aliases_share_identity(self):
        a={'title':'Online First','doi':'10.1/first'}
        b={'title':'Published title','doi':'10.1/final','identityAliases':['doi:10.1/first']}
        self.assertTrue(set(identifiers(a)) & set(identifiers(b)))
    def test_validator_rejects_unpublished_and_unresolved_priorities(self):
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp);shutil.copytree(root/'scripts',target/'scripts');shutil.copytree(root/'site/data',target/'site/data')
            path=target/'site/data/2026-10-20.json';original=json.loads(path.read_text())
            for mutate,message in [
                (lambda d:d['dissertation']['papers'][0].update(peerReviewed=False),'Dissertation requires peer-reviewed'),
                (lambda d:d['dissertation']['topPapers'][0].update(doi='https://doi.org/10.invalid/missing'),'Invalid dissertation priorities'),
                (lambda d:d['dissertation']['papers'][0].update(doi=d['groups'][1]['papers'][0]['doi']),'Unresolved dissertation reference')]:
                data=json.loads(json.dumps(original));mutate(data);path.write_text(json.dumps(data))
                result=subprocess.run([sys.executable,str(target/'scripts/validate.py')],capture_output=True,text=True)
                self.assertNotEqual(result.returncode,0);self.assertIn(message,result.stderr)

if __name__=='__main__':unittest.main()
