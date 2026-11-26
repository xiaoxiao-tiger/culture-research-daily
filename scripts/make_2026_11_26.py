import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-26"


def paper(title, authors, venue, source, url, doi, topic, abstract, category, **extra):
    item = {
        "title": title, "titleZh": "Not displayed", "authors": authors, "year": 2026,
        "venue": venue, "source": source, "category": category,
        "evidence": "Publisher or authoritative index record verified",
        "takeaway": abstract, "theory": "See the linked article.", "data": "See the linked article.",
        "method": "See the linked article.", "results": abstract,
        "relevance": "Direct or explicitly labeled adjacent evidence under the strict topic hierarchy.",
        "limitations": "See the linked source for design-specific limitations.",
        "url": url, "doi": doi, "topicIds": [topic], "abstractMode": "summary",
        "originalAbstract": "", "abstractEn": abstract, "abstractSource": url,
        "abstractUnavailableReason": "Verbatim republication permission was not confirmed; this is an English summary based on the publisher abstract.",
        "readingPriority": "normal", "priorityReason": "Strict relevance and quality screening.",
        "readingUse": "Compact evidence briefing.", "researchConnection": "Relevant to the named research idea.",
        "publicationType": "journal", "peerReviewed": True, "publicationStatus": "published",
    }
    item.update(extra)
    return item


def formal(*args, tier, edition, quartile, reason="", **kwargs):
    return paper(*args, journalEdition=edition, jifQuartile=quartile,
                 indexSource="Web of Science Core Collection / 2025 Journal Citation Reports",
                 tierNote=f"{tier}. {reason}".strip(), **kwargs)


dissertation = [
    formal(
        "Interpretive incompleteness in global cultural flows: Ne Zha 2 and Labubu between visibility and decentralization",
        "Sizhou Pan", "International Journal of Cultural Studies, 29(6)", "SAGE",
        "https://doi.org/10.1177/13678779261455102", "https://doi.org/10.1177/13678779261455102", "culture",
        "A critical discourse analysis examines 349 media articles about the Chinese cultural icons Ne Zha 2 and Labubu. It identifies selective visibility followed by economic narratives that erase cultural subjecthood, political narratives that construct symbolic boundaries, and security narratives that recode popularity as social risk. The article argues that market visibility can coexist with limited interpretive power and proposes interpretive incompleteness as a structural feature of global cultural circulation. This is direct evidence about foreign media reception of Chinese cultural icons, but it analyzes media discourse rather than individual audience attitudes, identification, or sharing intentions.",
        "Dissertation · direct cultural-reception evidence", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1",
        publicationDate="2026-06-02", publicationDateSource="SAGE article record", publicationStatus="online-first"),
    formal(
        "Selecting and testing cultural symbols for character IP: evidence from Mount Tai, China",
        "Yu Wang and Changqiang Si", "Frontiers in Psychology, 17, 1946141", "Frontiers",
        "https://doi.org/10.3389/fpsyg.2026.1946141", "https://doi.org/10.3389/fpsyg.2026.1946141", "culture",
        "The study combines expert scoring and an entropy-weight TOPSIS model with a structural equation model of 331 valid university-student questionnaires collected around Mount Tai. Anthropomorphic reinvention and emotional-compensation potential received the largest symbol-selection weights, while stronger cultural identity was associated with willingness to interact through new media and with cultural-tourism consumption. The self-report, hypothetical-stimulus design supports associations rather than causal claims. It is adjacent evidence because it studies domestic young audiences rather than foreign reception, but it directly separates resonance, identity, interaction, recommendation, and consumption outcomes for a Chinese character IP.",
        "Dissertation · adjacent character-IP reception evidence", tier="Primary tier: SSCI JCR Q2", edition="SSCI", quartile="JCR Q2",
        publicationDate="2026-09-03", publicationDateSource="Frontiers article record", abstractLicense="CC BY; summary based on the open article"),
]

ishow = [
    formal(
        "Imported Nationalism: How Foreign Influencers and Local Followers Amplify the Chinese Dream in Weibo’s Attention Economy",
        "Saif Shahin and Jing Cai", "Journal of Contemporary China, OnlineFirst", "Taylor & Francis",
        "https://doi.org/10.1080/10670564.2026.2639981", "https://doi.org/10.1080/10670564.2026.2639981", "ishow-speed",
        "Using posts published by Western and non-Western influencers on Weibo during 2020–2021 and the comments of their Chinese followers, this study analyzes how foreign influencers articulate Chinese nationalist discourse and how local audiences amplify it through platform engagement. The analysis links comparative claims about China and the West to user-generated nationalism and to the incentives of the platform attention economy. It is adjacent rather than direct evidence for the IShowSpeed idea because it concerns domestic Chinese followers, not changes in foreign fans’ attitudes after a China visit.",
        "甲亢哥访华 · adjacent foreign-influencer mechanism", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1",
        publicationDate="2026-03-09", publicationDateSource="Publisher record", publicationStatus="online-first"),
]

