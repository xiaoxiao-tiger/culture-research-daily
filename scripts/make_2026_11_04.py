import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-11-04"
unavailable = "本次核验未取得允许本站完整转载摘要的明确许可。请通过来源链接查看原文摘要，中文概述依据可核验证据原创。"
fallback = {
    "reason": "Google Scholar原生页面返回异常流量验证，未取得可核验结果或引用次数，且未尝试绕过验证。",
    "channel": "改用出版方官网、期刊官方目录、NBER、SSRN与arXiv官方记录进行发现和逐篇核验。",
    "checkedAt": date,
}


def paper(**v):
    x = {
        "evidence": "摘要核验", "relevance": "研究启示是本简报依据论文证据作出的推论，不是论文作者已经检验的结论。",
        "abstractMode": "unavailable", "originalAbstract": "", "abstractUnavailableReason": unavailable,
        "readingPriority": "normal", "priorityReason": "与当日主题相关，且题录、摘要与发表状态可以核验。",
        "readingUse": "用于理论框架、研究设计或结果讨论。", "researchConnection": "作为一般研究追踪，和博士论文的具体关系见逐篇说明。",
    }
    x.update(v); x.setdefault("abstractZh", x["takeaway"]); x.setdefault("abstractSource", x["url"])
    return x


def journal(**v):
    d = {
        "publicationType": "journal", "publicationStatus": "published", "peerReviewed": True,
        "discoverySource": "Publisher", "journalEdition": "SSCI", "discipline": "communication",
        "indexSource": "site/data/journals.json中的用户上传传播学SSCI Q1/Q2期刊表",
        "quartileSource": "site/data/journals.json中的用户上传传播学SSCI Q1/Q2期刊表", "jifQuartile": "Q1",
        "citationStatus": "unverified", "citationCount": None, "citationSource": None, "citationSourceUrl": None, "citationCheckedAt": None,
        "citationNote": "Google Scholar原生页面触发异常流量验证，未取得实际被引次数，不以其他指标替代。",
        "selectionReason": "在出版方可核验候选中按主题直接相关性、研究设计质量和发表日期综合选择。",
        "topicIds": ["culture"], "category": "传播学与社会科学 · 出版方回退",
    }
    d.update(v); return paper(**d)


def dissertation(x, apa, status="online-first", priority="normal", reason="与博士论文的理论或方法问题直接相关。"):
    x.update(apaCitation=apa, publicationStatus=status, peerReviewed=True, readingPriority=priority, priorityReason=reason,
             publicationDateSource=x["url"], peerReviewSource=x["url"])
    return x


