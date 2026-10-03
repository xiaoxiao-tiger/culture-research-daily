# 每日研究简报

网站：https://xiaoxiao-tiger.github.io/culture-research-daily/

每天上午10点（UTC+8）启动检索，完成后发布。检索覆盖Google Scholar、NBER、SSRN和arXiv，先主题检索再筛选。使用Google Scholar网页；取消WoS。四个平台分别展示实际检索式和状态，公开域名网页检索注明渠道。

两个栏目各5篇：其他研究按首次公开时间降序；传播学与社会科学从Google Scholar检索结果筛选，按其实际被引次数降序，并展示来源和核验日期。传播学按上传表中的77种SSCI Q1/Q2名单筛选，其他社会科学正式期刊另核验SSCI收录，排除ESCI。2026-10-03已清空此前网站记录，不维护历史推荐登记，允许重复推荐。

下一次检索设置可更换主题。填写后提交GitHub Issue，由所有者身份验证工作流保存。收藏保存在浏览器，支持阅读状态、笔记、导入和导出。

完整摘要在许可允许时提供，否则附来源链接；理论和数据注明核验范围。质量与相关性优先，不为凑数量放入无关文章。

开发检查：`python scripts/validate.py`、`python -m unittest discover -s tests`、`node --test tests/core.test.js`。推送main后Actions部署GitHub Pages。