ai = [
    formal(
        "The dark side of GenAI in the workplace: technostress, loneliness, and the buffering role of transformational leadership",
        "Fei Liu, Minxuan Qu, and Yixiao Zhang", "Frontiers in Psychology, 17, 1910745", "Frontiers",
        "https://doi.org/10.3389/fpsyg.2026.1910745", "https://doi.org/10.3389/fpsyg.2026.1910745", "ai-wellbeing",
        "A survey of 290 public-school teachers in Taiwan tests a stressor-strain-outcome and conservation-of-resources model. GenAI-induced technostress is associated with lower work effort indirectly through greater work loneliness, while its direct association with effort is not significant. Transformational leadership weakens the negative link between loneliness and effort but does not significantly moderate the technostress-to-loneliness path or the overall moderated mediation. The cross-sectional design cannot establish causality, but the study directly connects workplace GenAI use with socio-emotional strain.",
        "Workplace AI and well-being · direct evidence", tier="Primary tier: SSCI JCR Q2", edition="SSCI", quartile="JCR Q2",
        publicationDate="2026-11-05", publicationDateSource="Frontiers article record", abstractLicense="CC BY 4.0; publisher abstract summarized"),
    paper(
        "Technostress and trust in AI mediate the association between AI adoption and employee well-being",
        "K. D. V. Prasad, Ved Srinivas, Shivoham Singh, Hemant Kothari, Debanjan Nag, et al.", "Discover Psychology, OnlineFirst", "Springer Nature",
        "https://doi.org/10.1007/s44202-026-00928-9", "https://doi.org/10.1007/s44202-026-00928-9", "ai-wellbeing",
        "A cross-sectional survey of 499 IT employees in AI-enabled organizations in Hyderabad, India, uses exploratory and confirmatory factor analysis and covariance-based structural equation modeling. AI adoption is positively associated with psychological well-being and trust in AI while also increasing technostress. Technostress is negatively associated with well-being, trust is positively associated with well-being, and bootstrapped models indicate full mediation through both pathways. Because the study is observational and self-reported, the paths should not be read as causal effects.",
        "Workplace AI and well-being · direct evidence", journalEdition="ESCI", jifQuartile="No JCR quartile verified",
        indexSource="Web of Science Core Collection journal record", tierNote="Downgrade tier 3: ESCI. No second unrecommended SSCI/SCIE Q1–Q4 article was verified with comparable directness; this direct employee-well-being study was retained.",
        publicationDate="2026-10-11", publicationDateSource="Springer Nature article record", publicationStatus="online-first"),
]

# Reuse the already verified complete Social Media + Society issue without re-registering its articles.
old = json.loads((root / "2026-11-19.json").read_text())
sms_old = next(g for g in old["groups"] if g["id"] == "communication-issue")
sms_toc = []
for row in sms_old["collection"]["toc"]:
    item = dict(row)
    item["status"] = "previously-recommended"
    item["recommendedDate"] = item.get("recommendedDate") or "2026-11-19"
    item["reviewUrl"] = f"?date={item['recommendedDate']}"
    sms_toc.append(item)

general = formal(
    "Exploring enhanced self-esteem reactivity in response to social prediction errors in adolescence",
    "Klara Gregorova, Geert-Jan Will, Pia Burkard, Marcel Romanos, et al.", "Nature Communications", "Nature Portfolio",
    "https://doi.org/10.1038/s41467-026-79292-0", "https://doi.org/10.1038/s41467-026-79292-0", "methods",
    "This open-access study examines how social experiences shape self-esteem in 141 participants aged 10–40 using an experimental social-evaluation task and ecological momentary assessment. In the experiment, self-esteem responses to unexpected social feedback follow a nonlinear age pattern and peak in late adolescence. In daily life, younger participants show stronger self-esteem reactivity to pleasant social interactions and naturalistic social prediction errors. Experimental and daily-life reactivity are associated, supporting heightened self-esteem malleability during adolescence.",
    "综合顶刊 · social psychology", tier="Nature Communications rotation", edition="SCIE", quartile="JCR Q1",
    publicationDate="2026-11-25", publicationDateSource="Nature Communications article record", socialScienceAssessment="confirmed",
    socialScienceReason="Human social-evaluation experiment and ecological momentary assessment.", abstractLicense="CC BY 4.0; publisher abstract summarized")

