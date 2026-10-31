import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site/data"
date = "2026-10-31"
unavailable = "本次核验未取得允许本站完整转载摘要的明确许可。请通过来源链接查看原文摘要，中文概述依据可核验证据原创。"


def paper(**values):
    item = {
        "evidence": "摘要核验",
        "relevance": "研究启示是本简报基于论文证据作出的推论，不是论文作者已经检验的结论。",
        "abstractMode": "unavailable",
        "originalAbstract": "",
        "abstractUnavailableReason": unavailable,
        "readingPriority": "normal",
        "priorityReason": "与当日主题相关，且题录、摘要与发表状态可以核验。",
        "readingUse": "用于理论框架、研究设计或结果讨论。",
        "researchConnection": "作为一般研究追踪，和博士论文的具体关系见逐篇说明。",
    }
    item.update(values)
    item.setdefault("abstractZh", item["takeaway"])
    item.setdefault("abstractSource", item["url"])
    return item


def dissertation(**values):
    defaults = {
        "publicationType": "journal",
        "publicationStatus": "published",
        "peerReviewed": True,
        "topicIds": ["culture"],
        "category": "博士论文专题 · 同行评审",
    }
    defaults.update(values)
    return paper(**defaults)


cross = [
    paper(
        title="When Personas Become Harmful: Guiding LLMs with Global Citizenship Values Alignment",
        titleZh="当人格设定产生伤害：以全球公民价值引导大语言模型",
        authors="Siqi Shen, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, Rada Mihalcea",
        year=2026,
        venue="arXiv:2610.33899 · EMNLP 2026 Main Conference accepted",
        source="arXiv",
        sourceDatabase="arXiv",
        category="其他研究 · 最新",
        url="https://arxiv.org/abs/2610.33899",
        doi="https://doi.org/10.48550/arXiv.2610.33899",
        arxivId="2610.33899",
        topicIds=["culture", "sycophancy", "methods"],
        takeaway="作者把Schwartz价值维度映射到人格设定，构建约1.1万个争议主题与价值人格配对。代理式搜索在商业模型中诱发有害回答的成功率超过47%，而可控对齐模型在多数样本上同时改善安全性和人格遵循。",
        theory="区分尊重多元价值表达与无条件迎合人格设定，主张以全球公民原则作为价值多元下的最低共同边界。",
        data="约1.1万个争议主题与价值人格配对，价值人格映射到Schwartz Value Survey维度。公开摘要没有报告各价值维度的样本分布。",
        method="代理式流程迭代细化主题与人格，测试已对齐商业模型的有害响应，再训练推理时可调节人格遵循与安全权衡的模型。",
        results="代理式流程诱发有害回答的成功率超过47%。可控模型在多数样本上比基线更安全，同时保持更高人格遵循。",
        limitations="arXiv版本虽已获EMNLP 2026主会接收，但本站仅核验摘要，没有核验正文中的模型清单、评估者一致性、统计检验和跨语言稳健性。模型价值人格不等于真实受众价值观。",
        selectionBucket="latest",
        publicationDate="2026-10-24",
        publicationDatePrecision="day",
        publicationDateSource="https://arxiv.org/abs/2610.33899",
        publicationType="conference-preprint",
        readingUse="用于Schwartz价值操作化、AI迎合边界和安全性评估。",
        researchConnection="可借鉴其把抽象价值维度转为可操纵人格描述的方法，但博士论文必须测量真实受众价值，并区分价值契合、道德评价和文化接近。",
    ),
    paper(
        title="LLM-Enhanced Speech Translation for AI-Mediated Multilingual Healthcare Communication: A Cascade Architecture and Experimental Evaluation",
        titleZh="面向多语医疗沟通的LLM增强语音翻译：级联架构与实验评估",
        authors="Francisco Javier Lima Florido, Gloria Corpas Pastor",
        year=2026,
        venue="SSRN Working Paper 7649668",
        source="SSRN",
        sourceDatabase="SSRN",
        category="其他研究 · 最新",
        url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7649668",
        doi="https://doi.org/10.2139/ssrn.7649668",
        topicIds=["culture", "methods"],
        takeaway="COVInterpreter把语音识别、机器翻译、LLM与检索增强生成组合为可替换的级联系统。合成患者语音实验中，级联配置比直接音频配置产生更少无效输出并取得更高F1，但所有配置的分类性能仍有限。",
        theory="把多语专业沟通分解为语音转写、翻译、知识检索与报告生成环节，强调模块化架构便于定位跨语言信息损失。",
        data="基于既有临床数据集生成的合成患者语音描述。当前实验只评估二元COVID-19分类，公开记录未给出样本数和语言组合。",
        method="自动化实验框架比较级联式与直接音频式配置，以无效输出和F1评估分类与沟通管线表现。",
        results="级联方案的无效输出更少且F1更高，但整体分类性能有限，配置差异不能只归因于架构。",
        limitations="SSRN论文尚未同行评审，且许可页明确保留权利。合成语音与二元分类不足以代表真实临床对话，摘要未提供具体F1、误差区间和语言别表现。",
        selectionBucket="latest",
        publicationDate="2026-10-22",
        publicationDatePrecision="day",
        publicationDateSource="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7649668",
        publicationType="working-paper",
        readingUse="用于跨语言传播管线、模块消融和错误定位。",
        researchConnection="提示本国相似神话人物类比若经过翻译与生成式改写，应分别记录翻译、类比和叙事生成造成的变化，不能把总效果归于单一文化机制。",
    ),
    paper(
        title="HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior",
        titleZh="HouseholdBench：评估大语言模型预测家庭经济行为的能力",
        authors="Jin Huang, Diego Ferreras Garrucho, Yutong Xie, Walter M. Yuan, Qiaozhu Mei, Chen Lian, Jonathon Hazell",
        year=2026,
        venue="NBER Working Paper 35927",
        source="NBER",
        sourceDatabase="NBER",
        category="其他研究 · 最新",
        url="https://www.nber.org/papers/w35927",
        doi="https://doi.org/10.3386/w35927",
        identityAliases=["arxiv:2610.07563", "doi:10.48550/arxiv.2610.07563"],
        topicIds=["methods", "sycophancy"],
        takeaway="HouseholdBench汇集6项美国家庭调查和32项预测任务。多数LLM优于不变化基线，最佳模型将数值结果误差降低12.2%，但梯度提升树在多数任务仍居首；微调并汇总每个观测的16次预测，可让40亿参数开放模型接近专有模型。",
        theory="把LLM视为可量化的家庭行为预测器，重点检验模型是否能从历史行为、人口特征和宏观条件预测政策变化下的调整。",
        data="6项美国家庭调查，32项数值、分类和概率任务，覆盖消费、收入、劳动、预期和住房。可重新分发的17项任务含1,670,349行，全部32项任务合计4,663,568行。",
        method="比较13个专有或开放权重LLM、不变化基线和梯度提升树，并检验微调及每个观测16次预测聚合。政策响应任务不进入微调，用于外推检验。",
        results="多数LLM优于不变化基线，最佳模型将数值误差降低12.2%，但梯度提升树多数任务第一。微调加多次预测聚合使40亿参数开放模型匹配专有模型水平，并外推到未用于微调的政策响应任务。",
        limitations="NBER工作论文尚未同行评审。NBER只给出2026年10月的月份精度，不能虚构具体日期。跨任务系统性高估和低估说明平均性能不能替代分任务校准。",
        selectionBucket="latest",
        publicationDate="2026-10",
        publicationDatePrecision="month",
        publicationDateSource="https://www.nber.org/papers/w35927",
        publicationType="working-paper",
        readingUse="用于预测基准、外推验证和多模型比较。",
        researchConnection="可借鉴其任务分层与政策外推设计，把理解、好感、人物认同和传播意向设为独立任务，并比较简单统计模型与复杂文本模型。",
    ),
]


