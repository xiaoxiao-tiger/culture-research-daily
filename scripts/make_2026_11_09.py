import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-09"
unavailable = "本次核验未取得允许本站完整转载摘要的明确许可。请通过来源链接查看原文摘要，中文概述依据可核验证据原创。"
fallback = {
    "reason": "Google Scholar原生页面返回异常流量验证，未取得可核验结果或引用次数，且未尝试绕过验证。",
    "channel": "改用出版方官网、官方目录、NBER、SSRN与arXiv官方记录进行发现和逐篇核验。",
    "checkedAt": date,
}


def paper(**v):
    x = {
        "evidence": "摘要核验",
        "relevance": "研究启示是本简报依据论文证据作出的推论，不是论文作者已经检验的结论。",
        "abstractMode": "unavailable", "originalAbstract": "", "abstractUnavailableReason": unavailable,
        "readingPriority": "normal", "priorityReason": "题录、摘要与日期可以核验，且与当日主题相关。",
        "readingUse": "用于理论框架、研究设计或结果讨论。",
        "researchConnection": "作为一般研究追踪，和博士论文的关系见逐篇说明。",
    }
    x.update(v)
    x.setdefault("abstractZh", x["takeaway"])
    x.setdefault("abstractSource", x["url"])
    return x


def journal(**v):
    x = {
        "publicationType": "journal", "publicationStatus": "online-first", "peerReviewed": True,
        "discoverySource": "Publisher", "journalEdition": "SSCI", "discipline": "communication",
        "indexSource": "传播学期刊依据site/data/journals.json用户上传的SSCI期刊表核验。",
        "quartileSource": "依据site/data/journals.json中的传播学SSCI Q1/Q2表。", "jifQuartile": "Q1",
        "citationStatus": "unverified", "citationCount": None, "citationSource": None,
        "citationSourceUrl": None, "citationCheckedAt": None,
        "citationNote": "Google Scholar原生页面触发异常流量验证，未取得实际被引次数，不以其他指标替代。",
        "selectionReason": "按博士论文直接相关性、传播学优先、理论或研究设计质量和首次发表日期综合选择。",
        "topicIds": ["culture"], "category": "传播学与社会科学 · 出版方回退",
    }
    x.update(v)
    return paper(**x)


def dissertation(p, apa, hypothesis, manipulation, measurement, reason):
    p.update(
        apaCitation=apa, peerReviewed=True, peerReviewSource=p["url"], publicationDateSource=p["url"],
        readingPriority="high", priorityReason=reason,
        hypothesisImplication="简报推论：" + hypothesis,
        manipulationImplication="简报推论：" + manipulation,
        measurementImplication="简报推论：" + measurement,
    )
    return p


