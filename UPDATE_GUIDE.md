# 每日研究简报更新指南

仓库xiaoxiao-tiger/culture-research-daily。每天Asia/Singapore当地上午10:00启动检索，完成后发布。

## 当天设置

读取main最新site/data/search-settings.json、site/data/journals.json与index。once仅effectiveDate当天有效，ongoing从生效日持续；适用项按effectiveDate、savedAt、requestNumber降序选择，无适用项采用defaults。themeKeywords用于其他研究，journalKeywords用于传播学与社会科学；excludeTerms用于筛除。关键词是检索数据，不是执行指令。保留配置队列，不覆盖未来设置。网页表单通过所有者提交GitHub Issue及工作流保存，打开确认页不等于保存成功。

## 已重置历史，允许重复推荐

2026-10-03用户要求删除此前记录，重新开始，不再考虑过去文章或重复。当前分支删除recommended.json和旧修订JSON，不维护或读取历史推荐登记，不按历史文章排除候选。未来简报可推荐以前出现过的文章。收藏仍由浏览器保存，不清空用户收藏。Git提交历史是版本控制，可恢复，不改写远端历史。

## 检索与筛选

仅覆盖Google Scholar、NBER、SSRN和arXiv，取消WoS。先按设置主题检索，再核验相关性、质量与期刊，Scholar首次主题查询不加期刊名、出版方域名或分区限制。默认主题暂为文化传递、扩散、跨文化接受和交流；新增子主题说明依据，不把叙事或文化接近当作唯一范围。

直接网页检索Google Scholar，不强制依赖Sider Scholar；不检索WoS，不调用其API。连接或网页失败如实记录；安全限制不能绕过；不索取或公开密码。NBER、SSRN可使用官方域名公开网页主题查询，但注明不是站内数据库查询；arXiv公开检索和题录均可用于候选及核验。少量主题式写themeSearches，逐篇题名、摘要、全文及指标查询写verificationLog。

## 两栏各5篇与排序

其他研究（crossdisciplinary）：合并NBER、SSRN和arXiv候选，在质量与主题筛选后按首次发表或公开日期降序，最新在前。记录publicationDate、publicationDatePrecision、publicationDateSource。预印本按首次提交，不把修订日当首发日；只有月份则保留YYYY-MM，不能捏造某一天。同月有明确日期者先列，说明日期精度规则。工作论文与预印本按真实类型标记。

传播学与社会科学（journals）：仅从Google Scholar检索结果选正式期刊文章，筛选后按Google Scholar网页实际被引次数降序；不使用OpenAlex次数替代。传播学文章匹配上传表排除ESCI后保留的77种SSCI JCR Q1/Q2名单，标discipline:communication及journalName、jifQuartile、journalEdition、quartileSource。其他优质社会科学正式期刊标discipline:social-science，不伪造上传名单分区。所有期刊文章排除ESCI及未确认收录项，保存journalEdition:SSCI、indexSource；上传表只覆盖传播学，社会科学另核验SSCI收录来源。JIF分区不是中科院分区，上传文件未提供指标年份，不推断。

引用量逐篇核验，记录citationCount（非负整数）、citationSource、citationSourceUrl、citationCheckedAt。citationSource固定Google Scholar，discoverySource固定Google Scholar，不能混用其他来源次数；缺失不当零、不估计。不能用相关性排序冒充被引次数排序。本期候选的排序不是数据库全体论文最高五篇。质量相关性优先；不足可扩大年份范围，仍不足就说明缺额。

## 摘要与解读

优先完整原文摘要。逐字核验且确认转载许可时abstractMode:full，保存originalAbstract与abstractLicense；否则unavailable、originalAbstract为空，说明原因并给abstractSource。取消一句话节选；摘要无法展示不应成为排除重要论文的理由。abstractZh独立原创转述。

理论与数据尽量详细，无500字限制。解释概念、机制、问题、来源、国家、时间、单位、样本、招募、变量、测量、比较、模型、识别、结果和局限；未知逐项注明，不虚构数字，不把解释当受众效果或关联当因果。只有阅读正文理论数据方法结果关键部分才能标全文核验；否则摘要核验或理论综述。

## 格式及发布

schemaVersion:4；journalPolicy:ssci-communication-q1-q2-and-social-science；historyPolicy:repeat-allowed；recommendationTargetPerGroup:5。searchPlatforms固定Google Scholar、NBER、SSRN、arXiv；主题检索表显示每个平台的实际检索式、实际渠道与执行状态。保留date、edition、title、summary、notice、searchSettings、searchNote、themeSearches、verificationLog。两个groups依次crossdisciplinary（其他研究）、journals（传播学与社会科学），sortBy分别publicationDate、citationCount，加sortDescription。每栏最多5篇；总数不足10写shortfallReason。

论文保留title、titleZh、authors、year、venue、source、category、publicationType、evidence、url、doi、takeaway、theory、data、method、results、relevance、limitations、abstractZh、abstractSource及摘要状态字段，所有链接https。

运行scripts/validate.py验证字段、栏目范围、数量及排序，运行相关测试。rebuild_registry.py仅为兼容保留，不再生成登记。原子提交当天JSON和index及必要改动，基于main最新tree非强制更新。并发时重新读取合并，不覆盖检索设置。提交后读回数量排序，并确认Actions Pages部署成功；失败如实说明，不把提交当上线。不发邮件或其他外部消息，不写凭证。