hcr_new = dissertation(
    title="Narrative character networks are associated with storytelling success",
    titleZh="叙事人物网络结构与故事成功相关",
    authors="Xuanjun Gong, Allison Eden, Frederic R. Hopp, Anna W. Wolfe, Matthew Grizzard",
    year=2026,
    venue="Human Communication Research, Advance Article, hqag004",
    source="Human Communication Research",
    category="传播学顶刊推荐 · Online First",
    url="https://doi.org/10.1093/hcr/hqag004",
    doi="https://doi.org/10.1093/hcr/hqag004",
    publicationStatus="online-first",
    publicationDate="2026-10-26",
    publicationDatePrecision="day",
    publicationDateSource="https://academic.oup.com/hcr/advance-articles",
    peerReviewSource="https://academic.oup.com/hcr/advance-article/doi/10.1093/hcr/hqag004/9002324",
    apaCitation="Gong, X., Eden, A., Hopp, F. R., Wolfe, A. W., & Grizzard, M. (2026). Narrative character networks are associated with storytelling success. Human Communication Research. Advance online publication. https://doi.org/10.1093/hcr/hqag004",
    takeaway="两项大规模计算研究分析1万余部小说和1000部电影剧本。较低人物聚类同时关联更高小说下载量与电影评分，较高模块度只关联小说成功，较短路径只关联电影评分；网络指标对结果的解释量约为2.2%。",
    theory="以图学习理论和情境模型解释叙事人物网络如何影响结构可学习性、加工流畅性与总体接收，同时把人物间关系而非单个人物作为分析单位。",
    data="研究一使用Standardized Project Gutenberg Corpus中1万余部英文长篇小说，研究二使用1000部电影剧本，并匹配小说下载量和电影受众评分。",
    method="用自然语言处理抽取人物与互动，构建人物网络，计算规模、密度、最短路径、聚类和模块度，再以多元回归关联总体受众结果并控制文本长度、年代代理和类型。",
    results="低聚类在小说和电影中都与更高成功相关。高模块度只预测小说下载量，短路径只预测电影评分。加入控制变量后，小说中部分规模关系消失；两个数据集的调整R方均约0.022。",
    limitations="作者直接测量的是叙事结构与总体下载或评分的关联，没有直接测量个体加工流畅性、运输、理解或人物认同。观察性设计不能确认网络结构导致成功。",
    readingUse="用于叙事结构、人物关系网络和加工流畅性机制。",
    researchConnection="可把中国神话人物及其关系建成网络，检验类比版本是否降低跨文化受众的结构理解成本，但个体接收仍需独立测量。",
    readingPriority="high",
    priorityReason="它是本期最新传播学顶刊论文，直接连接人物关系结构、加工流畅性和总体接收，并提供可复用的计算方法。",
    hypothesisImplication="简报推论：在人物与事件相同的条件下，更易形成清晰社区和主角中心结构的叙事可能提高理解与运输，进而促进人物认同。",
    manipulationImplication="简报推论：保持人物价值行为不变，只改变人物关系的呈现顺序、桥接角色和模块边界，以操纵结构可学习性。",
    measurementImplication="简报推论：同时测量网络结构、主观加工流畅性、事实理解、运输、人物认同和传播意向，并预先区分总体评分与个体心理结果。",
    evidence="全文核验",
    abstractMode="full",
    originalAbstract="Narratives are central to human communication and entertainment, yet why some stories captivate audiences better than others remains poorly understood. Building on theories emphasizing character interdependence, this study introduces a network-based framework for examining storytelling success. We conceptualize narratives as networks composed of characters and their interactions and apply large-scale computational analysis to over 10,000 novels and 1,000 film screenplays. Structural features of these networks are related to storytelling success: lower clustering is associated with greater novel popularity and higher film ratings, whereas higher modularity is associated only with novel popularity and shorter path lengths only with film ratings. These findings demonstrate that storytelling success is related to how characters are structurally connected and organized. By formalizing story architecture as a measurable network, we provide a scalable framework for advancing media entertainment theory, linking cognitive models of graph learning with the structural organization of stories at scale.",
    abstractLicense="CC BY 4.0 https://creativecommons.org/licenses/by/4.0/；原文摘要未作实质修改，作者及来源见题录。",
)