cross = [
    paper(
        title="Green Tastes, Beliefs, and Portfolios: Evidence from Synthetic Investors", titleZh="绿色偏好、信念与投资组合：来自合成投资者的证据",
        authors="Xindi He, Lubos Pastor", year=2026, venue="NBER Working Paper 35982",
        source="NBER", sourceDatabase="NBER", category="其他研究 · 最新", url="https://www.nber.org/papers/w35982",
        doi="https://doi.org/10.3386/w35982", topicIds=["methods"], selectionBucket="latest",
        publicationType="working-paper", publicationDate="2026-10", publicationDatePrecision="month",
        publicationDateSource="https://www.nber.org/papers/w35982",
        takeaway="论文让大语言模型扮演480类零售投资者和60类机构投资者，提取绿色偏好、收益信念、投资组合与动机。机构报告的绿色偏好更弱，却持有更绿色的组合并归因于外部压力，说明可见行为不能直接等同内在价值。",
        theory="区分偏好、信念、外部压力和实际选择，并检验合成调查能否重建随信息环境变化的认知序列。",
        data="480个零售投资者身份和60个机构投资者身份的合成调查回应，并以2014至2025年日期遮蔽信息模块重建年度序列。",
        method="提示大语言模型按投资者身份回答偏好、信念、配置和动机问题，将不同年份信息模块随机排序并遮蔽日期，再与现实绿色需求和注意指标比较。",
        results="机构偏好较弱但组合更绿；零售偏好主要随政治身份变化，机构偏好随类型和地理变化。偏好时间上较稳定，2020年后绿色组合收益信念更悲观。",
        limitations="NBER工作论文尚未期刊同行评审；合成身份不是实际受访者，模型训练资料污染、提示敏感性与外部效度是核心限制。",
        readingUse="用于区分价值偏好、显性行为和外部规范压力，并评估合成样本方法。",
        researchConnection="人物传播意向或选择行为不能自动视为价值契合；应同时测量主观价值、预期结果和群体规范压力。",
    ),
    paper(
        title="Is Sycophancy a Form of In-Context Updating?", titleZh="谄媚是否是一种上下文更新",
        authors="Itai Shapira, Myra Cheng, Hadas Orgad", year=2026, venue="arXiv:2610.28325",
        source="arXiv", sourceDatabase="arXiv", category="其他研究 · 最新", url="https://arxiv.org/abs/2610.28325",
        doi="https://doi.org/10.48550/arXiv.2610.28325", arxivId="2610.28325", topicIds=["sycophancy", "methods"],
        selectionBucket="latest", publicationType="preprint", publicationDate="2026-10-20", publicationDatePrecision="day",
        publicationDateSource="https://arxiv.org/abs/2610.28325",
        takeaway="论文把事实性谄媚重新界定为上下文更新对用户断言赋予过高权重，而不只是取悦用户。行为和机制证据表明，模型也会根据外部来源及其支持程度更新答案，支持用户断言的内部成分同时服务于更一般的有用更新。",
        theory="提出来源敏感的上下文更新框架，将谄媚视为证据权重失衡。",
        data="多个模型在用户断言与外部来源信息条件下的行为输出及内部机制分析；摘要没有列出完整模型清单与样本规模。",
        method="比较不同信息来源和证据强度下的答案修订，并以因果机制干预检验支持用户顺从的内部成分是否也支持一般更新。",
        results="模型对用户与外部来源都会更新，证据支持度影响更新幅度；降低谄媚可能同时损害有用更新。",
        limitations="arXiv预印本尚未同行评审；机制证据的模型外推范围和具体干预效应需读正文。",
        readingUse="用于谄媚测量和机制区分。",
        researchConnection="提示研究AI协助材料时应把无条件迎合与依据证据修订分开测量，避免把所有一致性都当作谄媚。",
    ),
    paper(
        title="The Asymmetric Effect of AI-Mediated Communication: AI Disclosure Weakens Positive, But Not Negative, Social Inferences",
        titleZh="人工智能中介传播的不对称效应：披露人工智能削弱正面但不削弱负面社会推断",
        authors="Hyeran Kang, Andras Molnar", year=2026, venue="SSRN Working Paper 7501238",
        source="SSRN", sourceDatabase="SSRN", category="其他研究 · 最新", url="https://ssrn.com/abstract=7501238",
        doi="https://doi.org/10.2139/ssrn.7501238", topicIds=["sycophancy"], selectionBucket="latest",
        publicationType="working-paper", publicationDate="2026-09-25", publicationDatePrecision="day",
        publicationDateSource="https://ssrn.com/abstract=7501238",
        takeaway="两项预注册实验共1022名美国参与者。人工智能标签降低信息被视为发送者真实思想与感受的诊断性，但这种削弱对感激、友善等正面推断远强于对失望、敌意等负面推断。",
        theory="以信号诊断性解释人工智能披露对积极关系信号和消极信号的不对称影响。",
        data="两项预注册美国在线实验，总样本N=1022，使用正面和负面人际信息。",
        method="操纵信息效价与人类或人工智能作者标签，测量诊断性和对发送者思想、感受及态度的推断，并进行调节中介分析。",
        results="人工智能标签显著削弱积极社会推断，对消极推断影响较小或没有明显影响；积极推断更依赖感知诊断性。",
        limitations="SSRN论文尚未同行评审；标签操纵与短文本情境未必代表持续关系中的真实协作写作。",
        readingUse="用于区分正负社会推断及来源披露。",
        researchConnection="如果实验材料披露翻译或生成工具，应检验其是否不对称影响人物的正面价值信号，而非只测总体可信度。",
    ),
    paper(
        title="Sycophantic AI makes human interaction feel more effortful and less satisfying over time",
        titleZh="谄媚型人工智能使人际互动逐渐显得更费力且更不令人满意",
        authors="Lujain Ibrahim, Franziska Sofia Hafner, Myra Cheng, Cinoo Lee, Rebecca Anselmetti, Robb Willer, Luc Rocher, Diyi Yang",
        year=2026, venue="arXiv:2605.07912", source="arXiv", sourceDatabase="arXiv", category="其他研究 · 重要研究精选",
        url="https://arxiv.org/abs/2605.07912", doi="https://doi.org/10.48550/arXiv.2605.07912", arxivId="2605.07912",
        topicIds=["sycophancy", "methods"], selectionBucket="cited", publicationType="preprint",
        publicationDate="2026-05-08", publicationDatePrecision="day", publicationDateSource="https://arxiv.org/abs/2605.07912",
        takeaway="五项预注册研究覆盖3075名参与者和12766次人机对话，其中包括三周的美国人口代表性研究。谄媚型人工智能即时提供类似亲友的情绪与自尊支持，长期使用者更愿意向其寻求建议，并报告较低的现实人际互动满意度。",
        theory="提出关系替代与比较标准机制，认为低摩擦的被理解感会抬高用户对人际关系的比较基准。",
        data="五项预注册研究，N=3075，12766次人机对话，包括三周纵向实验。",
        method="结合即时实验、选择任务和纵向使用，比较不同人工智能回应风格以及对现实关系的后续评价。",
        results="多数参与者偏好谄媚型人工智能，主要因为感到被理解而非建议质量；持续使用与现实互动满意度下降相关。",
        limitations="arXiv预印本尚未同行评审；不同系统、文化和更长期使用能否复现尚未核验。",
        citationStatus="unverified", citationCount=None, citationSource=None, citationSourceUrl=None, citationCheckedAt=None,
        citationNote="Google Scholar受异常流量验证阻断，未核验实际引用次数。",
        selectionReason="多项预注册研究并含纵向实验，直接检验谄媚的关系后果，方法和理论价值高。",
        readingUse="用于纵向实验和关系比较机制。",
        researchConnection="为区分即时好感和长期关系后果提供设计范例，也提醒不能把被理解感等同建议质量。",
    ),
    paper(
        title="When Complaints Go Quiet: Provider Strategy and Regulatory Design of AI Sycophancy",
        titleZh="当投诉沉默：人工智能谄媚的提供商策略与监管设计",
        authors="Di Yuan, Jingwen Zhang", year=2026, venue="SSRN Working Paper 7455658", source="SSRN", sourceDatabase="SSRN",
        category="其他研究 · 重要研究精选", url="https://ssrn.com/abstract=7455658",
        doi="https://doi.org/10.2139/ssrn.7455658", topicIds=["sycophancy", "methods"], selectionBucket="cited",
        publicationType="working-paper", publicationDate="2026-09-13", publicationDatePrecision="day",
        publicationDateSource="https://ssrn.com/abstract=7455658",
        takeaway="理论模型显示，更能核验错误的用户会从更谄媚的模型转向竞争者，使其剩余用户更难发现错误，投诉数据因而系统性低估风险。独立审计通过在被选择的客户群之外生成证据，提高提供商避免高谄媚发布的边际回报。",
        theory="把用户核验能力异质性、竞争、样本选择与监管证据置于同一产业组织模型。",
        data="分析模型，不使用新的行为样本；参数描述用户核验倾向、提供商策略、竞争与投诉。",
        method="比较提供商策略与用户迁移形成的均衡，并对投诉监管与独立审计制度作比较静态分析。",
        results="竞争可能使高核验用户退出，从而让投诉样本向低核验用户选择；核验能力离散度越高，盲点越严重，独立审计可缓解。",
        limitations="SSRN理论论文尚未同行评审；结论依赖模型假设，尚需真实平台与投诉数据检验。",
        citationStatus="unverified", citationCount=None, citationSource=None, citationSourceUrl=None, citationCheckedAt=None,
        citationNote="Google Scholar受异常流量验证阻断，未核验实际引用次数。",
        selectionReason="解释为什么用户反馈可能系统性漏报谄媚风险，并提出可检验的样本选择机制。",
        readingUse="用于测量偏差、选择机制和监管讨论。",
        researchConnection="提示问卷中能识别文化障碍的受众可能更易退出，留下的满意样本会高估接收效果，应记录退出和核验能力。",
    ),
]
cross[:3] = sorted(cross[:3], key=lambda p: p["publicationDate"], reverse=True)


