import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-28"


def paper(title, authors, venue, source, url, doi, topic, abstract, category, **extra):
    item = {
        "title": title, "titleZh": "Not displayed", "authors": authors, "year": 2026,
        "venue": venue, "source": source, "category": category,
        "evidence": "Publisher or authoritative scholarly-index record verified",
        "takeaway": abstract, "theory": "See the linked article.",
        "data": "See the linked article.", "method": "See the linked article.",
        "results": abstract,
        "relevance": "Direct or explicitly labeled adjacent evidence under the strict topic hierarchy.",
        "limitations": "See the linked source for design-specific limitations.",
        "url": url, "doi": doi, "topicIds": [topic], "abstractMode": "summary",
        "originalAbstract": "", "abstractEn": abstract, "abstractSource": url,
        "abstractUnavailableReason": "Verbatim republication permission was not confirmed; this is an English summary based on the publisher or repository abstract.",
        "readingPriority": "normal", "priorityReason": "Strict relevance and quality screening.",
        "readingUse": "Compact evidence briefing.", "researchConnection": "Relevant to the named research idea.",
        "publicationType": "journal", "peerReviewed": True, "publicationStatus": "published",
    }
    item.update(extra)
    return item


def formal(*args, tier, edition, quartile, reason="", **kwargs):
    return paper(*args, journalEdition=edition, jifQuartile=quartile,
                 indexSource="Web of Science Core Collection / 2025 Journal Citation Reports or disclosed alternative record",
                 tierNote=f"{tier}. {reason}".strip(), **kwargs)


dissertation = [
    formal(
        "Western Audience Reception of Chinese Cultural IP in Ne Zha 2: An LDA and Critical Metaphor Analysis of Film Reviews",
        "Hongying Zhou and Runkun Guo", "Innovation in Applied Linguistics", "Mason Publish",
        "https://doi.org/10.37420/j.ial.2026.003", "https://doi.org/10.37420/j.ial.2026.003", "culture",
        "The study analyzes 658 English-language reviews of Ne Zha 2 from IMDb and Rotten Tomatoes using latent Dirichlet allocation and critical metaphor analysis. It identifies recurring themes in Western viewers’ evaluations and shows that reviews often translate the film’s culturally embedded conflicts into familiar individual-rebellion frames while assessing visual and narrative qualities through established Western cinematic benchmarks. The article provides unusually direct evidence about foreign reception of a Chinese mythological character, but platform reviewers are self-selected and the observational text analysis cannot separate comprehension, liking, character identification, and sharing intention as distinct outcomes.",
        "Dissertation · direct foreign-audience reception evidence",
        tier="Downgrade tier 4: other peer-reviewed journal", edition="Other peer-reviewed", quartile="No verified JCR quartile",
        reason="No unused SSCI/SCIE Q1–Q4 or ESCI paper with equally direct foreign-audience evidence about a Chinese mythological character was verified.",
        publicationDate="2026-04-30", publicationDateSource="Publisher article record"),
    formal(
        "Narrative Strategies and Audience Reception in the Reimagining of Chinese Mythology",
        "Xing Enhe and Myung Jin Park", "Journal of Chinese Language and Literature, 102, 241–270", "Korea Citation Index",
        "https://doi.org/10.15792/clsyn..102.202608.241", "https://doi.org/10.15792/clsyn..102.202608.241", "culture",
        "This comparative study examines Creation of the Gods II and Ne Zha II through narrative structure, visual signs, and audience responses. It finds that Creation of the Gods II uses a multi-linear epic structure centered on collective heroes, political order, historical legitimacy, and cultural continuity, whereas Ne Zha II builds a single-line growth narrative around personal experience, self-redemption, resistance to fate, and modern subjectivity. The reception component helps connect formal narrative choices with audience evaluation, but the study does not isolate foreign audiences or experimentally distinguish value congruence, moral evaluation, cultural proximity, identification, and transmission intention.",
        "Dissertation · adjacent mythology-reception evidence",
        tier="Downgrade tier 4: other peer-reviewed journal", edition="KCI peer-reviewed", quartile="No verified JCR quartile",
        reason="The second slot could not be filled by an unused SSCI/SCIE or ESCI article meeting the strict Chinese-mythology reception criterion.",
        publicationDate="2026-08-30", publicationDateSource="KCI record"),
]


ishow = [formal(
    "Unveiling digital narratives of transnational migration to China: foreign wanghong on Douyin and Xiaohongshu",
    "Xintian Li, Yihui Zheng, and Guodong Du", "Chinese Journal of Communication, 19(2)", "Taylor & Francis",
    "https://doi.org/10.1080/17544750.2026.2614056", "https://doi.org/10.1080/17544750.2026.2614056", "ishow-speed",
    "This mixed-methods study combines critical discourse analysis and framing theory to examine how Chinese users perceive foreign wanghong active on Douyin and Xiaohongshu. It analyzes 1,074 Douyin comments and 1,493 Xiaohongshu comments and identifies frames of nationalist backlash and othering, language and cultural humor, exoticism and admiration, integration and assimilation, and national pride and normalization. The article is adjacent rather than direct evidence for the IShowSpeed idea because it studies Chinese audiences’ responses to foreign creators, not foreign followers’ attitudes toward China after observing an influencer visit.",
    "甲亢哥访华 · adjacent foreign-influencer mechanism", tier="Primary tier: SSCI JCR Q2", edition="SSCI", quartile="JCR Q2",
    publicationDate="2026-01-20", publicationDateSource="Taylor & Francis article record")]


