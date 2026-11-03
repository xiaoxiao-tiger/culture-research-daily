import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-03"
unavailable = "本次核验未取得允许本站完整转载摘要的明确许可。请通过来源链接查看原文摘要，中文概述依据可核验证据原创。"
fallback = {
    "reason": "Google Scholar原生页面返回异常流量验证，未取得可核验结果或引用次数，且未尝试绕过验证。",
    "channel": "改用出版方官网、期刊官方目录、NBER、SSRN与arXiv官方记录进行发现和逐篇核验。",
    "checkedAt": date,
}


def paper(**v):
    x = {
        "evidence": "摘要核验",
        "relevance": "研究启示是本简报依据论文证据作出的推论，不是论文作者已经检验的结论。",
        "abstractMode": "unavailable",
        "originalAbstract": "",
        "abstractUnavailableReason": unavailable,
        "readingPriority": "normal",
        "priorityReason": "与当日主题相关，且题录、摘要与发表状态可以核验。",
        "readingUse": "用于理论框架、研究设计或结果讨论。",
        "researchConnection": "作为一般研究追踪，和博士论文的具体关系见逐篇说明。",
    }
    x.update(v)
    x.setdefault("abstractZh", x["takeaway"])
    x.setdefault("abstractSource", x["url"])
    return x


def journal(**v):
    d = {
        "publicationType": "journal", "publicationStatus": "published", "peerReviewed": True,
        "discoverySource": "Publisher", "journalEdition": "SSCI", "discipline": "communication",
        "indexSource": "site/data/journals.json中的用户上传传播学SSCI Q1/Q2期刊表",
        "quartileSource": "site/data/journals.json中的用户上传传播学SSCI Q1/Q2期刊表",
        "jifQuartile": "Q1", "citationStatus": "unverified", "citationCount": None,
        "citationSource": None, "citationSourceUrl": None, "citationCheckedAt": None,
        "citationNote": "Google Scholar原生页面触发异常流量验证，未取得实际被引次数，不以其他指标替代。",
        "selectionReason": "在出版方可核验候选中按主题直接相关性、研究设计质量和发表日期综合选择。",
        "topicIds": ["culture"], "category": "传播学与社会科学 · 出版方回退",
    }
    d.update(v)
    return paper(**d)


