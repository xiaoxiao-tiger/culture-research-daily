import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-24"


def paper(title, authors, year, venue, source, url, doi, topic, abstract, category, **extra):
    item = {
        "title": title,
        "titleZh": "Not displayed",
        "authors": authors,
        "year": year,
        "venue": venue,
        "source": source,
        "category": category,
        "evidence": "Publisher or authoritative index record verified",
        "takeaway": abstract,
        "theory": "See the linked article.",
        "data": "See the linked article.",
        "method": "See the linked article.",
        "results": abstract,
        "relevance": "Selected under the strict relevance hierarchy; adjacent evidence is explicitly labeled.",
        "limitations": "See the linked source for design-specific limitations.",
        "url": url,
        "doi": doi,
        "topicIds": [topic],
        "abstractMode": "summary",
        "originalAbstract": "",
        "abstractUnavailableReason": "Verbatim republication permission was not confirmed; this is an English summary based on the publisher or repository abstract.",
        "abstractEn": abstract,
        "abstractSource": url,
        "readingPriority": "normal",
        "priorityReason": "Direct or explicitly labeled adjacent evidence.",
        "readingUse": "Compact evidence briefing.",
        "researchConnection": "Relevant to the named research idea.",
        "publicationType": "journal",
        "peerReviewed": True,
        "publicationStatus": "published",
    }
    item.update(extra)
    return item


def formal(*args, tier, edition, quartile, reason="", **kwargs):
    return paper(
        *args,
        journalEdition=edition,
        jifQuartile=quartile,
        indexSource="Web of Science Core Collection / Journal Citation Reports",
        tierNote=f"{tier}. {reason}".strip(),
        **kwargs,
    )


