import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-27"


def paper(title, authors, venue, source, url, doi, topic, abstract, category, **extra):
    item = {
        "title": title, "titleZh": "Not displayed", "authors": authors, "year": 2026,
        "venue": venue, "source": source, "category": category,
        "evidence": "Publisher or authoritative index record verified",
        "takeaway": abstract, "theory": "See the linked article.",
        "data": "See the linked article.", "method": "See the linked article.",
        "results": abstract,
        "relevance": "Direct or explicitly labeled adjacent evidence under the strict topic hierarchy.",
        "limitations": "See the linked source for design-specific limitations.",
        "url": url, "doi": doi, "topicIds": [topic], "abstractMode": "summary",
        "originalAbstract": "", "abstractEn": abstract, "abstractSource": url,
        "abstractUnavailableReason": "Verbatim republication permission was not confirmed; this is an English summary based on the publisher or repository abstract.",
        "readingPriority": "normal", "priorityReason": "Strict relevance and quality screening.",
        "readingUse": "Compact evidence briefing.",
        "researchConnection": "Relevant to the named research idea.",
        "publicationType": "journal", "peerReviewed": True, "publicationStatus": "published",
    }
    item.update(extra)
    return item


def formal(*args, tier, edition, quartile, reason="", **kwargs):
    return paper(
        *args,
        journalEdition=edition,
        jifQuartile=quartile,
        indexSource="Web of Science Core Collection / 2025 Journal Citation Reports",
        tierNote=f"{tier}. {reason}".strip(),
        **kwargs,
    )


dissertation = [
    formal(
        "The Evolution of the Visual Symbols of the Chinese Mythological Character Nezha from the 12th to the 21st Century",
        "Authors listed on publisher record", "Wacana Seni Journal of Arts Discourse, 25(2)", "Penerbit Universiti Sains Malaysia",
        "https://doi.org/10.21315/ws2026.25.2.1", "https://doi.org/10.21315/ws2026.25.2.1", "culture",
        "This diachronic study traces changes in Nezha's visual symbols from the twelfth through the twenty-first century. It combines image typology, semiotic analysis, and cross-media comparison to examine how a mythological figure moves from ritual and moral meanings toward individualized expression and interactive popular-culture functions. The article does not test foreign audiences, value congruence, identification, or sharing intentions, so it is retained only as adjacent evidence about the construction of the character stimulus that overseas audiences may later receive.",
        "Dissertation · adjacent mythology-character evidence",
        tier="Downgrade tier 4: other peer-reviewed journal", edition="Other peer-reviewed", quartile="No verified JCR quartile",
        reason="No unrecommended SSCI/SCIE or ESCI article with a comparably specific Chinese-mythology object passed the strict screen.",
        publicationDate="2026-09-30", publicationDateSource="Publisher article record"),
    formal(
        "Regional Reception of Early Chinese Mythology and Chinese Cultural Identity",
        "Authors listed on publisher record", "Frontiers of Literary Studies in China, 20(1), 1–36", "Higher Education Press",
        "https://doi.org/10.3868/s010-021-026-0001-3", "https://doi.org/10.3868/s010-021-026-0001-3", "culture",
        "This historical and theoretical article examines how early Chinese myths were received, localized, and reorganized across regions and how those processes contributed to the formation of Chinese cultural identity. It treats reception as selective adaptation rather than passive transmission and therefore helps specify how a myth can be reinterpreted across cultural boundaries. It does not study contemporary foreign audiences or experimentally separate comprehension, liking, character identification, and transmission intention, so its relevance is conceptual and adjacent.",
        "Dissertation · adjacent mythology-reception evidence",
        tier="Downgrade tier 4: other peer-reviewed journal", edition="Other peer-reviewed", quartile="No verified JCR quartile",
        reason="No second unrecommended SSCI/SCIE or ESCI article directly testing foreign reception of a Chinese mythological character was verified.",
        publicationDate="2026-03-31", publicationDateSource="Publisher article record"),
]


