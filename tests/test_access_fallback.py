import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from access_fallback import validate_fallback, validate_unverified, validate_rotation_fallback

class AccessFallbackTests(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((Path(__file__).resolve().parents[1] / 'site/data/reading-plan.json').read_text())
        self.meta = {'reason':'Google Scholar human verification', 'channel':'Publisher', 'checkedAt':'2026-11-01'}

    def test_documented_fallback(self):
        validate_fallback(self.meta, '2026-11-01')

    def test_no_retroactive_fallback(self):
        with self.assertRaises(AssertionError):
            validate_fallback(self.meta, '2026-10-31')

    def test_incomplete_evidence_rejected(self):
        with self.assertRaises(AssertionError):
            validate_fallback({'reason':'blocked'}, '2026-11-01')

    def test_unknown_citations_not_zero(self):
        p = {'citationStatus':'unverified', 'citationNote':'本次Google Scholar引用次数未核验'}
        validate_unverified(p)
        with self.assertRaises(AssertionError):
            validate_unverified(dict(p, citationCount=0))

    def test_ordered_rotation_replacement(self):
        g = {'rotationJournalId':'scientific-data', 'selectedJournalId':'nature-communications', 'papers':[{}],
             'rotationFallback':{'reason':'verification wall', 'checkedAt':'2026-11-01', 'attempts':[
                 {'journalId':'scientific-data','status':'blocked','reason':'human verification'},
                 {'journalId':'nature-communications','status':'selected','reason':'eligible paper verified'}]}}
        validate_rotation_fallback(g, self.plan, '2026-11-01')
        bad = copy.deepcopy(g)
        bad['rotationFallback']['attempts'][0]['status'] = 'no-candidate'
        with self.assertRaises(AssertionError):
            validate_rotation_fallback(bad, self.plan, '2026-11-01')
        bad = copy.deepcopy(g)
        bad['selectedJournalId'] = 'pnas'
        bad['rotationFallback']['attempts'][-1]['journalId'] = 'pnas'
        with self.assertRaises(AssertionError):
            validate_rotation_fallback(bad, self.plan, '2026-11-01')

if __name__ == '__main__':
    unittest.main()
