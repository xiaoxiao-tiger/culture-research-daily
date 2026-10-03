# 每日文献简报更新指南

目标仓库：`xiaoxiao-tiger/culture-research-daily`，默认分支main。按Asia/Singapore当天日期建立一期，只更新简报数据。网站有两个tab：跨学科精选10篇、传播学与社会科学期刊10篇，合计20篇；同一期两栏不重复。

## 检索与筛选

读取本指南、数据索引及历史期次，按DOI和题名去重。优先近期新增或重大更新，补充未推荐过的经典时明确标注。没有足够可核验文献时报告不足，不编造、不复用旧内容冒充每日新增。

主题覆盖文化传播、扩散、演化、跨文化接受、文化接近、神话与叙事、影视游戏全球流动、媒介和平台传播。跨学科栏访问可用的NBER、Google Scholar、SSRN、arXiv连接及公开网页；每次实际检查可访问状态，不沿用历史故障说明。Google Scholar在2026-10-03认证后查询成功，不保证后续始终可访问。

期刊栏独立选10篇正式期刊文章，优先传播学并纳入相关社会科学，建议约7篇传播学、3篇社会科学，按实际高质量文献调整。检索Journal of Communication、Communication Research、Human Communication Research、Communication Theory、New Media & Society、Journal of Computer-Mediated Communication、Media Culture & Society、Information Communication & Society，以及相关Poetics、Cultural Sociology、社会学、社会心理学等期刊。综合期刊只收与主题直接相关的社会科学文章。不得将NBER工作论文、仅arXiv预印本或会议论文冒充期刊文章；核对正式题录与版本。

候选检索式（按主题和平台调整并实际执行）：
- ("cultural transmission" OR "cultural diffusion" OR "cultural proximity") AND (media OR narrative OR entertainment)
- ("narrative persuasion" OR transportation OR identification) AND (culture OR audience)
- (myth OR folklore OR "cultural heritage") AND ("cross-cultural" OR reception OR diffusion)
- ("global audiences" OR "audience overlap") AND (language OR culture)

简报开头必须记录实际检索式、平台/渠道、实际时间范围、检索日期、用途与成功或受限状态。网页引擎的关键词查询不要改写成未执行的布尔数据库查询；限定域名搜索不要冒称直接使用数据库。可记录实际成功和失败的查询。时间范围优先上次成功更新之后，必要时逐步扩展并记录。

按相关性、理论贡献、数据与方法质量、研究价值和新颖性筛选，不虚构评分。优先合法开放全文：出版方→作者主页→大学仓储→可信工作论文库；检索完整题名加PDF，核对作者和版本。403不等于没有开放版本，不索取用户密码，不绕过访问控制。只有实际阅读理论、数据、方法、结果及局限关键部分后才标注“全文核验”；只有摘要则写“摘要核验”，不补写未知细节。

## 每篇写作要求

每篇提供原文摘要、来源和中文概述。`originalAbstract`必须逐字核对，不能把自己生成的英文写成原文。明确允许转载的摘要可完整展示（`abstractMode: full`），必须记录许可名称和可核验许可来源；许可不明确时仅给不超过25个英文单词的原文节选（`excerpt`）以及完整摘要页面链接。中文概述用原创转述，标明简报编写，避免贴近原文的大段翻译。开放访问或能下载PDF本身不等于允许转载。

理论与数据尽量详细，不再设置每篇500字上限；信息足够时可写约800–1500中文字符或更长，避免填充。理论写清名称、概念、机制链、假设、分析层次、边界及与相近理论区别。数据写清来源、国家地区、时段、分析单位、样本量、招募/抽样、纳入排除、关键变量及测量；模型文章和综述明确没有统一新样本。方法写研究设计、比较组、识别假设、控制、稳健性与估计范围。结果报告已核验数值及不确定性，不把关系写成因果。读不到的细节逐项写“未核验”，不靠常识补全。启示与原文发现分开，说明推广限制和版本。

## 数据格式（schemaVersion 2）

新建`site/data/YYYY-MM-DD.json`，保留日期、edition、title、summary、notice，并新增：
- `schemaVersion: 2`
- `searchNote`: 检索范围与限制说明
- `searchLog`: 数组，每项含platform、query、timeRange、purpose、status
- `groups`: 两项，依次为`{id: "crossdisciplinary", label: "跨学科精选", papers: [...]}`和`{id: "journals", label: "传播学与社会科学期刊", papers: [...]}`，各10篇。

每篇沿用title、titleZh、authors、year、venue、source、category、evidence、url、doi、takeaway、theory、data、method、results、relevance、limitations，并新增publicationType、originalAbstract、abstractMode、abstractSource、abstractZh；完整转载时加abstractLicense（包含许可及来源信息）。期刊栏publicationType必须为journal。evidence只允许全文核验、摘要核验、理论综述。source如实写发现渠道或出版来源。原文链接使用https。

更新`site/data/index.json`，新增或更新`{date,title,count:20}`，保留所有历史期次，同日重试不重复添加。旧schema仍能显示，不删历史。

## 写入与发布

读取main最新提交，基于当前tree在一个提交中写入期次和索引，非强制更新main；有并发修改时重新读取合并，不force覆盖。写入前运行scripts/validate.py或等效结构核验。提交后读回两个文件核对20篇、摘要、检索记录和完整正文，并检查GitHub Actions Pages部署结果。提交成功不等于上线成功。失败保留历史内容，如实报告。不得写入账号、凭证、私人聊天记录；不发邮件或其他外部消息。