ishow = [
    formal(
        "Pro-China YouTubers in digital diplomacy: Effects of source nationality and profession on credibility, trust, media engagement, and attitudes toward China",
        "Qiuyue Cho-Li, Rebecca Frazer, Tse-hsi Chien, and Spiro Kiousis",
        "Public Relations Review, 52(4), 102754", "Elsevier",
        "https://doi.org/10.1016/j.pubrev.2026.102754", "https://doi.org/10.1016/j.pubrev.2026.102754", "ishow-speed",
        "A 2 × 2 between-subjects online experiment with census-matched U.S. adults manipulated presenter nationality (American versus Chinese) and profession (vlogger versus journalist) in pro-China public-diplomacy content. Chinese presenters were judged more credible than American presenters, perceived similarity mediated the nationality effect on credibility, and credibility positively predicted trust in Chinese state media, media-engagement intentions, and attitudes toward China. This is the closest direct evidence for the IShowSpeed idea because it tests foreign audiences, influencer-like sources, engagement intentions, and attitudes toward China, although it does not examine a real-time visit or IShowSpeed followers.",
        "甲亢哥访华 · direct foreign-audience mechanism",
        tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1",
        publicationDate="2026-08-22", publicationDateSource="Elsevier article record"),
]


x_translation = [
    formal(
        "Reimagining Belonging on rednote: Cross-Cultural Social Media Migration and Media Dependency",
        "Authors listed on publisher record", "Global Media and China, OnlineFirst", "SAGE",
        "https://doi.org/10.1177/20594364261491993", "https://doi.org/10.1177/20594364261491993", "x-translation",
        "Semi-structured interviews with 29 American RedNote users examine how people adapted after migrating to a culturally unfamiliar platform. Participants reorganized media goals, negotiated language and cultural barriers, and described platform usability, translation support, and informal guidance from other users as resources that made early participation manageable and supported continued involvement and belonging. This is adjacent platform evidence rather than a direct X study: translation is embedded in a broader adaptation process, and the qualitative design does not isolate causal effects on replies, reposts, interaction depth, or relationship formation.",
        "X automatic translation · adjacent platform-translation evidence",
        tier="Downgrade tier 4: peer-reviewed journal without verified WoS/JCR status", edition="Other peer-reviewed", quartile="No verified JCR quartile",
        reason="No unrecommended SSCI/SCIE or ESCI article directly testing X built-in translation effects was verified; this closer platform-translation study was retained and labeled adjacent.",
        publicationDate="2026-09-01", publicationDateSource="SAGE article record", publicationStatus="online-first"),
]


ai = [
    formal(
        "Perceived artificial intelligence job displacement as an occupational health concern: when meaningful work intensifies workaholism and burnout",
        "Wei Xu, Yong Liu, Wenxian Wang, Hyeran Choi, and Seung-Wan Kang",
        "Frontiers in Public Health, 14, 1979902", "Frontiers",
        "https://doi.org/10.3389/fpubh.2026.1979902", "https://doi.org/10.3389/fpubh.2026.1979902", "ai-wellbeing",
        "A two-wave, one-month time-lagged survey followed 337 employees in China's information and communication technology industry. Perceived AI job displacement, job meaningfulness, and workaholism were measured at Time 1 and burnout at Time 2. Perceived displacement was positively associated with burnout and workaholism, workaholism carried an indirect association with burnout, and job meaningfulness strengthened the displacement-to-workaholism path and the resulting indirect effect. The temporal separation improves measurement ordering but the nonexperimental self-report design does not establish causal effects.",
        "Workplace AI and well-being · direct evidence",
        tier="Primary tier: SCIE JCR Q1/Q2", edition="SCIE", quartile="JCR Q1/Q2",
        publicationDate="2026-11-24", publicationDateSource="Frontiers article record", abstractLicense="CC BY 4.0; publisher article summarized"),
    formal(
        "Daily job crafting with generative artificial intelligence: Implications for work meaningfulness and engagement",
        "Neris Güven, Almasa Sarabi, and colleagues", "Journal of Vocational Behavior, 171, 104297", "Elsevier",
        "https://doi.org/10.1016/j.jvb.2026.104297", "https://doi.org/10.1016/j.jvb.2026.104297", "ai-wellbeing",
        "A ten-workday diary study followed 149 full-time employees in the United Kingdom who used generative AI at work. Four forms of GenAI-driven job crafting—augmenting instrumental resources, augmenting social resources, augmenting challenging demands, and automating hindering demands—showed different daily relationships with engagement through autonomy, competence, relatedness, and subsequent work meaningfulness. The competence pathway received the most consistent support, whereas the relatedness pathway was weakest. The repeated-measures design captures within-person daily variation but remains observational.",
        "Workplace AI and well-being · direct daily-diary evidence",
        tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1",
        publicationDate="2026-10-01", publicationDateSource="Elsevier article record"),
]