cross = [
    paper(
        title="Not Everyone Has a Voice, or an Ear, on Social Media: The Poster-Observer Model of Opinion Dynamics",
        titleZh="并非每个人都在社交媒体上发声或倾听：意见动力学的发布者—观察者模型",
        authors="Nikos Theologis, Aristides Gionis, Evaggelia Pitoura, Evimaria Terzi, Panayiotis Tsaparas",
        year=2026, venue="arXiv:2610.41434", source="arXiv", sourceDatabase="arXiv",
        category="其他研究 · 最新", url="https://arxiv.org/abs/2610.41434",
        doi="https://doi.org/10.48550/arXiv.2610.41434", arxivId="2610.41434",
        topicIds=["methods"], selectionBucket="latest", publicationType="preprint",
        publicationDate="2026-10-30", publicationDatePrecision="day", publicationDateSource="https://arxiv.org/abs/2610.41434",
        takeaway="作者把社交媒体用户区分为发布意见者与只观察内容者。该模型不会像传统平均化模型那样必然收敛，而可产生持续振荡，并允许比较平台干预的长期影响。",
        theory="Poster-Observer Friedkin-Johnsen模型把表达与观察拆为两个状态过程，用以解释可见意见与私人接收之间的结构性差异。",
        data="合成网络与真实网络。官方摘要未报告真实网络名称、规模及参数估计细节。",
        method="推导模型的封闭形式与动态性质，并在合成和真实网络上模拟不同干预。",
        results="发布和观察的分离阻止系统静态收敛，并可形成永久振荡；不同干预改变可见表达与观察状态的演化路径。",
        limitations="预印本尚未同行评审，模型结论依赖网络与更新规则，不能直接等同于真实用户态度。",
        readingUse="用于区分公开表达、内容暴露与私人接收。",
        researchConnection="博士论文可将传播意向视为发布状态，将理解、好感和人物认同视为接收状态，避免用可见分享代替真实接收。",
    ),
    paper(
        title="Toward Adaptive Internal Communication: Linking Communication Conditions, Internal Communication Satisfaction, and Employee Outcomes",
        titleZh="迈向适应性内部传播：连接传播条件、内部传播满意度与员工结果",
        authors="Ana Tkalac Verčič, Nina Pološki Vokić, Ana Aleksić",
        year=2026, venue="SSRN Working Paper 7657203", source="SSRN", sourceDatabase="SSRN",
        category="其他研究 · 最新", url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7657203",
        doi="https://doi.org/10.2139/ssrn.7657203", topicIds=["methods"], selectionBucket="latest",
        publicationType="working-paper", publicationDate="2026-10-22", publicationDatePrecision="day",
        publicationDateSource="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7657203",
        takeaway="三波调查显示，领导传播和数字传播接受度与内部传播满意度相关，满意度又通过工作生活平衡、生活满意度、组织信任和传播有效性感知关联员工结果。",
        theory="以适应性内部传播为框架，把传播条件、满意度、生活结果与组织结果串联为多阶段路径。",
        data="三波调查N=136。公开记录未提供国家、组织构成与各波流失率。",
        method="采用多波问卷和复合指标路径分析，估计传播条件经满意度及两类中介通向结果的关系。",
        results="领导传播和数字传播接受度正向关联传播满意度；满意度分别通过个人生活路径和组织信任路径关联后续结果。",
        limitations="工作论文尚未同行评审，样本较小，路径模型不能排除未测混淆。",
        readingUse="用于纵向中介链和构念区分。",
        researchConnection="可借鉴多波设计，把故事理解、人物好感、人物认同和传播意向分时测量，降低同源测量对中介结论的影响。",
    ),
    paper(
        title="When Does Bad News Stick? Topic-Level Asymmetry in Narrative Dynamics",
        titleZh="坏消息何时更容易留下：叙事动力学中的主题层面不对称",
        authors="Isha Agarwal, Wentong Chen, Eswar S. Prasad",
        year=2026, venue="NBER Working Paper 35838", source="NBER", sourceDatabase="NBER",
        category="其他研究 · 最新", url="https://www.nber.org/papers/w35838", doi="https://doi.org/10.3386/w35838",
        topicIds=["methods"], selectionBucket="latest", publicationType="working-paper",
        publicationDate="2026-10", publicationDatePrecision="month", publicationDateSource="https://www.nber.org/papers/w35838",
        takeaway="基于1990至2025年《华尔街日报》完整档案构建12个主题的月度正负面叙事指标。每个主题中，坏消息的累计响应都大于好消息，但不对称程度存在明显差异。",
        theory="把叙事持续性理解为具有方向与主题异质性的动态过程，检验负面信息是否比正面信息更持久。",
        data="《华尔街日报》1990至2025年完整档案，按12个主题构建月度正负面情绪序列。",
        method="构造主题层面叙事指数并估计正负冲击的动态累计响应。公开摘要未披露具体文本模型与识别规格。",
        results="所有主题都呈现坏消息更强的累计响应，但效应大小和持续性随主题变化。",
        limitations="工作论文尚未同行评审，单一英文财经媒体的叙事动力不能直接外推至跨文化人物接收。",
        readingUse="用于时间序列中的方向不对称检验。",
        researchConnection="可以检验人物负面道德信息是否比正面价值契合更持久，并将这种效应与文化内外群边界交互。",
    ),
    paper(
        title="ChatGPT as Information Intermediary: Media Partnerships, Sycophancy, and the Pricing of Earnings News",
        titleZh="作为信息中介的ChatGPT：媒体合作、谄媚与盈利新闻定价",
        authors="Ziqing Tian, Valerie Zhang",
        year=2026, venue="SSRN Working Paper 7435681", source="SSRN", sourceDatabase="SSRN",
        category="其他研究 · 重要研究精选", url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7435681",
        doi="https://doi.org/10.2139/ssrn.7435681", topicIds=["sycophancy", "methods"], selectionBucket="cited",
        publicationType="working-paper", publicationDate="2026-09-10", publicationDatePrecision="day",
        publicationDateSource="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7435681",
        takeaway="研究结合媒体合作分期进入、2025年4月GPT-4o谄媚事件和提示实验，发现媒体合作提高相关报道在人工智能回答中的可见度，并放大市场对新闻的反应；谄媚阶段会弱化坏消息定价。",
        theory="将生成式人工智能视为选择和重述新闻的信息中介，谄媚倾向可能系统性改变负面信息的显著性。",
        data="媒体合作、公司盈利新闻、人工智能流量和市场回报数据，并含提示实验。论文共55页，公开摘要未列完整样本规模。",
        method="利用合作关系分期进入、GPT-4o谄媚事件与提示实验形成多重证据。",
        results="合作媒体报道增加人工智能流量和价格反应；谄媚期每增加一篇合作媒体报道，坏消息回报约少负0.35个百分点；实验中每篇合作报道使显著性约增3.2个百分点。",
        limitations="工作论文尚未同行评审。事件与合作安排的外生性仍需正文识别检验，金融市场结果也不等同一般受众接收。",
        citationStatus="unverified", citationCount=None, citationSource=None, citationSourceUrl=None, citationCheckedAt=None,
        citationNote="Google Scholar异常流量验证导致实际被引次数不可核验，本篇按直接相关性和多方法识别质量入选。",
        selectionReason="直接研究谄媚如何改变信息中介与坏消息反应，并采用事件、准实验和提示实验交叉验证。",
        accessFallback=fallback,
        readingUse="用于人工智能中介、谄媚事件与负面信息反应。",
        researchConnection="如果实验材料由模型解释神话人物，应检验模型是否因迎合用户立场而弱化人物的争议价值或道德缺陷。",
    ),
    paper(
        title="Counterfactual assessment of social media interventions by separating exposure from engagement",
        titleZh="通过分离暴露与参与反事实评估社交媒体干预",
        authors="Tommaso Pisani, Pietro Gravino, Giulio Prevedello",
        year=2026, venue="arXiv:2610.37864", source="arXiv", sourceDatabase="arXiv",
        category="其他研究 · 重要研究精选", url="https://arxiv.org/abs/2610.37864",
        doi="https://doi.org/10.48550/arXiv.2610.37864", arxivId="2610.37864", topicIds=["methods"], selectionBucket="cited",
        publicationType="preprint", publicationDate="2026-10-27", publicationDatePrecision="day", publicationDateSource="https://arxiv.org/abs/2610.37864",
        takeaway="作者提出暴露—参与模型，并用2018至2022年意大利Twitter讨论校准。反事实结果显示，预先澄清和准确性提示降低参与；时间顺序信息流提高多样性并降低隔离；定制推荐同时提高参与和多样性并降低隔离。",
        theory="把平台干预对看见什么与如何反应的影响分开，避免把内容暴露直接视为参与。",
        data="2018至2022年意大利Twitter公共讨论数据，并进行个体与总体层面的验证。公开摘要未列用户和帖子规模。",
        method="估计暴露—参与模型，再对预先澄清、准确性提示、时间顺序信息流与定制推荐执行反事实模拟。",
        results="行为提示降低参与且对隔离影响有限；时间顺序信息流提高多样性并降低隔离；定制推荐的改善更全面但幅度较小。",
        limitations="预印本尚未同行评审，反事实结果依赖模型拟合和平台环境稳定性。",
        citationStatus="unverified", citationCount=None, citationSource=None, citationSourceUrl=None, citationCheckedAt=None,
        citationNote="Google Scholar异常流量验证导致实际被引次数不可核验，本篇按方法贡献和主题相关性入选。",
        selectionReason="明确分离暴露与参与，并对多种平台干预给出统一反事实比较。", accessFallback=fallback,
        readingUse="用于区分暴露、认知接收和行为参与。",
        researchConnection="对应论文题目从被看见到被接收的核心区分，可把文化内容暴露、人物理解、认同和分享分别建模。",
    ),
]