dissertation_papers = [
    dissertation(
        title="Reader-character identity interdependence: An empirical investigation of congruence in identity and reading",
        titleZh="读者与人物身份的相互依存：身份契合与阅读的经验研究",
        authors="Millicent Weber, Rachel Noorda",
        year=2026,
        venue="Poetics, 114, 102075",
        source="Elsevier / Australian National University",
        url="https://doi.org/10.1016/j.poetic.2026.102075",
        doi="https://doi.org/10.1016/j.poetic.2026.102075",
        publicationDate="2026-01-16",
        publicationDatePrecision="day",
        publicationDateSource="https://openresearch-repository.anu.edu.au/entities/publication/01939350-9269-48e5-8f34-f07483fa4298",
        peerReviewSource="https://researchportalplus.anu.edu.au/en/publications/reader-character-identity-interdependence-an-empirical-investigat/",
        apaCitation="Weber, M., & Noorda, R. (2026). Reader-character identity interdependence: An empirical investigation of congruence in identity and reading. Poetics, 114, Article 102075. https://doi.org/10.1016/j.poetic.2026.102075",
        takeaway="对美国、英国和澳大利亚3089名读者的调查显示，各类读者都会在阅读中寻求人物认同，但多重边缘化读者必须主动跨越主流再现结构寻找可认同人物，同时仍会阅读主流规范空间；主导身份读者较少反向跨越。",
        theory="以交叉性身份和社会参与理解阅读选择，强调身份契合不是单一人口属性相同，而是读者在不平等再现结构中寻找自我位置的过程。",
        data="2022年美国、英国和澳大利亚3089名读者的在线调查，包含多维身份、阅读实践和自由文本。",
        method="以读者自报阅读实践和多重身份进行描述性与批判性比较，并分析自由文本中的反向意见。公开摘要未给出加权、模型和缺失处理。",
        results="所有读者都报告通过人物寻求认同。多重边缘化读者更主动寻找代表性并跨越主流规范空间，收入和教育可能限制接触多样书籍；少数人反对问卷把身份与阅读联系。",
        limitations="横断面自报不能识别人物代表性对认同的因果效应。国家样本和招募代表性尚未从摘要核验，身份契合也不是Schwartz价值契合。",
        readingUse="用于文化内外群体边界、身份可见性和样本异质性。",
        researchConnection="提醒博士论文把文化边界视为结构条件，并检验边缘化经历和媒介可得性是否改变价值契合到人物认同的路径。",
        readingPriority="high",
        priorityReason="它用大样本直接展示人物认同如何受多重身份和再现结构约束，可帮助避免把文化内外群体简化为单一国籍。",
        hypothesisImplication="简报推论：文化外群体身份不必削弱人物认同，深层价值契合的作用可能在缺少表层代表性的受众中更强。",
        manipulationImplication="简报推论：分开操纵人物文化身份标签和价值行为，并记录受众多重身份与既有代表性经验。",
        measurementImplication="简报推论：除国籍外测量身份中心性、边缘化经历、代表性可得性、价值契合和人物认同。",
    ),
    dissertation(
        title="Encountering the ‘familiar stranger’: Activating latent cultural identification among Vietnamese tourists in China",
        titleZh="遭遇熟悉的陌生人：越南游客在中国的潜在文化认同激活",
        authors="Thi Lam Nguyen, Zongkun Guo, Ganghua Chen",
        year=2027,
        venue="Tourism Management, 118, 105507",
        source="Elsevier",
        url="https://doi.org/10.1016/j.tourman.2026.105507",
        doi="https://doi.org/10.1016/j.tourman.2026.105507",
        publicationStatus="online-first",
        publicationDate="2026-08",
        publicationDatePrecision="month",
        publicationDateSource="https://www.sciencedirect.com/science/article/pii/S0261517726001172",
        peerReviewSource="https://www.sciencedirect.com/science/article/pii/S0261517726001172",
        apaCitation="Nguyen, T. L., Guo, Z., & Chen, G. (2027). Encountering the ‘familiar stranger’: Activating latent cultural identification among Vietnamese tourists in China. Tourism Management, 118, Article 105507. https://doi.org/10.1016/j.tourman.2026.105507",
        takeaway="对41名赴华越南游客的访谈显示，物质、社会和媒介线索让沉积的共享文化意义变得可见，内部文化图式帮助解释这些线索，情感共鸣进一步提高自我相关性；反应从顺应、探询到重释和共创不等。",
        theory="以图式激活解释文化接近情境中的潜在文化认同，提出熟悉的陌生人状态，即形式可识别但意义未必充分理解。",
        data="41名在中国旅行的越南游客深度访谈，围绕中国文化线索、既有媒介记忆、情感反应和行为参与。",
        method="质性访谈构建时间分层的过程模型，识别物质、社会和媒介三类触发线索及不同参与反应。",
        results="共享文化线索通过既有图式被解释，情感共鸣是条件性加速器而非必然结果。熟悉性可与差异和不理解并存，行为参与又反过来重塑意义。",
        limitations="旅游情境、越南受众和质性样本限制外推。研究没有实验操纵，也没有区分人物认同与对国家文化的总体认同。",
        readingUse="用于本国相似神话人物类比、文化熟悉性和图式激活。",
        researchConnection="这是本国相似神话人物类比最接近的机制证据之一，说明类比可能先提高可识别性，再经图式解释和情感共鸣影响接收。",
        readingPriority="high",
        priorityReason="它直接展示文化接近并非简单好感，而是可识别、可解释和情感自我相关性的分阶段过程。",
        hypothesisImplication="简报推论：本国相似人物类比先提升文化线索可识别性和解释流畅性，再影响理解与人物认同，情感共鸣构成条件性中介。",
        manipulationImplication="简报推论：设置无类比、表层形式类比和深层价值类比三组，并保持目标人物信息量一致。",
        measurementImplication="简报推论：分别测量可识别性、文化熟悉性、图式激活、加工流畅性、情感共鸣、理解和人物认同。",
    ),
    dissertation(
        title="The Impact of Perceptual Fluency and Schema Congruence Manipulation with Hetero- and Homosexual Characters: Are Gender Schemas more Entrenched than Sexuality?",
        titleZh="知觉流畅性与图式一致如何影响异性恋和同性恋人物判断",
        authors="Emalie Hendel, Annie Roy-Charland, Denis Vaillancourt, Joël Dickinson",
        year=2026,
        venue="Journal of Psycholinguistic Research, 55(3), Article 42",
        source="Springer Nature / PubMed",
        url="https://doi.org/10.1007/s10936-026-10229-w",
        doi="https://doi.org/10.1007/s10936-026-10229-w",
        publicationDate="2026-04-04",
        publicationDatePrecision="day",
        publicationDateSource="https://pubmed.ncbi.nlm.nih.gov/41934502/",
        peerReviewSource="https://pubmed.ncbi.nlm.nih.gov/41934502/",
        apaCitation="Hendel, E., Roy-Charland, A., Vaillancourt, D., & Dickinson, J. (2026). The impact of perceptual fluency and schema congruence manipulation with hetero- and homosexual characters: Are gender schemas more entrenched than sexuality? Journal of Psycholinguistic Research, 55(3), Article 42. https://doi.org/10.1007/s10936-026-10229-w",
        takeaway="实验把人物性取向、男性化或女性化属性以及流畅或不流畅呈现结合，并以眼动推断加工速度。涉及女同性恋人物且与女性性别角色不一致的材料阅读更慢，说明性别图式可能比性取向图式更顽固。",
        theory="区分知觉流畅性与语义图式一致，两者都可能改变信息加工和人物判断，但不同图式的约束强度并不相同。",
        data="成人参与者阅读异性恋或同性恋人物的文字描述。公开索引未给出样本量、国家和试次数。",
        method="交叉操纵人物性取向、性别属性一致性和呈现流畅性，以眼动阅读速度和属性判断量表测量加工与评价。",
        results="女性人物条件中，女同性恋人物在符合性取向刻板图式但违反女性性别角色时阅读显著更慢。结果支持图式层级可能比单一一致或不一致更重要。",
        limitations="公开索引不足以核验样本量、完整交互、效应量和刺激材料。性别与性取向图式不能直接等同文化或神话图式。",
        readingUse="用于加工流畅性、图式一致和竞争图式设计。",
        researchConnection="提示本国人物类比可能同时激活文化、道德和角色图式，若只操纵一个线索，其他更强图式可能覆盖预期效果。",
        priorityReason="它提供直接的实验和眼动证据，适合设计类比与图式一致的过程测量。",
        hypothesisImplication="简报推论：类比带来的流畅性收益取决于目标人物是否同时违反更强的道德或角色图式。",
        manipulationImplication="简报推论：把类比与目标人物行为的图式一致性正交操纵，并在预试中测量各图式强度。",
        measurementImplication="简报推论：增加阅读时长或眼动、主观流畅性、图式一致判断、道德评价和人物认同。",
    ),
    dissertation(
        title="Mediated Contact with LGBTQ Characters: Associations Between Recognizability, Parasocial Friendship, Wishful Identification, and LGBTQ Prejudice",
        titleZh="与LGBTQ人物的媒介接触：可识别性、寄生友谊、愿望认同与偏见",
        authors="Bartosz G. Żerebecki, Suzanna J. Opree, Joep Hofhuis",
        year=2025,
        venue="Communication Studies, 76(2), 186–204",
        source="Taylor & Francis",
        url="https://doi.org/10.1080/10510974.2024.2390703",
        doi="https://doi.org/10.1080/10510974.2024.2390703",
        publicationDate="2024-08-16",
        publicationDatePrecision="day",
        publicationDateSource="https://doi.org/10.1080/10510974.2024.2390703",
        peerReviewSource="https://www.tandfonline.com/doi/full/10.1080/10510974.2024.2390703",
        apaCitation="Żerebecki, B. G., Opree, S. J., & Hofhuis, J. (2025). Mediated contact with LGBTQ characters: Associations between recognizability, parasocial friendship, wishful identification, and LGBTQ prejudice. Communication Studies, 76(2), 186–204. https://doi.org/10.1080/10510974.2024.2390703",
        takeaway="247名美国居民的横断面调查显示，人物在个性、态度和社会经验上的深层可识别性与寄生友谊和愿望认同相关，并通过愿望认同与较低LGBTQ偏见形成直接和间接关联；寄生友谊与愿望认同并非可互换。",
        theory="把深层相似拆为个性、态度和经验可识别性，并区分寄生友谊与希望成为人物的愿望认同。",
        data="247名美国居民，围绕一个LGBTQ媒介人物报告三类深层可识别性、寄生友谊、愿望认同和LGBTQ偏见。",
        method="横断面问卷与潜变量结构方程模型，同时控制LGBTQ身份和年龄。测量模型及结构模型拟合达到作者设定的可接受标准。",
        results="深层可识别性与偏见存在直接和经愿望认同的间接关联。愿望认同比寄生友谊更直接关联态度结果，说明不同人物关系机制作用不同。",
        limitations="横断面自报不能确定因果，也不能排除原有低偏见导致更强认同。LGBTQ人物语境与跨文化神话接收存在重要差异。",
        readingUse="用于深层价值相似、人物关系机制和结果区分。",
        researchConnection="可将Schwartz价值契合放入态度可识别性维度，并检验人物认同、寄生关系和愿望认同是否是不同中介。",
        priorityReason="它把深层相似拆成可测量维度，并证明不同人物关系机制不能合并，直接服务理论模型精化。",
        hypothesisImplication="简报推论：价值契合更可能先提升态度可识别性，再通过人物认同或愿望认同影响好感和传播意向。",
        manipulationImplication="简报推论：用人物在关键两难中的行为操纵价值契合，而不是只在简介中贴价值标签。",
        measurementImplication="简报推论：分别测量个性、态度、经验可识别性，人物认同、寄生关系、愿望认同和传播意向，并检验区分效度。",
    ),
]