ai = [
    formal(
        "The Impact of Artificial Intelligence Usage on Affective Work Well-Being: A Self-Determination Theory Perspective",
        "Chi Zhang, Shuping Chen, Dianru Zhang, and Qichao Zhang", "Behavioral Sciences, 16(5), 670", "MDPI",
        "https://doi.org/10.3390/bs16050670", "https://doi.org/10.3390/bs16050670", "ai-wellbeing",
        "A three-wave time-lagged survey of 360 employees tests how workplace AI use relates to affective work well-being. AI use positively predicts affective well-being through two parallel mediators, work meaningfulness and work engagement, and higher-quality human–AI collaboration strengthens both indirect paths. The temporal separation improves measurement ordering, but the self-report observational design does not establish that AI use causes the reported gains.",
        "Workplace AI and well-being · direct evidence", tier="Downgrade tier 4: peer-reviewed journal without a verified JCR record in this run", edition="Peer-reviewed journal", quartile="JCR status not asserted",
        reason="A current Web of Science edition and JCR quartile could not be independently verified from an authoritative record during this run, so no Q1/Q2 claim is made.",
        publicationDate="2026-04-28", publicationDateSource="Publisher article record", abstractLicense="CC BY 4.0; publisher abstract summarized"),
    formal(
        "Generative artificial intelligence (GenAI) use, work outcomes, and the moderating role of GenAI literacy in early organizational adoption",
        "Authors listed on publisher record", "Computers in Human Behavior: Artificial Humans, 6, 100380", "Elsevier",
        "https://doi.org/10.1016/j.chbah.2026.100380", "https://doi.org/10.1016/j.chbah.2026.100380", "ai-wellbeing",
        "A cross-sectional online survey of 1,001 administrative employees at a global industrial company was conducted shortly before an organization-wide GenAI rollout in early 2025. Structural equation models show small positive associations between GenAI-use frequency and work engagement and quantitative job performance. GenAI literacy moderates associations with qualitative performance, quantitative performance, and meaningfulness of work, indicating that access alone is not uniformly beneficial. The design captures an important pre-transformation stage but remains correlational and does not measure broad life satisfaction.",
        "Workplace AI and well-being · direct engagement and meaningful-work evidence", tier="Downgrade tier 4: other peer-reviewed journal", edition="Other peer-reviewed", quartile="No verified JCR quartile",
        reason="The journal did not have a verified SSCI/SCIE or ESCI/JCR record in the authoritative sources checked; it was retained because the study is directly relevant and uses a large organizational sample.",
        publicationDate="2026-08-01", publicationDateSource="Elsevier article record"),
]


preprints = [paper(
    "How Does AI Exacerbate Job Burnout Among Media Professionals? A Multi-Logic Analysis Integrating JD-R and COR",
    "Authors listed on repository record", "SSRN working paper 7411384", "SSRN",
    "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7411384", "https://doi.org/10.2139/ssrn.7411384", "ai-wellbeing",
    "This working paper examines how AI-related work conditions contribute to burnout among media professionals by integrating the Job Demands–Resources model with Conservation of Resources theory. It models AI as a source of changing demands and resource pressures rather than assuming a uniformly positive productivity effect, and it focuses directly on occupational burnout in an AI-intensive profession. The repository record was first posted on 4 September 2026. The paper has not completed journal peer review, so its findings should be treated as provisional.",
    "Preprint · workplace AI and well-being · not peer reviewed",
    publicationType="preprint", peerReviewed=False, publicationStatus="preprint",
    publicationDate="2026-09-04", publicationDateSource="SSRN record", sourceDatabase="SSRN")]


old = json.loads((root / "2026-11-21.json").read_text())
hcr = old["groups"][4]["collection"]
hcr["title"] = "Advance Articles snapshot checked 28 November 2026"
hcr["checkedAt"] = date
for row in hcr["toc"]:
    row["status"] = "previously-recommended"
    row["recommendedDate"] = "2026-11-21"
    row["reviewUrl"] = "?date=2026-11-21"