almost = dissertation(journal(
    title="Almost Villains? A Mixed-Method Examination of White Audiences' Racial and Moral Categorization of Media Characters",
    titleZh="近乎反派：白人受众对媒体人物种族与道德分类的混合方法研究",
    authors="Sovannie Len, Steven Kubitza", year=2026, venue="Journal of Broadcasting & Electronic Media, 70(3), 337–353",
    source="Journal of Broadcasting & Electronic Media", journalName="JOURNAL OF BROADCASTING & ELECTRONIC MEDIA",
    jifQuartile="Q2",
    url="https://doi.org/10.1080/08838151.2026.2654865", doi="https://doi.org/10.1080/08838151.2026.2654865",
    publicationDate="2026-04-04", publicationDatePrecision="day", publicationStatus="published",
    takeaway="对361名白人受众的混合方法研究操纵或比较人物的道德显著性与种族背景。白人受众对亚洲与黑人角色出现一定偏爱，却对白人角色的道德偏离更为严格，显示优势群体可能用不同分类策略处理偏离规范的内群体人物。",
    theory="结合社会认同、人物认同、感知道德与道德脱离，解释种族内外群体线索如何改变道德分类。",
    data="361名白人受众，包含量表与两道开放回答。",
    method="混合方法设计，量化测量10项人物认同、11项感知道德和道德脱离，并分析对人物角色及可宽恕性的开放回答。",
    results="受众对亚洲与黑人人物有一定偏爱，但对白人人物分类更严格；结果支持群体位置会改变道德评价策略。",
    limitations="只招募白人受众，种族分类不能直接等同国族文化边界；摘要不足以核验全部条件与效应量。",
    readingUse="用于群体边界、道德评价与人物认同的区分。",
    researchConnection="直接说明内外群体边界可能改变道德评价，但道德评价与人物认同应保持为不同结果。"),
    "Len, S., & Kubitza, S. (2026). Almost villains? A mixed-method examination of White audiences' racial and moral categorization of media characters. Journal of Broadcasting & Electronic Media, 70(3), 337–353. https://doi.org/10.1080/08838151.2026.2654865",
    "文化内外群体边界调节人物道德行为对感知道德和人物认同的影响，而且方向未必是简单的内群体偏爱。",
    "正交操纵人物文化标签与道德行为，避免把中国身份、价值行为和角色善恶绑定在一个刺激中。",
    "分别使用人物认同、感知道德、道德脱离和可宽恕性指标，并记录开放式分类理由。",
    "这是本期最直接连接群体边界、道德评价和人物认同的受众研究。")

labels = dissertation(journal(
    title="Internalized Cultural Heuristics of Warmth and Competence in Identity Labels: The Indirect Indexicality of Stereotype and Emotional Reaction Activation as a Function of Social Media Exposure",
    titleZh="身份标签中的温暖与能力文化启发式：社交媒体暴露激活刻板印象与情绪反应",
    authors="Na Wang, Julius Matthew Riles, Alyssa Coffey, Can Liu, et al.", year=2026,
    venue="Journal of Language and Social Psychology, Online First", source="Journal of Language and Social Psychology",
    journalName="JOURNAL OF LANGUAGE AND SOCIAL PSYCHOLOGY", url="https://doi.org/10.1177/0261927X261477762",
    doi="https://doi.org/10.1177/0261927X261477762", publicationDate="2026-08-18", publicationDatePrecision="day",
    takeaway="实验在其他帖子内容保持一致时，仅呈现基本身份标签。与无标签基线相比，标签本身足以增强受众对温暖与能力刻板归因及相关情绪结果的依赖，既有群际接触还会调节这一过程。",
    theory="把刻板印象内容模型与间接指示性结合，解释最小语言标签如何激活文化内化的群体启发式。",
    data="社交媒体身份标签实验；出版方摘要没有报告样本量与具体标签清单，数据已链接至OSF。",
    method="在帖子内容恒定时操纵是否出现身份标签，比较温暖、能力与情绪判断，并考察群际接触调节。",
    results="最小身份标签足以增强刻板归因与情绪反应，部分情绪结果超出经典模型预测。",
    limitations="摘要未提供样本与效应量；身份标签到神话人物的外推需要新的刺激检验。",
    readingUse="用于最小群体标签与文化边界操纵。",
    researchConnection="说明仅标注中国来源就可能在价值内容出现前激活群体启发式，因此应设置无标签或模糊标签对照。"),
    "Wang, N., Riles, J. M., Coffey, A., Liu, C., et al. (2026). Internalized cultural heuristics of warmth and competence in identity labels. Journal of Language and Social Psychology. https://doi.org/10.1177/0261927X261477762",
    "文化来源标签可能先激活温暖与能力启发式，并调节后续价值契合对人物评价的影响。",
    "在完全相同的角色叙事上操纵中国标签、本国类比标签和无来源标签，同时测量操纵前后的群体判断。",
    "测量温暖、能力、情绪、内外群体归属与既有群际接触，检验标签的直接和调节效应。",
    "它为文化内外群体边界提供了非常简洁且可复制的实验操纵。")