def add_dissertation(x, apa, date_value, source, status="published", priority="normal", reason="与博士论文的理论或方法问题直接相关。"):
    x.update(publicationType="journal", publicationStatus=status, peerReviewed=True, apaCitation=apa,
             publicationDate=date_value, publicationDatePrecision="day", publicationDateSource=source,
             peerReviewSource=source, readingPriority=priority, priorityReason=reason)
    return x


j1 = add_dissertation(journal(
    title="When Communications Fail and Values Clash: What Drives Employees to Resist Information Security Compliance?",
    titleZh="当传播失效且价值冲突：什么驱动员工抵制信息安全合规",
    authors="Inho Hwang, Ribin Seo", year=2026, venue="International Journal of Business Communication, OnlineFirst",
    source="International Journal of Business Communication", journalName="International Journal of Business Communication",
    url="https://doi.org/10.1177/23294884261418215", doi="https://doi.org/10.1177/23294884261418215",
    takeaway="对397名员工的调查显示，传播不确定性、传播模糊性与个人—组织价值差异会提高预期性和抑制性焦虑，进而降低信息安全合规意向。",
    theory="结合个人—环境契合与焦虑机制，区分信息不清和价值不相似两类阻力来源。",
    data="397名员工问卷。出版方摘要未提供国家、行业与抽样框。",
    method="横断面调查和路径模型，估计传播条件、价值差异、两类焦虑与合规意向之间的关系。",
    results="传播不确定、模糊和价值差异均与焦虑相关，焦虑进一步负向关联合规意向。",
    limitations="组织合规情境与神话人物接收差异较大，横断面中介不能建立时间因果。",
    readingUse="用于区分价值契合与传播可理解性。",
    researchConnection="可将文化不熟悉造成的理解困难与人物价值差异正交操纵，检验它们是否通过不同情绪路径影响接收。",
    hypothesisImplication="简报推论：价值不契合与信息不清会分别降低人物认同，且可能经不同类型的不确定或抵触情绪产生作用。",
    manipulationImplication="简报推论：分别改变人物价值与解释清晰度，避免把文化陌生度同时写入两项操纵。",
    measurementImplication="简报推论：分别测量理解难度、价值契合、道德评价、焦虑或抵触、人物认同与传播意向。",
), "Hwang, I., & Seo, R. (2026). When communications fail and values clash: What drives employees to resist information security compliance? International Journal of Business Communication. Advance online publication. https://doi.org/10.1177/23294884261418215", "2026-02-15", "https://journals.sagepub.com/doi/10.1177/23294884261418215", "online-first")

j2 = journal(
    title="Reframing Internal Communication: Cross-Cultural Links to Engagement and Life Satisfaction",
    titleZh="重构内部传播：员工投入与生活满意度的跨文化联系", authors="Ana Tkalac Verčič, Dejan Verčič, Krishnamurthy Sriramesh",
    year=2026, venue="International Journal of Business Communication, OnlineFirst", source="International Journal of Business Communication",
    journalName="International Journal of Business Communication", url="https://doi.org/10.1177/23294884251399650", doi="https://doi.org/10.1177/23294884251399650",
    publicationStatus="online-first", publicationDate="2025-12-18", publicationDatePrecision="day", publicationDateSource="https://journals.sagepub.com/doi/10.1177/23294884251399650",
    takeaway="克罗地亚、意大利、斯洛文尼亚和英国共1458名员工的三波调查显示，组织支持、内部传播满意度、员工投入和生活满意度存在稳定路径，但文化调节仅支持五项假设中的两项。",
    theory="把内部传播满意度置于组织支持与员工生活结果之间，并用文化价值检验路径边界。",
    data="四国三波员工调查N=1458。", method="分国回归和跨文化调节检验。",
    results="主要路径在各国显著；高权力距离强化组织支持与传播满意度关系，个人主义强化传播满意度与投入关系，其余文化假设未获支持。",
    limitations="国家数有限，国家文化指标与个体价值不能互换，组织传播结论不直接等同人物接收。",
    readingUse="用于跨文化多组比较和调节假设约束。", researchConnection="提示文化调节应提出具体路径而非假定所有关系都随国家文化改变。",
)

