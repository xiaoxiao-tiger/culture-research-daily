import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-25"


def paper(title, authors, year, venue, source, url, doi, topic, abstract, category, **extra):
    item = {
        "title": title, "titleZh": "Not displayed", "authors": authors, "year": year,
        "venue": venue, "source": source, "category": category,
        "evidence": "Publisher or authoritative repository record verified",
        "takeaway": abstract, "theory": "See the linked article.", "data": "See the linked article.",
        "method": "See the linked article.", "results": abstract,
        "relevance": "Direct or explicitly labeled adjacent evidence under the strict topic hierarchy.",
        "limitations": "See the linked source for design-specific limitations.",
        "url": url, "doi": doi, "topicIds": [topic], "abstractMode": "summary",
        "originalAbstract": "",
        "abstractUnavailableReason": "Verbatim republication permission was not confirmed; this is an English summary based on the publisher or repository abstract.",
        "abstractEn": abstract, "abstractSource": url, "readingPriority": "normal",
        "priorityReason": "Direct or explicitly labeled adjacent evidence.",
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
        "Genre-convention congruence and narrative immersion: The mediating roles of emotional engagement and character identification in viewers' sharing intentions",
        "Bowen Zhao", 2026, "Frontiers in Psychology, 17, 2036525", "Frontiers",
        "https://doi.org/10.3389/fpsyg.2026.2036525", "https://doi.org/10.3389/fpsyg.2026.2036525", "culture",
        "This two-study article examines perceived genre-convention congruence, narrative immersion, emotional engagement, character identification, and sharing intentions around the Korean drama Queen of Tears. A survey of 377 Chinese adults who had watched all 16 episodes found positive associations linking perceived congruence to immersion, immersion to emotional engagement and identification, and those responses to sharing intentions. In a clip experiment with 88 retained participants, only immersion remained significant after Holm correction; the clips also differed in plot and character circumstances. The evidence is therefore adjacent, reverse-direction cross-cultural reception evidence rather than a study of foreign reception of Chinese mythology.",
        "Dissertation · adjacent cross-cultural reception mechanism", tier="Primary tier: SSCI JCR Q2", edition="SSCI", quartile="JCR Q2",
        publicationDate="2026-11-23", publicationDateSource="Publisher record", abstractLicense="CC BY 4.0; publisher abstract used as the factual basis for this summary"),
    paper(
        "The dimensionality and cross-cultural invariance of narrative transportability: evidence from 50 countries and 21 languages",
        "Markus Appel et al.", 2026, "Global Perspectives in Communication, 1(1), wpaf002", "Oxford Academic",
        "https://doi.org/10.1093/gpcomm/wpaf002", "https://doi.org/10.1093/gpcomm/wpaf002", "culture",
        "Using 8,814 participants from 50 countries and 21 languages, this study evaluates the dimensionality and cross-cultural measurement invariance of narrative transportability. Exploratory analysis on 2,644 participants identifies cognitive involvement, cognitive-emotional imagination, sensory imagination, and personal involvement as four dimensions, followed by confirmatory and cross-cultural tests in the remaining sample. The article supplies measurement evidence for comparing narrative receptivity across cultures, but it does not test Chinese mythology, value congruence, or character-level reception directly.",
        "Dissertation · adjacent cross-cultural measurement evidence", journalEdition="Other peer-reviewed journal", jifQuartile="No established JCR quartile verified",
        indexSource="Oxford Academic journal record", tierNote="Downgrade tier 4. No second unrecommended SSCI/SCIE paper met the dissertation topic more directly; this large cross-cultural measurement study was retained as adjacent evidence.",
        publicationDate="2026-03-10", publicationDateSource="Publisher record"),
]


