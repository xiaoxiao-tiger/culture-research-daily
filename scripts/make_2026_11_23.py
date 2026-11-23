import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-23"


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
    formal(
        "How does the Chinese animation Ne Zha 2 journey to the world?—From the perspective of Intercultural New Media Studies",
        "Yan Yan and Ziye Liu",
        2026,
        "International Communication of Chinese Culture, 13(1), 131–150",
        "Springer Nature",
        "https://doi.org/10.1007/s40636-025-00351-0",
        "https://doi.org/10.1007/s40636-025-00351-0",
        "culture",
        "This mixed-methods case study develops an Intercultural Communication Diamond Model and examines news reports, X posts, YouTube comments, and Reddit discussions about Ne Zha 2. It finds platform-specific reception: X decentralizes conventional gatekeeping, YouTube content fits audience preferences but language barriers limit emotional resonance, and Reddit supports participatory meaning-making. The evidence directly concerns overseas reception of a Chinese mythological character, although it does not isolate understanding, liking, identification, and sharing intention as separate causal outcomes.",
        "Dissertation · direct overseas reception of Chinese mythology",
        tier="Downgrade tier 3: ESCI JCR Q3",
        edition="ESCI",
        quartile="JCR Q3",
        reason="No unrecommended SSCI/SCIE JCR Q1/Q2 article met the same direct foreign-audience reception threshold today.",
    ),
    formal(
        "Recognizing beauty, engaging with goodness, and approaching truth: foreign players’ cross-cultural identification with Chinese culture through Black Myth: Wukong",
        "Junhua Chen and Lin Chen",
        2026,
        "Cogent Arts & Humanities, 13(1), 2657188",
        "Taylor & Francis",
        "https://doi.org/10.1080/23311983.2026.2657188",
        "https://doi.org/10.1080/23311983.2026.2657188",
        "culture",
        "Using foreign-player and critic reviews, this study combines Scene Theory with the Cultural Iceberg Model to describe a three-level path of cross-cultural identification. Players first recognize aesthetic beauty, then engage with moral context and identity formation, and finally approach deeper cultural meanings, although deep identification remains partial. Narrative complexity and cross-cultural misunderstanding constrain reception, making this article directly relevant to distinguishing surface appreciation from deeper character and cultural identification.",
        "Dissertation · direct foreign-player identification",
        tier="Downgrade tier 3: ESCI",
        edition="ESCI",
        quartile="JCR quartile not assigned in the verified record",
        reason="A second unused SSCI/SCIE JCR Q1/Q2 paper with direct foreign-player reception evidence was not verified; this ESCI article was retained for its substantially higher direct relevance.",
    ),
]

ishow = [
    formal(
        "Selling China’s story: the multimodal semiotics of positive symbolic communication in national image building through Laowai Wanghong’s vlogs",
        "Luanying Li, Xiaoping Wu, and Richard Fitzgerald",
        2026,
        "Social Semiotics",
        "Taylor & Francis",
        "https://doi.org/10.1080/10350330.2025.2601620",
        "https://doi.org/10.1080/10350330.2025.2601620",
        "ishow-speed",
        "A multimodal critical discourse analysis examines how foreign internet celebrities use YouTube videos to represent China through modern factories, cultural richness, and a foreigner-friendly environment. The study finds that these portrayals are curated and filtered and often align implicitly with state-led image-building themes. It is directly relevant to foreign creators visiting and narrating China, but its primary evidence concerns content strategies rather than causal changes in followers’ attitudes.",
        "甲亢哥访华 · direct foreign-vlogger China representation",
        tier="Primary tier: SSCI JCR Q1/Q2",
        edition="SSCI",
        quartile="JCR Q2",
    ),
    formal(
        "Nation branding via sportswashing: An exploration of pro-China YouTube influencers and commenters around the 2022 Winter Olympic Games",
        "Authors listed on publisher record",
        2025,
        "Public Relations Review, 51(4), 102611",
        "Elsevier",
        "https://doi.org/10.1016/j.pubrev.2025.102611",
        "https://doi.org/10.1016/j.pubrev.2025.102611",
        "ishow-speed",
        "The study analyzes 27 videos from eight pro-China YouTube channels and 21,958 comments surrounding the 2022 Beijing Winter Olympics. It identifies strategies for building a desirable national brand and countering unfavorable perceptions, then compares engagement and language patterns across likely ordinary users and potentially coordinated accounts. The article offers direct evidence on foreign-facing influencer content, audience engagement, and China’s national image, while the state-linked sports campaign differs from an independent creator visit such as IShowSpeed’s.",
        "甲亢哥访华 · adjacent China-influencer audience mechanism",
        tier="Primary tier: SSCI JCR Q1/Q2",
        edition="SSCI",
        quartile="JCR Q1",
    ),
]

