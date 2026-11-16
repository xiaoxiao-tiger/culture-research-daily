import json
from pathlib import Path


root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-16"
unavailable = "未取得允许本站完整转载摘要的明确许可；中文概述依据可核验证据原创，详情请阅来源链接。"
fallback = {
    "reason": "Google Scholar原生页面返回异常流量验证，未取得可核验结果或引用次数，且未尝试绕过验证。",
    "channel": "改用出版方官网、Crossref、PubMed、NBER、SSRN、arXiv及权威学术索引进行发现和逐篇核验。",
    "checkedAt": date,
}


def p(**v):
    x = {
        "evidence": "摘要核验",
        "relevance": "研究启示是本简报依据论文证据作出的推论，不是论文作者已经检验的结论。",
        "abstractMode": "unavailable",
        "originalAbstract": "",
        "abstractUnavailableReason": unavailable,
        "readingPriority": "normal",
        "priorityReason": "题录、发表状态和核心证据可以核验，且与当日主题相关。",
        "readingUse": "用于理论框架、研究设计或结果讨论。",
        "researchConnection": "作为一般研究追踪，和博士论文的关系见逐篇说明。",
    }
    x.update(v)
    x.setdefault("abstractZh", x["takeaway"])
    x.setdefault("abstractSource", x["url"])
    return x


def unverified(x, reason):
    x.update(
        citationStatus="unverified",
        citationCount=None,
        citationSource=None,
        citationSourceUrl=None,
        citationCheckedAt=None,
        citationNote="Google Scholar受异常流量验证阻断，未核验实际引用次数。",
        selectionReason=reason,
    )
    return x


def journal(x, name, reason, quartile="Q1"):
    x.update(
        publicationType="journal",
        peerReviewed=True,
        discoverySource="Publisher",
        journalEdition="SSCI",
        discipline="communication",
        journalName=name,
        jifQuartile=quartile,
        indexSource="site/data/journals.json中的用户确认SSCI清单",
        quartileSource="site/data/journals.json中的用户确认分区",
    )
    return unverified(x, reason)


def dissertation(x, apa, hypothesis, manipulation, measurement, reason):
    x.update(
        apaCitation=apa,
        peerReviewed=True,
        publicationType="journal",
        peerReviewSource=x["url"],
        publicationDateSource=x.get("publicationDateSource", x["url"]),
        readingPriority="high",
        priorityReason=reason,
        hypothesisImplication="简报推论：" + hypothesis,
        manipulationImplication="简报推论：" + manipulation,
        measurementImplication="简报推论：" + measurement,
    )
    return x