groups = [
    {"id":"ishow-speed","label":"甲亢哥访华","target":2,"sortBy":"relevance-quality-date","papers":ishow,"description":"One unused high-tier adjacent foreign-influencer study passed the screen.","shortfallReason":"No second unrecommended study directly examining IShowSpeed or foreign fans’ attitude change after an influencer’s China visit was verified. Lower-relevance destination-image papers were not used to fill the slot."},
    {"id":"x-translation","label":"X自动翻译","target":2,"sortBy":"relevance-quality-date","papers":[],"description":"Strictly limited to platform-integrated translation and cross-language interaction.","shortfallReason":"No unrecommended peer-reviewed study directly testing X/Twitter built-in translation effects on replies, reposts, interaction depth, or relationship formation was verified. Machine-translation quality studies were excluded."},
    {"id":"ai-wellbeing","label":"使用AI提升还是降低幸福感","target":2,"sortBy":"relevance-quality-date","papers":ai,"description":"Direct workplace evidence on GenAI technostress, loneliness, trust, effort, and psychological well-being."},
    {"id":"preprints","label":"Preprints · arXiv / SSRN / NBER","target":4,"sortBy":"topic-publication-date-desc","papers":[],"description":"Strict-relevance, newest-first preprint screen.","shortfallReason":"No unrecommended strict-relevance arXiv, SSRN, or NBER item remained for the four topic slots after unified history deduplication. Previously recommended working papers were not repeated, and newer but generic papers were excluded."},
    {"id":"communication-issue","label":"传播学顶刊推荐","target":0,"sortBy":"issue","unit":"issue","collection":{"journalId":"sms","journalName":"Social Media + Society","kind":"issue","volume":"12","issue":"4","title":"Volume 12, Issue 4, October–December 2026","url":"https://journals.sagepub.com/toc/sms/current","checkedAt":date,"complete":True,"toc":sms_toc},"papers":[]},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"nature-communications","selectedJournalId":"nature-communications","papers":[general]},
]

issue = {
    "schemaVersion":7,"layoutVersion":"compact-ideas-v1","date":date,
    "title":"Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary":"Two dissertation papers, one foreign-influencer paper, an explicit X-translation shortfall, two workplace-AI papers, explicit preprint shortfalls, the complete Social Media + Society issue with English summaries, and one Nature Communications article.",
    "historyPolicy":"exclude-recommended","journalPolicy":"jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],
    "themeSearches":[
        {"topicId":"culture","platform":"Publisher sites and scholarly indexes","query":"Chinese mythology character reception cultural visibility interpretation character IP audience response","timeRange":"verified through 2026-11-26","status":"one SSCI Q1 direct media-reception study and one SSCI Q2 adjacent audience-response study"},
        {"topicId":"ishow-speed","platform":"Publisher sites, SSRN, arXiv, NBER","query":"IShowSpeed China visit foreign influencer China image foreign fans attitudes mediated contact","timeRange":"verified through 2026-11-26","status":"one SSCI Q1 adjacent study; second slot left empty"},
        {"topicId":"x-translation","platform":"Publisher sites, arXiv, SSRN, NBER","query":"X Twitter built-in automatic translation cross-language replies reposts relationships","timeRange":"verified through 2026-11-26","status":"formal and preprint shortfall; translation-quality-only results excluded"},
        {"topicId":"ai-wellbeing","platform":"Publisher sites, SSRN, arXiv, NBER","query":"workplace generative AI employee well-being technostress loneliness trust burnout","timeRange":"verified through 2026-11-26","status":"one SSCI Q2 direct paper and one disclosed ESCI downgrade"},
    ],
    "periodicalChecks":[
        {"platform":"SAGE","query":"Social Media + Society Volume 12 Issue 4","timeRange":"checked 2026-11-26","purpose":"Complete communication-journal issue","status":f"all {len(sms_toc)} research articles reconciled with English summaries and linked to prior recommendation dates"},
        {"platform":"Nature Portfolio","query":"Nature Communications latest social-science research","timeRange":"checked 2026-11-26","purpose":"General top-journal rotation","status":"one unrecommended open-access social-psychology article selected"},
    ],
    "searchNote":"Formal papers were screened in the required database and JCR order. Adjacent evidence and the ESCI downgrade are explicitly labeled. English text is a faithful summary based on publisher abstracts unless a reuse license is stated; no summary is presented as a verbatim abstract.",
    "shortfallReason":"IShowSpeed has one formal-paper vacancy; X has two; all four preprint topic slots are empty under strict relevance and permanent deduplication.",
    "groups":groups,"coreTracking":[],"coreTrackingNote":"No new owner-submitted core-paper request was present.",
    "dissertation":{"title":"从被看见到被接收","timeRange":"Current and high-relevance peer-reviewed research","selectionNote":"One direct study of foreign media interpretation of Chinese cultural icons and one adjacent domestic audience-response study of character IP.","historyCoverage":"Checked the public index and permanent recommendation registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.","selectedPapers":[p["doi"] for p in dissertation],"papers":dissertation,"topPapers":[{"doi":p["doi"],"reason":"Direct or clearly labeled adjacent reception evidence"} for p in dissertation]},
}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [row for row in index if row["date"] != date]
count = len(dissertation) + sum(len(g.get("papers", [])) for g in groups)
index.insert(0,{"date":date,"title":issue["title"],"summary":issue["summary"],"edition":"正式第53期","count":count,"file":f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
state["communication"]["sms"].update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,reason=f"Official current issue remains Volume 12 Issue 4; all {len(sms_toc)} research articles were reconciled with English summaries and linked to prior recommendation dates.")
state["general"]["nature-communications"].update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,lastRecommendedDoi=general["doi"],publicationDate="2026-11-25",socialScienceAssessment="confirmed",reason="Official Nature Communications listing yielded an unrecommended social-psychology study using experimental and ecological momentary assessment data.")
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

print(root / f"{date}.json")