general = paper(
    title="The Fireside Database: Large-scale evidence from 25,419 psychedelic support interactions",
    titleZh="Fireside数据库：25419次迷幻体验支持互动的大规模证据",
    authors="Felix Schoeller et al.",
    year=2026,
    venue="Science Advances, 12, aeg4737",
    source="Science Advances",
    category="综合顶刊推荐 · 最新社会科学与公共健康",
    url="https://doi.org/10.1126/sciadv.aeg4737",
    doi="https://doi.org/10.1126/sciadv.aeg4737",
    topicIds=["methods"],
    takeaway="研究建立包含25419次支持热线互动、220名支持者和2777份事后满意度问卷的去标识数据库。求助发生在体验中还是体验后，比具体物质更能预测痛苦程度；数据还记录43起自报的引导者虐待事件。",
    theory="把非临床迷幻体验中的同伴支持视为可系统观察的公共健康与沟通过程，强调真实世界求助情境与临床试验不同。",
    data="2021年4月至2026年2月的25419次电话或文字互动，220名受训同伴支持者，2777份互动后满意度问卷，并包含开放文本和结构化元数据。",
    method="研究资源论文对去标识互动、支持者编码信息和事后问卷进行描述统计与比较分析，并公开数据和复现代码。",
    results="裸盖菇素占有物质编码互动的59.9%，大麻占12.8%。大麻的汇总痛苦率最高，但主要由使用者更常在体验中求助解释；相同求助类型内主要物质间痛苦率没有显著差异。",
    limitations="样本只代表主动联系热线的人，不能估计总体物质风险。物质、剂量与虐待事件多为自报，未独立核实。本站核验了AAAS发布记录与DOI，但出版方完整作者列表尚未在可访问目录中展开。",
    publicationDate="2026-10-30",
    publicationDatePrecision="day",
    publicationDateSource="https://doi.org/10.1126/sciadv.aeg4737",
    publicationType="journal",
    publicationStatus="published",
    peerReviewed=True,
    socialScienceAssessment="confirmed",
    socialScienceReason="研究对象为人的求助互动、同伴支持、体验情境与公共健康结果，采用大规模真实世界社会行为数据。",
    readingUse="用于自然发生互动数据库、支持者效应和选择偏差讨论。",
    researchConnection="与博士论文主题不直接，但其把互动文本、情境元数据和事后问卷连接的方法可用于跨文化人物接收的自然场景研究。",
)