j3 = journal(
    title="Is an emoji worth a thousand words in breaking the online spiral of silence? Cross-cultural comparisons of emoji use in online political discussion",
    titleZh="表情符号能否打破网络沉默螺旋：在线政治讨论中的跨文化比较", authors="Dongdong Yang, David J. Atkin, Yuren Qin",
    year=2025, venue="Information, Communication & Society, OnlineFirst", source="Information, Communication & Society",
    journalName="Information Communication & Society", url="https://doi.org/10.1080/1369118X.2025.2588355", doi="https://doi.org/10.1080/1369118X.2025.2588355",
    publicationStatus="online-first", publicationDate="2025-11-24", publicationDatePrecision="day", publicationDateSource="https://www.tandfonline.com/doi/full/10.1080/1369118X.2025.2588355",
    takeaway="中国微博与美国X用户调查比较四类表情符号使用。人格特征通过敌意和威吓感知关联政治表达，中国样本中的间接表达路径更强。",
    theory="把沉默螺旋与非言语数字线索结合，关注表情符号如何改变敌意知觉和表达成本。",
    data="中国微博与美国X在线调查，出版方可见摘要未报告样本量。", method="跨文化问卷与间接效应比较。",
    results="四类表情符号使用与表达路径存在文化差异，中国样本的间接表达作用更突出。",
    limitations="自报横断面数据不能确定表情使用的因果效应，平台和国家同时变化。",
    readingUse="用于表达意向与平台文化比较。", researchConnection="可帮助区分真实人物接收与公开传播意向，并考虑传播符号对表达成本的影响。",
)

j4 = journal(
    title="Revisiting Framing Codebooks with AI: Employing Large Language Models as Analytical Collaborators in Deductive Content Analysis",
    titleZh="用人工智能重访框架编码本：将大语言模型作为演绎内容分析的协作分析者", authors="Diego Gómez-Zará, Hernán Valdivieso, Jorge Pérez, Denis Parra, Sebastián Valenzuela",
    year=2026, venue="Digital Journalism, OnlineFirst", source="Digital Journalism", journalName="Digital Journalism",
    url="https://doi.org/10.1080/21670811.2026.2730327", doi="https://doi.org/10.1080/21670811.2026.2730327",
    publicationStatus="online-first", publicationDate="2026-09-15", publicationDatePrecision="day", publicationDateSource="https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2730327",
    topicIds=["methods"], takeaway="论文在拉丁美洲新闻语料上展示一种人机协作流程，让大语言模型帮助外显编码规则、暴露模糊案例并迭代演绎式编码本，同时保留研究者判断。",
    theory="把大语言模型定位为分析协作者而非自动真值来源，强调编码本本身需要被诊断和修订。",
    data="拉丁美洲新闻语料。公开摘要未报告篇数与人工编码规模。", method="在演绎内容分析中循环比较模型判断、规则解释和研究者修订。",
    results="流程可暴露框架定义中的歧义并支持编码本迭代，而非仅追求一次性自动分类准确率。",
    limitations="可见证据不足以核验可靠性系数、提示稳定性和跨模型复现。",
    readingUse="用于人物价值、道德评价和文化接近编码本的迭代。", researchConnection="可先让模型指出人物价值编码的模糊案例，再由人工依据Schwartz价值定义裁决。",
)

j5 = journal(
    title="Feeling Iffy About Generative AI: Investigating Audiences’ Trustworthiness Perceptions of Task-Specific AI Disclosures",
    titleZh="对生成式人工智能感到犹疑：受众如何判断任务特定的人工智能披露", authors="Nicolas Mattis, Kimon Kieslich, Claes H. de Vreese",
    year=2026, venue="Digital Journalism, OnlineFirst", source="Digital Journalism", journalName="Digital Journalism",
    url="https://doi.org/10.1080/21670811.2026.2703599", doi="https://doi.org/10.1080/21670811.2026.2703599",
    publicationStatus="online-first", publicationDate="2026-07-24", publicationDatePrecision="day", publicationDateSource="https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2703599",
    topicIds=["sycophancy"], takeaway="一项N=683的联合实验显示，不同新闻任务中的人工智能披露总体都降低可信度评价，但效应随任务类型和受众特征而变化，形成五类反应画像。",
    theory="把人工智能披露视为任务特定的可信度线索，而非单一有无标签。", data="联合实验N=683。",
    method="操纵新闻生产中不同任务的人工智能使用披露，并估计属性效应与受众异质性。",
    results="各类披露的平均方向均为负，但强度存在任务和人群差异，并可归纳为五类可信度反应。",
    limitations="披露情境集中于新闻生产，短期判断不等同长期信任或实际使用。",
    readingUse="用于来源披露和受众异质性实验。", researchConnection="若神话解释由人工智能生成，应单独披露翻译、类比生成和事实核验任务，检验其对接收的不同影响。",
)

journals = [j1, j2, j3, j4, j5]