groups = [
    {"id":"ishow-speed","label":"甲亢哥访华","target":2,"sortBy":"relevance-quality-date","papers":ishow,"shortfallReason":"Only one unused paper met the strict relevance threshold. It is explicitly adjacent because the audience direction is reversed; generic tourism and destination-image studies were excluded."},
    {"id":"x-translation","label":"X自动翻译","target":2,"sortBy":"relevance-quality-date","papers":[],"shortfallReason":"No unused formal paper directly testing X/Twitter built-in translation, cross-language replies, reposts, interaction depth, or relationship formation passed permanent deduplication. Machine-translation quality studies were excluded."},
    {"id":"ai-wellbeing","label":"使用AI提升还是降低幸福感","target":2,"sortBy":"relevance-quality-date","papers":ai},
    {"id":"preprints","label":"Preprints · arXiv / SSRN / NBER","target":4,"sortBy":"topic-publication-date-desc","papers":preprints,"shortfallReason":"One unused strict-relevance SSRN working paper was verified for workplace AI and burnout. No unused strict-relevance arXiv, SSRN, or NBER item was found for the dissertation, IShowSpeed, or X translation; newer generic items were excluded."},
    {"id":"communication-issue","label":"传播学顶刊推荐","target":0,"sortBy":"issue","unit":"issue","collection":hcr,"papers":[]},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"nature","selectedJournalId":"nature","papers":[],"shortfallReason":"The latest socially relevant Nature candidates identified in the current rotation were already present in the post-reset permanent history. No unused article passed both the relevance and deduplication checks."},
]


issue = {
    "schemaVersion":7, "layoutVersion":"compact-ideas-v1", "date":date,
    "title":"Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary":"Two dissertation papers, one adjacent foreign-influencer paper, no reusable X-translation paper, two workplace-AI papers, one SSRN working paper, a complete Human Communication Research Advance Articles check, and an explicit Nature vacancy.",
    "historyPolicy":"exclude-recommended", "journalPolicy":"jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],
    "themeSearches":[
        {"topicId":"culture","platform":"Publisher sites and scholarly indexes","query":"Chinese mythology character foreign reception Ne Zha values identification","timeRange":"verified through 2026-11-28","purpose":"Dissertation screening","status":"two peer-reviewed papers; tier-4 downgrades disclosed"},
        {"topicId":"ishow-speed","platform":"Publisher sites and scholarly indexes","query":"IShowSpeed China foreign influencer wanghong visit attitudes China","timeRange":"verified through 2026-11-28","purpose":"Foreign-influencer idea screening","status":"one SSCI Q2 adjacent paper; second slot vacant"},
        {"topicId":"x-translation","platform":"Publisher sites, arXiv, SSRN, NBER","query":"X Twitter built-in translation cross-language replies reposts interaction relationship","timeRange":"verified through 2026-11-28","purpose":"Platform-translation screening","status":"no unused strict-relevance paper; both slots vacant"},
        {"topicId":"ai-wellbeing","platform":"Publisher sites, SSRN, arXiv, NBER","query":"workplace generative AI well-being engagement meaningful work technostress burnout","timeRange":"verified through 2026-11-28","purpose":"Workplace AI and well-being screening","status":"two direct journal studies and one separate SSRN working paper"},
    ],
    "periodicalChecks":[
        {"platform":"Oxford Academic","query":"Human Communication Research Advance Articles","timeRange":"checked 2026-11-28","purpose":"Complete communication-top-journal snapshot","status":"all five research articles reconciled with English summaries and linked to the prior recommendation date"},
        {"platform":"Nature","query":"Nature latest social-science research","timeRange":"checked 2026-11-28","purpose":"General top-journal rotation","status":"no unused candidate; vacancy disclosed"},
    ],
    "searchNote":"Formal papers were screened in the required database and JCR order. Any downgrade and every adjacent match is explicit on its card. The preprint section is separate and marks work that has not completed journal peer review. English text is a detailed summary based on publisher or repository abstracts unless an open reuse license is stated; it is not presented as a verbatim abstract.",
    "shortfallReason":"The IShowSpeed section has one vacancy, X translation has two, the preprint section has three, and the Nature rotation has one after strict relevance and permanent deduplication.",
    "groups":groups, "coreTracking":[], "coreTrackingNote":"No new owner-submitted core-paper request was present.",
    "dissertation":{
        "title":"从被看见到被接收", "timeRange":"Current and high-relevance peer-reviewed research",
        "selectionNote":"One paper directly analyzes Western Ne Zha 2 reviews; the second is adjacent comparative reception evidence. Both required tier-4 downgrades are disclosed.",
        "historyCoverage":"Checked the public index and permanent recommendation registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.",
        "selectedPapers":[p["doi"] for p in dissertation], "papers":dissertation,
        "topPapers":[{"doi":p["doi"],"reason":"Retained after strict relevance screening; quality tier and evidence distance are explicit."} for p in dissertation],
    },
}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [row for row in index if row["date"] != date]
count = len(dissertation) + sum(len(g.get("papers", [])) for g in groups)
index.insert(0, {"date":date,"title":issue["title"],"summary":issue["summary"],"edition":"正式第55期","count":count,"file":f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
state["communication"]["hcr"].update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,reason="Official Advance Articles snapshot reconciled as five research articles; all were previously recommended on 2026-11-21 and are linked rather than duplicated.")
state["general"]["nature"].update(lastAttemptAt=date,lastCheckedAt=date,status="no-new",reason="Latest socially relevant Nature candidates found in the rotation were already in the post-reset permanent history; no unused article passed strict screening.")
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

print(root / f"{date}.json")