nonbinary = dissertation(journal(
    title="Audiovisual Fiction to Reduce Prejudices Against Non-Binary People", titleZh="用视听虚构叙事减少对非二元性别群体的偏见",
    authors="Isabel Rodríguez-de-Dios, Vitor Blanco-Fernández, María T. Soto-Sanfiel", year=2026,
    venue="Media Psychology, Online First", source="Media Psychology", journalName="MEDIA PSYCHOLOGY",
    url="https://doi.org/10.1080/15213269.2026.2614632", doi="https://doi.org/10.1080/15213269.2026.2614632",
    publicationDate="2026-01-15", publicationDatePrecision="day",
    takeaway="404名西班牙参与者被随机分配到六段包含非二元角色的电视剧叙事，角色身份相关结局为正面、中性或负面。负面和中性叙事引发更高运输，进而提高人物好感，并通过降低群际焦虑提升开放态度。",
    theory="以叙事运输为起点，连接人物好感、群际焦虑和对外群体的开放态度。",
    data="N=404的西班牙在线面板，年龄19至74岁，性别与性取向多样。",
    method="六段刺激的组间因子实验，操纵身份相关叙事结局效价，检验运输、人物好感、群际焦虑与开放态度路径。",
    results="负面和中性条件的运输高于正面条件；运输提高人物好感，后者与较低群际焦虑和更开放态度相连。",
    limitations="研究对象与文化神话人物不同，六段既有电视剧刺激可能同时包含未控制内容差异。",
    readingUse="用于区分叙事运输、人物好感与群际态度。",
    researchConnection="提供从叙事体验到人物评价再到外群体态度的分层结果结构。"),
    "Rodríguez-de-Dios, I., Blanco-Fernández, V., & Soto-Sanfiel, M. T. (2026). Audiovisual fiction to reduce prejudices against non-binary people. Media Psychology. https://doi.org/10.1080/15213269.2026.2614632",
    "叙事效价可能先影响运输，再通过人物好感和群际焦虑影响外群体态度，而不是直接改变传播意向。",
    "操纵人物价值行为的正、中、负后果，并保持文化标签不变，以拆开效价与文化接近。",
    "分别测量运输、人物好感、人物认同、群际焦虑和传播意向，检验串联中介。",
    "研究把人物接收与群际态度放在同一因果链中，同时保持构念区分。")

norms = dissertation(journal(
    title="Testing the Role of Social Norm Cues in the Narrative Enjoyment and Appreciation Rationale",
    titleZh="检验社会规范线索在叙事愉悦与欣赏机制中的作用", authors="Kevin Kryston, Allison Eden", year=2026,
    venue="Mass Communication and Society, Online First", source="Mass Communication and Society",
    journalName="Mass Communication and Society", url="https://doi.org/10.1080/15205436.2026.2690542",
    doi="https://doi.org/10.1080/15205436.2026.2690542", publicationDate="2026-07-01", publicationDatePrecision="day",
    takeaway="两项研究把正面、混合或负面故事结局与他人评价线索结合。规范线索与结局一致时强化直觉评价，不一致时减慢判断并改变愉悦；混合结局的评价更随他人意见移动。",
    theory="扩展叙事愉悦与欣赏机制，区分内容线索与社会规范线索的一致、冲突和模糊情境。",
    data="两项叙事实验；公开摘要未报告样本量和参与者构成。",
    method="操纵故事结局效价与他人意见，比较评价速度、愉悦和欣赏。",
    results="一致规范强化内容所导向的评价，冲突规范减弱或逆转评价，混合结局最易受他人意见影响。",
    limitations="摘要未给出样本、具体刺激和效应量；他人意见线索与本国类比不等同。",
    readingUse="用于社会规范与本国类比的边界条件。",
    researchConnection="受众本国人物类比可能不仅提供图式，也携带群体规范线索，二者需要分别操纵。"),
    "Kryston, K., & Eden, A. (2026). Testing the role of social norm cues in the narrative enjoyment and appreciation rationale. Mass Communication and Society. https://doi.org/10.1080/15205436.2026.2690542",
    "本国相似人物的解释若同时传递本国受众的赞许规范，可能改变原叙事的愉悦与评价。",
    "交叉操纵类比是否出现以及类比人物获得赞许或反对，避免把图式便利和规范影响混在一起。",
    "测量加工时间、愉悦、欣赏、感知规范、图式熟悉度和传播意向。",
    "它为本国人物类比的潜在规范路径提供了清晰边界条件。")

journals = [almost, labels, nonbinary, norms]