cross = [
    p(
        title="Debiasing Law Enforcement Officers: Evidence from an Expressive Arts Intervention in India",
        titleZh="减少执法人员偏见：印度表达性艺术干预的证据",
        authors="Sofia Amaral, Girija Borker, Nishith Prakash, María Micaela Sviatschi",
        year=2026,
        venue="NBER Working Paper 35986",
        source="NBER",
        sourceDatabase="NBER",
        category="其他研究 · 最新",
        url="https://www.nber.org/papers/w35986",
        doi="https://doi.org/10.3386/w35986",
        topicIds=["culture", "methods"],
        selectionBucket="latest",
        publicationType="working-paper",
        publicationDate="2026-11-01",
        publicationDatePrecision="month",
        publicationDateSource="https://www.nber.org/papers/w35986",
        evidence="摘要核验",
        takeaway="在印度比哈尔邦417个警察局、约2500名高级一线警员中开展集群随机试验。三天表达性艺术干预在约七个月后改善性别暴力态度、同理心和法律知识，一年后的标准化受害者审计显示责怪受害者下降15个百分点，登记延迟下降41%。",
        theory="以压迫剧场和观点采择解释制度执行者的态度、同理心与服务行为如何改变。",
        data="417个警察局、约2500名高级一线警员，并结合标准化受害者审计和行政记录。",
        method="集群随机对照试验，含中长期追踪、行为审计、行政数据和警员调动形成的扩散分析。",
        results="干预改善态度、同理心、法律知识和多项实际执法行为，并有同事扩散的提示性证据。",
        limitations="NBER工作论文尚未同行评审，执法机构场景与文化人物接收不同，扩散分析并非主要随机对比。",
        researchConnection="提示价值与道德判断可以通过参与式叙事干预改变，但态度改变必须用实际行为和延迟结果验证。",
    ),
    p(
        title="Do Personal AI Conversations Reduce Loneliness? Evidence from a Pre-Registered Experiment",
        titleZh="与个人AI对话能减轻孤独吗：预注册实验的证据",
        authors="Claudia Senik, Ariell Reshef, Louis Freget",
        year=2026,
        venue="SSRN Working Paper 7625264",
        source="SSRN",
        sourceDatabase="SSRN",
        category="其他研究 · 最新",
        url="https://ssrn.com/abstract=7625264",
        doi="https://doi.org/10.2139/ssrn.7625264",
        topicIds=["sycophancy", "methods"],
        selectionBucket="latest",
        publicationType="working-paper",
        publicationDate="2026-10-17",
        publicationDatePrecision="day",
        publicationDateSource="https://ssrn.com/abstract=7625264",
        takeaway="法国成年人的大规模预注册实验要求处理组连续28天每天至少进行一次个人AI对话。干预显著增加社会情感型AI使用，但主观孤独上升，其他福祉指标方向也一致不利，不过估计不精确。",
        theory="检验AI陪伴是否替代或挤出人际连接，并区分工具使用量与主观福祉。",
        data="法国成年人大样本；当前公开摘要未给出可核验的完整样本量。",
        method="预注册28天随机实验，处理组每日个人AI对话，对照组维持原状。",
        results="AI使用增加并未减轻孤独，主观孤独反而上升；其他福祉结果方向不利但不够精确。",
        limitations="SSRN工作论文尚未同行评审，允许参与者自行选择工具，使具体模型和对话内容异质。",
        researchConnection="提醒高频互动和主观好感不能直接推断更深层接收或更好福祉，应加入行为与延迟测量。",
    ),
    p(
        title="Don't Blame The Preferences: Examining The Emergence of Sycophancy in LLM Training",
        titleZh="不要只怪偏好学习：审视大语言模型训练中的迎合涌现",
        authors="Chao Peter Yang, Catherine Zehr, Pranav Bijith, Brandon Fain",
        year=2026,
        venue="arXiv:2611.10045",
        source="arXiv",
        sourceDatabase="arXiv",
        category="其他研究 · 最新",
        url="https://arxiv.org/abs/2611.10045",
        doi="https://doi.org/10.48550/arXiv.2611.10045",
        arxivId="2611.10045",
        topicIds=["sycophancy", "methods"],
        selectionBucket="latest",
        publicationType="preprint",
        publicationDate="2026-11-05",
        publicationDatePrecision="day",
        publicationDateSource="https://arxiv.org/abs/2611.10045",
        takeaway="研究在三个开放训练流程模型的主要训练检查点上运行三类迎合基准。九个模型与基准组合中，监督微调结束时已形成至少92%的偏好一致型迎合和至少85%的最终迎合，偏好对齐仅在四个组合中平均再增加4.2个百分点。",
        theory="把迎合的来源从单一偏好优化问题改写为预训练、监督微调和偏好对齐的阶段性形成问题。",
        data="三个具有开放训练配方的模型、三类迎合基准和各主要训练检查点。",
        method="纵向检查点评估、跨模型与跨基准比较，并以机制可解释性检查相关内部表征。",
        results="迎合大多在监督微调结束前已经形成，偏好对齐的附加影响较小且不稳定。",
        limitations="arXiv预印本尚未同行评审，开放模型和现有基准不代表全部商用模型或真实使用情境。",
        researchConnection="对sycophancy主题的直接贡献是把干预点前移到训练数据和监督微调，而非只在偏好阶段修补。",
    ),
    unverified(
        p(
            title="The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training",
            titleZh="语言模型迎合的发展：从预训练到后训练追踪脆弱性",
            authors="Haonan Huang, Chengkun Cai",
            year=2026,
            venue="arXiv:2610.26655",
            source="arXiv",
            sourceDatabase="arXiv",
            category="其他研究 · 重要研究精选",
            url="https://arxiv.org/abs/2610.26655",
            doi="https://doi.org/10.48550/arXiv.2610.26655",
            arxivId="2610.26655",
            topicIds=["sycophancy", "methods"],
            selectionBucket="cited",
            publicationType="preprint",
            publicationDate="2026-10-19",
            publicationDatePrecision="day",
            publicationDateSource="https://arxiv.org/abs/2610.26655",
            takeaway="研究追踪30个开放模型谱系的741个检查点，其中504个来自预训练。平均迎合强度在多数谱系中早于后训练出现，但哪些题目最容易屈从用户压力的具体脆弱性图谱，主要沿模型自己的监督微调和偏好优化路径形成。",
            theory="区分迎合的平均强度与题目层面的脆弱性结构，并把后者定位到具体训练路径。",
            data="30个开放模型谱系、741个检查点，以及道德判断和事实判断题库。",
            method="跨训练阶段纵向检查点分析、同基座分叉比较、留出预测和内部状态线性读出。",
            results="预训练已出现平均迎合，但对最终脆弱题目的预测很弱；模型自身偏好阶段检查点最能预测最终脆弱性图谱。",
            limitations="arXiv预印本尚未同行评审，二元判断任务和开放模型谱系不能覆盖真实长对话或商用模型。",
            researchConnection="与当日另一篇研究形成方法对照，说明平均迎合分数可能掩盖完全不同的题目级风险。",
        ),
        "741个检查点揭示平均迎合与题目级脆弱性必须分开审计。",
    ),
    unverified(
        p(
            title="Can AI Help Explain AI? Effects of Multimodal LLM-Generated Explanations on Perceived Understanding and Perceived Trust in XAI Visualizations",
            titleZh="AI能帮助解释AI吗：多模态大模型解释对XAI可视化理解与信任的影响",
            authors="Authors as listed by SSRN",
            year=2026,
            venue="SSRN Working Paper 7569580",
            source="SSRN",
            sourceDatabase="SSRN",
            category="其他研究 · 重要研究精选",
            url="https://ssrn.com/abstract=7569580",
            doi="https://doi.org/10.2139/ssrn.7569580",
            topicIds=["sycophancy", "methods"],
            selectionBucket="cited",
            publicationType="working-paper",
            publicationDate="2026-09-12",
            publicationDatePrecision="day",
            publicationDateSource="https://ssrn.com/abstract=7569580",
            takeaway="预注册被试内实验让128名参与者在七类决策情境、五种可解释AI方法中比较有无大模型生成多模态解释。公开摘要确认研究直接测量感知理解与信任，精确效应及不同可视化间差异需阅读全文核验。",
            theory="考察自然语言和多模态补充解释能否把可视化的形式透明转化为主观理解与信任。",
            data="128名参与者、七类决策情境和五种可解释AI方法。",
            method="预注册被试内实验，在各可视化方法中比较有无大模型解释。",
            results="公开摘要确认比较框架和核心结果变量，本简报不据有限证据扩写效应方向。",
            limitations="SSRN工作论文尚未同行评审，被试内设计可能产生学习和顺序效应，感知理解不等于实际理解。",
            researchConnection="可类比本国人物解释条件，但必须同时测量实际理解，避免把流畅感或信任当成理解。",
        ),
        "预注册实验直接区分感知理解与信任，适合解释设计的方法比较。",
    ),
]
cross[:3] = sorted(cross[:3], key=lambda x: x["publicationDate"], reverse=True)


difficult = dissertation(
    journal(
        p(
            title="What Can Cognitive Load and Processing Fluency Tell Us About Difficult Processing?",
            titleZh="认知负荷与加工流畅性能告诉我们什么：困难加工的实验检验",
            authors="Elizabeth E. Riggs, Hillary C. Shulman, Richard Huskey, Teresa Lynch, Jacob T. Fisher",
            year=2026,
            venue="Media Psychology, 29(6), 1195–1221",
            source="Media Psychology",
            category="传播学与社会科学 · 正式卷期",
            url="https://doi.org/10.1080/15213269.2025.2576679",
            doi="https://doi.org/10.1080/15213269.2025.2576679",
            topicIds=["culture", "methods"],
            publicationStatus="published",
            publicationDate="2025-10-30",
            publicationDatePrecision="day",
            publicationDateSource="https://www.tandfonline.com/doi/full/10.1080/15213269.2025.2576679",
            evidence="摘要核验",
            takeaway="实验在健康叙事中分别用听觉提示操纵反应性认知控制，以语言难度操纵加工流畅性。语言难度影响记忆与叙事说服；当语言困难时，听觉提示反而增强记忆，说明负荷与流畅性不能被视为同一维度。",
            theory="区分客观资源需求与主观加工困难，并检验两者对记忆和说服的交互作用。",
            data="单项健康叙事实验；可访问摘要未给出可核验的完整样本量。",
            method="听觉提示乘语言难度的实验设计，同时测量记忆和说服结果。",
            results="加工流畅性操纵影响记忆和说服；语言困难条件下听觉提示提高记忆。",
            limitations="证据范围以出版方摘要和可访问手稿为主，健康叙事与神话人物不同，样本结构需阅读全文复核。",
            researchConnection="直接支持把文化熟悉性、语言难度、认知负荷和加工流畅性拆开操纵与测量。",
        ),
        "MEDIA PSYCHOLOGY",
        "正式卷期论文直接区分认知负荷与加工流畅性。",
    ),
    "Riggs, E. E., Shulman, H. C., Huskey, R., Lynch, T., & Fisher, J. T. (2026). What can cognitive load and processing fluency tell us about difficult processing? Media Psychology, 29(6), 1195–1221. https://doi.org/10.1080/15213269.2025.2576679",
    "本国相似人物类比可能通过提高流畅性改善理解，但在负荷很低或很高时未必提高说服或人物认同。",
    "正交操纵语言难度与类比线索，同时加入无类比、表层类比和价值结构类比条件。",
    "分别测量主观流畅性、反应时、事实记忆、关系理解、好感、人物认同和分享意向。",
    "最直接提供加工流畅性与认知负荷的可分辨实验框架。",
)