cross = [
    paper(title="SEAM: Situated Executable Associative Memory for a Co-located Community", titleZh="SEAM：面向共处社群的情境化可执行联想记忆",
          authors="Keru Wang, Michael Xu, Ken Perlin, Nebojsa Jojic, Andrzej Banburski-Fahey", year=2026, venue="arXiv:2611.04296", source="arXiv", sourceDatabase="arXiv",
          category="其他研究 · 最新", url="https://arxiv.org/abs/2611.04296", doi="https://doi.org/10.48550/arXiv.2611.04296", arxivId="2611.04296", topicIds=["methods"], selectionBucket="latest",
          publicationType="preprint", publicationDate="2026-11-03", publicationDatePrecision="day", publicationDateSource="https://arxiv.org/abs/2611.04296",
          takeaway="作者把社群成员提交的碎片化时刻组织为可联想、可执行且可由成员继续编程的共享记忆。两周部署显示，系统可连接原本分散的人物、主题与经历。",
          theory="把集体记忆视为可由社群持续解释和重组的联想基础设施，而非静态内容档案。", data="一个共处社群46人使用两周，后续工作坊14人。",
          method="部署式研究结合系统日志、社群使用观察与后续工作坊。", results="系统从任意生活片段中提炼群体知识，并促进参与者发现共同人物和主题。",
          limitations="预印本尚未同行评审，样本来自单一小型共处社群，短期使用不能证明长期社群整合。",
          readingUse="用于社群记忆与质性部署研究。", researchConnection="可启发研究中国神话人物如何在海外社群的日常叙事中被重新联结，但不能替代对理解、好感、认同和传播意向的分项测量。"),
    paper(title="Human Oversight and Bounded Automation in AI-mediated Organizational Communication", titleZh="人工监督与有界自动化：人工智能中介的组织传播",
          authors="Evgeniya Dianova", year=2026, venue="SSRN Working Paper 7628020", source="SSRN", sourceDatabase="SSRN", category="其他研究 · 最新",
          url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7628020", doi="https://doi.org/10.2139/ssrn.7628020", topicIds=["sycophancy"], selectionBucket="latest", publicationType="working-paper",
          publicationDate="2026-10-20", publicationDatePrecision="day", publicationDateSource="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7628020",
          takeaway="论文综合既有研究提出六项设计原则，主张在人工智能生成组织信息时保留明确的人类责任、审查节点、可追溯性与任务边界。",
          theory="以有界自动化解释为何高效率的生成式传播仍需人类监督和责任配置。", data="概念性综合，不包含新的受众样本。", method="跨组织传播、人工智能治理与人机协作研究的理论综合。",
          results="提出六项原则用于限定自动化范围并维持人类问责。", limitations="工作论文尚未同行评审，也没有直接检验原则对可信度或参与的因果效应。",
          readingUse="用于人工智能传播治理与研究设计边界。", researchConnection="若用模型生成神话人物类比材料，应记录人工审查、事实核验和改写过程，避免把模型迎合当作受众真实价值契合。"),
    paper(title="Competition in Generative AI: Evidence from Consumer Demand", titleZh="生成式人工智能竞争：来自消费者需求的证据",
          authors="Mark L. Egan, Dominic Russel, Claire Shi, Vincent Yao", year=2026, venue="NBER Working Paper 35953", source="NBER", sourceDatabase="NBER", category="其他研究 · 最新",
          url="https://www.nber.org/papers/w35953", doi="https://doi.org/10.3386/w35953", topicIds=["sycophancy"], selectionBucket="latest", publicationType="working-paper",
          publicationDate="2026-10", publicationDatePrecision="month", publicationDateSource="https://www.nber.org/papers/w35953",
          takeaway="基于1.74亿消费者和1140亿笔卡交易，研究发现截至2026年4月约2.9%的美国消费者付费使用主要生成式人工智能服务，多平台订阅常见但下降，年度留存率约20%至45%。",
          theory="从产品差异化、转换成本与多平台使用解释生成式人工智能市场竞争。", data="覆盖1.74亿消费者的1140亿笔信用卡和借记卡交易。",
          method="用交易数据测量付费采用、多平台订阅、留存与转换。", results="付费采用集中于年轻和高收入消费者，基础套餐占主导，留存率低于许多订阅产品，显示转换成本有限。",
          limitations="工作论文尚未同行评审，卡交易不能观测免费使用、对话内容或价值迎合。", readingUse="用于平台采用、留存和用户异质性。",
          researchConnection="提醒博士论文的传播意向并不等同持续使用，可将一次分享、继续接触和跨平台寻找内容区分为不同结果。"),
    paper(title="Understanding the Limits of Social Media Bans", titleZh="理解社交媒体禁令的边界",
          authors="Leonardo Bursztyn, Angela L. Duckworth, Rafael Jiménez-Durán, Aaron Leonard, Filip Milojević, Christopher Roth, Cass R. Sunstein", year=2026,
          venue="NBER Working Paper 35162", source="NBER", sourceDatabase="NBER", category="其他研究 · 重要研究精选", url="https://www.nber.org/papers/w35162", doi="https://doi.org/10.3386/w35162",
          topicIds=["methods"], selectionBucket="cited", publicationType="working-paper", publicationDate="2026-04", publicationDatePrecision="month", publicationDateSource="https://www.nber.org/papers/w35162",
          takeaway="澳大利亚禁令实施四个月后，约四分之一的14至15岁青少年遵守禁令。青少年表示通常需要三位同伴中至少两位也遵守，且遵守者被认为较不受欢迎。",
          theory="以协调问题和同伴网络外部性解释可规避禁令为何难以持续。", data="澳大利亚14至15岁青少年调查，公开摘要未报告样本规模。",
          method="在政策实施四个月后测量遵守率、同伴阈值与受欢迎度判断。", results="实际遵守率低，所需同伴遵守阈值高于当前水平，且遵守与较低受欢迎度相联系。",
          limitations="首次公开于2026年4月，10月只是修订，不冒称新发表；调查关系不能单独建立同伴效应因果。",
          citationStatus="unverified", citationCount=None, citationSource=None, citationSourceUrl=None, citationCheckedAt=None, citationNote="Google Scholar受异常流量验证阻断，未核验实际引用次数。",
          selectionReason="直接展示平台行为中的协调门槛和同伴外部性，且政策情境与研究设计清晰。", readingUse="用于协调机制与同伴阈值。",
          researchConnection="传播意向可能受同伴可见行为影响，即使个体已理解并喜欢人物，也未必愿意在外群体环境公开分享。"),
    paper(title="The Confidence Pill: The Causal Effect of Exposure to Police Social Media", titleZh="信心药丸：接触警方社交媒体的因果效应",
          authors="Melissa Beckett, Till O. Weber, Diego Zambiasi", year=2026, venue="SSRN Working Paper 7173918", source="SSRN", sourceDatabase="SSRN", category="其他研究 · 重要研究精选",
          url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7173918", doi="https://doi.org/10.2139/ssrn.7173918", topicIds=["methods"], selectionBucket="cited", publicationType="working-paper",
          publicationDate="2026-07-24", publicationDatePrecision="day", publicationDateSource="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7173918",
          takeaway="大型在线实验比较英国警方真实Instagram帖子与中性内容。警方内容提高机构信心和付出成本的支持，但降低即时幸福感，社区参与内容获得相近信心提升且幸福感代价较小。",
          theory="把机构社交媒体视为同时影响信任、支持行为和情绪福祉的传播干预。", data="英国大型在线实验，公开摘要未报告具体样本量。",
          method="随机分派真实警方Instagram帖子、中性内容和不同警方内容类型，并测量态度、情绪与成本性支持。", results="总体内容提高信心和支持，降低即时幸福感；社区参与型内容的情绪代价较小。",
          limitations="工作论文尚未同行评审，短期实验不能说明长期信任，警方情境也不等同文化人物接收。",
          citationStatus="unverified", citationCount=None, citationSource=None, citationSourceUrl=None, citationCheckedAt=None, citationNote="Google Scholar受异常流量验证阻断，未核验实际引用次数。",
          selectionReason="随机实验同时测量认知、情绪和成本性行为结果，可避免只用单一态度指标判断传播效果。",
          readingUse="用于多结果传播实验。", researchConnection="应把理解、好感、人物认同与愿意付出成本的传播行为分开测量，因为同一内容可能同时改善信心并损害情绪体验。"),
]