ishow = [
    formal(
        "The role of social media influencers in nation branding and relationship building with foreign audiences",
        "Hyun Ju Park and Joon Soo Lim", 2025, "Public Relations Review, 51(2), 102570", "Elsevier",
        "https://doi.org/10.1016/j.pubrev.2025.102570", "https://doi.org/10.1016/j.pubrev.2025.102570", "ishow-speed",
        "This study examines how social media influencers negotiate identity and communication strategy when addressing foreign audiences for nation-branding and public-diplomacy purposes. Its findings emphasize that cultural-exchange content is more effective than one-sided host-country promotion, that shared and different cultural backgrounds shape reception, and that disrespect toward an audience's culture produces negative reactions. The article does not study IShowSpeed, but it directly addresses the broader mechanism linking influencer communication to relationship building with foreign publics.",
        "甲亢哥访华 · adjacent nation-branding mechanism", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1",
        publicationDate="2025-06-01", publicationDateSource="Publisher record"),
    formal(
        "Short-form travel vlogs: The influence of parasocial interaction on viewers’ destination–self congruence and behavioural intention",
        "Made Handijaya Dewantara, Xin Jin, and Sarah Gardiner", 2026, "Journal of Vacation Marketing, OnlineFirst", "SAGE",
        "https://doi.org/10.1177/13567667261487698", "https://doi.org/10.1177/13567667261487698", "ishow-speed",
        "Australian Millennials (N = 459) watched a short-form travel vlog and completed an online survey. Vlogger attractiveness, attitude homophily, and perceived technology skill predicted parasocial interaction, which in turn predicted viewer-destination self-congruence, travel intention, and willingness to generate electronic word of mouth. Vlogger credibility had a negative but nonsignificant association with parasocial interaction. This is adjacent travel-vlog mechanism evidence rather than an IShowSpeed or China-image study.",
        "甲亢哥访华 · adjacent travel-vlog mechanism", tier="Primary tier: SSCI JCR Q2", edition="SSCI", quartile="JCR Q2",
        publicationDate="2026-09-17", publicationDateSource="Publisher record", publicationStatus="online-first"),
]


ai = [
    formal(
        "From breach to fulfilment: navigating digital natives’ AI-induced psychological contracts for workplace outcomes",
        "Sandeep Kaur et al.", 2026, "Behaviour & Information Technology, OnlineFirst", "Taylor & Francis",
        "https://doi.org/10.1080/0144929X.2026.2686168", "https://doi.org/10.1080/0144929X.2026.2686168", "ai-wellbeing",
        "A survey of 415 digital-native employees in Indian high-technology industries examines psychological contracts formed with generative AI. Experiences of bias, privacy breach, and opacity are treated as contract breach and are associated with worse innovative-work and well-being outcomes. Perceived contract fulfilment buffers the negative association only when breach is relatively low. The cross-sectional self-report design cannot establish causal effects, but it directly links workplace GenAI experiences to employee well-being.",
        "Workplace AI and well-being · direct evidence", tier="Primary tier: SSCI JCR Q1", edition="SSCI", quartile="JCR Q1",
        publicationDate="2026-06-15", publicationDateSource="Publisher record", publicationStatus="online-first"),
    formal(
        "Relying on AI at work reduces self-efficacy, ownership, and meaning while active collaboration mitigates the effects",
        "Natasha Jia Song et al.", 2026, "Scientific Reports, 16", "Springer Nature",
        "https://doi.org/10.1038/s41598-026-42312-6", "https://doi.org/10.1038/s41598-026-42312-6", "ai-wellbeing",
        "Across workplace-task experiments, passive reliance on AI lowered self-efficacy, psychological ownership, and perceived meaning in work. Passive use could initially raise enjoyment and satisfaction, but these benefits reversed after participants returned to manual work. More active human-AI collaboration mitigated the losses, indicating that the design of AI involvement, rather than AI access alone, shapes worker experience. The experiments focus on proximal psychological outcomes rather than long-term organizational well-being.",
        "Workplace AI and well-being · direct experimental evidence", tier="Primary tier: SCIE JCR Q1", edition="SCIE", quartile="JCR Q1",
        publicationDate="2026-03-15", publicationDateSource="Publisher record"),
]


preprint = paper(
    "Working with Generative AI vs Humans: The Impact on Well-being",
    "Eirini Spiliotopoulou, Tim Kraft, Shawn Mankad, and Yanchong Zheng", 2026, "SSRN Working Paper 6197938", "SSRN",
    "https://ssrn.com/abstract=6197938", "https://doi.org/10.2139/ssrn.6197938", "ai-wellbeing",
    "An incentivized laboratory experiment assigns participants to complete two operational tasks with either a GenAI assistant or a human collaborator. Validated psychological scales and text analyses indicate lower mental well-being in human-GenAI collaboration than in human-human collaboration. Human pairs reduced negative emotions, whereas human-GenAI pairs did not; human-GenAI collaboration reduced positive emotions, whereas human-human collaboration did not. Transcript analyses associate human interaction with more expressive and uncertainty language and AI interaction with more technical, task-oriented communication. This working paper has not completed journal peer review.",
    "Preprint · workplace AI and well-being", publicationType="preprint", peerReviewed=False, publicationStatus="working-paper",
    publicationDate="2026-02-18", publicationDateSource="SSRN first-posted date", ssrnId="6197938",
)

