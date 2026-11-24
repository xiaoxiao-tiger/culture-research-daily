"""Rebuild recommendation identities from the currently published archive."""
import json
from pathlib import Path
from paper_identity import identifiers,papers_in
root=Path(__file__).resolve().parents[1]/'site/data'
path=root/'recommended.json'
ledger={'version':1,'records':[]}
keys={(r['date'],tuple(r['identifiers'])) for r in ledger['records']}
for issue in json.loads((root/'index.json').read_text()):
    data=json.loads((root/(issue['date']+'.json')).read_text())
    for p in papers_in(data):
        ids=identifiers(p);key=(issue['date'],tuple(ids))
        if key not in keys:
            ledger['records'].append({'date':issue['date'],'title':p['title'],'identifiers':ids});keys.add(key)
    # Complete-issue recommendations live in collection.toc rather than paper cards.
    # Register newly introduced TOC articles so later runs cannot recommend them again.
    for group in data.get('groups', []):
        for entry in group.get('collection', {}).get('toc', []):
            if entry.get('status') != 'new':
                continue
            p={'title':entry['title'],'doi':entry.get('doi',''),'url':entry.get('url','')}
            ids=identifiers(p);key=(issue['date'],tuple(ids))
            if ids and key not in keys:
                ledger['records'].append({'date':issue['date'],'title':p['title'],'identifiers':ids});keys.add(key)
path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(f"Registered {len(ledger['records'])} recommendations.")