prior_hcr = json.loads((root / "2026-10-17.json").read_text())["groups"][2]
toc = [{"title": hcr_new["title"], "url": hcr_new["url"], "articleType": "Research Article", "status": "new"}]
for entry in prior_hcr["collection"]["toc"]:
    toc.append({**entry, "status": "previously-recommended", "recommendedDate": "2026-10-17", "reviewUrl": "./?date=2026-10-17"})

groups = [
    {
        "id": "crossdisciplinary", "label": "其他研究", "target": 5, "sortBy": "split",
        "selectionBuckets": [{"id": "latest", "label": "最新", "target": 3}, {"id": "cited", "label": "高被引", "target": 2}],
        "sourceCoverage": [{"database": x, "status": "included"} for x in ["NBER", "SSRN", "arXiv"]],
        "sortDescription": "最新3篇按首次公开日期降序，NBER、SSRN和arXiv各1篇。Google Scholar返回异常流量验证页，高被引2篇不使用替代指标，因而留缺。",
        "papers": cross,
    },
    {
        "id": "journals", "label": "传播学与社会科学", "target": 5, "sortBy": "citationCount",
        "journalPriorityNote": "先执行Google Scholar主题检索，再优先筛选传播学SSCI Q1或Q2期刊。原生页面被异常流量验证页阻断，无法完成规定发现与引用排序。",
        "sortDescription": "本栏必须按Google Scholar实际引用次数降序。本期没有取得可核验结果，因而留空。",
        "papers": [],
    },
    {
        "id": "communication-issue", "label": "传播学顶刊推荐", "unit": "issue", "target": 1, "sortBy": "issue",
        "collection": {
            "journalId": "hcr", "journalName": "Human Communication Research", "kind": "online-first",
            "title": "Human Communication Research · Advance Access · 2026-10-31在线集合",
            "url": "https://academic.oup.com/hcr/advance-articles", "checkedAt": date, "complete": True, "toc": toc,
            "scopeNote": "出版方Advance Access完整可见目录共4篇研究论文。与2026-10-17完整快照比较，新增1篇研究论文，其余3篇均链接至既往解读。",
        },
        "sortDescription": "不使用关键词，完整检查当前Advance Access。只对尚未推荐的新研究论文作完整解读。",
        "papers": [hcr_new],
    },
    {
        "id": "general-science", "label": "综合顶刊推荐", "target": 1, "sortBy": "publicationDate", "rotationJournalId": "science-advances",
        "sortDescription": "今天轮到Science Advances。不使用关键词，检查2026年10月30日最新一期，选择最新且社会科学或公共健康属性明确的研究。",
        "papers": [general],
    },
]