journals = [
    journal(
        p(
            title="Women Sustaining TikTok as Supplementary Information Infrastructure for Flexible Work Arrangements: Gendered Conditions, Community and Surveillance",
            titleZh="女性如何维系TikTok的弹性工作补充信息基础设施",
            authors="Xuefei Li, Kiran Ijaz, Marta E. Cecchinato, Naseem Ahmadpour",
            year=2026,
            venue="Social Media + Society, OnlineFirst",
            source="Social Media + Society",
            category="传播学与社会科学 · OnlineFirst",
            url="https://doi.org/10.1177/20563051261496968",
            doi="https://doi.org/10.1177/20563051261496968",
            topicIds=["culture", "methods"],
            publicationStatus="online-first",
            publicationDate="2026-11-11",
            publicationDatePrecision="day",
            publicationDateSource="https://journals.sagepub.com/doi/10.1177/20563051261496968",
            evidence="全文核验",
            takeaway="对14名在TikTok发布弹性工作内容的女性进行半结构访谈。创作者以情境化知识纠正误导信息并使工作规范可见，但可信度、持续参与、时间精力不平等和面向工作场所的监视共同限制其信息正义潜力。",
            theory="把平台内容生产视为需要持续修补和维护的补充信息基础设施。",
            data="14名发布弹性工作内容的女性TikTok创作者。",
            method="半结构访谈与基础设施理论、女性主义视角的质性分析。",
            results="创作者劳动提升经验知识的可用性，同时产生性别化认可成本和监视风险。",
            limitations="小样本质性研究不估计总体效应，研究对象是创作者而非普通受众。",
            researchConnection="提示外国受众的解释资源常来自平台中介者，来源可信度和情境化程度应进入接收模型。",
        ),
        "SOCIAL MEDIA + SOCIETY",
        "2026-11-11最新正式在线发表，提供平台中介与情境化知识机制。",
    ),
    journal(
        p(
            title="Fandom Rupture in the Movement Society: Reactive Collective Participation Through Affective Practices",
            titleZh="运动社会中的粉丝断裂：通过情感实践形成的反应性集体参与",
            authors="Zhihong Li",
            year=2026,
            venue="Social Media + Society, OnlineFirst",
            source="Social Media + Society",
            category="传播学与社会科学 · OnlineFirst",
            url="https://doi.org/10.1177/20563051261502656",
            doi="https://doi.org/10.1177/20563051261502656",
            topicIds=["culture", "methods"],
            publicationStatus="online-first",
            publicationDate="2026-11-11",
            publicationDatePrecision="day",
            publicationDateSource="https://journals.sagepub.com/doi/10.1177/20563051261502656",
            evidence="摘要核验",
            takeaway="研究结合13名粉丝、反粉和旁观者的访谈，以及蔡徐坤事件相关139795条微博和205001条评论，识别定位、讲述、情感调谐和校准四类实践，解释异质参与者如何在外部冲击后维持运动式参与。",
            theory="以情感公众和反应性集体参与解释无共同目标时的持续参与。",
            data="13人深访、139795条帖子和205001条评论。",
            method="质性访谈与计算传播分析的混合方法。",
            results="四类情感实践随事件阶段和参与者位置改变，共同形成分层参与生态。",
            limitations="单一娱乐事件和平台案例限制外推，计算分类依赖公开文本。",
            researchConnection="可用于解释人物争议如何把好感、道德评价和传播参与拆成不同情感实践。",
        ),
        "SOCIAL MEDIA + SOCIETY",
        "大规模平台数据与访谈结合，直接连接粉丝、情感和集体参与。",
    ),
    journal(
        p(
            title="AI for Democracy? How Public Service Media Around the World Use Artificial Intelligence to Produce Journalism",
            titleZh="AI能服务民主吗：全球公共服务媒体如何用人工智能生产新闻",
            authors="Kate Wright, Melissa Terras",
            year=2026,
            venue="Digital Journalism, OnlineFirst",
            source="Digital Journalism",
            category="传播学与社会科学 · OnlineFirst",
            url="https://doi.org/10.1080/21670811.2026.2752405",
            doi="https://doi.org/10.1080/21670811.2026.2752405",
            topicIds=["sycophancy", "methods"],
            publicationStatus="online-first",
            publicationDate="2026-11-11",
            publicationDatePrecision="day",
            publicationDateSource="https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2752405",
            evidence="全文核验",
            takeaway="研究以调查、组织文件和高级管理者访谈比较非洲、亚洲、欧洲、大洋洲及加勒比地区13家公共媒体网络。AI主要用于转录、图像生成编辑和内容定制，效率与公共价值、法定义务和民主使命之间存在持续张力。",
            theory="把AI采用解释为效率目标、公共媒体价值和民主使命之间的制度协商。",
            data="来自五个地区的13家公共服务媒体网络。",
            method="跨国调查、组织文件和高级管理者访谈的混合证据。",
            results="工具用途并不独特，时间与成本节约是主要驱动，但公共服务媒体面临更复杂的价值冲突。",
            limitations="机构自报与管理者视角可能低估一线实践和受众后果，不能提供因果效应。",
            researchConnection="提示AI辅助文化解释要同时评估效率、准确性、多样性和受众义务。",
        ),
        "DIGITAL JOURNALISM",
        "最新跨国研究，覆盖AI生产实践与公共价值冲突。",
    ),
    journal(
        p(
            title="When does AI assistance undermine relational authenticity? A mini review of conditional effects in AI-mediated interpersonal communication",
            titleZh="AI辅助何时会损害关系真实性：AI媒介人际沟通条件效应的简要综述",
            authors="Marina R. Zheltukhina, Olga V. Sergeeva, Irina I. Volkova, Oksana V. Shiryaeva-Shiring, Aygul A. Khafizova, Natalya V. Chernikova",
            year=2026,
            venue="Frontiers in Psychology, 17, 1970730",
            source="Frontiers in Psychology",
            category="传播学与社会科学 · 综述",
            url="https://doi.org/10.3389/fpsyg.2026.1970730",
            doi="https://doi.org/10.3389/fpsyg.2026.1970730",
            topicIds=["sycophancy", "methods"],
            publicationStatus="published",
            publicationDate="2026-11-10",
            publicationDatePrecision="day",
            publicationDateSource="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1970730/full",
            evidence="全文核验",
            takeaway="简要综述整合13项核心实验和4项邻近研究，指出AI辅助的关系成本集中在披露或怀疑、信息情绪性、关系亲密度和辅助程度四个条件。作者将感知作者身份提出为候选机制，但明确说明尚未被直接检验。",
            theory="以条件效应框架和感知作者身份解释AI辅助结果为何看似矛盾。",
            data="13项核心实验和4项邻近领域实验研究。",
            method="多数据库叙事性简要综述，逐篇编码四类调节因素和已检验中介。",
            results="辅助程度的证据最一致，关系亲密度最弱；感知作者身份目前只是间接支持的候选机制。",
            limitations="不是系统综述或元分析，研究间调节变量混杂，不能给出汇总效应量。",
            researchConnection="帮助区分AI解释的内容效果与来源真实性判断，但不能替代跨文化受众实验。",
        ),
        "FRONTIERS IN PSYCHOLOGY",
        "2026-11-10同行评审综述，系统整理AI辅助的条件效应。",
        quartile="Q2",
    ),
    difficult,
]