d1 = add_dissertation(paper(
    title="Navigating Friendship Formation in the Digital Era: The Role of Value Congruence in Emerging Adulthood",
    titleZh="数字时代的友谊形成：成年初显期的价值契合", authors="Johannes A. Karl, Joanne Sneddon, Ronald Fischer",
    year=2026, venue="Emerging Adulthood, OnlineFirst", source="Emerging Adulthood", category="博士论文专题 · 同行评审",
    url="https://doi.org/10.1177/21676968261425276", doi="https://doi.org/10.1177/21676968261425276", topicIds=["culture"],
    takeaway="两项研究显示，潜在朋友在保守、开放和自我超越价值上的契合提高友谊兴趣，价值对立会降低兴趣；自我提升价值的契合效应不稳定。",
    theory="以基本人类价值观和同质性交往解释在线友谊形成，区分不同高阶价值的契合与冲突。",
    data="研究一N=322，研究二N=451，均聚焦成年初显期。",
    method="使用价值表达型自我描述和在线相遇情境操纵或呈现潜在朋友价值，再测量友谊兴趣。",
    results="保守、开放和自我超越价值的契合提高兴趣，对立价值降低兴趣；自我提升的证据不稳定。",
    limitations="友谊形成与媒介人物认同不同，样本年龄范围限制外推，价值线索的显著程度可能影响结果。",
    readingUse="用于Schwartz高阶价值契合的实验操作。",
    researchConnection="这是本期最直接的价值契合证据，可将朋友自述改写为神话人物的行为与动机，并保留价值对立条件。",
    hypothesisImplication="简报推论：人物与受众在开放、自我超越和保守价值上的契合会提高人物认同，但不同价值维度的效应不应被假定相同。",
    manipulationImplication="简报推论：用人物行为和选择表达单一高阶价值，建立契合、中性和对立条件，同时保持道德结果不变。",
    measurementImplication="简报推论：前测受众价值，计算维度内契合，并分别测量道德评价、文化接近、人物认同和传播意向。",
), "Karl, J. A., Sneddon, J., & Fischer, R. (2026). Navigating friendship formation in the digital era: The role of value congruence in emerging adulthood. Emerging Adulthood. Advance online publication. https://doi.org/10.1177/21676968261425276", "2026-02-14", "https://journals.sagepub.com/doi/10.1177/21676968261425276", "online-first", "high", "两项研究直接用Schwartz价值维度检验契合与对立，是博士论文价值契合操纵的最直接依据。")

d2 = add_dissertation(paper(
    title="When visual concreteness meets temporal framing in foreign-brand storytelling on social media",
    titleZh="当视觉具体性遇到时间框架：社交媒体外国品牌故事的匹配效应", authors="Jing Huang, Cheng Lu Wang, Yu Jia, Feifei Liu",
    year=2026, venue="Asia Pacific Journal of Marketing and Logistics, OnlineFirst", source="Asia Pacific Journal of Marketing and Logistics",
    category="博士论文专题 · 同行评审", url="https://doi.org/10.1108/APJML-11-2025-2455", doi="https://doi.org/10.1108/APJML-11-2025-2455", topicIds=["culture"],
    takeaway="三项在线实验发现，具体视觉与回顾式叙事匹配、抽象视觉与前瞻式叙事匹配时效果更好，叙事运输发挥中介作用；匹配优势在中等文化契合时最强。",
    theory="提出视觉具体性与时间框架的故事设计匹配，并把文化契合作为非线性边界条件。",
    data="单一东道国市场的三项在线实验。出版方摘要未报告各实验样本量。",
    method="正交操纵视觉具体性和时间框架，检验品牌反应、叙事运输中介与感知文化契合调节。",
    results="具体—回顾和抽象—前瞻组合更有效，叙事运输解释效应；文化契合过低或过高时，匹配优势弱于中等水平。",
    limitations="单一市场和品牌情境限制外推，样本与操纵材料细节未由可见摘要核验。",
    readingUse="用于文化故事形式匹配和非线性文化契合边界。",
    researchConnection="可将本国相似神话人物类比设计成不同具体程度，并检验其与故事时间框架共同影响理解和认同。",
    hypothesisImplication="简报推论：文化契合对类比效果可能不是线性增强，而是在中等熟悉度时最有利于加工和叙事运输。",
    manipulationImplication="简报推论：正交操纵类比的视觉具体性与回顾或前瞻时间框架，并设置低、中、高感知文化契合预试。",
    measurementImplication="简报推论：测量叙事运输、加工流畅性、感知文化契合、人物理解、人物认同和传播意向。",
), "Huang, J., Wang, C. L., Jia, Y., & Liu, F. (2026). When visual concreteness meets temporal framing in foreign-brand storytelling on social media. Asia Pacific Journal of Marketing and Logistics, 1–27. https://doi.org/10.1108/APJML-11-2025-2455", "2026-06-01", "https://www.emerald.com/apjml/article-abstract/doi/10.1108/APJML-11-2025-2455/1368901/", "online-first", "high", "三项实验同时检验叙事形式、运输和文化契合的非线性边界，可直接转化为类比解释实验。")

d3 = add_dissertation(paper(
    title="Fostering tolerance through museums: assessing visitor engagement with historical analogies at three archaeological galleries in the UK",
    titleZh="通过博物馆培育宽容：英国三家考古展厅中参观者对历史类比的参与", authors="Chiara Bonacchi, Marta Krzyzanska, Kate Sharpe, Zachary Horne, Richard Hingley",
    year=2026, venue="Humanities and Social Sciences Communications, 13, 32", source="Humanities and Social Sciences Communications",
    category="博士论文专题 · 同行评审", url="https://doi.org/10.1057/s41599-025-06333-2", doi="https://doi.org/10.1057/s41599-025-06333-2", topicIds=["culture"],
    takeaway="英国三家博物馆803名参观者对把古代概念与当代政治观念相联的历史类比作出判断。多数参与者持批判、非二元的古代观和自由主义价值，但展览较难吸引或改变威权倾向成年人。",
    theory="把历史类比视为连接过去图式与当代价值判断的公共传播机制，并关注既有政治价值对接收的选择作用。",
    data="三家英国博物馆的Tolerant Futures互动装置，共803名参观者。",
    method="分析参观者对铁器时代、罗马过去与当代概念类比的回答，并用贝叶斯预测模型检验价值和历史理解的关联。",
    results="参与者总体不认同排外民族主义话语中的类比，多持自由价值和非二元历史观；成人态度改变空间有限，作者提出儿童与代际项目可能更有前景。",
    limitations="现场参与者存在强自选择，研究主要识别相关与受众构成，不能把参观后观点当作展览造成的变化。",
    readingUse="用于历史类比、受众选择和价值边界条件。",
    researchConnection="直接说明类比传播不能忽视谁会接触内容。即使类比易懂，也可能只吸引本来就认同其价值的受众。",
    hypothesisImplication="简报推论：本国神话人物类比的效果会受受众既有价值与文化边界调节，且接触选择可能先于说服。",
    manipulationImplication="简报推论：比较无类比、单一对应和保留差异的非二元类比，并记录受众是否主动选择继续阅读。",
    measurementImplication="简报推论：除理解与认同外，测量既有价值、威权倾向、选择性接触、类比接受度和态度变化。",
), "Bonacchi, C., Krzyzanska, M., Sharpe, K., Horne, Z., & Hingley, R. (2026). Fostering tolerance through museums: Assessing visitor engagement with historical analogies at three archaeological galleries in the UK. Humanities and Social Sciences Communications, 13, Article 32. https://doi.org/10.1057/s41599-025-06333-2", "2025-12-01", "https://www.nature.com/articles/s41599-025-06333-2", "published", "high", "以真实博物馆场景检验历史类比、政治价值和受众选择，能为类比解释的边界条件提供直接警示。")