selected = [hcr_new["doi"]] + [p["doi"] for p in dissertation_papers]
data = {
    "schemaVersion": 6,
    "date": date,
    "timezone": "Asia/Shanghai",
    "edition": "正式第28期",
    "title": "人物网络、文化图式与深层相似：接收机制的结构化证据",
    "summary": "本期完成NBER、SSRN和arXiv最新研究各1篇，核验Human Communication Research在线集合新增1篇研究论文，推荐Science Advances最新公共健康研究1篇，并为博士论文精选5篇尚未推荐的同行评审论文。Google Scholar异常流量限制导致高被引与主题期刊栏留缺。",
    "historyPolicy": "exclude-recommended",
    "journalPolicy": "ssci-communication-q1-q2-and-social-science",
    "searchPlatforms": ["Google Scholar", "NBER", "SSRN", "arXiv"],
    "activeTopicIds": ["culture", "sycophancy", "methods"],
    "searchSettings": {"source": "defaults + reading-plan", "lookbackDays": 30, "conflictNote": "当日没有生效的一次性用户设置，未来设置保持不变。culture继续以博士论文的人物接收、价值契合、文化边界、图式和类比机制为重点，同时保留culture、sycophancy和methods三个主题。"},
    "notice": "本期逐篇依据可访问的出版方页面、权威索引、官方摘要或正式记录核验。未读取正文关键部分时不标全文核验，无法核验的样本、系数和识别细节均明确说明。",
    "searchNote": "Google Scholar原生主题查询返回异常流量提示，随即停止，不绕过验证，也不以其他索引数字冒充引用次数。NBER、SSRN和arXiv通过公开域名网页发现并回到官方记录核验。公开网页检索不冒称站内高级检索。博士论文专题另使用出版方和权威学术索引核验同行评审状态。",
    "themeSearches": [
        {"platform": "Google Scholar", "query": "(\"cultural transmission\" OR \"cross-cultural reception\" OR \"value congruence\" OR sycophancy OR \"text measurement\")", "timeRange": "不限年份；检索日期2026-10-31", "purpose": "culture、sycophancy和methods主题发现，随后筛期刊并核验被引次数", "status": "原生页面返回异常流量验证，未取得结果和引用次数，未绕过验证。"},
        {"platform": "NBER", "query": "site:nber.org/papers October 2026 (culture OR communication OR AI OR methods)", "timeRange": "优先近30日；检索日期2026-10-31", "purpose": "NBER最新候选发现", "status": "公开域名网页检索成功，入选论文的题名、作者、编号、月份和摘要由NBER论文页核验。"},
        {"platform": "SSRN", "query": "site:papers.ssrn.com/sol3/papers.cfm 2026 (culture OR narrative OR communication OR persuasion OR multilingual)", "timeRange": "优先近30日；检索日期2026-10-31", "purpose": "SSRN最新候选发现", "status": "公开域名网页检索成功，入选论文题名、作者、首次发布日、摘要和SSRN DOI由论文页或其官方PDF记录核验。"},
        {"platform": "arXiv", "query": "submittedDate:[202610010000 TO 202610312359] AND all:(culture OR value OR narrative OR communication OR social)", "timeRange": "2026-10-01至2026-10-31；检索日期2026-10-31", "purpose": "arXiv最新候选发现", "status": "公开摘要记录检索成功，入选论文的首次提交日期、作者、摘要和arXiv ID完成核验。"},
    ],
    "periodicalChecks": [
        {"platform": "Oxford Academic · Human Communication Research", "query": "当前完整Advance Access目录，不使用关键词", "timeRange": "检查日期2026-10-31", "purpose": "传播学顶刊整期轮换", "status": "官方目录完整可见4篇研究论文，较2026-10-17快照新增1篇。新增论文完成全文关键部分核验。"},
        {"platform": "Science Advances", "query": "2026年10月30日最新一期，不使用关键词", "timeRange": "检查日期2026-10-31", "purpose": "综合顶刊轮换推荐", "status": "最新一期及AAAS发布记录完成核验，入选1篇以人的求助互动和公共健康结果为对象的研究资源论文。"},
    ],
    "verificationLog": [
        {"platform": "Google Scholar", "query": "当日主题检索与引用次数", "timeRange": "核验日期2026-10-31", "purpose": "主题发现与引用次数排序", "status": "原生页面提示异常流量，停止后续请求。高被引2篇和主题期刊5篇留缺，不使用替代指标。"},
        {"platform": "NBER、SSRN与arXiv官方记录", "query": "其他研究3篇的题名、作者、日期、摘要、DOI或arXiv ID", "timeRange": "核验日期2026-10-31", "purpose": "逐篇身份、首次公开日期与摘要核验", "status": "3篇均完成官方记录核验。NBER与SSRN为未同行评审工作论文，arXiv记录注明已获EMNLP 2026主会接收。"},
        {"platform": "期刊出版方、PubMed和大学研究门户", "query": "博士论文5篇、HCR新增论文和Science Advances论文的题录、发表状态、DOI、摘要与研究设计", "timeRange": "核验日期2026-10-31", "purpose": "同行评审与逐篇内容核验", "status": "题录与同行评审状态完成核验。只有HCR开放全文完成正文关键部分核验，其他论文按摘要或权威索引证据表述。"},
    ],
    "groups": groups,
    "shortfallReason": "Google Scholar原生页面返回异常流量验证，无法取得实际引用次数，其他研究高被引2篇和传播学与社会科学5篇留缺。所有缺额均未以替代引用指标、非指定数据库或不完整目录补齐。",
    "periodicalCheckNote": "轮换栏目不使用主题关键词。Human Communication Research按当前完整在线集合检查；Science Advances按最新一期检查。",
    "coreTracking": [],
    "coreTrackingNote": "reading-plan与core-papers当日没有用户提交的核心论文请求，因此本期没有核心文献状态更新。",
    "dissertation": {
        "title": "从被看见到被接收",
        "timeRange": "优先检查2026-10-30上期发布以来的新发表研究。高相关新论文不足5篇后，扩展至2024年至2026年尚未推荐的同行评审论文，并把较早研究视为补充，不冒称当日最新。",
        "selectionNote": "本期精选5篇尚未推荐的同行评审论文。其中Human Communication Research新增论文同时属于轮换栏目和博士论文重点，采用DOI跨栏目引用，不重复完整解读。重点覆盖人物网络、身份契合、文化图式、加工流畅性和深层相似。",
        "historyCoverage": "已核对网站359条永久登记、截至2026-10-30的简报和博士论文专题、用户明确列出的既有文献及本轮可见对话，并按DOI、arXiv ID、规范化题名和已知版本别名去重。无法访问的完整旧对话和未同步私人清单不在覆盖范围内，因此不声称绝对完全去重。",
        "selectedPapers": selected,
        "papers": dissertation_papers,
        "topPapers": [
            {"doi": "https://doi.org/10.1093/hcr/hqag004", "reason": "以1万余部小说和1000部电影把人物关系结构、加工流畅性与总体接收连接起来，最适合建立叙事结构层变量。"},
            {"doi": "https://doi.org/10.1016/j.tourman.2026.105507", "reason": "直接提出熟悉的陌生人和图式激活过程，为本国相似神话人物类比提供最清晰的阶段性机制。"},
            {"doi": "https://doi.org/10.1080/10510974.2024.2390703", "reason": "把个性、态度和经验的深层相似与多种人物关系机制分开，最适合精化价值契合的操纵与测量。"},
        ],
    },
}

