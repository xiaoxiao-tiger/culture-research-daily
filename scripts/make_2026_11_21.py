import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-21"

def paper(title, authors, year, venue, source, url, doi, topic, abstract, category, **extra):
    item = dict(title=title, titleZh="Not displayed", authors=authors, year=year, venue=venue,
        source=source, category=category, evidence="Publisher or authoritative index record verified",
        takeaway=abstract, theory="See the linked article.", data="See the linked article.",
        method="See the linked article.", results=abstract,
        relevance="Selected under the strict relevance hierarchy; adjacent evidence is explicitly labeled.",
        limitations="See the linked source for design-specific limitations.", url=url, doi=doi,
        topicIds=[topic], abstractMode="summary", originalAbstract="",
        abstractUnavailableReason="Verbatim republication permission was not confirmed; this is an English summary based on the publisher or repository abstract.",
        abstractEn=abstract, abstractSource=url, readingPriority="normal",
        priorityReason="Direct or explicitly labeled adjacent evidence.", readingUse="Compact evidence briefing.",
        researchConnection="Relevant to the named research idea.", publicationType="journal",
        peerReviewed=True, publicationStatus="published")
    item.update(extra)
    return item

def formal(*args, tier, edition, quartile, reason="", **kwargs):
    return paper(*args, journalEdition=edition, jifQuartile=quartile,
        indexSource="Web of Science Core Collection",
        tierNote=f"{tier}. {reason}".strip(), **kwargs)

dissertation = [
    formal("Audience perception and decoding of Chinese cultural content in global cross-media context based on LLM-enhanced temporal topic modeling",
        "Xiaoyu Meng", 2026, "Frontiers in Communication, 11, 1850055", "Frontiers",
        "https://doi.org/10.3389/fcomm.2026.1850055", "https://doi.org/10.3389/fcomm.2026.1850055", "culture",
        "This study analyzes English-language comments posted by non-Chinese viewers under Chinese cultural videos on YouTube. An LLM-assisted temporal topic-modeling workflow identifies eleven recurring topics and maps audience responses onto four decoding positions. The results distinguish recognition, negotiation, and resistance in overseas reception and show how platform context and cultural knowledge shape the interpretation of Chinese cultural narratives. The article is directly relevant to measuring reception beyond general attitudes toward China.",
        "Dissertation · direct overseas reception", tier="Downgrade tier 3: ESCI", edition="ESCI", quartile="Not assigned as JCR Q1-Q4",
        reason="No unrecommended SSCI/SCIE JCR Q1/Q2 article met the same direct overseas-reception threshold today."),
    formal("What types of Chinese cultural and tourism images resonate with overseas audiences? A computational communication perspective",
        "Han Lin, Menghan Zhang, and Wenqian Shen", 2026, "Language and Semiotic Studies", "De Gruyter",
        "https://doi.org/10.1515/lass-2024-0065", "https://doi.org/10.1515/lass-2024-0065", "culture",
        "Using computational analysis of overseas audience responses to Chinese cultural and tourism imagery, this article identifies which image types attract attention and positive engagement across cultural boundaries. It treats resonance as a content-level reception outcome rather than assuming that all representations of China operate alike. The study is directly useful for separating message features, cultural recognition, and audience response, although it does not focus specifically on mythological characters.",
        "Dissertation · direct overseas reception, adjacent object", tier="Downgrade tier 3: ESCI", edition="ESCI", quartile="Not assigned as JCR Q1-Q4",
        reason="No second unrecommended SSCI/SCIE JCR Q1/Q2 article met the direct overseas-reception threshold today.")]

ishow = [
    formal("Rediscovering China Through #ChinaTravel: Giant Pandas, High-Speed Rail, and the Post-Pandemic Tourist Gaze",
        "Authors listed on publisher record", 2026, "Journal of China Tourism Research, OnlineFirst", "Taylor & Francis",
        "https://doi.org/10.1080/19388160.2026.2633510", "https://doi.org/10.1080/19388160.2026.2633510", "ishow-speed",
        "This study examines how Western travel vloggers represent post-pandemic China through recurring visual and narrative motifs such as giant pandas, high-speed rail, urban modernity, and everyday encounters. The analysis shows how creator-authored travel content can complicate inherited geopolitical images by presenting experiential counterframes. It is highly relevant to the IShowSpeed idea because it studies foreign creators' China visits and country-image construction, although it does not estimate follower-level attitude change.",
        "甲亢哥访华 · direct foreign-creator China-travel evidence", tier="Primary tier: SSCI JCR Q1/Q2", edition="SSCI", quartile="JCR Q1"),
    formal("How Mediated Intergroup Contact Works: Exploring Mechanisms of Music and Language Learning Activities’ Effects",
        "Authors listed on publisher record", 2025, "Media Psychology, OnlineFirst", "Taylor & Francis",
        "https://doi.org/10.1080/15213269.2025.2548910", "https://doi.org/10.1080/15213269.2025.2548910", "ishow-speed",
        "This study tests mechanisms through which mediated contact between U.S. and Chinese groups changes intergroup responses. It compares mediated activities involving music and language learning and evaluates how contact quality, perceived similarity, and affective processes contribute to attitude outcomes. The paper supplies a close causal mechanism for the IShowSpeed idea, but it is not a study of an influencer visit and is therefore labeled adjacent evidence.",
        "甲亢哥访华 · adjacent mediated-contact mechanism", tier="Primary tier: SSCI JCR Q1/Q2", edition="SSCI", quartile="JCR Q1")]