# Reuse the already verified complete NMS issue, but do not re-register its articles.
old = json.loads((root / "2026-11-18.json").read_text())
nms_old = next(g for g in old["groups"] if g["id"] == "communication-issue")
nms_toc = []
for row in nms_old["collection"]["toc"]:
    item = dict(row)
    item["status"] = "previously-recommended"
    item["recommendedDate"] = "2026-11-18"
    item["reviewUrl"] = "?date=2026-11-18"
    nms_toc.append(item)

general = formal(
    "A twelve-language dataset for the study of event descriptions in expository and narrative texts",
    "David Peeters, Keigo Kamakura, Alfons Maes, et al.", 2026, "Scientific Data", "Nature Portfolio",
    "https://doi.org/10.1038/s41597-026-08909-2", "https://doi.org/10.1038/s41597-026-08909-2", "methods",
    "This Data Descriptor reports a standardized online text-elicitation study with 1,200 participants, 100 in each of 12 language groups. Every participant described two events in both expository and narrative genres, producing 2,400 short texts. The dataset supports comparisons of how writers, languages, and genres shape descriptions of the same events and includes participant demographics and reusable experimental materials. It is relevant to social-science and cross-cultural communication research as an openly available multilingual data resource.",
    "综合顶刊 · social-science data descriptor", tier="Scientific Data rotation", edition="SCIE", quartile="JCR Q1",
    publicationDate="2026-11-23", publicationDateSource="Publisher record", socialScienceAssessment="confirmed",
    socialScienceReason="Human-participant multilingual narrative data directly support cross-cultural language and communication research.",
    abstractLicense="CC BY 4.0; publisher abstract used as the factual basis for this summary")

groups = [
    {"id":"ishow-speed","label":"甲亢哥访华","target":2,"sortBy":"relevance-quality-date","papers":ishow,"description":"Two high-tier adjacent mechanisms; no new unrecommended direct IShowSpeed study passed the screen."},
    {"id":"x-translation","label":"X自动翻译","target":2,"sortBy":"relevance-quality-date","papers":[],"description":"Strictly limited to platform-integrated translation and cross-language interaction.","shortfallReason":"No unrecommended peer-reviewed study directly testing X/Twitter built-in translation effects on replies, reposts, interaction depth, or relationship formation was verified. Translation-quality-only studies were excluded."},
    {"id":"ai-wellbeing","label":"使用AI提升还是降低幸福感","target":2,"sortBy":"relevance-quality-date","papers":ai,"description":"Workplace GenAI, employee well-being, meaning, ownership, and psychological contracts."},
    {"id":"preprints","label":"Preprints · arXiv / SSRN / NBER","target":4,"sortBy":"topic-publication-date-desc","papers":[preprint],"description":"One strict-relevance working paper; three topic slots remain empty.","shortfallReason":"No new unrecommended strict-relevance arXiv, SSRN, or NBER item was verified for the dissertation, IShowSpeed, or X-translation topics. The workplace-AI slot is filled by the newest eligible unused paper found in the screened results."},
    {"id":"communication-issue","label":"传播学顶刊推荐","target":0,"sortBy":"issue","unit":"issue","collection":{"journalId":"nms","journalName":"New Media & Society","kind":"issue","volume":"28","issue":"11","title":"Volume 28, Issue 11, November 2026","url":"https://journals.sagepub.com/toc/nms/current","checkedAt":date,"complete":True,"toc":nms_toc},"papers":[]},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"scientific-data","selectedJournalId":"scientific-data","papers":[general]},
]