j1 = dissertation(journal(title="When Metaphors Hurt or Heal: The Effects of Metaphor Use and Protagonist-Reader Similarity in Mental Illness Narratives on Stigma",
    titleZh="隐喻何时伤害或疗愈：隐喻与主人公读者相似性对污名的影响", authors="Yujie Dong, Yin Yang", year=2026, venue="Journal of Health Communication, Online First", source="Journal of Health Communication", journalName="JOURNAL OF HEALTH COMMUNICATION",
    url="https://doi.org/10.1080/10810730.2026.2713983", doi="https://doi.org/10.1080/10810730.2026.2713983", publicationDate="2026-08-10", publicationDatePrecision="day",
    takeaway="4乘2实验显示，战争和旅程隐喻只在主人公与读者高度相似时提高希望并促进反污名行为意向；相似性低时反而降低认同。对话隐喻在两类相似条件下都呈现较稳健路径。",
    theory="结合叙事说服和概念隐喻理论，检验隐喻效果如何取决于受众与人物的相似性。", data="无相关个人经历的参与者522人。",
    method="4种隐喻条件乘以高低主人公读者相似性的组间随机实验。", results="战争和旅程隐喻存在显著相似性边界，对话隐喻的作用路径较稳定。",
    limitations="研究对象是心理疾病污名，使用的是综合相似性而非Schwartz价值契合，也未检验跨国神话人物。",
    readingUse="用于类比或隐喻与人物相似性的交互设计。", researchConnection="最直接支持把本国神话人物类比与价值契合同时操纵，并警惕低契合条件下类比造成反效果。",
    hypothesisImplication="简报推论：本国相似人物类比对接收的正效应受价值契合调节，低契合时可能降低人物认同。",
    manipulationImplication="简报推论：正交操纵类比框架与人物价值契合，设置无类比基线并保持情节信息不变。",
    measurementImplication="简报推论：分别测量加工流畅性、希望或情绪、人物认同、污名或道德评价和传播意向。"),
    "Dong, Y., & Yang, Y. (2026). When metaphors hurt or heal: The effects of metaphor use and protagonist-reader similarity in mental illness narratives on stigma. Journal of Health Communication. Advance online publication. https://doi.org/10.1080/10810730.2026.2713983", priority="high", reason="以随机实验直接检验隐喻与人物受众相似性的交互，是本国神话人物类比设计的最接近模板。")

j2 = dissertation(journal(title="A Match Made in Language: Examining the Role of Linguistic Similarity in Adolescents’ Preference for Persuasive Health Messages in Social Media Contexts",
    titleZh="语言上的匹配：语言相似性如何影响青少年对社交媒体健康信息的偏好", authors="Jonas Schlicht, Thabo van Woudenberg, David J. Blok, Bojan Simoski, Moniek Buijzen", year=2026,
    venue="Health Communication, Online First", source="Health Communication", journalName="HEALTH COMMUNICATION", url="https://doi.org/10.1080/10410236.2026.2613120", doi="https://doi.org/10.1080/10410236.2026.2613120",
    publicationDate="2026-01-08", publicationDatePrecision="day", takeaway="预注册研究依据191名荷兰青少年捐赠的WhatsApp对话构建语言画像，并比较22组Instagram式健康信息。语言相似性对偏好和个性化感知的证据不确定，对感知效果存在中等强度的零效应证据。",
    theory="以相似吸引为基础，把传播匹配从内容扩展到语言风格。", data="191名13至15岁荷兰青少年的WhatsApp对话和22组信息评价。",
    method="预注册设计，以捐赠对话建立语言画像，逐类操纵语言相似性，并用多层贝叶斯模型分析。", results="未发现稳定的语言相似性优势，受众更稳定偏好积极且词语简单的信息。",
    limitations="单项语言类别操纵可能过弱，研究测量偏好和感知效果而非实际长期行为。",
    readingUse="用于区分客观匹配、感知匹配与信息简洁性。", researchConnection="提示本国神话类比不能仅假设表面语言相似就有效，需要同时检验感知相似、流畅性和实际理解。",
    hypothesisImplication="简报推论：类比的正效应不应只由客观相似推导，感知文化熟悉性和加工流畅性可能是必要中介。",
    manipulationImplication="简报推论：预试类比强度，并将语言简洁度与文化相似性分别操纵。",
    measurementImplication="简报推论：同时测量客观匹配、感知相似、加工流畅性、理解准确度和传播意向。"),
    "Schlicht, J., van Woudenberg, T., Blok, D. J., Simoski, B., & Buijzen, M. (2026). A match made in language: Examining the role of linguistic similarity in adolescents’ preference for persuasive health messages in social media contexts. Health Communication. Advance online publication. https://doi.org/10.1080/10410236.2026.2613120", priority="high", reason="预注册研究提供相似性操纵失败的负面证据，有助于避免把表面匹配误当作文化接近或价值契合。")