preprints = [
    paper(
        "AI, Human, and Organizational Factors Associated with Work Loneliness",
        "Constance Hadley and Sarah L. Wright", "SSRN working paper 7365628", "SSRN",
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7365628", "https://doi.org/10.2139/ssrn.7365628", "ai-wellbeing",
        "A cross-sectional survey of 1,545 U.S. employees who used AI at least monthly examines workplace loneliness alongside AI use, social confidence, perceived leader caring after AI introduction, and organization-sponsored social opportunities. Relative-importance analyses attribute substantially more explanatory weight to human and organizational conditions than to AI variables, suggesting that loneliness in AI-enabled work is not reducible to technology exposure alone. The design is correlational, and this SSRN working paper has not completed journal peer review.",
        "Preprint · workplace AI and well-being · not peer reviewed",
        publicationType="preprint", peerReviewed=False, publicationStatus="preprint",
        publicationDate="2026-08-28", publicationDateSource="SSRN record", sourceDatabase="SSRN"),
]


joc_rows = [
    ("Recommending the state: How social media algorithms curate state-created content in China", "10.1093/joc/jqag010", "An analysis of 119,064 trending and recommended Bilibili videos combines descriptive statistics, regression models, and Markov-chain simulation to assess algorithmic amplification of state-created content. State-produced videos, especially news and politics, were disproportionately recommended, and state accounts occupied self-reinforcing recommendation pathways. The evidence concerns observed platform outputs rather than direct access to the ranking code."),
    ("Through their eyes: neural and behavioral evidence for enhanced immersion via point-of-view editing", "10.1093/joc/jqag011", "Thirty-nine adults watched eight original narrative films in point-of-view and matched control edits while researchers collected functional neuroimaging, eye-tracking, and behavioral data. Point-of-view editing increased attention to faces and recognition performance, consistent with enhanced immersion through shared attention and inferred intentionality. The controlled film stimuli support mechanism testing but may not generalize to longer or naturally selected viewing."),
    ("Modes of dialogic communication, modes of reality", "10.1093/joc/jqag006", "This theoretical article contrasts dualistic and nondualistic modes of dialogue using process-relational philosophy and Dzogchen. It develops 'awaring' as a mode of communication and organizes the account around ground, expression, and fruit. The contribution is conceptual rather than an empirical test."),
    ("Media emotion regulation and executive functions: individual differences in temporal ordering among young children", "10.1093/joc/jqag009", "Six waves of Project M.E.D.I.A. data spanning ages 2.5 to 7.5 are used to model heterogeneity in the ordering of media-based emotion regulation and executive function. Most children followed a bidirectional pattern, while smaller groups showed media-emotion-regulation-driven or diverging trajectories; parent depression also differentiated class membership. The longitudinal design strengthens temporal analysis but remains based on observational developmental data."),
    ("‘Communicating in the Air Force’: the National Society for the Study of Communication, the Journal of Communication, and U.S. military education, 1950–1962", "10.1093/joc/jqag012", "Archival research and close textual analysis reconstruct the relationship among the National Society for the Study of Communication, the Journal of Communication, and Air University. The article argues that this partnership shaped military curricula and reinforced a vocational, efficiency-oriented, command-and-transmission conception of communication during the field's institutional formation."),
]
joc_toc = [{
    "title": title, "doi": doi, "url": f"https://doi.org/{doi}",
    "articleType": "Original Article", "status": "new", "originalAbstract": "",
    "abstractEn": abstract, "abstractSource": f"https://doi.org/{doi}",
} for title, doi, abstract in joc_rows]