d4 = add_dissertation(paper(
    title="The Metaphorical and Analogical Structure of Myth",
    titleZh="神话的隐喻与类比结构", authors="Angie Padilla", year=2025, venue="Journal of Cognition and Culture, 25(5), 518–540",
    source="Journal of Cognition and Culture", category="博士论文专题 · 同行评审", url="https://doi.org/10.1163/15685373-12340221", doi="https://doi.org/10.1163/15685373-12340221", topicIds=["culture"],
    evidence="理论综述", takeaway="论文提出神话的认知循环框架，认为神话通过隐喻和行为原型把具身经验组织为可理解知识，同时神话又为理解其产生文化提供窗口。",
    theory="认知循环强调经验基础、隐喻或类比结构、行为原型与文化解释之间的双向关系。",
    data="理论论文，不含新的受众样本。", method="概念论证并结合神话、具身认知与隐喻研究提出理论框架。",
    results="论文主张理解神话需要追溯其经验基础，而神话叙事反过来使生活经验与文化知识可理解。",
    limitations="缺少因果实验和跨文化受众验证，理论普遍性需要经验检验。",
    readingUse="用于界定神话类比与具身经验的理论关系。",
    researchConnection="可帮助解释为什么本国相似人物类比既可能提高理解，也可能遮蔽原神话的文化经验基础。",
    hypothesisImplication="简报推论：类比只有在保留目标人物关键经验结构时才会提高理解；表面相似但经验基础不一致可能降低准确接收。",
    manipulationImplication="简报推论：分别操纵表面特征类比和深层价值或行为原型类比，并设置不类比条件。",
    measurementImplication="简报推论：增加结构映射准确性、加工流畅性、文化意义理解和误读指标。",
), "Padilla, A. (2025). The metaphorical and analogical structure of myth. Journal of Cognition and Culture, 25(5), 518–540. https://doi.org/10.1163/15685373-12340221", "2025-10-01", "https://brill.com/view/journals/jocc/25/5/article-p518_4.xml", "published")

general = paper(
    title="Calibration, accuracy, and domain variation across one million collective forecasts from prediction platforms",
    titleZh="一百万次预测平台集体预测的校准、准确性与领域差异", authors="Justin Dickerson, Hilla Shinitzky, Maayan Peer, Mattan S. Ben-Shachar, Michael Gilead",
    year=2026, venue="Proceedings of the National Academy of Sciences, 123", source="PNAS", category="综合顶刊推荐 · 社会科学",
    url="https://doi.org/10.1073/pnas.2615627123", doi="https://doi.org/10.1073/pnas.2615627123", topicIds=["methods"],
    publicationType="journal", publicationStatus="published", peerReviewed=True, publicationDate="2026-10-19", publicationDatePrecision="day",
    publicationDateSource="https://www.pnas.org/doi/10.1073/pnas.2615627123", socialScienceAssessment="confirmed",
    socialScienceReason="研究对象是群体判断、预测行为和平台机制，跨心理学、行为科学与计算社会科学。",
    takeaway="研究汇集Polymarket、Kalshi、Manifold和Metaculus约101万次已结算集体预测。总体校准良好，但不同领域偏差明显，冲突、地缘政治和技术事件常被高估，部分选举结果被低估。",
    theory="以概率校准与准确性评估集体判断，强调总体表现可能掩盖领域特定偏差。",
    data="四个平台约1,014,122次已结算预测，覆盖12个领域、约十年和从小时到年的预测期限。",
    method="跨平台汇总已结算概率预测，比较校准、准确性、领域和时间跨度差异。",
    results="总体预测接近校准，但领域差异系统存在；冲突、地缘政治和技术风险倾向高估，部分选举结果倾向低估。",
    limitations="平台参与者自选择且平台规则不同，集体概率不等于一般公众信念。",
    readingUse="用于大规模预测数据校准与异质性分析。",
    researchConnection="对博士论文直接关联有限，但提醒不能只报告总体平均效应，应检验人物类型、文化背景和价值维度的校准差异。",
)

old = json.loads((root / "2026-10-27.json").read_text())
old_collection = next(g for g in old["groups"] if g["id"] == "communication-issue")["collection"]
toc = []
for e in old_collection["toc"]:
    q = dict(e)
    if e["articleType"] == "Research Article":
        q.update(status="previously-recommended", recommendedDate="2026-10-27", reviewUrl="./?date=2026-10-27")
    else:
        q["status"] = "non-research"
        q.pop("recommendedDate", None); q.pop("reviewUrl", None)
    toc.append(q)