j3 = dissertation(journal(title="Can fictional stories beat the congeniality bias? Selective exposure to fiction and non-fiction", titleZh="虚构故事能否克服一致性偏误：对虚构与非虚构信息的选择性接触",
    authors="Markus Appel, et al.", year=2026, venue="Human Communication Research, 52(3), 161–175", source="Human Communication Research", journalName="HUMAN COMMUNICATION RESEARCH",
    url="https://doi.org/10.1093/hcr/hqaf027", doi="https://doi.org/10.1093/hcr/hqaf027", publicationDate="2025-11-25", publicationDatePrecision="day", publicationStatus="published",
    takeaway="两项大样本实验分别围绕难民与宗教信仰，发现受众更愿意选择与既有态度一致的叙事信息，且虚构性并未削弱这种一致性偏误。",
    theory="把叙事加工与选择性接触结合，检验虚构标签是否降低态度一致性偏好。", data="实验一1326人，实验二1316人。",
    method="在两个极化议题中操纵信息立场和虚构或新闻报道标签，测量阅读选择。", results="一致性偏误在两项实验中稳定存在，且不因信息被标为虚构而减弱。",
    limitations="测量的是选择进入而非阅读后的理解和人物认同，议题极化程度可能限制外推。",
    readingUse="用于把被看见、选择接触与接收效果分开。", researchConnection="说明神话的虚构属性不会自动跨越价值或群体边界，博士论文应记录是否选择接触并与接触后的接收指标区分。",
    hypothesisImplication="简报推论：价值契合可能先影响是否选择接触人物叙事，再影响接触后的认同。",
    manipulationImplication="简报推论：先提供可选择的故事摘要，再对实际进入者实施人物价值与类比操纵。",
    measurementImplication="简报推论：区分点击选择、阅读完成、理解、好感、认同与传播意向，并处理选择造成的样本差异。"),
    "Appel, M., et al. (2026). Can fictional stories beat the congeniality bias? Selective exposure to fiction and non-fiction. Human Communication Research, 52(3), 161–175. https://doi.org/10.1093/hcr/hqaf027", status="published", priority="high", reason="两项大样本实验直接说明虚构性不能消除价值一致性选择，是从可见到被接收链条中的关键前置边界。")

j4 = dissertation(journal(title="How Narrative Transportation in Anonymous Employee Dissent Threatens Corporate Reputation: The Mediating Roles of Perceived Similarity and Personal Relevance",
    titleZh="匿名员工异议中的叙事运输如何威胁企业声誉：感知相似与个人相关性的中介作用", authors="Kayoung Kim, Youngmin Yoon", year=2026, venue="International Journal of Business Communication, OnlineFirst",
    source="International Journal of Business Communication", journalName="International Journal of Business Communication", url="https://doi.org/10.1177/23294884261462508", doi="https://doi.org/10.1177/23294884261462508",
    publicationDate="2026-07-07", publicationDatePrecision="day", takeaway="400名韩国在职成年人接触匿名员工职场霸凌叙事后，叙事运输通过提高与异议员工的感知相似性和议题个人相关性，增强企业责任归因并损害声誉和口碑。",
    theory="整合叙事运输与防御性归因，说明相似性和个人相关性如何把内部异议转化为外部声誉判断。", data="400名韩国在职成年人。",
    method="向参与者呈现匿名员工平台Blind上的职场霸凌叙事，并用路径模型检验中介。", results="更高运输与更强企业责任归因、负面声誉和口碑意向相关，感知相似与个人相关性发挥中介作用。",
    limitations="摘要描述为调查暴露设计，不能据此确认随机操纵或强因果识别，且组织危机不同于神话人物接收。",
    readingUse="用于运输、相似性、个人相关性与口碑路径。", researchConnection="可借鉴其串联测量，但需把感知相似拆为价值契合、道德评价和文化接近。",
    hypothesisImplication="简报推论：价值契合与个人相关性可能分别经人物认同和叙事运输影响传播意向。",
    manipulationImplication="简报推论：操纵人物价值时保持故事个人相关性稳定，或将两者正交设计。",
    measurementImplication="简报推论：分别测量叙事运输、价值契合、文化接近、个人相关性、责任归因和口碑意向。"),
    "Kim, K., & Yoon, Y. (2026). How narrative transportation in anonymous employee dissent threatens corporate reputation: The mediating roles of perceived similarity and personal relevance. International Journal of Business Communication. Advance online publication. https://doi.org/10.1177/23294884261462508")