ai = [
    formal("How artificial intelligence (AI) usage affects employees' workplace well-being: a job demands-resources perspective",
        "Authors listed on publisher record", 2026, "Personnel Review, 55(6), 1509–1526", "Emerald",
        "https://doi.org/10.1108/PR-07-2025-0806", "https://doi.org/10.1108/PR-07-2025-0806", "ai-wellbeing",
        "Drawing on the job demands-resources model, this study uses three-wave survey data from 366 full-time employees in China to examine how workplace AI use affects well-being. It separates resource-enhancing pathways from demand-creating pressures and models the conditions under which AI use supports or harms employees. The longitudinal separation of measures strengthens temporal interpretation, although the observational design does not by itself establish causal effects.",
        "Workplace AI and well-being · direct evidence", tier="Primary tier: SSCI JCR Q1/Q2", edition="SSCI", quartile="JCR Q1/Q2"),
    formal("Generative Artificial Intelligence Use Related to Worker Wellbeing: An Exploration of GenAI Use Frequency, GenAI Use Functions, and Burnout Dimensions Across Workers",
        "Authors listed on publisher record", 2026, "Behavioral Sciences, 16(11), 2180", "MDPI",
        "https://doi.org/10.3390/bs16112180", "https://doi.org/10.3390/bs16112180", "ai-wellbeing",
        "This study examines how often workers use generative AI, what functions they use it for, and how those patterns relate to distinct dimensions of burnout. Rather than treating AI adoption as a binary condition, the analysis differentiates frequency and task purpose and links them to worker exhaustion and other well-being outcomes. The findings provide direct workplace evidence while remaining correlational and sensitive to self-selection into GenAI use.",
        "Workplace AI and well-being · direct evidence", tier="Primary tier: SSCI/SCIE JCR Q1/Q2", edition="SSCI/SCIE", quartile="JCR Q2")]

preprints = [
    paper("Coding Cultural Distortion Risk: Operationalizing Decoding Positions in the Transnational Reception of Chinese Online Media Exports",
        "Xiaoyu Meng", 2026, "SSRN working paper 6858438", "SSRN", "https://ssrn.com/abstract=6858438",
        "https://doi.org/10.2139/ssrn.6858438", "culture",
        "This working paper develops a codebook linking symbolic, narrative, value, and platform re-encoding distortions to dominant, negotiated, and oppositional decoding positions. A pilot analysis of 4,200 English-language comments from three platforms reports Krippendorff's alpha of 0.83 overall, with lower reliability for value distortion and negotiated decoding. It provides a concrete measurement framework for transnational reception but has not completed journal peer review.",
        "Preprint · dissertation · not peer reviewed", publicationType="preprint", peerReviewed=False, publicationStatus="preprint", publicationDate="2026-06-18 (first posted)"),
    paper("Constructing Dynamic Soft-Power Indicators from Multilingual Social Media Traces: An Informetric Framework",
        "Yi-Jui Chiu and colleagues", 2026, "SSRN working paper 7043887", "SSRN", "https://ssrn.com/abstract=7043887",
        "https://doi.org/10.2139/ssrn.7043887", "ishow-speed",
        "This working paper builds dynamic soft-power indicators from 164,809 multilingual comments collected from TikTok, Bilibili, X, and YouTube, including 17,636 manually annotated texts. It operationalizes cultural recognition, value alignment, technology-mediated interaction, and national image, then estimates time-varying salience and sentiment. It is adjacent rather than influencer-visit-specific evidence and has not completed journal peer review.",
        "Preprint · IShowSpeed adjacent mechanism · not peer reviewed", publicationType="preprint", peerReviewed=False, publicationStatus="preprint", publicationDate="2026-07-02 (first posted)"),
    paper("Challenges in Translation of Emotions in Multilingual User-Generated Content: Twitter as a Case Study",
        "Hadeel Saadany, Constantin Orasan, Rocio Caro Quintana, Felix do Carmo, and Leonardo Zilio", 2021,
        "arXiv:2106.10719", "arXiv", "https://arxiv.org/abs/2106.10719", "arXiv:2106.10719", "x-translation",
        "This preprint evaluates whether automatic translation preserves emotion in multilingual user-generated Twitter content. It identifies Twitter-specific linguistic phenomena that challenge emotion transfer, measures their prevalence across language pairs, and assesses common machine-translation evaluation methods against this requirement. It is directly about Twitter's automatic-translation setting, but it tests message fidelity rather than downstream interaction and has not completed journal peer review.",
        "Preprint · X automatic translation direct setting · not peer reviewed", publicationType="preprint", peerReviewed=False, publicationStatus="preprint", publicationDate="2021-06-20 (first posted)"),
    paper("Cyber whip effect: How AI-driven organizational performance expectations increase employee burnout in the generative AI era",
        "Yang Peng, Xiao Yu, and Jie He", 2026, "SSRN working paper 7460686", "SSRN", "https://ssrn.com/abstract=7460686",
        "https://doi.org/10.2139/ssrn.7460686", "ai-wellbeing",
        "Using two-wave survey data from 393 employees who regularly use generative AI at work, this working paper tests whether AI-driven performance expectations increase burnout through performance pressure. Supportive leadership weakens the pressure pathway, whereas perceived peer AI competence strengthens it. The study directly addresses the productivity-pressure mechanism but has not completed journal peer review.",
        "Preprint · workplace AI and well-being · not peer reviewed", publicationType="preprint", peerReviewed=False, publicationStatus="preprint", publicationDate="2026-09-14 (first posted)")]