ai = [
    formal(
        "Generative AI, Job Satisfaction and Type of Work",
        "Dorota Bosek-Rak and Dariusz Kaszyński",
        2026,
        "Journal of Computer Information Systems, 1–16",
        "Taylor & Francis",
        "https://doi.org/10.1080/08874417.2026.2615836",
        "https://doi.org/10.1080/08874417.2026.2615836",
        "ai-wellbeing",
        "A survey of 433 white-collar employees in Poland’s financial-services sector uses ordered logit models to relate generative-AI conditions to job satisfaction. Organizational support and leadership effectiveness are positively associated with satisfaction, whereas individual enthusiasm toward GenAI is not. AI-related technostress is more strongly associated with lower satisfaction in roles highly exposed to AI-driven task transformation, indicating that workplace context and job design shape whether GenAI becomes a resource or a demand.",
        "Workplace AI and well-being · direct job-satisfaction evidence",
        tier="Primary tier: SCIE JCR Q1/Q2",
        edition="SCIE",
        quartile="JCR Q1",
    ),
    formal(
        "The impact of generative AI use on employees’ psychological distress: a moderated mediation model",
        "M. Liu, Y. Li, and J. Li",
        2026,
        "Frontiers in Public Health, 14, 1798423",
        "Frontiers",
        "https://doi.org/10.3389/fpubh.2026.1798423",
        "https://doi.org/10.3389/fpubh.2026.1798423",
        "ai-wellbeing",
        "Using survey data from 424 Chinese employees, this study tests a moderated mediation model linking workplace GenAI use to psychological distress. Job insecurity and workplace loneliness carry the positive association between use and distress, while information literacy and perceived AI ethical risk operate as boundary conditions. The results provide direct evidence of strain pathways, although the cross-sectional self-report design does not establish that GenAI use itself causes distress.",
        "Workplace AI and well-being · direct psychological-distress evidence",
        tier="Primary tier: SSCI/SCIE JCR Q1/Q2",
        edition="SSCI/SCIE",
        quartile="JCR Q1",
    ),
]

preprints = [
    paper(
        "A Game Sense Theory Approach to Translating Culturally Specific Chinese Video Games",
        "Dariush Robertson",
        2026,
        "SSRN working paper 6454141",
        "SSRN",
        "https://ssrn.com/abstract=6454141",
        "https://doi.org/10.2139/ssrn.6454141",
        "culture",
        "This working paper uses translator interviews and player-reception data to examine how culturally specific Chinese video games are localized. It argues that foreignizing strategies predominate for cultural content, while more domesticating strategies are used for interactive terms such as items and skills. Excessive transliteration is associated with less favorable player reception. The paper directly links translation choices to reception of Chinese mythological and cultural material but has not completed journal peer review.",
        "Preprint · dissertation translation and reception · not peer reviewed",
        publicationType="preprint",
        peerReviewed=False,
        publicationStatus="preprint",
        publicationDate="2026-04-12 (latest revision)",
    ),
    paper(
        "Investigating the relationship between generative AI usage and wellbeing: a multi-dimensional analysis of work and private life",
        "Shinichi Yamaguchi, Hidetaka Oshima, Yukiko Osaka, and Tomoaki Watanabe",
        2026,
        "SSRN working paper 6639121",
        "SSRN",
        "https://ssrn.com/abstract=6639121",
        "https://doi.org/10.2139/ssrn.6639121",
        "ai-wellbeing",
        "Using a large-scale Japanese survey, this working paper examines how GenAI use and use frequency relate to multiple dimensions of well-being and distinguishes work from private use. Work-related use is more strongly associated with life satisfaction, self-realization, and growth, whereas private use is more strongly associated with positive affect, social connection, and gratitude. The observational associations are context-dependent and the paper has not completed journal peer review.",
        "Preprint · workplace GenAI and multidimensional well-being · not peer reviewed",
        publicationType="preprint",
        peerReviewed=False,
        publicationStatus="preprint",
        publicationDate="2026-09-11 (latest revision)",
    ),
]

prior = json.loads((root / "2026-11-16.json").read_text())
prior_jcmc = next(g for g in prior["groups"] if g["id"] == "communication-issue")["collection"]
toc = []
for entry in prior_jcmc["toc"]:
    copied = dict(entry)
    copied["status"] = "previously-recommended"
    copied.pop("abstractZh", None)
    toc.append(copied)

groups = [
    {"id": "ishow-speed", "label": "甲亢哥访华", "target": 2, "sortBy": "relevance-quality-date", "papers": ishow},
    {"id": "x-translation", "label": "X自动翻译", "target": 2, "sortBy": "relevance-quality-date", "papers": [], "shortfallReason": "No unrecommended peer-reviewed study directly testing X/Twitter built-in translation effects on replies, reposts, interaction depth, or relationship formation was verified. Machine-translation performance studies were excluded."},
    {"id": "ai-wellbeing", "label": "使用AI提升还是降低幸福感", "target": 2, "sortBy": "relevance-quality-date", "papers": ai},
    {"id": "preprints", "label": "Preprints · arXiv / SSRN / NBER", "target": 4, "sortBy": "topic-publication-date-desc", "papers": preprints, "shortfallReason": "No new unrecommended arXiv, SSRN, or NBER paper met the strict IShowSpeed/foreign-creator China-visit threshold, and none met the X built-in translation and user-interaction threshold. Both topic slots remain unfilled rather than repeating history or using generic material."},
    {"id": "communication-issue", "label": "传播学顶刊推荐", "target": 0, "sortBy": "issue", "unit": "issue", "collection": {"journalId": "jcmc", "journalName": "Journal of Computer-Mediated Communication", "kind": "issue", "volume": "31", "issue": "6", "title": "Volume 31, Issue 6, November 2026 (In Progress)", "url": "https://academic.oup.com/jcmc/issue/31/6", "checkedAt": date, "complete": True, "toc": toc}, "papers": []},
    {"id": "general-science", "label": "综合顶刊推荐", "target": 1, "sortBy": "publicationDate", "rotationJournalId": "science", "selectedJournalId": "science", "papers": [], "shortfallReason": "No unrecommended social-science original research or review in Science was verified for the current rotation; the slot remains empty rather than substituting another journal."},
]

