# 每日研究简报

网站：https://xiaoxiao-tiger.github.io/culture-research-daily/

每天上午10点（UTC+8）启动Google Scholar、NBER、SSRN、arXiv主题检索，完成后发布。分别展示实际检索式与执行状态，不提前限制期刊名称，不使用WoS。

2026-10-16起四个栏目：其他研究5篇（最新3篇分别来自NBER、SSRN、arXiv，高被引2篇）；传播学与社会科学5篇，优先传播学SSCI Q1/Q2；传播学七刊每天轮换完整一期，Online First单独算一期；综合六刊每天轮换1篇最新在线社会科学研究。后两个栏目不使用主题关键词。访问受限或合格候选不足时明确说明，不凑数。

主题为跨文化接收与价值观契合、AI价值谄媚与人机互动、计算传播方法，不设置新闻与leader注意力主题。新论文附研究用途、相关性与阅读优先级。配置见site/data/reading-plan.json，轮换进度见rotation-state.json；历史简报保持原版。

今天（2026-10-03）的测试简报已清空，不计入推荐历史。从下一期开始按DOI、arXiv ID、题名及核验的版本对应关系排除已推荐论文，推荐登记追加保存，跨栏目也不重复。

下一次检索设置通过所有者提交GitHub Issue保存。收藏保存在浏览器，支持待读、已读、准备引用、不相关、备注、核心文献标记以及导入导出。核心文献须通过网页生成的GitHub Issue提交并经工作流保存，之后每日追踪前后引用；私人笔记不会自动上传。每周五的每日任务同时编写周评；每周整理页提供最近7天目录与已发布精读建议。

发布前运行scripts/rebuild_registry.py追加历史，再运行scripts/validate.py、Python测试和Node测试；main推送后Actions部署GitHub Pages。具体规则见UPDATE_GUIDE.md。