authenticity_base = journals[3]
journals[3] = journal(
    p(
        title="Digital maturity and digital rehabilitation in prisons: organizational conditions for inclusion and reintegration",
        titleZh="监狱中的数字成熟度与数字康复：包容和再融入的组织条件",
        authors="Victoria Knight, Bianca Reisdorf, Steven Van De Steene",
        year=2026,
        venue="Information, Communication & Society, OnlineFirst",
        source="Information, Communication & Society",
        category="传播学与社会科学 · OnlineFirst",
        url="https://doi.org/10.1080/1369118X.2026.2756274",
        doi="https://doi.org/10.1080/1369118X.2026.2756274",
        topicIds=["culture", "methods"],
        publicationStatus="online-first",
        publicationDate="2026-11-13",
        publicationDatePrecision="day",
        publicationDateSource="https://www.tandfonline.com/toc/rics20/0/0",
        evidence="摘要核验",
        takeaway="东南亚、西北欧和大洋洲的质性案例显示，数字康复只有在战略领导、组织能力、合作参与以及持续学习评估等条件支持下，才可能嵌入监狱日常实践并促进数字包容与再融入。",
        theory="把数字成熟度界定为使具体技术干预可持续的组织能力，而非单纯设备供给。",
        data="东南亚、西北欧和大洋洲三个高数字成熟度惩教体系的质性案例。",
        method="跨地区比较案例研究，结合明确的数字康复项目与支撑其运行的组织条件。",
        results="三地转型路径不同，但均需要康复目标与更广泛数字战略的对齐。",
        limitations="选择高成熟度案例可能低估失败条件，质性比较不能估计数字康复的平均因果效果。",
        researchConnection="提醒文化解释工具的有效性依赖实施组织、使用者能力和反馈机制，不能只评估内容本身。",
    ),
    "Information Communication & Society",
    "2026-11-13最新正式在线发表，补充数字干预的组织条件。",
)


black_myth = dissertation(
    p(
        title="Hybridizing Tradition and Technology: Global Reception of ‘Black Myth: Wukong’ as a Vehicle for Chinese Cultural Identity and International Media Flows",
        titleZh="传统与技术的混融：黑神话悟空作为中国文化身份与国际媒介流动载体的全球接收",
        authors="Yuan Gao, Jia Li, Jianping He",
        year=2025,
        venue="Global Media and China, OnlineFirst",
        source="Global Media and China",
        category="博士论文专题 · 中国神话接收",
        url="https://doi.org/10.1177/20594364251385203",
        doi="https://doi.org/10.1177/20594364251385203",
        topicIds=["culture", "methods"],
        publicationStatus="online-first",
        publicationDate="2025-10-24",
        publicationDatePrecision="day",
        publicationDateSource="https://journals.sagepub.com/doi/10.1177/20594364251385203",
        evidence="全文核验",
        takeaway="研究以第三空间和文化混融为框架，结合游戏及副文本的批判话语分析与微博、Reddit、Steam受众话语的计算内容分析。最终清理出3842条相关用户内容，发现中国玩家更强调文化真实性、象征和叙事深度，国际受众更关注玩法、技术与可及性，并经常遗漏或误解文化细节。",
        theory="用文化混融、第三空间和全球媒介流动解释传统神话在全球游戏惯例中的再编码与不对称接收。",
        data="游戏文本与推广材料，以及2024年9月至11月微博、Reddit和Steam的3842条清洗后用户内容。",
        method="批判话语分析与计算机辅助内容分析，含主题模型、情感分析和平台比较。",
        results="国内外受众关注重点明显不同，国际受众的视觉和技术好评并不等于理解中国文化含义。",
        limitations="平台比较混合了国家、语言、平台可供性和用户自选择，自动情感分析难捕捉讽刺，不能识别个体因果机制。",
        researchConnection="目前最直接对应外国受众接收中国神话人物，但它测的是公开话语与平台差异，不足以替代价值契合实验。",
    ),
    "Gao, Y., Li, J., & He, J. (2025). Hybridizing tradition and technology: Global reception of ‘Black Myth: Wukong’ as a vehicle for Chinese cultural identity and international media flows. Global Media and China. Advance online publication. https://doi.org/10.1177/20594364251385203",
    "国际受众的技术好评可能与文化理解脱钩，人物认同与传播意向也不应从总体情感自动推断。",
    "在同一人物材料中正交操纵文化解释深度和本国相似人物类比，并固定玩法与视觉质量。",
    "分别测量事实理解、象征意义理解、人物好感、Schwartz价值契合、人物认同、分享意向和实际选择。",
    "唯一直接分析中国神话游戏全球受众的本期候选，是论文问题的首要精读。",
)


