"""Preserve historical entries and append newly recommended papers. Never reset the ledger."""
import json
from pathlib import Path
from paper_identity import identifiers, papers_in
root=Path(__file__).resolve().parents[1]/'site/data'
path=root/'recommended.json'
ledger=json.loads(path.read_text()) if path.exists() else {'version':1,'papers':[]}
for issue in sorted(json.loads((root/'index.json').read_text()),key=lambda x:x['date']):
    data=json.loads((root/f"{issue['date']}.json").read_text())
    for p in papers_in(data):
        ids=identifiers(p)
        old=next((r for r in ledger['papers'] if set(ids)&set(r['identifiers'])),None)
        if old:
            if old['firstRecommended']!=issue['date']:
                raise ValueError(f"Repeated paper on {issue['date']}: {p['title']}")
            old['identifiers']=sorted(set(old['identifiers'])|set(ids))
        else:
            ledger['papers'].append({'title':p['title'],'authors':p['authors'],'doi':p.get('doi',''),'identifiers':ids,'firstRecommended':issue['date']})
path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(f"Registry contains {len(ledger['papers'])} distinct recommendations.")