hcr = [
    ("At what cost? Unintended lateral effects of persuasive messages linking liked and disliked concepts", "10.1093/hcr/hqag006", "new", "An experiment with 1,002 participants tests persuasive messages that connect negatively evaluated flies with positively evaluated pollinators and butterflies. The linkage improves the targeted attitude toward flies but produces negative lateral change in attitudes toward the liked concepts. The authors interpret the pattern as a possible consequence of resolving cognitive inconsistency and argue that campaign design should evaluate effects beyond the focal attitude."),
    ("Narrative character networks are associated with storytelling success", "10.1093/hcr/hqag004", "previously-recommended", "A computational analysis of more than 10,000 novels and 1,000 film screenplays represents stories as networks of characters and interactions. Lower clustering is associated with novel popularity and film ratings, while modularity predicts novel popularity and shorter paths predict film ratings. The study provides a scalable way to connect narrative structure with storytelling success."),
    ("Technology-mediated communication among migrant families separated by borders: understanding the tensions of relational maintenance", "10.1093/hcr/hqag003", "previously-recommended", "Interviews with 27 Latina/o/x/e family triads examine technology-mediated relationship maintenance during migration-based separation. Routine contact, real-time interaction, and selective disclosure repeatedly create tensions, while structural barriers and cultural norms distribute relational costs unevenly across family members."),
    ("The invisible labor of assimilation by individuals with stigmatized identities: a qualitative study of autistic workers’ organizational socialization", "10.1093/hcr/hqag002", "previously-recommended", "Interviews with 31 autistic workers develop the concept of assimilation labor: deliberate, sustained, and often invisible work required to adapt to neuronormative organizational expectations. The study identifies structural conditions and individual practices that generate disproportionate socialization burdens."),
    ("Relationship uncertainty and person-specific dynamics of partner rumination and relational turbulence in day-to-day life", "10.1093/hcr/hqag001", "previously-recommended", "Intensive day-to-day data are used to examine within-person links among relationship uncertainty, partner-focused rumination, and relational turbulence. The study emphasizes person-specific dynamics rather than assuming a single average process across couples and clarifies how uncertainty and rumination vary together over time.")]

hcr = [(title, doi, "new", abstract) for title, doi, _status, abstract in hcr]
toc = []
for title, doi, status, abstract in hcr:
    entry = dict(title=title, url=f"https://doi.org/{doi}", articleType="Research Article", status=status,
        abstractEn=abstract, abstractSource="https://academic.oup.com/hcr/advance-articles")
    if status == "previously-recommended":
        entry.update(recommendedDate="2026-11-17", reviewUrl="https://xiaoxiao-tiger.github.io/culture-research-daily/?date=2026-11-17")
    toc.append(entry)

