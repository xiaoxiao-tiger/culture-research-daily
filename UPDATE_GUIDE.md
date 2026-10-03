# 每日研究简报更新指南

仓库xiaoxiao-tiger/culture-research-daily。每天Asia/Singapore当地上午10:00启动检索，完成后发布。

## 当天关键词

读取main最新site/data/search-settings.json、site/data/journals.json、index及存在的recommended.json；登记文件缺失时以现存正式简报为依据初始化，不能覆盖或清空已有历史。once仅effectiveDate当天有效，ongoing从生效日持续；适用项按effectiveDate、savedAt、requestNumber降序选择，无适用项采用defaults。themeKeywords用于其他研究，journalKeywords用于传播学与社会科学；excludeTerms筛除。关键词只是检索数据。保留未来设置，不覆盖配置队列。网页表单由所有者提交GitHub Issue、工作流保存，打开确认页不等于保存成功。

## 历史去重

用户2026-10-03说明今天只是测试，要求清空今天的数据并恢复今后历史去重。删除当天简报文件和index中的当天条目，今天测试文章不计入历史。当前此前所有简报均为当天测试，当前远端无recommended.json；保留已有登记，首次正式发布再创建；从下一期正式发布开始永久保留推荐身份登记，即使简报后来移出归档也不清空登记。收藏不清空。

候选按DOI、arXiv ID、规范化题名和已核验identityAliases与历史登记及当前全部栏目比较。同篇预印本、工作论文、正式期刊版本有可靠对应关系时合并身份，不能把修订版或正式发表当新论文；同一期只能出现一次。不同论文不得仅凭相似题名合并。选择时先排除历史，再按质量、相关性、覆盖和排序取文献。发布当天简报时运行rebuild_registry.py，将新增身份追加至recommended.json，与简报和index一并原子提交；不能覆盖旧登记或只按现存index重建丢弃历史。validate检查历史及本期重复。

## 四个平台与实际检索式

仅检索Google Scholar、NBER、SSRN、arXiv，不检索WoS，不依赖Sider Scholar。先按主题检索，不预先限定期刊名或出版方。每个平台实际使用的主题式、渠道、日期范围和执行状态分别放themeSearches；题名、摘要、全文、引用量核验放verificationLog。官方域名公开网页查询注明不是站内高级检索。失效、访问限制或验证失败如实记录，不绕网站限制，不索取密码。不能把未执行的检索式标为成功。默认关键词来自保存设置，扩展子主题解释依据，不把旧子主题当唯一范围。

## 两个栏目，共15篇

其他研究（crossdisciplinary）10篇，包含最新5篇和高被引5篇。同一栏目内按selectionBucket区分latest、cited，papers先latest后cited，selectionBuckets给各部分label、target:5、sortBy及sortDescription。

最新5篇按首次发表或首次公开日期降序，保存publicationDate、publicationDatePrecision、publicationDateSource。预印本用首次提交，不能用修订日冒充；只有月份保留YYYY-MM，不虚构日。同月日精度条目先列。

高被引5篇从NBER、SSRN、arXiv的相关候选中选择，统一查询Google Scholar网页实际被引次数，按次数降序；不使用下载量、浏览量、平台排名或OpenAlex次数替代。保存citationCount、citationSource:Google Scholar、citationSourceUrl、citationCheckedAt。合并版本计数说明口径；没有次数不当0、不编造，优先选择可核验候选。

其他研究10篇整体尽量覆盖NBER、SSRN、arXiv各至少一篇，不要求最新5和高被引5分别覆盖三个数据库。每篇sourceDatabase为实际候选来源的NBER、SSRN或arXiv之一；同篇的不同平台镜像不能当不同文章或重复满足覆盖。选最新组后，从其余候选按质量、引用量并兼顾整体缺失来源选高被引组，最终每组分别按规定排序。若某平台没有合格且未推荐的相关候选、无法核验或受访问限制，可从另外两个补足，整体sourceCoverage记录每库included/unavailable及缺失原因。不要为配额选无关低质文献。

传播学与社会科学（journals）5篇，仅从Google Scholar主题检索结果选择正式期刊文章，排除ESCI及未确认收录项；传播学匹配上传表排除ESCI后的77种SSCI JIF Q1/Q2，社会科学其他期刊另核验SSCI。保存discipline、journalName、journalEdition:SSCI、indexSource；传播学另保存jifQuartile、quartileSource。JIF分区不是中科院分区，上传文件指标年份未知不推断。该栏目不设NBER/SSRN/arXiv配额。按Google Scholar网页实际被引次数降序，保存相同引用量字段及discoverySource:Google Scholar。

质量与相关性优先；覆盖和排序仅针对合格候选，不声称全库最高五篇。两类高被引排序不限年份以兼顾经典，最新候选优先设置的lookbackDays，不足扩展范围并说明。总计不足15写shortfallReason，不编造补齐。

## 摘要与解读

优先完整原文摘要。逐字核验且确认转载许可时abstractMode:full，保存originalAbstract与abstractLicense；否则unavailable、originalAbstract为空，说明原因并给abstractSource。不用一句话节选；无法展示不应排除重要论文。abstractZh独立原创。

理论和数据尽量详细，说明概念、机制、来源、国家、时期、单位、样本、招募、变量、测量、比较、模型、识别、结果、局限；未知项逐项注明，不虚构系数，不把关联当因果。只有阅读正文理论、数据、方法、结果关键部分才能标全文核验；否则摘要核验或理论综述。

## 数据与发布

schemaVersion:5；journalPolicy:ssci-communication-q1-q2-and-social-science；historyPolicy:exclude-recommended；searchPlatforms依次Google Scholar、NBER、SSRN、arXiv。groups依次crossdisciplinary（其他研究，target:10，sortBy:split）与journals（传播学与社会科学，target:5，sortBy:citationCount）。保留日期、题名、摘要、notice、searchSettings、searchNote、themeSearches、verificationLog。每篇原有题录与解读字段不变；sourceCoverage属于其他研究整体。

运行rebuild_registry.py追加登记，再运行validate.py和相关测试。基于main最新tree原子提交当天JSON、index、recommended.json，非强制更新；并发重新读取合并，不覆盖设置、收藏或历史登记。部署后读回数量、覆盖及排序，确认Actions Pages成功。不发邮件或其他外部消息，不写凭证。