issue = {
    "schemaVersion":7,"layoutVersion":"compact-ideas-v1","date":date,
    "title":"Research ideas: reception, influencer visits, platform translation, and workplace AI",
    "summary":"Two dissertation papers, two influencer-mechanism papers, an explicit X-translation shortfall, two workplace-AI papers, one workplace-AI preprint, the complete 33-article New Media & Society issue with summaries, and one Scientific Data descriptor.",
    "historyPolicy":"exclude-recommended","journalPolicy":"jcr-q1-q2-then-q3-q4-then-esci-then-other-peer-reviewed",
    "searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],
    "themeSearches":[
        {"topicId":"culture","platform":"Publisher sites and scholarly indexes","query":"cross-cultural narrative reception character identification transportability value congruence mythology","timeRange":"verified through 2026-11-25","status":"one SSCI Q2 adjacent study and one peer-reviewed cross-cultural measurement downgrade"},
        {"topicId":"ishow-speed","platform":"Publisher sites, SSRN, arXiv, NBER","query":"IShowSpeed China visit foreign influencer nation branding travel vlog parasocial destination image","timeRange":"verified through 2026-11-25","status":"two SSCI Q1/Q2 adjacent mechanism papers; no new direct unused paper"},
        {"topicId":"x-translation","platform":"Publisher sites, arXiv, SSRN, NBER","query":"X Twitter built-in automatic translation replies reposts interaction relationships","timeRange":"verified through 2026-11-25","status":"formal and preprint shortfall; translation-quality-only results excluded"},
        {"topicId":"ai-wellbeing","platform":"Publisher sites, SSRN, arXiv, NBER","query":"workplace generative AI employee well-being meaning ownership psychological contract","timeRange":"verified through 2026-11-25","status":"two direct JCR Q1 formal papers and one separate SSRN working paper"},
    ],
    "periodicalChecks":[
        {"platform":"SAGE","query":"New Media & Society Volume 28 Issue 11","timeRange":"checked 2026-11-25","purpose":"Complete communication-journal issue","status":"all 33 research articles reconciled against the previously completed issue and displayed with English summaries; no duplicate registration"},
        {"platform":"Nature Portfolio","query":"Scientific Data latest social-science Data Descriptors","timeRange":"checked 2026-11-25","purpose":"General top-journal rotation","status":"one unrecommended multilingual human-participant dataset selected"},
    ],
    "searchNote":"Formal-topic papers were screened in the required order. Adjacent evidence is labeled explicitly. The second dissertation item uses the disclosed final-tier downgrade because no more direct unused SSCI/SCIE candidate was verified. English text is a faithful summary based on publisher or repository abstracts unless a reuse license is stated; it is not presented as a verbatim abstract.",
    "shortfallReason":"X has no formal paper; three of four preprint topic slots remain empty under strict relevance and no-repeat rules.",
    "groups":groups,"coreTracking":[],"coreTrackingNote":"No new owner-submitted core-paper request was present.",
    "dissertation":{"title":"从被看见到被接收","timeRange":"Current and high-relevance peer-reviewed research","selectionNote":"Two adjacent studies on cross-cultural narrative reception and cross-cultural measurement; neither is presented as direct evidence about foreign reception of Chinese mythology.","historyCoverage":"Checked the public index and permanent recommendation registry after the 2026-11-17 reset; inaccessible private notes are outside this coverage.","selectedPapers":[p["doi"] for p in dissertation],"papers":dissertation,"topPapers":[{"doi":p["doi"],"reason":"Adjacent evidence for reception or cross-cultural measurement"} for p in dissertation]},
}

(root / f"{date}.json").write_text(json.dumps(issue, ensure_ascii=False, indent=2) + "\n")
index = json.loads((root / "index.json").read_text())
index = [row for row in index if row["date"] != date]
count = len(dissertation) + sum(len(g.get("papers", [])) for g in groups)
index.insert(0,{"date":date,"title":issue["title"],"summary":issue["summary"],"edition":"正式第52期","count":count,"file":f"{date}.json"})
(root / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state = json.loads((root / "rotation-state.json").read_text())
state["updatedAt"] = date
nms = state["communication"]["nms"]
nms.update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,reason="Official current issue remains Volume 28 Issue 11; all 33 research articles were reconciled with English summaries and were already recommended on 2026-11-18.")
sd = state["general"]["scientific-data"]
sd.update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,lastRecommendedDoi=general["doi"],publicationDate="2026-11-23",socialScienceAssessment="confirmed",reason="Official Scientific Data listing yielded an unrecommended multilingual human-participant dataset relevant to cross-cultural communication research.")
(root / "rotation-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

print(root / f"{date}.json")