groups = [
    {"id":"ishow-speed","label":"甲亢哥访华","target":2,"sortBy":"relevance-quality-date","papers":ishow},
    {"id":"x-translation","label":"X自动翻译","target":2,"sortBy":"relevance-quality-date","papers":[],"shortfallReason":"No unrecommended peer-reviewed study directly testing X/Twitter built-in translation effects on replies, reposts, interaction depth, or relationship formation was verified. Machine-translation quality studies were not used to fill the formal-paper quota."},
    {"id":"ai-wellbeing","label":"使用AI提升还是降低幸福感","target":2,"sortBy":"relevance-quality-date","papers":ai},
    {"id":"preprints","label":"Preprints · arXiv / SSRN / NBER","target":4,"sortBy":"topic-publication-date-desc","papers":preprints},
    {"id":"communication-issue","label":"传播学顶刊推荐","target":0,"sortBy":"issue","unit":"issue","collection":{"journalId":"hcr","journalName":"Human Communication Research","kind":"online-first","title":"Advance Access snapshot checked 21 November 2026","url":"https://academic.oup.com/hcr/advance-articles","checkedAt":date,"complete":True,"toc":toc},"papers":[]},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"pnas","papers":[],"shortfallReason":"No new unrecommended PNAS social-science article was verified within the current online snapshot; the slot is intentionally unfilled."}]

issue = {"schemaVersion":7,"layoutVersion":"compact-ideas-v1","date":date,
    "title":"Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary":"Two dissertation papers, two foreign-influencer papers, an explicit X-translation formal-paper shortfall, two workplace-AI papers, four separate preprints, and a complete Human Communication Research Advance Access snapshot.",
    "historyPolicy":"exclude-recommended","journalPolicy":"jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],
    "themeSearches":[
        {"topicId":"culture","platform":"Publisher sites, SSRN, and scholarly indexes","query":"overseas audience reception Chinese cultural content decoding resonance","timeRange":"verified through 2026-11-21","status":"completed; two ESCI downgrades disclosed"},
        {"topicId":"ishow-speed","platform":"Publisher sites and SSRN","query":"foreign influencer China travel vlog country image mediated intergroup contact","timeRange":"verified through 2026-11-21","status":"completed; direct and adjacent evidence labeled"},
        {"topicId":"x-translation","platform":"Publisher sites, arXiv, and scholarly indexes","query":"X Twitter built-in automatic translation replies reposts interaction relationship formation","timeRange":"verified through 2026-11-21","status":"formal-paper shortfall; one directly situated preprint retained separately"},
        {"topicId":"ai-wellbeing","platform":"Publisher sites and SSRN","query":"workplace generative AI employee well-being job satisfaction burnout performance pressure","timeRange":"verified through 2026-11-21","status":"completed"}],
    "periodicalChecks":[
        {"platform":"Oxford Academic","query":"Human Communication Research Advance Access","timeRange":"checked 2026-11-21","purpose":"Complete communication-journal online-first snapshot","status":"five research articles reconciled; one new item"},
        {"platform":"PNAS","query":"current social-science research","timeRange":"checked 2026-11-21","purpose":"General top-journal rotation","status":"no new unrecommended eligible article verified"}],
    "searchNote":"Formal-topic papers were screened in order: SSCI/SCI/SCIE JCR Q1/Q2, then Q3/Q4, then ESCI, then other peer-reviewed venues. X automatic translation is intentionally underfilled because no unrecommended direct formal study met the interaction-outcome threshold. Preprints are separate and explicitly not peer reviewed. English text is a faithful summary based on the publisher or repository abstract unless reuse permission is stated.",
    "shortfallReason":"The X automatic-translation formal section and PNAS section are underfilled under the strict relevance and deduplication rules.",
    "groups":groups,"coreTracking":[],"coreTrackingNote":"No new owner-submitted core-paper request was present.",
    "dissertation":{"title":"从被看见到被接收","timeRange":"Current and high-relevance peer-reviewed research",
        "selectionNote":"Two direct studies of overseas reception of Chinese cultural content and imagery are placed first.",
        "historyCoverage":"Checked the public index and recommended registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.",
        "selectedPapers":[p["doi"] for p in dissertation],"papers":dissertation,
        "topPapers":[{"doi":p["doi"],"reason":"Direct overseas reception evidence"} for p in dissertation]}}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [entry for entry in index if entry["date"] != date]
count = len(dissertation) + sum(len(group.get("papers", [])) for group in groups)
index.insert(0, {"date":date,"title":issue["title"],"summary":issue["summary"],"edition":"正式第48期","count":count,"file":f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
h = state["communication"]["hcr"]
h.update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,reason="Official Advance Access snapshot reconciled as five research articles with English summaries; one newly published item.")
h.setdefault("onlineSnapshots", []).append({"checkedAt":date,"url":"https://academic.oup.com/hcr/advance-articles","complete":True,"dois":[f"https://doi.org/{doi}" for _,doi,_,_ in hcr]})
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
print(root / f"{date}.json")