issue = {
    "schemaVersion": 7,
    "layoutVersion": "compact-ideas-v1",
    "date": date,
    "title": "Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary": "Two direct dissertation papers, two China-influencer papers, two workplace-AI papers, explicit formal and preprint shortfalls, two separate preprints, and the complete current JCMC issue.",
    "historyPolicy": "exclude-recommended",
    "journalPolicy": "jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms": ["Google Scholar", "NBER", "SSRN", "arXiv"],
    "themeSearches": [
        {"topicId": "culture", "platform": "Publisher sites, SSRN, and scholarly indexes", "query": "foreign audience reception Chinese mythology Ne Zha Wukong cross-cultural identification", "timeRange": "verified through 2026-11-23", "status": "completed; two direct ESCI downgrades disclosed"},
        {"topicId": "ishow-speed", "platform": "Publisher sites and SSRN", "query": "foreign influencer China visit national image YouTube audience engagement attitudes", "timeRange": "verified through 2026-11-23", "status": "two formal papers verified; no new unrecommended strict-threshold preprint"},
        {"topicId": "x-translation", "platform": "Publisher sites, arXiv, SSRN, and NBER", "query": "X Twitter built-in automatic translation cross-language replies reposts relationships", "timeRange": "verified through 2026-11-23", "status": "formal and preprint shortfall; generic machine-translation studies excluded"},
        {"topicId": "ai-wellbeing", "platform": "Publisher sites and SSRN", "query": "workplace generative AI job satisfaction technostress psychological distress wellbeing", "timeRange": "verified through 2026-11-23", "status": "two direct formal articles and one separate preprint verified"},
    ],
    "periodicalChecks": [
        {"platform": "Oxford Academic", "query": "Journal of Computer-Mediated Communication Volume 31 Issue 6", "timeRange": "checked 2026-11-23", "purpose": "Complete communication-journal issue", "status": "two research articles verified; both previously recommended and both retain English summaries"},
        {"platform": "Science", "query": "current social-science original research and reviews", "timeRange": "checked 2026-11-23", "purpose": "General top-journal rotation", "status": "no eligible unrecommended paper verified; no substitution"},
    ],
    "searchNote": "Formal-topic papers were screened in order: SSCI/SCI/SCIE JCR Q1/Q2, then Q3/Q4, then ESCI, then other peer-reviewed venues. The dissertation section uses two direct-relevance ESCI papers because no unused Q1/Q2 paper met the same foreign-audience threshold. X automatic translation is intentionally empty in both formal and preprint sections. English text is a faithful summary based on publisher or repository abstracts; it is not presented as a verbatim abstract.",
    "shortfallReason": "The X automatic-translation formal and preprint slots are empty, the IShowSpeed preprint slot has no new unrepeated candidate, and the Science rotation has no qualifying item.",
    "groups": groups,
    "coreTracking": [],
    "coreTrackingNote": "No new owner-submitted core-paper request was present.",
    "dissertation": {
        "title": "从被看见到被接收",
        "timeRange": "Current and high-relevance peer-reviewed research",
        "selectionNote": "Two direct foreign-audience studies of Chinese myth-based media are placed first; both required an explicitly disclosed ESCI downgrade.",
        "historyCoverage": "Checked the public index and permanent recommendation registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.",
        "selectedPapers": [p["doi"] for p in dissertation],
        "papers": dissertation,
        "topPapers": [{"doi": p["doi"], "reason": "Direct foreign-audience reception evidence"} for p in dissertation],
    },
}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [item for item in index if item["date"] != date]
count = len(dissertation) + sum(len(group.get("papers", [])) for group in groups)
index.insert(0, {"date": date, "title": issue["title"], "summary": issue["summary"], "edition": "正式第50期", "count": count, "file": f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
jcmc = state["communication"]["jcmc"]
jcmc.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date, reason="Official current issue reconciled as two research articles; both previously recommended and both shown with English summaries.")
jcmc.setdefault("issues", []).append({"checkedAt": date, "url": "https://academic.oup.com/jcmc/issue/31/6", "complete": True, "title": "Volume 31, Issue 6, November 2026 (In Progress)"})
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

print(root / f"{date}.json")