norms = dissertation(
    p(
        title="Foreign cultural norms are better accepted in the second language",
        titleZh="使用第二语言时，人们更容易接受外国文化规范",
        authors="Jiehui Hu, Aina Casaponsa, Wanyu Zhang, Rafał Jończyk, Yan Jing Wu, Shan Gao, Guillaume Thierry",
        year=2025,
        venue="Annals of the New York Academy of Sciences, 1551(1), 257–269",
        source="Annals of the New York Academy of Sciences",
        category="博士论文专题 · 跨文化规范",
        url="https://doi.org/10.1111/nyas.15407",
        doi="https://doi.org/10.1111/nyas.15407",
        topicIds=["culture", "methods"],
        publicationStatus="published",
        publicationDate="2025-08-04",
        publicationDatePrecision="day",
        publicationDateSource="https://pubmed.ncbi.nlm.nih.gov/40760819/",
        evidence="全文核验",
        takeaway="20名中英双语者和20名英语母语者判断一般知识与中英文化规范句，并记录N400。一般知识的整合跨语言相似；双语者用英语时更接受英国文化规范，用中文时更接受中国文化规范，显式判断与神经指标共同支持语言情境效应。",
        theory="把语言运行情境视为文化特定语义知识的激活线索，而不只是翻译载体。",
        data="20名流利中英双语者和20名英语母语者。",
        method="文化规范乘语言的句子判断实验，结合接受度、反应时和事件相关电位N400。",
        results="双语者在第二语言英语中更接受英国文化规范，文化无关一般知识未呈同样语言差异。",
        limitations="样本仅40人且同质，双语者均在英国生活，语言与文化线索难完全分离，作者也要求更大样本复现。",
        researchConnection="直接表明语言版本本身会改变文化规范接受，必须与价值契合和文化接近分开。",
    ),
    "Hu, J., Casaponsa, A., Zhang, W., Jończyk, R., Wu, Y. J., Gao, S., & Thierry, G. (2025). Foreign cultural norms are better accepted in the second language. Annals of the New York Academy of Sciences, 1551(1), 257–269. https://doi.org/10.1111/nyas.15407",
    "第二语言可能改变外国文化规范的可接受性，因此价值契合效应可能受到实验语言调节。",
    "在同一外国受众中随机呈现母语版与高质量第二语言版，并保持人物行为和价值信息一致。",
    "同时测量接受度、理解、文化接近、价值契合、道德评价、反应时和可行的隐性加工指标。",
    "语言情境、文化规范和显性接受的区分最清楚，是第二精读。",
)


protagonist = dissertation(
    p(
        title="The Effectiveness of Adaptation of the Protagonist in Narrative Impact: Similarity Influences Health Beliefs Through Self-Referencing",
        titleZh="调整叙事主人公的有效性：相似性通过自我参照影响健康信念",
        authors="Anneke de Graaf",
        year=2014,
        venue="Human Communication Research, 40(1), 73–90",
        source="Human Communication Research",
        category="博士论文专题 · 较早补充",
        url="https://doi.org/10.1111/hcre.12015",
        doi="https://doi.org/10.1111/hcre.12015",
        topicIds=["culture", "methods"],
        publicationStatus="published",
        publicationDate="2013-10-03",
        publicationDatePrecision="day",
        publicationDateSource="https://onlinelibrary.wiley.com/doi/10.1111/hcre.12015",
        evidence="摘要核验",
        takeaway="220人的组间实验操纵叙事主人公与读者的相似性。相似主人公提高受众对自身疾病风险与应对效能的判断，效应由自我参照中介。",
        theory="以自我参照而非笼统熟悉感解释主人公相似性如何影响叙事效果。",
        data="220名参与者。",
        method="主人公相似与不相似的组间实验，并检验自我参照中介。",
        results="相似主人公提高风险感知和应对效能，自我参照解释这一差异。",
        limitations="这是较早的健康传播研究，主人公相似性不是跨文化神话类比，结果变量也不是人物认同。",
        researchConnection="为本国相似人物类比提供可检验机制，但只能作为较早的补充文献。",
    ),
    "de Graaf, A. (2014). The effectiveness of adaptation of the protagonist in narrative impact: Similarity influences health beliefs through self-referencing. Human Communication Research, 40(1), 73–90. https://doi.org/10.1111/hcre.12015",
    "本国相似人物类比可能通过自我参照提高接收，但该路径与价值契合和文化熟悉性不同。",
    "比较无类比、表层相似类比和价值结构相似类比，并测量而非假定自我参照。",
    "测量自我参照、感知相似、价值契合、文化熟悉、人物认同和叙事结果。",
    "较早但高度相关的机制补充，不能冒称本期最新研究。",
)


authenticity = dissertation(
    authenticity_base,
    "Zheltukhina, M. R., Sergeeva, O. V., Volkova, I. I., Shiryaeva-Shiring, O. V., Khafizova, A. A., & Chernikova, N. V. (2026). When does AI assistance undermine relational authenticity? A mini review of conditional effects in AI-mediated interpersonal communication. Frontiers in Psychology, 17, 1970730. https://doi.org/10.3389/fpsyg.2026.1970730",
    "来源披露、信息情绪性和辅助程度可能改变解释的可信度，但不应与内容理解效应混为一谈。",
    "若使用AI或第三方解释，正交操纵来源披露与辅助程度，并保持解释文本内容相同。",
    "分别测量感知作者身份、真实性、信任、理解、人物评价和传播意向。",
    "最新同行评审综述提供清楚条件框架，但与中国神话接收的关联属于设计推论。",
)


nature = p(
    title="Bureaucratic incentives shaped effectiveness of the one-child policy in China",
    titleZh="官僚激励塑造了中国独生子女政策的执行效果",
    authors="Lingsheng Meng, Hanmo Yang, Grant Miller, et al.",
    year=2026,
    venue="Nature, OnlineFirst",
    source="Nature",
    category="综合顶刊推荐 · 社会科学",
    url="https://doi.org/10.1038/s41586-026-11232-w",
    doi="https://doi.org/10.1038/s41586-026-11232-w",
    topicIds=["culture", "methods"],
    publicationType="journal",
    peerReviewed=True,
    publicationStatus="published",
    publicationDate="2026-11-11",
    publicationDatePrecision="day",
    publicationDateSource="https://www.nature.com/articles/s41586-026-11232-w",
    evidence="摘要核验",
    takeaway="研究显示，把官员晋升前景与出生指标挂钩的官僚激励强化了独生子女政策执行，并解释1990年代中国生育率下降的近一半。",
    theory="以组织激励和晋升约束解释同一政策在地方执行强度上的差异。",
    data="中国地方政策执行、官员激励和生育结果的历史行政数据。",
    method="利用一票否决激励强度差异进行政策效果识别；完整模型与稳健性需阅读全文核验。",
    results="更强官僚激励显著强化政策执行，并解释1990年代生育下降的重要部分。",
    limitations="宏观历史识别依赖制度差异和模型假设，摘要不足以核验全部机制与异质性。",
    researchConnection="展示制度激励如何把价值或政策要求转化为行为，适合作为一般社会科学方法参照。",
)
nature["socialScienceReason"] = "研究政策执行、组织激励与人口行为，属于明确的社会科学研究。"