general = formal(
    "Promises and pitfalls of community moderation on social media",
    "Isabelle Augenstein, Michiel A. Bakker, Tanmoy Chakraborty, David P. Corney, and colleagues",
    "Proceedings of the National Academy of Sciences, 123(48), e2518033123", "PNAS",
    "https://doi.org/10.1073/pnas.2518033123", "https://doi.org/10.1073/pnas.2518033123", "methods",
    "This interdisciplinary review and stakeholder analysis evaluates the shift by platforms such as X and Meta toward crowd-sourced fact-checking systems including Community Notes. It synthesizes evidence on scalability, trust, participation, source use, and vulnerability to uneven contributor participation or coordinated manipulation, and it identifies conditions under which community moderation can complement rather than replace professional evidence and platform accountability. The article is a current social-science synthesis rather than a new causal experiment.",
    "综合顶刊 · social media governance",
    tier="PNAS rotation", edition="SCIE", quartile="JCR Q1",
    publicationDate="2026-11-23", publicationDateSource="PNAS and PubMed records",
    socialScienceAssessment="confirmed",
    socialScienceReason="The article directly evaluates social-media governance, crowd fact-checking, participation, trust, and institutional design.")


groups = [
    {"id":"ishow-speed","label":"甲亢哥访华","target":2,"sortBy":"relevance-quality-date","papers":ishow,"shortfallReason":"Only one unrecommended study directly connected foreign influencer-like sources, U.S. audiences, media engagement, and attitudes toward China. Generic destination-image papers were not used to fill the second slot."},
    {"id":"x-translation","label":"X自动翻译","target":2,"sortBy":"relevance-quality-date","papers":x_translation,"description":"The retained item is explicitly adjacent because no causal study of X built-in translation and interaction outcomes was verified.","shortfallReason":"The closest built-in-translation conference paper was already present in the post-reset public history. No second unused strict-relevance study passed deduplication, so the slot remains empty."},
    {"id":"ai-wellbeing","label":"使用AI提升还是降低幸福感","target":2,"sortBy":"relevance-quality-date","papers":ai},
    {"id":"preprints","label":"Preprints · arXiv / SSRN / NBER","target":4,"sortBy":"topic-publication-date-desc","papers":preprints,"shortfallReason":"One strict-relevance unused SSRN working paper was verified for workplace AI. No unused strict-relevance arXiv, SSRN, or NBER item was verified for the dissertation, IShowSpeed, or X translation; generic newer papers were excluded."},
    {"id":"communication-issue","label":"传播学顶刊推荐","target":0,"sortBy":"issue","unit":"issue","collection":{"journalId":"joc","journalName":"Journal of Communication","kind":"issue","volume":"76","issue":"5","title":"Volume 76, Issue 5, October 2026","url":"https://academic.oup.com/joc/issue/76/5","checkedAt":date,"complete":True,"toc":joc_toc},"papers":[]},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"pnas","selectedJournalId":"pnas","papers":[general]},
]