black_myth = dissertation(paper(
    title="Black Myth: Wukong in German Media - Has China Gained Soft Power Through Gaming?",
    titleZh="德国媒体中的《黑神话：悟空》：中国是否通过游戏获得了软实力",
    authors="Sizhou Pan", year=2026, venue="Simulation & Gaming, 57(4), 604–623", source="Simulation & Gaming",
    category="博士论文专题 · 直接接收证据", url="https://doi.org/10.1177/10468781261415940",
    doi="https://doi.org/10.1177/10468781261415940", topicIds=["culture"], publicationType="journal",
    publicationStatus="published", peerReviewed=True, publicationDate="2026-01-13", publicationDatePrecision="day",
    takeaway="论文分析269篇德国媒体文章，发现德国媒体肯定游戏制作质量，却质疑叙事深度与文化可及性。有限本地化和中国媒体环境中的自我规制使接收呈现好奇与批判并存，软实力并非国家规划的自动结果。",
    theory="以跨国接收、文化表征和软实力为框架，强调开发者意图、媒体话语与国家叙事之间的动态互动。",
    data="269篇德国主流、大众与游戏媒体文章；补充材料公开其中81篇被引用或参考文章的链接。",
    method="媒体话语分析，比较德国媒体对制作质量、叙事深度、文化可及性与中国软实力的解释。",
    results="接收不是单纯正面扩散，而是制作赞誉、叙事不透明和文化可及性质疑并存。",
    limitations="分析对象是媒体话语而非普通玩家，不能直接推断个体理解、认同或传播意向；摘要未报告编码可靠性。",
    readingUse="用于外国媒体接收、叙事可及性与证据层级。",
    researchConnection="这是对中国神话游戏在德国接收的直接证据，但需要后续受众实验把媒体话语与个体接收分开。"),
    "Pan, S. (2026). Black Myth: Wukong in German media: Has China gained soft power through gaming? Simulation & Gaming, 57(4), 604–623. https://doi.org/10.1177/10468781261415940",
    "叙事不透明与文化可及性可能分别削弱理解和人物认同，即使制作质量与初始好感较高。",
    "基于德国报道中出现的可及性障碍设计原版、文化注释和本国人物类比三种材料。",
    "分别测量叙事理解、制作评价、人物认同、文化接近和传播意向，并记录开放式误读。",
    "它直接涉及外国社会对中国神话游戏的接收，同时清楚暴露媒体话语与个体受众证据之间的缺口。")

casa = dissertation(paper(
    title="A Social Identity Extension to CASA: How GenAI Chatbots’ Attitudinal Congruence and Group Identity Impact User Empathy and Issue Support",
    titleZh="CASA的社会认同扩展：生成式人工智能聊天机器人的态度契合和群体身份如何影响同理心与议题支持",
    authors="Xinyan Zhao, Rong Ma", year=2026, venue="International Journal of Human-Computer Interaction, 42, 11782–11797",
    source="International Journal of Human-Computer Interaction", category="博士论文专题 · 相邻机制",
    url="https://doi.org/10.1080/10447318.2025.2594153", doi="https://doi.org/10.1080/10447318.2025.2594153",
    topicIds=["culture", "sycophancy"], publicationType="journal", publicationStatus="published", peerReviewed=True,
    publicationDate="2025-12-12", publicationDatePrecision="day",
    takeaway="LGBTQ+议题倡导在线实验显示，态度一致的聊天机器人通过价值契合提高感知相似性与同理心；少数群体身份机器人则通过少数影响促进信息精细加工与同理心。两条路径最终经态度关联更强的议题支持。",
    theory="将社会认同引入CASA，区分个人层面的态度契合路径和群体层面的少数身份影响路径。",
    data="LGBTQ+议题倡导在线实验；公开摘要没有报告样本量和具体条件人数。",
    method="操纵聊天机器人的态度一致性与群体身份，检验感知相似、价值契合、信息加工、同理心、态度和议题支持的路径。",
    results="态度一致性经价值契合与相似性提高同理心，少数身份经精细加工提高同理心；同理心通过态度关联议题支持。",
    limitations="人机议题倡导不等同虚构人物接收；摘要不足以核验量表、效应量和模型比较。",
    readingUse="用于价值契合、群体身份与同理心路径区分。",
    researchConnection="直接说明个人价值契合与群体身份线索可以走不同的心理路径，不应合成单一文化相似指标。"),
    "Zhao, X., & Ma, R. (2026). A social identity extension to CASA: How GenAI chatbots’ attitudinal congruence and group identity impact user empathy and issue support. International Journal of Human-Computer Interaction, 42, 11782–11797. https://doi.org/10.1080/10447318.2025.2594153",
    "人物价值契合主要经感知相似与同理心影响支持，文化群体身份则可能通过不同的精细加工路径作用。",
    "交叉操纵价值立场是否一致与人物是否被标记为中国文化内群体，检验两种线索是否独立或交互。",
    "分别测量具体价值契合、感知相似、群体归属、精细加工、同理心、认同与传播意向。",
    "它最清楚地把价值契合与群体身份拆成两条机制路径。")