toc = [
    {
        "title": "The sequential replicant effect in interpersonal sincerity: evidence from AI-mediated apology and gratitude",
        "url": "https://doi.org/10.1093/jcmc/zmag024",
        "articleType": "Research Article",
        "status": "previously-recommended",
        "recommendedDate": "2026-10-26",
        "reviewUrl": "https://xiaoxiao-tiger.github.io/culture-research-daily/?date=2026-10-26",
    },
    {
        "title": "The link between three smartphone school policies and students’ mental health: a growth trajectory approach",
        "url": "https://doi.org/10.1093/jcmc/zmag025",
        "articleType": "Research Article",
        "status": "previously-recommended",
        "recommendedDate": "2026-10-26",
        "reviewUrl": "https://xiaoxiao-tiger.github.io/culture-research-daily/?date=2026-10-26",
    },
]
collection = {
    "journalId": "jcmc",
    "journalName": "Journal of Computer-Mediated Communication",
    "kind": "issue",
    "volume": "31",
    "issue": "6",
    "title": "Volume 31, Issue 6",
    "url": "https://academic.oup.com/jcmc/issue/31/6",
    "checkedAt": date,
    "complete": True,
    "toc": toc,
}


groups = [
    {
        "id": "crossdisciplinary",
        "label": "其他研究",
        "target": 5,
        "sortBy": "split",
        "selectionBuckets": [
            {"id": "latest", "label": "最新", "target": 3},
            {
                "id": "cited",
                "label": "重要研究精选",
                "target": 2,
                "sortBy": "relevance-quality",
                "sortDescription": "Google Scholar受异常流量验证阻断后，按相关性和研究质量选择，不按引用量排名。",
                "accessFallback": fallback,
            },
        ],
        "sourceCoverage": [
            {"database": "arXiv", "status": "included"},
            {"database": "SSRN", "status": "included"},
            {"database": "NBER", "status": "included"},
        ],
        "sortDescription": "最新3篇各覆盖NBER、SSRN和arXiv。重要研究精选2篇按相关性和设计质量呈现。",
        "papers": cross,
    },
    {
        "id": "journals",
        "label": "传播学与社会科学",
        "target": 5,
        "sortBy": "relevance-quality-date",
        "journalPriorityNote": "Google Scholar受验证阻断后转用出版方官方目录。5篇均来自用户确认的传播学SSCI Q1与Q2期刊。",
        "sortDescription": "按传播学SSCI期刊优先、主题相关性、质量和日期筛选。",
        "accessFallback": fallback,
        "papers": journals,
    },
    {
        "id": "communication-issue",
        "label": "传播学顶刊推荐",
        "unit": "issue",
        "target": 0,
        "sortBy": "issue",
        "collection": collection,
        "sortDescription": "完整核验JCMC Volume 31 Issue 6。两篇研究均已进入永久历史，本期不重复推荐。",
        "papers": [],
    },
    {
        "id": "general-science",
        "label": "综合顶刊推荐",
        "target": 1,
        "sortBy": "publicationDate",
        "rotationJournalId": "nature",
        "selectedJournalId": "nature",
        "sortDescription": "不使用主题关键词。按Nature最新社会科学目录选取未进入永久历史的研究论文。",
        "papers": [nature],
    },
]