j5 = dissertation(journal(title="How storytelling modality affects transportation and storyteller persuasion", titleZh="故事讲述方式如何影响运输与讲述者自我说服",
    authors="Anne Hamby, Rebecca Krause-Galoni, Adam Duhachek, Derek Rucker", year=2026, venue="Journal of Consumer Psychology, 36, 362–368", source="Journal of Consumer Psychology", journalName="Journal of Consumer Psychology",
    discipline="social-science", indexSource="Wiley期刊信息页列明Social Sciences Citation Index；2024 JCR公开表列为SSCI Q1", quartileSource="2024 JCR公开表", jifQuartile="Q1",
    url="https://doi.org/10.1002/jcpy.70029", doi="https://doi.org/10.1002/jcpy.70029", publicationDate="2026-05-22", publicationDatePrecision="day", publicationStatus="published",
    takeaway="多项研究发现，对受众而言口述故事往往更具运输力，但对讲述者而言，书写比口述更能促进结构化思考、运输与自我说服，且故事效价改变说服方向。",
    theory="把传播方式与结构化思考联系起来，区分受众说服和讲述者自我说服。", data="多项实验，出版方可见摘要未列各研究样本量。",
    method="比较书写与口述故事，并检验结构化思考和故事效价的作用。", results="书写更能说服讲述者，故事效价决定自我说服方向。",
    limitations="关注讲述者而非跨文化受众，且可见证据不足以核验各实验样本与全部统计结果。",
    readingUse="用于区分接收者与再传播者的心理过程。", researchConnection="传播意向实现为实际讲述后，受众可能因重新组织人物故事而改变自身态度，因此实验可增加讲述后测量。",
    hypothesisImplication="简报推论：传播行为不仅是结果，也可能反过来强化或改变讲述者对人物的态度。",
    manipulationImplication="简报推论：在接收后随机要求书写、口述或不复述人物故事，并操纵故事效价。",
    measurementImplication="简报推论：在传播前后重复测量理解、人物认同和好感，并编码复述结构和价值内容。"),
    "Hamby, A., Krause-Galoni, R., Duhachek, A., & Rucker, D. (2026). How storytelling modality affects transportation and storyteller persuasion. Journal of Consumer Psychology, 36, 362–368. https://doi.org/10.1002/jcpy.70029", status="published")

journals = [j1, j2, j3, j4, j5]

comm = [
    paper(title="Practicing love with algorithms: How online communities narrate and make sense of human–AI intimacy", titleZh="与算法实践爱情：网络社群如何叙述并理解人机亲密关系", authors="Fanjue Liu, Haiyan Hao, Kun Xu", year=2026, venue="New Media & Society, OnlineFirst", source="New Media & Society", category="传播学顶刊推荐 · OnlineFirst",
          url="https://doi.org/10.1177/14614448261496596", doi="https://doi.org/10.1177/14614448261496596", topicIds=["sycophancy"], publicationType="journal", publicationStatus="online-first", peerReviewed=True,
          publicationDate="2026-10-27", publicationDatePrecision="day", publicationDateSource="https://journals.sagepub.com/doi/10.1177/14614448261496596",
          takeaway="研究分析小红书58篇帖子下13059条评论，结合BERTopic与人机协作情绪分类，识别人机亲密关系的共同建构、基础设施与边界协商叙事。",
          theory="把人机亲密视为由平台社群叙事和情绪实践共同建构的关系。", data="58篇小红书帖子及13059条评论。", method="BERTopic主题建模与人机协作情绪分类。",
          results="评论围绕关系共同建构、技术基础设施和边界协商形成主题簇，不同叙事伴随不同情绪。", limitations="单一中文平台与选择性发帖限制外推，自动分类仍依赖标注与模型质量。",
          readingUse="用于人机亲密的社群叙事分析。", researchConnection="与神话人物接收直接关联有限，但可启发从评论叙事而非单一情感分数观察人物关系建构。"),
    paper(title="The managed sisterhood: Gendered labor and intimacy in Chinese fashion influencer industry", titleZh="被管理的姐妹情谊：中国时尚网红产业中的性别化劳动与亲密", authors="Qiheng Lin, Chenyu Dong", year=2026, venue="New Media & Society, OnlineFirst", source="New Media & Society", category="传播学顶刊推荐 · OnlineFirst",
          url="https://doi.org/10.1177/14614448261493399", doi="https://doi.org/10.1177/14614448261493399", topicIds=["culture"], publicationType="journal", publicationStatus="online-first", peerReviewed=True,
          publicationDate="2026-10-22", publicationDatePrecision="day", publicationDateSource="https://journals.sagepub.com/doi/10.1177/14614448261493399",
          takeaway="民族志研究提出被管理的姐妹情谊，说明女性主导的时尚网红团队如何用亲密和归属感组织劳动，同时遮蔽强制并强化劳动要求。",
          theory="把姐妹情谊视为嵌入等级关系的管理机制，连接亲密劳动与平台产业。", data="中国女性主导时尚网红团队的民族志材料。", method="组织民族志与质性分析。",
          results="亲密话语制造团结与归属，也掩盖等级强制并形成可替代的亲属关系。", limitations="单一行业和团队环境限制外推，摘要未披露田野时长与访谈规模。",
          readingUse="用于平台文化产业与亲密劳动。", researchConnection="可提醒研究者把人物好感与平台产业制造的亲密感区分开。"),
    paper(title="Guardians of the cyberverse: Dispositional, attitudinal, and autobiographical correlates of user engagement against misogynist digital hate", titleZh="赛博空间守护者：用户反对厌女数字仇恨参与的个体、态度与经历相关因素", authors="Rinat Meerson, Kevin Koban, Jörg Matthes", year=2026, venue="New Media & Society, OnlineFirst", source="New Media & Society", category="传播学顶刊推荐 · OnlineFirst",
          url="https://doi.org/10.1177/14614448261492098", doi="https://doi.org/10.1177/14614448261492098", topicIds=["methods"], publicationType="journal", publicationStatus="online-first", peerReviewed=True,
          publicationDate="2026-10-20", publicationDatePrecision="day", publicationDateSource="https://journals.sagepub.com/doi/10.1177/14614448261492098",
          takeaway="奥地利、法国、匈牙利和瑞典调查分别约800人，比较直接干预、间接干预与支持平台审核的预测因素，显示性格、态度和亲历经验对应不同参与方式。",
          theory="把反数字仇恨参与拆分为多种行为，并从个体倾向、态度和自传经历解释。", data="奥地利791人、法国800人、匈牙利775人、瑞典785人。", method="四国横断面调查与多结果比较。",
          results="不同个体和经历因素对直接、间接干预及审核支持的关联模式不同。", limitations="横断面相关不能建立因果，四国结果也不自动代表其他文化环境。",
          readingUse="用于分解传播参与结果和跨国比较。", researchConnection="提示传播意向应拆为公开评论、转发、私下推荐和支持平台治理，而非合成单一指标。"),
    paper(title="Stress and self-efficacy under artificial intelligence disruption: A mixed-methods study on the usage of artificial intelligence among Finnish workers", titleZh="人工智能冲击下的压力与自我效能：芬兰劳动者人工智能使用的混合方法研究", authors="Atte Oksanen, Teo Keipi, Moona Heiskari, Iina Savolainen", year=2026, venue="New Media & Society, OnlineFirst", source="New Media & Society", category="传播学顶刊推荐 · OnlineFirst",
          url="https://doi.org/10.1177/14614448261488700", doi="https://doi.org/10.1177/14614448261488700", topicIds=["sycophancy"], publicationType="journal", publicationStatus="online-first", peerReviewed=True,
          publicationDate="2026-10-15", publicationDatePrecision="day", publicationDateSource="https://journals.sagepub.com/doi/10.1177/14614448261488700",
          takeaway="芬兰全国调查2109人与54人访谈显示，人工智能使用、身份威胁和组织部署与压力相联系，自我效能则与使用、积极态度和福祉相关，并调节身份威胁。",
          theory="以身份威胁和自我效能解释劳动者面对人工智能冲击的压力与适应。", data="芬兰全国调查2109人，访谈54人。", method="全国调查与质性访谈的混合方法设计。",
          results="身份威胁与压力关联，自我效能与使用和积极结果关联，并对威胁路径产生调节。", limitations="主要证据来自单一国家，调查关联不能完全排除反向因果。",
          readingUse="用于技术冲击、身份与混合方法。", researchConnection="可启发把跨文化人物接收中的文化身份威胁作为价值契合效应的边界条件。"),
]