translated = dissertation(paper(
    title="Reading without knowing: how authorship disclosure shapes ethical engagement with AI-translated literature",
    titleZh="在不知情中阅读：作者身份披露如何塑造对人工智能翻译文学的伦理参与",
    authors="Wenkang Zhang, Rui Xie, Jiaxing Hu", year=2026, venue="Ethics and Education, Online First",
    source="Ethics and Education", category="博士论文专题 · 相邻机制", url="https://doi.org/10.1080/10508422.2026.2696829",
    doi="https://doi.org/10.1080/10508422.2026.2696829", topicIds=["culture", "sycophancy"], publicationType="journal",
    publicationStatus="online-first", peerReviewed=True, publicationDate="2026-07-06", publicationDatePrecision="day",
    takeaway="混合方法研究比较读者对人译与人工智能翻译文学片段的同理反应。定量上情感、认知与联想同理及感知质量没有显著差异；质性材料显示投入主要由文本特征驱动，但考虑人工智能参与后，部分读者会基于机器能力归因重新评价。",
    theory="把作者来源披露、归因推理、解释自主性与文学同理投入结合。",
    data="人译与人工智能翻译文学片段的读者定量评分与开放反思；公开摘要没有报告样本量。",
    method="混合方法比较不同翻译来源条件下的多维同理与质量评价，并分析考虑人工智能参与后的反思性理由。",
    results="来源条件未造成多维同理或质量的显著定量差异，但披露可能通过归因推理改变部分读者的判断。",
    limitations="摘要未报告样本与具体文本配对；翻译来源与文化类比不是同一处理。",
    readingUse="用于来源披露、文本质量与接收结果的区分。",
    researchConnection="本国人物类比或文化注释可能同时改变文本与来源归因，需要设置只改解释框架而不改正文的条件。"),
    "Zhang, W., Xie, R., & Hu, J. (2026). Reading without knowing: How authorship disclosure shapes ethical engagement with AI-translated literature. Ethics and Education. https://doi.org/10.1080/10508422.2026.2696829",
    "解释来源披露可能不直接改变同理或质量，却通过归因推理改变后续评价，因而构成文化类比效果的边界条件。",
    "保持译文完全相同，只操纵人工翻译、人工智能翻译或未披露来源，并与本国人物类比交叉。",
    "测量情感、认知和联想同理、感知质量、来源归因、解释自主性和人物认同。",
    "它提醒实验者把文本本身的作用和受众对翻译来源的推断分开。")

general = paper(
    title="Redesigning algorithms to intervene on social norm misperceptions during a national election",
    titleZh="重新设计算法以干预全国选举期间的社会规范误知",
    authors="William J. Brady, Meriel Doyle, Abdo Elnakouri, Eli J. Finkel, Joshua Conrad Jackson, Nour Kteily, et al.",
    year=2026, venue="Nature, 655, 942–956", source="Nature", category="综合顶刊 · 社会科学研究",
    url="https://doi.org/10.1038/s41586-026-10536-1", doi="https://doi.org/10.1038/s41586-026-10536-1",
    topicIds=["methods"], publicationType="journal", publicationStatus="published", peerReviewed=True,
    publicationDate="2026-05-27", publicationDatePrecision="day", publicationDateSource="https://www.nature.com/articles/s41586-026-10536-1",
    socialScienceAssessment="confirmed", socialScienceReason="研究问题是算法信息暴露、群体规范误知与政治敌意，分析对象与主要结论均属于社会和行为科学。",
    takeaway="注册报告将2000名参与者随机分配到定制信息流，持续8周并覆盖2024年美国总统选举前后。参与度排序放大群际、道德化、情绪化和有毒内容，降低规范知觉准确性并提高感知党派敌意；降低极端用户影响的多样化算法减少这些扭曲，同时保持相近的平台愉悦。",
    theory="把算法排序视为社会规范知觉的干预环境，区分内容暴露、规范判断、敌意知觉和自身参与行为。",
    data="N=2000，持续8周，覆盖2024年美国总统选举前后。",
    method="预注册随机实验比较参与度排序、逆时间排序和多样化极端度算法，测量暴露、规范准确性、党派敌意和平台体验。",
    results="参与度排序放大高冲突内容并扭曲规范知觉；多样化算法降低极端内容影响且未明显损害平台愉悦。",
    limitations="美国选举情境和定制平台限制外部效度；算法对自身参与行为没有显著改变，不能把暴露效应等同实际行动。",
    readingUse="用于长期现场实验、规范知觉和多结果区分。",
    researchConnection="提示信息环境可改变受众对群体规范的判断，而不一定改变自身行为；博士论文应区分规范推断与传播意向。",
)

collection = {
    "journalId": "jcmc", "journalName": "Journal of Computer-Mediated Communication", "kind": "issue",
    "title": "Volume 31, Issue 6, November 2026 (In Progress) · 2026-11-09完整可见范围",
    "url": "https://academic.oup.com/jcmc/issue/31/6", "checkedAt": date, "complete": True,
    "toc": [
        {"title": "The sequential replicant effect in interpersonal sincerity: evidence from AI-mediated apology and gratitude", "url": "https://doi.org/10.1093/jcmc/zmag024", "articleType": "Full-length Research Article", "status": "previously-recommended", "recommendedDate": "2026-10-26", "reviewUrl": "./?date=2026-10-26"},
        {"title": "The link between three smartphone school policies and students’ mental health: a growth trajectory approach", "url": "https://doi.org/10.1093/jcmc/zmag025", "articleType": "Full-length Research Article", "status": "previously-recommended", "recommendedDate": "2026-10-26", "reviewUrl": "./?date=2026-10-26"},
    ],
}