groups = [
    {"id":"crossdisciplinary","label":"其他研究","target":5,"sortBy":"split",
     "selectionBuckets":[{"id":"latest","label":"最新","target":3},{"id":"cited","label":"重要研究精选","target":2,"sortBy":"relevance-quality","sortDescription":"Google Scholar受异常流量验证阻断后，按相关性和研究质量选择。","accessFallback":fallback}],
     "sourceCoverage":[{"database":x,"status":"included"} for x in ["NBER","SSRN","arXiv"]],
     "sortDescription":"最新3篇按首次公开日期降序并各覆盖NBER、SSRN、arXiv；重要研究精选2篇按主题相关性与研究质量呈现。","papers":cross},
    {"id":"journals","label":"传播学与社会科学","target":5,"sortBy":"relevance-quality-date",
     "journalPriorityNote":"先执行不限期刊的主题检索。Google Scholar受阻后改用出版方发现，再按用户上传传播学SSCI Q1/Q2表筛选；本期优先传播学。",
     "sortDescription":"按主题直接相关性、设计质量和发表日期综合排序，不冒充引用次数排序。","accessFallback":fallback,"papers":journals},
    {"id":"communication-issue","label":"传播学顶刊推荐","unit":"issue","target":0,"sortBy":"issue",
     "collection":{"journalId":"ct","journalName":"Communication Theory","kind":"online-first","title":"Advance Articles · 2026-11-03完整可见范围","url":"https://academic.oup.com/ct/advance-articles","checkedAt":date,"complete":True,"toc":toc},
     "sortDescription":"不使用关键词。官方Advance Articles目录完整可读，共25篇研究论文、1篇勘误和1篇书评；研究论文均已于2026-10-27推荐，今天不重复。","papers":[]},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"pnas",
     "sortDescription":"今天轮到PNAS。不使用主题关键词，从官方当前内容中选择一篇最新社会科学研究。","papers":[general]},
]