dissertation = [
    formal("Intercultural circulation of canonical literature facilitated by popularizing translation: a case study of Julia Lovell’s English translation of Xi You Ji", "Jiachun Zhu and Xuanmin Luo", 2026, "Humanities and Social Sciences Communications, 13, 969", "Springer Nature", "https://doi.org/10.1057/s41599-026-07307-8", "https://doi.org/10.1057/s41599-026-07307-8", "culture", "This study uses close textual and paratextual analysis of Julia Lovell’s English Monkey King: Journey to the West to explain how popularizing translation broadens the circulation of canonical literature. It identifies transcreation through prose adaptation of poetry, recontextualized humor, generalized cultural differences, narrative condensation, and globally recognizable visual and audio elements. The evidence concerns how an Anglophone-facing version reduces specialized cultural knowledge demands and frames the Monkey King for international readers; it analyzes translation strategy and circulation rather than measuring audience attitudes experimentally.", "Dissertation · direct Chinese-myth translation and circulation", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1"),
    formal("A Meta-Analysis Examining the Role of Character-Recipient Similarity in Narrative Persuasion", "Meng Chen, Yujie Dong, and Jilong Wang", 2024, "Communication Research, 51(1)", "SAGE", "https://doi.org/10.1177/00936502231204834", "https://doi.org/10.1177/00936502231204834", "culture", "This meta-analysis synthesizes 123 effects from 19 articles on similarity between narrative characters and recipients. Character similarity produces small but significant increases in identification and self-referencing, while effects on transportation and resistance are marginal. Effects are stronger when similarity is deliberately selected rather than incidental and vary with demographic or biographical similarity, first-person perspective, and social-issue context. This is adjacent mechanism evidence rather than a study of Chinese mythology, but it directly informs whether audience-character congruence can move reception beyond liking toward identification.", "Dissertation · adjacent character-recipient congruence mechanism", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1"),
]

ishow = [
    formal("Emotion beyond boundaries: How multimodal cues foster cross-cultural affective contagion in immersive livestreaming", "Yu Zhang, Yuanyuan Liu, Haoran Mao, and Junxiang Zhao", 2026, "PLOS ONE, 21(5), e0349436", "PLOS", "https://doi.org/10.1371/journal.pone.0349436", "https://doi.org/10.1371/journal.pone.0349436", "ishow-speed", "Using Bilibili material surrounding IShowSpeed’s China tour, this study combines network analysis, sentiment analysis, and epidemiological modeling to examine cross-cultural emotional diffusion in immersive livestreaming. It finds decentralized, algorithmically amplified circulation, a prominent role for high-arousal positive emotion, and contagion patterns associated with emotional similarity. The evidence is directly tied to the China tour and helps explain how creator affect can spread across cultural boundaries, although it does not by itself establish durable changes in national image or attitudes toward China.", "甲亢哥访华 · direct IShowSpeed China-tour evidence", tier="Primary tier: SCIE JCR Q2", edition="SCIE", quartile="JCR Q2"),
    formal("“Oh my god! bro, is this really China?!” Telling the “China story” through digital storytelling: a case study of IShowSpeed’s China tour", "Mingli Mei and Guoyan Cen", 2026, "International Communication of Chinese Culture", "Springer Nature", "https://doi.org/10.1007/s40636-026-00383-0", "https://doi.org/10.1007/s40636-026-00383-0", "ishow-speed", "This mixed-methods case study analyzes IShowSpeed’s China tour as digital storytelling. It describes a combination of narrative reconstruction, emotional co-presence, multimodal presentation, and networked diffusion that turns travel livestreaming into a highly visible account of contemporary China. The study argues that the tour stimulated cultural curiosity and provided concrete, experience-based images of China, while warning that spectacle and compressed cultural explanation can flatten complexity. The article is retained for direct relevance despite its lower indexing tier.", "甲亢哥访华 · direct IShowSpeed China-tour evidence", tier="Downgrade tier 3: ESCI JCR Q3", edition="ESCI", quartile="JCR Q3", reason="Only one unrecommended SSCI/SCIE Q1/Q2 article met the direct IShowSpeed threshold; this direct case study was preferred to less relevant higher-tier work."),
]

ai = [
    formal("Artificial intelligence adoption and employee well-being: A job demands-resources perspective from academia and practice (scoping review)", "Carel Chan, Stephen Tan, Antonia Girardi, and Dominic Gasbarro", 2026, "Acta Psychologica, 270, 108047", "Elsevier", "https://doi.org/10.1016/j.actpsy.2026.108047", "https://doi.org/10.1016/j.actpsy.2026.108047", "ai-wellbeing", "This scoping review synthesizes 48 sources published from 2019 to 2025, including 35 academic studies and 13 practitioner reports, through a Job Demands–Resources lens. Existing work emphasizes stress and burnout more than engagement and gives limited attention to personal resources, work design, and job crafting. The review treats AI-enabled work as an ambivalent characteristic that can create demands and resources simultaneously and identifies job crafting as a promising way for employees to rebalance them. It offers a direct map of workplace AI and well-being evidence rather than a causal estimate from a single workforce.", "Workplace AI and well-being · direct scoping review", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1"),
    formal("Optimizing AI adoption through HR practices: Systematic review and theoretical framework for improved employee well-being", "Sitong Yu, Shota Kawasaki, Federico Magni, Kang Yang Trevor Yu, and Vijayan P. Munusamy", 2026, "Human Resource Management Review, 36(3), 101152", "Elsevier", "https://doi.org/10.1016/j.hrmr.2026.101152", "https://doi.org/10.1016/j.hrmr.2026.101152", "ai-wellbeing", "This systematic review synthesizes 74 articles on how workplace AI adoption relates to employees’ psychological, social, and physical well-being. It finds that AI presents both opportunities and challenges and that outcomes depend on how employees appraise and evaluate the technology. Drawing on the ability–motivation–opportunity model, the authors organize HR practices that can build employees’ capabilities, motivation, and opportunities to use AI while protecting well-being. The article directly addresses organizational conditions under which AI may improve or diminish well-being, but its framework integrates prior studies rather than testing one intervention.", "Workplace AI and well-being · direct systematic review", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1"),
]

preprints = []

ct_specs = [
    ("Communication and constitution: exploring classical and emerging topics relationally", "Mariaelena Bartesaghi et al.", "10.1093/ct/qtag013", "177–184", "This special-issue introduction treats communication as constitutive and relational rather than merely transmissive. It connects the issue’s articles through a relational ontology in which social forms emerge, endure, and transform through communicative events involving both humans and other-than-human actors."),
    ("Expression and reality: a dialogue on communication, constitution, and process philosophy", "Brian Massumi and Boris H. J. M. Brummans", "10.1093/ct/qtaf020", "185–195", "Presented as a theoretical dialogue, this article uses process philosophy to reconsider how communication participates in the constitution of collectives and reality. Communication is approached as expression and event, opening conceptual alternatives to models that begin with stable entities and then add relations between them."),
    ("How are worlds communicatively constituted?", "Robert B. Arundale", "10.1093/ct/qtaf015", "196–206", "This theoretical article explains how recurring everyday interaction in small-scale social worlds contributes to the constitution of larger social worlds. Repeated practices and meanings generate emergent interpretive properties through which groups become recognizable and durable."),
    ("Hybrid stakeholders and processes in social impact organizing: a constitutive approach to hybridity", "Jiawei Sophia Fu and Katherine R. Cooper", "10.1093/ct/qtaf027", "207–218", "The article develops a constitutive view of hybridity in social-impact organizing. It argues that hybrid stakeholders and hybrid processes do not merely inhabit pre-existing organizational arrangements but help communicatively construct the social reality in which impact organizing occurs."),
    ("Statues and culture wars. How statues communicatively constitute organizational cultures in conflictual situations", "Jonathan Clifton", "10.1093/ct/qtaf031", "219–228", "Using the Oxford Rhodes statue controversy and the Montreal School concept of ventriloquism, this article analyzes how statues are made to speak and act in organizational culture conflicts. It shows how material objects can be mobilized to impose or resist competing cultural narratives."),
    ("Communication skills as generic objects: a relational view", "David Boromisza-Habashi", "10.1093/ct/qtaf032", "229–240", "Drawing on public-speaking cases from the United States and China, this article asks how communication skills materialize relationally as generic objects. It argues that resources become desirable skills through their connections to valued ends and through narratives of personal transformation."),
    ("Communicative relationality meets Deleuzian techniques and forces: materializations of power in communicatively constituting a fluid social movement", "William Roth Smith", "10.1093/ct/qtag003", "241–251", "Based on interviews, observation, and social-media material from the Stop Cop City movement, this article traces how power materializes through multimodal links among activists and state actors. It extends a techniques-and-forces approach with the concept of substantiating and examines identity, geography, time, and civic relations in a fluid movement."),
    ("An articulation of the aesthetic tradition of communication theory for the future of Performance Studies in Communication", "Ethan Hunter", "10.1093/ct/qtag006", "252–261", "This theoretical article proposes an Aesthetic Tradition as an extension of Craig’s metamodel of communication theory. Reviewing nearly four decades of scholarship, it shows how the tradition can organize work in public speaking, interpersonal and family communication, organizational communication, and arts-based research."),
]
ct_papers, toc = [], []
for title, authors, doi, pages, summary in ct_specs:
    url = f"https://doi.org/{doi}"
    ct_papers.append(paper(title, authors, 2026, f"Communication Theory, 36(4), {pages}", "Oxford Academic", url, url, "methods", summary, "Communication Theory · complete issue"))
    toc.append({"title": title, "authors": authors, "doi": doi, "url": url, "status": "new", "abstractEn": summary, "abstractMode": "summary", "abstractSource": url})

groups = [
    {"id": "ishow-speed", "label": "甲亢哥访华", "target": 2, "sortBy": "relevance-quality-date", "papers": ishow},
    {"id": "x-translation", "label": "X自动翻译", "target": 2, "sortBy": "relevance-quality-date", "papers": [], "shortfallReason": "No unrecommended peer-reviewed study directly testing X/Twitter built-in translation effects on replies, reposts, interaction depth, or relationship formation was verified. Machine-translation performance studies were excluded."},
    {"id": "ai-wellbeing", "label": "使用AI提升还是降低幸福感", "target": 2, "sortBy": "relevance-quality-date", "papers": ai},
    {"id": "preprints", "label": "Preprints · arXiv / SSRN / NBER", "target": 4, "sortBy": "topic-publication-date-desc", "papers": preprints, "shortfallReason": "No new unrecommended arXiv, SSRN, or NBER candidate met the strict relevance threshold for any of the four topics. The closest built-in-translation preprint had already been recommended on 2026-11-19, so all four slots remain empty rather than repeating it or using generic material."},
    {"id": "communication-issue", "label": "传播学顶刊推荐", "target": 0, "sortBy": "issue", "unit": "issue", "collection": {"journalId": "ct", "journalName": "Communication Theory", "kind": "issue", "volume": "36", "issue": "4", "title": "Volume 36, Issue 4, November 2026", "url": "https://academic.oup.com/ct/issue/36/4", "checkedAt": date, "complete": True, "toc": toc}, "papers": []},
    {"id": "general-science", "label": "综合顶刊推荐", "target": 1, "sortBy": "publicationDate", "rotationJournalId": "science-advances", "selectedJournalId": "science-advances", "papers": [], "shortfallReason": "Science Advances volume 12, issue 46 was checked through official issue metadata. No unrecommended social-science article meeting this briefing’s relevance and verification threshold was identified, so the slot remains empty."},
]

issue = {
    "schemaVersion": 7,
    "layoutVersion": "compact-ideas-v1",
    "date": date,
    "title": "Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary": "Two dissertation papers, two IShowSpeed papers, an explicit X-translation shortfall, two workplace-AI reviews, a fully disclosed preprint shortfall, and all eight research articles in Communication Theory 36(4).",
    "historyPolicy": "exclude-recommended",
    "journalPolicy": "jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms": ["Google Scholar", "NBER", "SSRN", "arXiv"],
    "themeSearches": [
        {"topicId": "culture", "platform": "Publisher sites and scholarly indexes", "query": "Chinese mythology foreign audience translation character recipient similarity", "timeRange": "verified through 2026-11-24", "status": "two SSCI JCR Q1 papers verified; one is explicitly adjacent mechanism evidence"},
        {"topicId": "ishow-speed", "platform": "Publisher sites, SSRN, arXiv, NBER", "query": "IShowSpeed China tour audience affect national image cross-cultural", "timeRange": "verified through 2026-11-24", "status": "one SCIE Q2 direct paper and one direct ESCI Q3 downgrade; preprint shortfall"},
        {"topicId": "x-translation", "platform": "Publisher sites, arXiv, SSRN, NBER", "query": "X Twitter built-in automatic translation replies reposts relationships", "timeRange": "verified through 2026-11-24", "status": "formal and preprint shortfall; the closest preprint was already recommended"},
        {"topicId": "ai-wellbeing", "platform": "Publisher sites, PubMed, SSRN, arXiv, NBER", "query": "workplace artificial intelligence employee wellbeing job demands resources HR practices", "timeRange": "verified through 2026-11-24", "status": "two direct SSCI/SCIE Q1/Q2 reviews; preprint shortfall"},
    ],
    "periodicalChecks": [
        {"platform": "Oxford Academic", "query": "Communication Theory Volume 36 Issue 4", "timeRange": "checked 2026-11-24", "purpose": "Complete communication-journal issue", "status": "all eight Original Articles verified and supplied with English summaries"},
        {"platform": "Science Advances", "query": "Volume 12 Issue 46 current issue", "timeRange": "checked 2026-11-24", "purpose": "General top-journal rotation", "status": "no qualifying unrecommended social-science item; no substitution"},
    ],
    "searchNote": "Formal-topic papers were screened in order: SSCI/SCI/SCIE JCR Q1/Q2, then Q3/Q4, then ESCI, then other peer-reviewed venues. The second IShowSpeed article is an explicitly disclosed ESCI Q3 downgrade chosen for directness. X formal evidence remains empty. English text is a faithful summary based on publisher or repository abstracts and is not presented as a verbatim abstract.",
    "shortfallReason": "X has no formal paper; all four preprint topic slots and the Science Advances slot remain empty under the strict relevance and no-repeat rules.",
    "groups": groups,
    "coreTracking": [],
    "coreTrackingNote": "No new owner-submitted core-paper request was present.",
    "dissertation": {
        "title": "从被看见到被接收",
        "timeRange": "Current and high-relevance peer-reviewed research",
        "selectionNote": "One direct Chinese-myth translation study and one explicitly adjacent meta-analysis of character-recipient similarity are placed first.",
        "historyCoverage": "Checked the public index and permanent recommendation registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.",
        "selectedPapers": [p["doi"] for p in dissertation],
        "papers": dissertation,
        "topPapers": [{"doi": p["doi"], "reason": "Direct or explicitly adjacent evidence for reception and character congruence"} for p in dissertation],
    },
}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [item for item in index if item["date"] != date]
count = len(dissertation) + sum(len(group.get("papers", [])) for group in groups)
index.insert(0, {"date": date, "title": issue["title"], "summary": issue["summary"], "edition": "正式第51期", "count": count, "file": f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
ct = state["communication"]["ct"]
ct.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date, reason="Official Volume 36 Issue 4 reconciled as eight Original Articles; all eight were new and include English summaries.")
ct["issues"] = [row for row in ct.get("issues", []) if row.get("checkedAt") != date]
ct["issues"].append({"checkedAt": date, "url": "https://academic.oup.com/ct/issue/36/4", "complete": True, "title": "Volume 36, Issue 4, November 2026"})
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

print(root / f"{date}.json")