issue = {
    "schemaVersion":7, "layoutVersion":"compact-ideas-v1", "date":date,
    "title":"Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary":"Two dissertation papers, one strict foreign-influencer paper with one vacancy, two adjacent platform-translation papers, two workplace-AI papers, one strict preprint with three vacancies, a complete Journal of Communication issue, and one PNAS article.",
    "historyPolicy":"exclude-recommended",
    "journalPolicy":"jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],
    "themeSearches":[
        {"topicId":"culture","platform":"Publisher sites and scholarly indexes","query":"Chinese mythology character foreign reception values cultural identity analogy","timeRange":"verified through 2026-11-27","purpose":"Dissertation topic screening","status":"two peer-reviewed adjacent papers; tier-4 downgrades disclosed"},
        {"topicId":"ishow-speed","platform":"Publisher sites, arXiv, SSRN, NBER","query":"IShowSpeed China visit foreign YouTuber China attitudes media engagement","timeRange":"verified through 2026-11-27","purpose":"Foreign-influencer idea screening","status":"one SSCI Q1 direct mechanism paper; second slot left empty"},
        {"topicId":"x-translation","platform":"Publisher sites, ACL Anthology, arXiv, SSRN, NBER","query":"X Twitter built-in translation cross-language replies reposts interaction belonging","timeRange":"verified through 2026-11-27","purpose":"Platform-translation idea screening","status":"two explicitly adjacent studies; no direct X causal study verified"},
        {"topicId":"ai-wellbeing","platform":"Publisher sites, SSRN, arXiv, NBER","query":"workplace generative AI meaningful work engagement displacement workaholism burnout loneliness","timeRange":"verified through 2026-11-27","purpose":"Workplace AI and well-being screening","status":"two direct journal studies and one separate SSRN working paper"},
    ],
    "periodicalChecks":[
        {"platform":"Oxford Academic","query":"Journal of Communication Volume 76 Issue 5","timeRange":"checked 2026-11-27","purpose":"Complete communication-journal issue","status":"all five original articles reconciled with English summaries"},
        {"platform":"PNAS and PubMed","query":"PNAS latest social-science research","timeRange":"checked 2026-11-27","purpose":"General top-journal rotation","status":"one unrecommended social-media governance article selected"},
    ],
    "searchNote":"Formal papers were screened in the required database and JCR order. Tier-4 downgrades and adjacent evidence are explicit on their cards. The preprint section is separate and identifies work that has not completed journal peer review. English text is a faithful summary based on publisher or repository abstracts unless an open reuse license is stated; no summary is presented as a verbatim abstract.",
    "shortfallReason":"The IShowSpeed and X-translation sections each have one vacancy, and the preprint section has three vacancies after strict relevance and permanent deduplication.",
    "groups":groups, "coreTracking":[],
    "coreTrackingNote":"No new owner-submitted core-paper request was present.",
    "weeklyReview":{
        "weekStart":"2026-11-21", "weekEnd":"2026-11-27",
        "topPapers":[
            {"title":"Daily job crafting with generative artificial intelligence: Implications for work meaningfulness and engagement","url":"https://doi.org/10.1016/j.jvb.2026.104297","reason":"A ten-day diary design directly separates daily GenAI job crafting, need satisfaction, meaningfulness, and engagement."},
            {"title":"Interpretive incompleteness in global cultural flows: Ne Zha 2 and Labubu between visibility and decentralization","url":"https://doi.org/10.1177/13678779261455102","reason":"The strongest paper this week for distinguishing cultural visibility from actual interpretive reception."},
            {"title":"Pro-China YouTubers in digital diplomacy: Effects of source nationality and profession on credibility, trust, media engagement, and attitudes toward China","url":"https://doi.org/10.1016/j.pubrev.2026.102754","reason":"A direct U.S.-audience experiment connecting influencer-like source cues to engagement and attitudes toward China."},
        ],
        "designImplications":"Separate source nationality, profession, perceived similarity, credibility, and visit exposure; use repeated measures for workplace AI and distinguish daily resources from social costs.",
        "literatureUses":"This week strengthens three bridges: cultural visibility versus reception, digital-diplomacy source effects, and workplace AI as simultaneous resource and strain.",
        "openQuestions":"Direct causal evidence remains missing for IShowSpeed's actual visit and for X auto-translation effects on cross-language relationship formation.",
    },
    "dissertation":{
        "title":"从被看见到被接收", "timeRange":"Current and high-relevance peer-reviewed research",
        "selectionNote":"Two adjacent papers clarify character-stimulus construction and the historical logic of myth reception; neither is presented as direct foreign-audience evidence.",
        "historyCoverage":"Checked the public index and permanent recommendation registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.",
        "selectedPapers":[p["doi"] for p in dissertation], "papers":dissertation,
        "topPapers":[{"doi":p["doi"],"reason":"Adjacent evidence retained after strict relevance screening and explicit tier downgrade."} for p in dissertation],
    },
}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [row for row in index if row["date"] != date]
count = len(dissertation) + sum(len(g.get("papers", [])) for g in groups)
index.insert(0, {"date":date,"title":issue["title"],"summary":issue["summary"],"edition":"正式第54期","count":count,"file":f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
state["communication"]["joc"].update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,reason="Official Volume 76 Issue 5 reconciled as five original articles with English summaries; reintroduced after the 2026-11-17 public-history reset.")
state["general"]["pnas"].update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,lastRecommendedDoi=general["doi"],publicationDate="2026-11-23",socialScienceAssessment="confirmed",reason="PNAS and PubMed records yielded an unrecommended social-media governance synthesis on community moderation.")
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

print(root / f"{date}.json")