general = paper(title="Banking records reveal characteristics of financial abuse", titleZh="银行记录揭示金融虐待的特征", authors="Anna Trendl, Nicola Sharp-Jeffs, Karen Perrier, Jane Rodrick, John Gathergood, et al.", year=2026,
    venue="Nature", source="Nature", category="综合顶刊推荐 · 社会科学", url="https://doi.org/10.1038/s41586-026-11049-7", doi="https://doi.org/10.1038/s41586-026-11049-7", topicIds=["methods"],
    publicationType="journal", publicationStatus="published", peerReviewed=True, publicationDate="2026-09-23", publicationDatePrecision="day", publicationDateSource="https://www.nature.com/articles/s41586-026-11049-7",
    socialScienceAssessment="confirmed", socialScienceReason="研究使用行政金融数据分析家庭金融虐待、脆弱性与社会后果，属于社会科学与公共政策交叉研究。",
    takeaway="研究比较5428名披露金融虐待的女性与15602名匹配对照，分析披露前七年的373项金融指标。受害者储蓄下降、债务和漏付增加，信用评分恶化，并呈现自我照护支出下降及账户安全操作增加。",
    theory="把金融虐待理解为可在长期交易和账户管理中留下可测痕迹的强制控制。", data="英国大型零售银行匿名数据，5428名受害者和15602名匹配对照，373项指标，最长七年。",
    method="回顾性匹配病例对照设计，结合倾向得分匹配、时间轨迹和置换检验。", results="受害组在储蓄、债务、漏付、信用、福利领取、现金使用、法律支出和账户安全活动上呈系统差异。",
    limitations="披露存在自选择，控制组可能含未披露受害者，方法不能确定金融虐待与所有结果的因果方向，且数据来自一家银行。",
    readingUse="用于高维行政数据、匹配和敏感现象测量。", researchConnection="与博士论文主题直接关联有限，但其把不可见经历转化为长期行为痕迹的策略可启发研究从页面可见度到实际接收的多指标测量。")