(root / f"{date}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

index_path = root / "index.json"
index = json.loads(index_path.read_text())
index = [row for row in index if row["date"] != date]
count = len(cross) + len(dissertation_papers) + 1 + 1
index.insert(0, {"date": date, "title": data["title"], "summary": data["summary"], "edition": data["edition"], "count": count, "file": f"{date}.json"})
index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

rotation_path = root / "rotation-state.json"
rotation_state = json.loads(rotation_path.read_text())
rotation_state["updatedAt"] = date
hcr = rotation_state["communication"]["hcr"]
hcr.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date,
           reason="Oxford Academic Advance Access directory was fully readable. One new Research Article appeared since the complete 2026-10-17 snapshot.")
hcr["onlineSnapshots"].append({"checkedAt": date, "url": "https://academic.oup.com/hcr/advance-articles", "complete": True,
    "dois": ["https://doi.org/10.1093/hcr/hqag004", "https://doi.org/10.1093/hcr/hqag003", "https://doi.org/10.1093/hcr/hqag002", "https://doi.org/10.1093/hcr/hqag001"],
    "firstOnlineDates": ["2026-10-26", "2026-07-26", "2026-04-30", "2026-01-27"]})
sciadv = rotation_state["general"]["science-advances"]
sciadv.update(lastAttemptAt=date, lastCheckedAt=date, status="completed", lastCompletedAt=date,
              lastRecommendedDoi="https://doi.org/10.1126/sciadv.aeg4737", publicationDate="2026-10-30", socialScienceAssessment="confirmed")
rotation_path.write_text(json.dumps(rotation_state, ensure_ascii=False, indent=2) + "\n")