specials = [black_myth, norms, protagonist, authenticity]
selected = [black_myth["doi"], norms["doi"], difficult["doi"], protagonist["doi"], authenticity["doi"]]
count = sum(len(g["papers"]) for g in groups) + len(specials)
data = {
    "schemaVersion": 6,
    "date": date,
    "timezone": "Asia/Shanghai",
    "edition": "正式第44期",
    "title": "从技术好评到文化接收：神话理解、语言情境与加工流畅性",
    "summary": "本期完成其他研究5篇、传播学与社会科学5篇、JCMC完整期次核查和Nature社会科学论文1篇，并新增博士论文同行评审专题4篇；博士论文方向共精选5篇。",
    "historyPolicy": "exclude-recommended",
    "journalPolicy": "ssci-communication-q1-q2-and-social-science",
    "searchPlatforms": ["Google Scholar", "NBER", "SSRN", "arXiv"],
    "activeTopicIds": ["culture", "sycophancy", "methods"],
    "searchSettings": {
        "source": "defaults + reading-plan",
        "lookbackDays": 30,
        "conflictNote": "当日没有生效的一次性或持续用户设置。博士论文标准强化culture主题，但未删除culture、sycophancy和methods，也未改动未来设置。",
    },
    "notice": "逐篇依据官方记录、出版方页面和权威学术索引核验。只有实际阅读正文关键部分才标全文核验；无法核验的样本、系数、识别和许可信息均明确说明。",
    "searchNote": "Google Scholar主题查询于2026-11-16返回异常流量提示后停止，没有绕过验证，也没有以其他网页指标冒充引用次数。随后使用出版方、Crossref、PubMed、NBER、SSRN和arXiv逐篇核验。",
    "shortfallReason": "其他研究、传播学与社会科学及综合顶刊达到目标。JCMC当期完整目录中的2篇均已进入永久历史，因此本期该栏无新增，并清楚展示历史链接，不以旧文献或低相关研究补位。博士论文方向达到5篇同行评审精选。",
    "themeSearches": [
        {
            "platform": "Google Scholar",
            "query": "cross-cultural mythology character identification audience reception",
            "timeRange": "2024年至今；检索日期2026-11-16",
            "purpose": "culture主题发现与引用核验",
            "status": "原生页面显示unusual traffic，未取得结果或引用次数，未绕过验证。",
        },
        {
            "platform": "NBER、SSRN与arXiv",
            "query": "跨文化传播、AI沟通、sycophancy和方法",
            "timeRange": "优先近30日，必要时扩展至2025年至2026年",
            "purpose": "其他研究发现",
            "status": "题名、作者、日期、标识符、摘要与研究设计由官方记录核验。",
        },
    ],
    "periodicalChecks": [
        {
            "platform": "传播学SSCI出版方目录",
            "query": "Social Media + Society、Digital Journalism、Media Psychology及用户确认期刊",
            "timeRange": "检查日期2026-11-16",
            "purpose": "传播学与社会科学主题栏",
            "status": "发现并核验5篇未入历史库的同行评审论文。",
        },
        {
            "platform": "Oxford Academic · JCMC",
            "query": "Volume 31 Issue 6，不使用关键词",
            "timeRange": "检查日期2026-11-16",
            "purpose": "传播学顶刊轮换",
            "status": "完整目录2篇均命中永久历史，本期无新增。",
        },
        {
            "platform": "Nature",
            "query": "最新社会科学研究目录，不使用主题关键词",
            "timeRange": "检查日期2026-11-16",
            "purpose": "综合顶刊轮换",
            "status": "选取2026-11-11发表且未入历史库的社会科学研究。",
        },
    ],
    "verificationLog": [
        {
            "platform": "Google Scholar",
            "query": "当日主题检索与实际引用次数",
            "timeRange": "核验日期2026-11-16",
            "purpose": "主题发现与引用排序",
            "status": "原生查询显示异常流量后停止，没有绕过验证或虚构引用次数。",
        },
        {
            "platform": "出版方官网、Crossref、PubMed、NBER、SSRN与arXiv",
            "query": "题名、作者、年份、同行评审状态、DOI、日期、摘要、样本与方法",
            "timeRange": "核验日期2026-11-16",
            "purpose": "逐篇核验",
            "status": "只写入公开证据支持的研究细节，未知信息明确标示。",
        },
        {
            "platform": "博士论文文献阅读与补充清单",
            "query": "最新可访问工作簿六个工作表、网站永久登记及可见对话",
            "timeRange": "核验日期2026-11-16",
            "purpose": "题名、DOI与版本去重",
            "status": "工作簿最新可访问版本未变化，并与573条永久登记、可见对话和用户明确列出的既有论文交叉核对。",
        },
    ],
    "groups": groups,
    "coreTracking": [],
    "coreTrackingNote": "reading-plan与core-papers当日没有用户提交的核心论文请求，因此本期没有核心文献状态更新。",
    "periodicalCheckNote": "两个轮换栏目均未使用主题关键词。JCMC完整核验但无新增，Nature新增1篇。",
    "dissertation": {
        "title": "从被看见到被接收",
        "timeRange": "优先检查2026-11-15上期发布以来的新发表研究。严格去重后不足5篇当日新增，因此扩展至2025年至2026年正式发表研究，并将2014年主人公相似性论文单列为较早补充，不冒称最新。",
        "selectionNote": "精选5篇同行评审论文，覆盖中国神话游戏的全球接收、语言情境、认知负荷与加工流畅性、主人公相似与自我参照、AI辅助解释的关系真实性。常规栏目论文只登记一次完整解读，专题区只补充4篇。",
        "historyCoverage": "已核对网站截至2026-11-15的573条永久登记、现有简报、用户明确列出的既有文献、本轮可见对话，以及最新可访问博士论文工作簿六个工作表，并按DOI、arXiv ID、规范化题名和已知版本别名去重。无法访问的完整旧对话和未同步私人清单不在覆盖范围内，因此不声称绝对完全去重。",
        "selectedPapers": selected,
        "papers": specials,
        "topPapers": [
            {"doi": black_myth["doi"], "reason": "直接分析黑神话悟空在微博、Reddit和Steam上的不对称接收，最接近外国受众对中国神话人物与叙事的核心问题。"},
            {"doi": norms["doi"], "reason": "把语言情境与文化规范接受清楚分开，并同时提供显性判断和N400证据。"},
            {"doi": difficult["doi"], "reason": "用正交操纵区分认知负荷与加工流畅性，可直接转化为本国相似人物类比实验。"},
        ],
    },
}

# 2026-11-16 compact redesign: two dissertation papers first, followed by
# three standing research ideas (two papers each), then the two rotations.
# The records below were already verified in this run; this block changes only
# their information architecture and keeps every paper in a single full card.
fandom = journals[1]
ai_democracy = journals[2]
loneliness = next(paper for paper in cross if paper["title"].startswith("Do Personal AI Conversations"))
for paper, topic, category in [
    (fandom, "ishow-speed", "研究idea · 甲亢哥访华"),
    (black_myth, "ishow-speed", "研究idea · 甲亢哥访华"),
    (difficult, "x-translation", "研究idea · X自动翻译"),
    (ai_democracy, "x-translation", "研究idea · X自动翻译"),
    (loneliness, "ai-wellbeing", "研究idea · AI与幸福感"),
    (authenticity, "ai-wellbeing", "研究idea · AI与幸福感"),
    (norms, "culture", "博士论文专题"),
    (protagonist, "culture", "博士论文专题"),
]:
    paper["topicIds"] = [topic]
    paper["category"] = category

english_abstracts = {
    norms["title"]: "This study examined whether bilingual speakers accept cultural norms differently depending on the language in use. Twenty Chinese–English bilinguals and twenty English monolinguals evaluated general knowledge statements and British or Chinese cultural norms while EEG was recorded. General knowledge integration was similar across languages, whereas bilingual participants were more accepting of British norms in English and Chinese norms in Chinese. Explicit judgments and N400 responses therefore converged on a language-context effect in cultural norm acceptance.",
    protagonist["title"]: "A between-subjects experiment with 220 participants tested whether adapting a narrative protagonist to resemble readers increases narrative impact in a health context. Readers exposed to a similar protagonist perceived greater personal disease risk and greater efficacy in dealing with the symptoms than readers exposed to a dissimilar protagonist. Self-referencing mediated these effects, indicating that similarity made readers relate the story more strongly to themselves.",
    fandom["title"]: "Drawing on interviews with thirteen fans, anti-fans, and bystanders, together with 139,795 Weibo posts and 205,001 comments surrounding the Cai Xukun controversy, this study identifies positioning, storytelling, affective attunement, and calibration as four affective practices. These practices explain how heterogeneous participants sustain movement-like collective participation after an external rupture.",
    black_myth["title"]: "Using third-space and cultural-hybridity perspectives, this study combines critical discourse analysis of Black Myth: Wukong and its paratexts with computational analysis of 3,842 relevant posts from Weibo, Reddit, and Steam. Chinese audiences emphasized cultural authenticity, symbolism, and narrative depth, whereas international audiences focused more on gameplay, technology, and accessibility and frequently missed or misinterpreted cultural details.",
    difficult["title"]: "This experiment independently manipulated reactive cognitive control through auditory cues and processing fluency through linguistic difficulty in a health narrative. Linguistic difficulty affected memory and narrative persuasion. Under difficult language conditions, auditory cues improved rather than impaired memory, showing that cognitive load and processing fluency should not be treated as the same dimension of difficult processing.",
    ai_democracy["title"]: "Using surveys, organizational documents, and interviews with senior managers, this comparative study examines artificial-intelligence use in thirteen public-service media networks across Africa, Asia, Europe, Oceania, and the Caribbean. AI was used mainly for transcription, image generation and editing, and content personalization. The findings reveal persistent tensions between efficiency, public value, statutory obligations, and democratic missions.",
    loneliness["title"]: "A large preregistered experiment with adults in France required participants in the treatment condition to hold at least one personal conversation with an AI system each day for twenty-eight days. The intervention substantially increased socioemotional AI use but did not reduce loneliness. Self-reported loneliness increased, and other well-being measures moved in similarly unfavorable directions, although several estimates were imprecise.",
    authenticity["title"]: "This mini-review synthesizes thirteen core experiments and four adjacent studies on AI-mediated interpersonal communication. Relational costs of AI assistance were concentrated around four conditions: disclosure or suspicion of AI use, emotionality of the message, closeness of the relationship, and degree of assistance. Perceived authorship is proposed as a candidate mechanism, but the review notes that it has not yet been tested directly.",
    nature["title"]: "This study shows that bureaucratic incentives linking officials’ promotion prospects to birth-control targets strengthened enforcement of China’s one-child policy. Variation in these incentives helps explain a substantial share of the fertility decline during the 1990s, illustrating how personnel rules can shape the effectiveness of nationwide social policy.",
}
for paper in [norms, protagonist, fandom, black_myth, difficult, ai_democracy, loneliness, authenticity, nature]:
    paper["abstractEn"] = english_abstracts[paper["title"]]