toc = [{"title":p["title"],"url":p["url"],"articleType":"Research Article","status":"new"} for p in comm]
groups = [
    {"id":"crossdisciplinary","label":"其他研究","target":5,"sortBy":"split",
     "selectionBuckets":[{"id":"latest","label":"最新","target":3},{"id":"cited","label":"重要研究精选","target":2,"sortBy":"relevance-quality","sortDescription":"Google Scholar受异常流量验证阻断后，按相关性和研究质量选择。","accessFallback":fallback}],
     "sourceCoverage":[{"database":x,"status":"included"} for x in ["NBER","SSRN","arXiv"]],
     "sortDescription":"最新3篇按首次公开日期降序并分别覆盖arXiv、SSRN和NBER；重要研究精选2篇按相关性和研究质量呈现。","papers":cross},
    {"id":"journals","label":"传播学与社会科学","target":5,"sortBy":"relevance-quality-date",
     "journalPriorityNote":"先执行不限期刊的主题检索。Google Scholar受阻后改用出版方发现，再按传播学SSCI Q1/Q2表和已核验社会科学SSCI来源筛选；本期4篇传播学、1篇社会科学。",
     "sortDescription":"按与博士论文和活跃主题的直接相关性、设计质量和发表日期综合排序，不冒充引用次数排序。","accessFallback":fallback,"papers":journals},
    {"id":"communication-issue","label":"传播学顶刊推荐","unit":"issue","target":4,"sortBy":"issue",
     "collection":{"journalId":"nms","journalName":"New Media & Society","kind":"online-first","title":"OnlineFirst部分目录 · 2026-11-04已核验最新4篇","url":"https://journals.sagepub.com/toc/NMS/0/0","checkedAt":date,"complete":False,"toc":toc},
     "sortDescription":"不使用关键词。官方目录报告203条，但访问限制下仅逐篇核验最新4篇研究论文，因此保留为未完成的部分快照且不推进轮换完成状态。","papers":comm},
    {"id":"general-science","label":"综合顶刊推荐","target":1,"sortBy":"publicationDate","rotationJournalId":"nature",
     "sortDescription":"今天轮到Nature。不使用主题关键词；较新的社会科学候选已在历史中推荐，因此选取下一篇未推荐的最新社会科学研究。","papers":[general]},
]

