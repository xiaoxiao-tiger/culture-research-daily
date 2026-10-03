# 每日研究简报

网站：https://xiaoxiao-tiger.github.io/culture-research-daily/

每天上午10点（UTC+8）启动Google Scholar、NBER、SSRN、arXiv主题检索，完成后发布。分别展示实际检索式与执行状态，不提前限制期刊名称，不使用WoS。

两个栏目，共15篇：其他研究10篇，分最新5篇和高被引5篇，整体尽量覆盖NBER、SSRN、arXiv，无合格候选时由其他来源补足；传播学与社会科学5篇正式期刊论文，排除ESCI，不设数据库配额。高被引排序均使用Google Scholar实际次数，最新排序使用首次公开日期。

今天（2026-10-03）的测试简报已清空，不计入推荐历史。从下一期开始按DOI、arXiv ID、题名及核验的版本对应关系排除已推荐论文，推荐登记追加保存，跨栏目也不重复。

下一次检索设置通过所有者提交GitHub Issue保存。收藏保存在浏览器，支持阅读状态、笔记、导入和导出。完整摘要在许可允许时提供，否则附来源链接；理论和数据注明核验范围，质量优先。

发布前运行scripts/rebuild_registry.py追加历史，再运行scripts/validate.py、Python测试和Node测试；main推送后Actions部署GitHub Pages。具体规则见UPDATE_GUIDE.md。