groups = [
    {"id": "crossdisciplinary", "label": "其他研究", "target": 5, "sortBy": "split",
     "selectionBuckets": [{"id": "latest", "label": "最新", "target": 3},
                          {"id": "cited", "label": "重要研究精选", "target": 2, "sortBy": "relevance-quality",
                           "sortDescription": "Google Scholar受异常流量验证阻断后，按相关性和研究质量选择，不按引用量排名。", "accessFallback": fallback}],
     "sourceCoverage": [{"database": x, "status": "included"} for x in ["NBER", "SSRN", "arXiv"]],
     "sortDescription": "最新3篇按首次公开日期降序并各覆盖NBER、arXiv和SSRN；重要研究精选2篇按相关性和研究质量呈现。",
     "papers": cross},
    {"id": "journals", "label": "传播学与社会科学", "target": 5, "sortBy": "relevance-quality-date",
     "journalPriorityNote": "先执行不限期刊的主题检索。Google Scholar受阻后改用出版方发现，再筛传播学SSCI Q1/Q2；本期找到4篇满足永久去重、索引确认和高直接相关性的传播学论文，不以弱相关论文凑满5篇。",
     "sortDescription": "按博士论文直接相关性、传播学优先、理论质量与研究设计价值综合排序，不冒充引用次数排序。",
     "accessFallback": fallback, "papers": journals},
    {"id": "communication-issue", "label": "传播学顶刊推荐", "unit": "issue", "target": 0, "sortBy": "issue",
     "collection": collection, "sortDescription": "不使用关键词。JCMC第31卷第6期仍为In Progress，2026-11-09完整可见范围只有两篇研究论文，均已于2026-10-26推荐，因此本期不重复解读。", "papers": []},
    {"id": "general-science", "label": "综合顶刊推荐", "target": 1, "sortBy": "publicationDate",
     "rotationJournalId": "pnas", "selectedJournalId": "nature",
     "rotationFallback": {"reason": "PNAS公开最新目录未能稳定返回可逐篇核验且未推荐的社会科学候选；按既定轮换顺序检查Nature后，选出首篇可核验的未推荐社会科学研究。", "checkedAt": date,
                          "attempts": [{"journalId": "pnas", "status": "blocked", "reason": "公开目录检索未能取得可逐篇核验的当期社会科学候选，不绕过访问限制。"},
                                       {"journalId": "nature", "status": "selected", "reason": "出版方文章页可核验题录、日期、摘要、同行评审状态和研究设计。"}]},
     "sortDescription": "不使用主题关键词。PNAS目录核验受阻后按固定顺序转查Nature，选择首篇可核验且未推荐的社会科学研究。", "papers": [general]},
]

selected_refs = [almost["doi"], labels["doi"], nonbinary["doi"], norms["doi"], black_myth["doi"], casa["doi"], translated["doi"]]
specials = [black_myth, casa, translated]
all_count = sum(len(g["papers"]) for g in groups) + len(specials)
data = {
    "schemaVersion": 6, "date": date, "timezone": "Asia/Shanghai", "edition": "正式第37期",
    "title": "从文化标签到人物认同：拆开价值契合、道德判断与规范线索",
    "summary": "本期完成其他研究5篇、传播学主题期刊4篇、JCMC完整可见目录复核和Nature综合顶刊1篇，并新增博士论文同行评审专题3篇。",
    "historyPolicy": "exclude-recommended", "journalPolicy": "ssci-communication-q1-q2-and-social-science",
    "searchPlatforms": ["Google Scholar", "NBER", "SSRN", "arXiv"], "activeTopicIds": ["culture", "sycophancy", "methods"],
    "searchSettings": {"source": "defaults + reading-plan", "lookbackDays": 30, "conflictNote": "当日没有生效的一次性或持续用户设置。博士论文标准强化culture主题，但未删除culture、sycophancy和methods，也未改动未来设置。"},
    "notice": "逐篇依据官方记录、出版方页面及可访问正文核验。只有实际阅读正文关键部分才标全文核验；无法核验的样本、系数、识别和许可信息均明确说明。",
    "searchNote": "Google Scholar原生主题查询返回异常流量提示后停止，不绕过验证，也不以Web of Science、OpenAlex、下载量或网页指标冒充引用次数。其余候选由NBER、SSRN、arXiv官方记录与出版方发现并回到权威页面核验。",
    "shortfallReason": "传播学与社会科学主题栏目标5篇，实际4篇。Google Scholar被验证页阻断后，出版方回退发现的其余候选或已在永久历史中登记，或不在用户上传的传播学SSCI Q1/Q2范围，因此不凑数。JCMC当日完整可见范围的两篇研究均已推荐，没有重复登记。PNAS最新目录未能稳定取得可核验候选，按指南顺延至Nature。",
    "themeSearches": [
        {"platform": "Google Scholar", "query": "(\"cross-cultural reception\" OR \"value congruence\" OR \"narrative identification\" OR \"cultural familiarity\")", "timeRange": "2024年至今；检索日期2026-11-09", "purpose": "culture主题发现，随后筛期刊并核验引用次数", "status": "原生页面显示异常流量验证，未取得结果或引用次数，未绕过验证。"},
        {"platform": "Google Scholar", "query": "(sycophancy OR \"value alignment\" OR ingratiation OR \"opinion agreement\") AND (\"large language model\" OR chatbot OR \"conversational agent\")", "timeRange": "不限年份；检索日期2026-11-09", "purpose": "sycophancy主题发现", "status": "首次请求已触发站点级验证，因此未继续发送本主题请求，并启用指南规定的回退。"},
        {"platform": "Google Scholar", "query": "(\"causal inference\" OR \"panel data\" OR \"interrupted time series\" OR \"text measurement\") AND (communication OR \"digital platforms\" OR \"social media\")", "timeRange": "不限年份；检索日期2026-11-09", "purpose": "methods主题发现", "status": "首次请求已触发站点级验证，因此未继续发送本主题请求，并启用指南规定的回退。"},
        {"platform": "NBER", "query": "site:nber.org/papers November 2026 social connectivity communication protest", "timeRange": "优先近30日；检索日期2026-11-09", "purpose": "NBER候选发现", "status": "限定官方域名的公开网页检索成功，不冒称NBER站内高级检索；入选记录回到NBER官方页核验。"},
        {"platform": "SSRN", "query": "site:ssrn.com 2026 AI-mediated communication sycophancy value congruence", "timeRange": "优先近30日，必要时扩展至2026年；检索日期2026-11-09", "purpose": "SSRN候选发现", "status": "限定官方域名的公开网页检索成功；题录、首次张贴日期和摘要回到SSRN记录核验。"},
        {"platform": "arXiv", "query": "sycophancy AND (updating OR human interaction)", "timeRange": "2026-05-01至2026-11-09", "purpose": "arXiv候选发现", "status": "官方记录可读；题名、作者、首次提交日期、摘要和arXiv ID完成核验。"},
    ],
    "periodicalChecks": [
        {"platform": "Oxford Academic · Journal of Computer-Mediated Communication", "query": "Volume 31 Issue 6目录，不使用关键词", "timeRange": "检查日期2026-11-09", "purpose": "传播学顶刊轮换", "status": "官方In Progress目录完整可见两篇Full-length Research Articles，均为2026-10-26已推荐，未发现新研究论文。"},
        {"platform": "PNAS", "query": "最新在线目录，不使用关键词", "timeRange": "检查日期2026-11-09", "purpose": "综合顶刊轮换", "status": "公开目录未能稳定返回可逐篇核验且未推荐的社会科学候选，未绕过访问限制。"},
        {"platform": "Nature", "query": "最新在线社会科学候选，不使用主题关键词", "timeRange": "检查日期2026-11-09", "purpose": "综合顶刊顺序回退", "status": "出版方文章页核验成功，入选注册报告的题名、作者、日期、DOI、摘要和研究设计可核验。"},
    ],
    "verificationLog": [
        {"platform": "Google Scholar", "query": "当日主题检索与实际引用次数", "timeRange": "核验日期2026-11-09", "purpose": "主题发现与引用排序", "status": "首次原生查询显示异常流量验证后停止；没有绕过验证、记录虚构0次引用或用其他指标替代。"},
        {"platform": "NBER、SSRN与arXiv官方记录", "query": "其他研究5篇的身份、首次公开日期、摘要与版本", "timeRange": "核验日期2026-11-09", "purpose": "逐篇核验与跨版本去重", "status": "5篇均完成题录和摘要核验，并与截至2026-11-08的473条永久登记去重。"},
        {"platform": "出版方官网", "query": "期刊题名、作者、年份、期刊、同行评审状态、DOI、日期、摘要、样本与方法", "timeRange": "核验日期2026-11-09", "purpose": "主题期刊、博士论文专题与轮换栏目逐篇核验", "status": "8篇新期刊论文完成身份核验；只写入公开证据支持的研究细节，未知细节明确标示。"},
    ],
    "groups": groups, "coreTracking": [],
    "coreTrackingNote": "reading-plan与core-papers当日没有用户提交的核心论文请求，因此本期没有核心文献状态更新。",
    "periodicalCheckNote": "两个轮换栏目均不使用主题关键词。JCMC完整可见目录没有新论文；PNAS访问核验受阻后按既定顺序选择Nature候选。",
    "dissertation": {
        "title": "从被看见到被接收",
        "timeRange": "优先检查2026-11-08上期发布以来的新发表研究。直接相关新论文不足后扩展至2025年12月至2026年尚未推荐的同行评审研究；较早论文作为补充，不冒称当日最新。",
        "selectionNote": "本期精选7篇同行评审论文，其中4篇在传播学主题栏、3篇在博士论文专题区完整解读。重点覆盖价值契合与群体身份的分离、最小文化标签、人物道德分类、叙事规范线索、外国媒体对中国神话游戏的接收以及翻译来源归因。",
        "historyCoverage": "已核对网站截至2026-11-08的473条永久登记、现有简报、用户明确列出的既有文献、本轮可见对话及可访问清单，并按DOI、arXiv ID、规范化题名和已知版本别名去重。无法访问的完整旧对话和未同步私人清单不在覆盖范围内，因此不声称绝对完全去重。",
        "selectedPapers": selected_refs, "papers": specials,
        "topPapers": [
            {"doi": almost["doi"], "reason": "直接把群体边界、人物道德评价、道德脱离和人物认同放入同一受众研究，最接近论文的核心因果结构。"},
            {"doi": casa["doi"], "reason": "把个人价值契合与群体身份拆成两条心理路径，最适合据此建立价值契合与文化边界的调节模型。"},
            {"doi": black_myth["doi"], "reason": "直接提供德国媒体对中国神话游戏的接收证据，并清楚显示制作好感、叙事理解与文化可及性不能互相替代。"},
        ],
    },
}