selected = [j1["doi"], d1["doi"], d2["doi"], d3["doi"], d4["doi"]]
data = {
    "schemaVersion":6,"date":date,"timezone":"Asia/Shanghai","edition":"正式第31期",
    "title":"价值契合、文化类比与接收边界：从可见表达走向人物认同",
    "summary":"本期完成其他研究5篇、传播学SSCI Q1论文5篇、Communication Theory完整目录复核、PNAS轮换推荐，并为博士论文精选5篇同行评审研究。Google Scholar异常流量验证导致引用次数不可核验，相关栏目依指南启用出版方回退并如实标注。",
    "historyPolicy":"exclude-recommended","journalPolicy":"ssci-communication-q1-q2-and-social-science",
    "searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],"activeTopicIds":["culture","sycophancy","methods"],
    "searchSettings":{"source":"defaults + reading-plan","lookbackDays":30,"conflictNote":"当日没有生效的一次性用户设置。博士论文标准强化culture主题，但未删除culture、sycophancy和methods，也未改动未来设置。"},
    "notice":"逐篇依据官方记录、出版方页面及可访问正文核验。只有实际阅读正文关键部分才标全文核验；无法核验的样本、系数、识别和许可信息均明确说明。",
    "searchNote":"Google Scholar原生主题查询返回异常流量提示后停止，不绕过验证，也不以Web of Science、OpenAlex、下载量或网页指标冒充引用次数。NBER、SSRN与arXiv使用限定官方域名的公开网页检索发现候选，再回到官方记录核验。",
    "themeSearches":[
      {"platform":"Google Scholar","query":"(\"cultural transmission\" OR \"cultural diffusion\" OR \"cross-cultural reception\" OR \"intercultural communication\" OR \"cultural premium\" OR novelty OR exoticism OR cosmopolitanism OR ((\"value congruence\" OR \"value similarity\" OR \"shared values\") AND (character OR narrative OR audience)) OR (mythology AND analogy))","timeRange":"不限年份；检索日期2026-11-03","purpose":"culture主题发现，随后筛期刊并核验引用次数","status":"原生页面显示异常流量验证，未取得结果或引用次数，未绕过验证。"},
      {"platform":"Google Scholar","query":"(sycophancy OR \"value alignment\" OR ingratiation OR \"opinion agreement\") AND (\"large language model\" OR chatbot OR \"conversational agent\")","timeRange":"不限年份；检索日期2026-11-03","purpose":"sycophancy主题发现","status":"culture首次请求已触发站点级验证，因此未继续发送本主题请求，并启用指南规定的回退。"},
      {"platform":"Google Scholar","query":"(\"causal inference\" OR \"panel data\" OR \"interrupted time series\" OR \"text measurement\") AND (communication OR \"digital platforms\" OR \"social media\")","timeRange":"不限年份；检索日期2026-11-03","purpose":"methods主题发现","status":"culture首次请求已触发站点级验证，因此未继续发送本主题请求，并启用指南规定的回退。"},
      {"platform":"NBER","query":"site:nber.org/papers (narrative OR communication OR culture OR social) October 2026","timeRange":"优先近30日，必要时扩展；检索日期2026-11-03","purpose":"NBER候选发现","status":"限定官方域名的公开网页检索成功；不冒称NBER站内高级检索，入选记录回到NBER官方页核验。"},
      {"platform":"SSRN","query":"site:papers.ssrn.com (communication OR sycophancy OR narrative OR value) 2026","timeRange":"优先近30日，必要时扩展；检索日期2026-11-03","purpose":"SSRN候选发现","status":"限定官方域名的公开网页检索成功；题录、日期和摘要回到SSRN记录核验。"},
      {"platform":"arXiv","query":"submittedDate:[202610010000 TO 202611032359] AND all:(culture OR value OR narrative OR communication OR sycophancy OR social)","timeRange":"2026-10-01至2026-11-03","purpose":"arXiv候选发现","status":"官方摘要记录检索成功，题名、作者、首次提交日期、摘要和arXiv ID完成核验。"}],
    "periodicalChecks":[
      {"platform":"Oxford Academic · Communication Theory","query":"Advance Articles完整目录，不使用关键词","timeRange":"检查日期2026-11-03","purpose":"传播学顶刊整期轮换","status":"官方目录完整可读，仍为25篇研究论文、1篇勘误和1篇书评；研究论文均已于2026-10-27推荐，今天不重复。"},
      {"platform":"PNAS","query":"官方当前期及最新研究，不使用主题关键词","timeRange":"检查日期2026-11-03","purpose":"综合顶刊轮换推荐","status":"官方与PubMed题录完成核验，入选2026-10-19在线发表的社会科学研究1篇。"}],
    "verificationLog":[
      {"platform":"Google Scholar","query":"当日主题检索与实际引用次数","timeRange":"核验日期2026-11-03","purpose":"主题发现与引用排序","status":"首次原生查询显示异常流量验证后停止；没有绕过验证、记录虚构0次引用或用其他指标替代。"},
      {"platform":"NBER、SSRN与arXiv官方记录","query":"其他研究5篇的身份、首次公开日期、摘要与版本","timeRange":"核验日期2026-11-03","purpose":"逐篇核验与跨版本去重","status":"5篇均完成题录和摘要核验，且与截至2026-11-02的永久登记无重复。"},
      {"platform":"出版方与权威题录","query":"期刊论文题名、作者、年份、期刊、同行评审状态、DOI、摘要、样本与方法","timeRange":"核验日期2026-11-03","purpose":"主题期刊、博士论文专题与综合顶刊逐篇核验","status":"15篇当日登记均完成身份核验；只有公开证据支持的研究细节被写入，未知细节明确标示。"}],
    "groups":groups,"coreTracking":[],"coreTrackingNote":"reading-plan与core-papers当日没有用户提交的核心论文请求，因此本期没有核心文献状态更新。",
    "periodicalCheckNote":"轮换栏目不使用主题关键词。Communication Theory按检查日完整可见范围形成在线优先快照；PNAS按官方当前内容检查。",
    "dissertation":{"title":"从被看见到被接收","timeRange":"优先检查2026-11-02上期发布以来的新发表研究。直接相关新论文不足5篇后，扩展至2025年以来尚未推荐的同行评审研究；较早论文按补充处理，不冒称当日最新。",
      "selectionNote":"本期精选5篇同行评审论文。1篇在传播学与社会科学栏完整解读，另有4篇置于博士论文专题，覆盖Schwartz价值契合、文化故事匹配、历史类比与神话认知结构。",
      "historyCoverage":"已核对网站截至2026-11-02的永久登记、现有简报、用户明确列出的既有文献、本轮可见对话及可访问清单，并按DOI、arXiv ID、规范化题名和已知版本别名去重。无法访问的完整旧对话和未同步私人清单不在覆盖范围内，因此不声称绝对完全去重。",
      "selectedPapers":selected,"papers":[d1,d2,d3,d4],
      "topPapers":[
        {"doi":d1["doi"],"reason":"直接以Schwartz价值维度检验契合、对立与关系兴趣，为人物价值契合操纵提供最接近的经验模板。"},
        {"doi":d2["doi"],"reason":"三项实验同时处理叙事形式、叙事运输与非线性文化契合边界，可直接转化为本国神话人物类比实验。"},
        {"doi":d3["doi"],"reason":"真实博物馆场景显示历史类比受既有价值和选择性接触约束，能防止把可理解类比误判为说服成功。"}]},
}

(root / f"{date}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
index_path = root / "index.json"
index = [x for x in json.loads(index_path.read_text()) if x["date"] != date]
count = sum(len(g["papers"]) for g in groups) + len(data["dissertation"]["papers"])
index.insert(0,{"date":date,"title":data["title"],"summary":data["summary"],"edition":data["edition"],"count":count,"file":f"{date}.json"})
index_path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n")

state_path=root/"rotation-state.json"; state=json.loads(state_path.read_text()); state["updatedAt"]=date
ct=state["communication"]["ct"]
ct.update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,reason="Oxford Academic Advance Articles directory was fully readable on 2026-11-03: 25 Research Articles, one Correction and one Book Review. No research article was newer than or different from the complete 2026-10-27 snapshot.")
snap={"checkedAt":date,"url":"https://academic.oup.com/ct/advance-articles","complete":True,"dois":[e["url"] for e in toc if e["articleType"]=="Research Article"]}
ct["onlineSnapshots"]=[x for x in ct.get("onlineSnapshots",[]) if x.get("checkedAt")!=date]+[snap]
ct["directoryObservation"]={"checkedAt":date,"url":"https://academic.oup.com/ct/advance-articles","complete":True,"reportedTotal":27,"researchArticleCount":25,"nonResearchCount":2,"scopeNote":"Complete visible Advance Articles directory on 2026-11-03; no new research article since the complete 2026-10-27 snapshot."}
pnas=state["general"]["pnas"]
pnas.update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,lastRecommendedDoi=general["doi"],publicationDate=general["publicationDate"],socialScienceAssessment="confirmed")
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n")
print(f"Wrote {date} with {count} papers")