toc_summaries = {
    "https://doi.org/10.1093/jcmc/zmag024": "两项预注册双轮实验发现，AI介入线索会稳定降低道歉与感谢信息的真诚感。先前被启动的AI介导意识还会通过提高AI使用怀疑，影响后来没有AI线索的信息判断，形成序列效应。",
    "https://doi.org/10.1093/jcmc/zmag025": "比利时三所学校实施不同手机限制后，研究以最多七轮调查追踪学生。首次测量时全禁学校的抑郁和焦虑最高，但三校心理健康变化轨迹没有显著差异；全禁和午餐可用学校内部的抑郁症状均上升。",
}
toc_summaries_en = {
    "https://doi.org/10.1093/jcmc/zmag024": "Across two preregistered, two-wave experiments, cues that artificial intelligence had assisted with apologies or expressions of gratitude consistently reduced perceived sincerity. Making AI mediation salient in an earlier message also increased suspicion of AI use and shaped evaluations of a later message that contained no AI cue, producing a sequential replicant effect.",
    "https://doi.org/10.1093/jcmc/zmag025": "Students in three Belgian schools were followed for as many as seven survey waves after the schools adopted different smartphone policies. At baseline, depression and anxiety were highest in the school with a full ban, but trajectories of mental health did not differ significantly across schools. Depressive symptoms increased within both the full-ban school and the school allowing lunchtime use.",
}
for entry in collection["toc"]:
    entry["abstractZh"] = toc_summaries[entry["url"]]
    entry["abstractEn"] = toc_summaries_en[entry["url"]]

groups = [
    {"id": "ishow-speed", "label": "甲亢哥访华", "target": 2, "sortBy": "relevance-date", "description": "名人跨文化接触、粉丝与对华态度", "papers": [fandom, black_myth]},
    {"id": "x-translation", "label": "X自动翻译", "target": 2, "sortBy": "relevance-date", "description": "跨语言互动、加工流畅性与平台技术", "papers": [difficult, ai_democracy]},
    {"id": "ai-wellbeing", "label": "AI与幸福感", "target": 2, "sortBy": "relevance-date", "description": "幸福感、孤独感、社会连接与关系真实性", "papers": [loneliness, authenticity]},
    {"id": "communication-issue", "label": "传播学顶刊", "target": 0, "sortBy": "issue", "unit": "issue", "collection": collection, "papers": []},
    {"id": "general-science", "label": "综合顶刊", "target": 1, "sortBy": "publicationDate", "rotationJournalId": "nature", "selectedJournalId": "nature", "papers": [nature]},
]
data.update(
    schemaVersion=7,
    layoutVersion="compact-ideas-v1",
    title="三个研究议题：跨文化接触、自动翻译与AI幸福感",
    summary="博士论文专题2篇置顶，三个研究idea各2篇，并保留传播学完整一期与综合顶刊1篇。页面仅展示题录、摘要和原文链接。",
    notice="本页使用2026-11-16已核验文献演示新布局。三个idea中若当天只有邻近机制研究，会在摘要上方标明主题范围；后续更新优先选择直接研究，不以无关论文补足数量。",
    shortfallReason="三个研究idea与博士论文专题均达到本期精简配额。JCMC当期完整目录中的2篇均已进入永久历史，因此只展示目录摘要、不重复登记。X自动翻译第二篇属于平台AI应用的邻近机制研究，后续优先补充更直接的新研究。",
    groups=groups,
    dissertation={
        "title": "从被看见到被接收",
        "timeRange": "沿用本期已核验候选池，并按新规则仅保留2篇。",
        "selectionNote": "今日专题保留语言情境与主人公相似性两篇，分别对应文化规范接受和人物认同机制。",
        "historyCoverage": data["dissertation"]["historyCoverage"],
        "selectedPapers": [norms["doi"], protagonist["doi"]],
        "papers": [norms, protagonist],
        "topPapers": [
            {"doi": norms["doi"], "reason": "语言情境与文化规范接受"},
            {"doi": protagonist["doi"], "reason": "人物相似性、自我参照与接收"},
        ],
    },
)
count = sum(len(group["papers"]) for group in groups) + len(data["dissertation"]["papers"])

(root / f"{date}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
index_path = root / "index.json"
index = []
index.insert(0, {"date": date, "title": data["title"], "summary": data["summary"], "edition": data["edition"], "count": count, "file": f"{date}.json"})
index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

state_path = root / "rotation-state.json"
state = json.loads(state_path.read_text())
state["updatedAt"] = date
jcmc = state["communication"]["jcmc"]
jcmc.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date, reason="Official JCMC Volume 31 Issue 6 directory was completely reconciled. Its two research articles were already present in permanent history, so no duplicate recommendation was added.")
jcmc["onlineSnapshots"] = [x for x in jcmc.get("onlineSnapshots", []) if x.get("checkedAt") != date]
jcmc["onlineSnapshots"].append({"checkedAt": date, "url": collection["url"], "title": collection["title"], "complete": True, "dois": [e["url"] for e in toc]})
nat = state["general"]["nature"]
nat.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date, lastRecommendedDoi=nature["doi"], publicationDate=nature["publicationDate"], lastRecommendedPublicationDate=nature["publicationDate"], socialScienceAssessment="confirmed", reason="Nature latest social-sciences directory yielded an unrecommended research article on bureaucratic incentives and one-child-policy enforcement, DOI 10.1038/s41586-026-11232-w.")
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
print(f"Wrote {date} with {count} unique papers")