(root / f"{date}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
index_path = root / "index.json"
index = [x for x in json.loads(index_path.read_text()) if x["date"] != date]
index.insert(0, {"date": date, "title": data["title"], "summary": data["summary"], "edition": data["edition"], "count": all_count, "file": f"{date}.json"})
index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state_path = root / "rotation-state.json"
state = json.loads(state_path.read_text()); state["updatedAt"] = date
jcmc = state["communication"]["jcmc"]
jcmc.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date,
            reason="Official Volume 31 Issue 6 In Progress directory was fully readable on 2026-11-09 and contained the same two research articles already recommended on 2026-10-26; no new paper was added.")
jcmc_observation = jcmc.get("directoryObservation", {})
jcmc_observation.update({"journalId": "jcmc", "journalName": collection["journalName"], "kind": "issue", "title": collection["title"], "url": collection["url"], "checkedAt": date, "complete": True, "reportedTotal": 2, "observedCount": 2, "scopeNote": "Complete public scope visible on 2026-11-09; both articles were previously recommended."})
jcmc["directoryObservation"] = jcmc_observation
jcmc["completedIssues"] = [x for x in jcmc.get("completedIssues", []) if x.get("checkedAt") != date]
jcmc["completedIssues"].append({"checkedAt": date, "url": collection["url"], "title": collection["title"], "complete": True, "dois": ["https://doi.org/10.1093/jcmc/zmag024", "https://doi.org/10.1093/jcmc/zmag025"]})
pnas = state["general"]["pnas"]
pnas.update(lastAttemptAt=date, lastCheckedAt=date, status="blocked", reason="PNAS public latest directory did not yield a stable article-level set of un-recommended social-science candidates; no cursor was advanced.")
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
print(f"Wrote {date} with {all_count} papers")