refs = [p["doi"] for p in journals]
data = {
    "schemaVersion":6,"date":date,"timezone":"Asia/Shanghai","edition":"正式第32期",
    "title":"相似性并非总是有效：从选择接触到人物认同与再传播",
    "summary":"本期完成其他研究5篇、传播学与社会科学5篇、New Media & Society最新4篇OnlineFirst部分目录核验、Nature轮换推荐1篇，并从期刊栏为博士论文精选5篇同行评审研究。Google Scholar异常流量验证导致引用次数不可核验，相关栏目依指南启用出版方回退并如实标注。",
    "historyPolicy":"exclude-recommended","journalPolicy":"ssci-communication-q1-q2-and-social-science","searchPlatforms":["Google Scholar","NBER","SSRN","arXiv"],"activeTopicIds":["culture","sycophancy","methods"],
    "shortfallReason":"New Media & Society官方OnlineFirst目录报告203条，但出版方访问控制只允许可靠核验最新4篇研究论文，无法确认其余条目及完整分页，故本期发布部分目录并保持轮换未完成状态。",
    "searchSettings":{"source":"defaults + reading-plan","lookbackDays":30,"conflictNote":"当日没有生效的一次性或持续用户设置。博士论文标准强化culture主题，但未删除culture、sycophancy和methods，也未改动未来设置。"},
    "notice":"逐篇依据官方记录、出版方页面及可访问正文核验。只有实际阅读正文关键部分才标全文核验；无法核验的样本、系数、识别和许可信息均明确说明。",
    "searchNote":"Google Scholar原生主题查询返回异常流量提示后停止，不绕过验证，也不以Web of Science、OpenAlex、下载量或网页指标冒充引用次数。NBER、SSRN与arXiv使用限定官方域名的公开网页检索或官方记录发现候选，再回到官方页核验。",
    "themeSearches":[
      {"platform":"Google Scholar","query":"(\"cultural transmission\" OR \"cultural diffusion\" OR \"cross-cultural reception\" OR \"intercultural communication\" OR \"cultural premium\" OR novelty OR exoticism OR cosmopolitanism OR ((\"value congruence\" OR \"value similarity\" OR \"shared values\") AND (character OR narrative OR audience)) OR (mythology AND analogy))","timeRange":"不限年份；检索日期2026-11-04","purpose":"culture主题发现，随后筛期刊并核验引用次数","status":"原生页面显示异常流量验证，未取得结果或引用次数，未绕过验证。"},
      {"platform":"Google Scholar","query":"(sycophancy OR \"value alignment\" OR ingratiation OR \"opinion agreement\") AND (\"large language model\" OR chatbot OR \"conversational agent\")","timeRange":"不限年份；检索日期2026-11-04","purpose":"sycophancy主题发现","status":"首次请求已触发站点级验证，因此未继续发送本主题请求，并启用指南规定的回退。"},
      {"platform":"Google Scholar","query":"(\"causal inference\" OR \"panel data\" OR \"interrupted time series\" OR \"text measurement\") AND (communication OR \"digital platforms\" OR \"social media\")","timeRange":"不限年份；检索日期2026-11-04","purpose":"methods主题发现","status":"首次请求已触发站点级验证，因此未继续发送本主题请求，并启用指南规定的回退。"},
      {"platform":"NBER","query":"site:nber.org/papers (communication OR social media OR AI OR culture) October 2026","timeRange":"优先近30日，必要时扩展；检索日期2026-11-04","purpose":"NBER候选发现","status":"限定官方域名的公开网页检索成功；不冒称NBER站内高级检索，入选记录回到NBER官方页核验。"},
      {"platform":"SSRN","query":"site:papers.ssrn.com (communication OR narrative OR moderation OR value) 2026","timeRange":"优先近30日，必要时扩展；检索日期2026-11-04","purpose":"SSRN候选发现","status":"限定官方域名的公开网页检索成功；题录、日期和摘要回到SSRN记录核验。"},
      {"platform":"arXiv","query":"submittedDate:[202610050000 TO 202611042359] AND all:(culture OR value OR narrative OR communication OR sycophancy OR social)","timeRange":"2026-10-05至2026-11-04","purpose":"arXiv候选发现","status":"官方API与摘要记录检索成功，题名、作者、首次提交日期、摘要和arXiv ID完成核验。"}],
    "periodicalChecks":[
      {"platform":"SAGE · New Media & Society","query":"OnlineFirst目录，不使用关键词","timeRange":"检查日期2026-11-04","purpose":"传播学顶刊整期轮换","status":"官方目录报告203条；访问限制下仅可靠核验最新4篇研究论文，发布部分快照并不推进完成状态。"},
      {"platform":"Nature","query":"Nature当前研究与社会科学主题目录，不使用关键词","timeRange":"检查日期2026-11-04","purpose":"综合顶刊轮换推荐","status":"较新的社会科学论文均与永久历史重复，选取下一篇未推荐且已核验的2026-09-23研究。"}],
    "verificationLog":[
      {"platform":"Google Scholar","query":"当日主题检索与实际引用次数","timeRange":"核验日期2026-11-04","purpose":"主题发现与引用排序","status":"首次原生查询显示异常流量验证后停止；没有绕过验证、记录虚构0次引用或用其他指标替代。"},
      {"platform":"NBER、SSRN与arXiv官方记录","query":"其他研究5篇的身份、首次公开日期、摘要与版本","timeRange":"核验日期2026-11-04","purpose":"逐篇核验与跨版本去重","status":"5篇均完成题录和摘要核验，且与截至2026-11-03的永久登记无重复。"},
      {"platform":"出版方与权威题录","query":"期刊论文题名、作者、年份、期刊、同行评审状态、DOI、摘要、样本与方法","timeRange":"核验日期2026-11-04","purpose":"主题期刊、博士论文专题与轮换栏目逐篇核验","status":"10篇期刊论文均完成身份核验；只有公开证据支持的研究细节被写入，未知细节明确标示。"}],
    "groups":groups,"coreTracking":[],"coreTrackingNote":"reading-plan与core-papers当日没有用户提交的核心论文请求，因此本期没有核心文献状态更新。",
    "periodicalCheckNote":"轮换栏目不使用主题关键词。New Media & Society形成可核验的部分OnlineFirst快照；Nature按官方当前内容和永久历史选择下一篇未推荐社会科学论文。",
    "dissertation":{"title":"从被看见到被接收","timeRange":"优先检查2026-11-03上期发布以来的新发表研究。直接相关新论文不足5篇后，扩展至2025年以来尚未推荐的同行评审研究；扩展论文不冒称当日最新。",
      "selectionNote":"本期从传播学与社会科学栏精选5篇同行评审论文，不重复建立完整解读。它们覆盖隐喻或类比与人物相似性交互、语言匹配的零效应、选择性接触、叙事运输与再传播反馈。",
      "historyCoverage":"已核对网站截至2026-11-03的404条永久登记、现有简报、用户明确列出的既有文献、本轮可见对话及可访问清单，并按DOI、arXiv ID、规范化题名和已知版本别名去重。无法访问的完整旧对话和未同步私人清单不在覆盖范围内，因此不声称绝对完全去重。",
      "selectedPapers":refs,"papers":[],"topPapers":[
        {"doi":j1["doi"],"reason":"随机实验直接检验隐喻与人物受众相似性的交互，最接近本国神话人物类比与价值契合的正交设计。"},
        {"doi":j3["doi"],"reason":"两项大样本实验显示虚构性不能消除一致性选择，直接补上从可见到选择接触这一前置环节。"},
        {"doi":j2["doi"],"reason":"预注册研究提供相似性操纵未奏效的负面证据，可帮助严格区分客观匹配、感知文化接近和加工流畅性。"}]},
}

(root / f"{date}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
index_path = root / "index.json"; index = [x for x in json.loads(index_path.read_text()) if x["date"] != date]
count = sum(len(g["papers"]) for g in groups)
index.insert(0,{"date":date,"title":data["title"],"summary":data["summary"],"edition":data["edition"],"count":count,"file":f"{date}.json"})
index_path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n")

state_path=root/"rotation-state.json"; state=json.loads(state_path.read_text()); state["updatedAt"]=date
nms=state["communication"]["nms"]
nms.update(lastAttemptAt=date,lastCheckedAt=date,status="partial",reason="Official OnlineFirst directory reported 203 entries, but publisher access controls allowed reliable verification of only the four newest research articles. Partial snapshot published; rotation completion not advanced.")
nms["directoryObservation"]={"checkedAt":date,"url":"https://journals.sagepub.com/toc/NMS/0/0","complete":False,"reportedTotal":203,"verifiedResearchArticleCount":4,"scopeNote":"Newest four research articles verified individually; remaining directory pagination inaccessible."}
nature=state["general"]["nature"]
nature.update(lastAttemptAt=date,lastCheckedAt=date,status="completed",lastCompletedAt=date,lastRecommendedDoi=general["doi"],publicationDate=general["publicationDate"],socialScienceAssessment="confirmed")
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n")
print(f"Wrote {date} with {count} papers")
