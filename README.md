# 每日研究简报

网站：https://xiaoxiao-tiger.github.io/culture-research-daily/

每天北京时间10:00开始检索和核验，完成后发布。两个tab各目标10篇：可自选主题的主题精选、按用户上传JCR名单筛选的传播学Q1/Q2。先看论文质量；新文献不足则说明缺额，不重复旧文凑数。

简报开头仅显示主题检索式，逐篇题名和摘要核验记录折叠展示。完整原文摘要能提供且允许转载时展示，否则保留来源链接与原创中文概述，取消一句话节选。理论与数据详解不设500字上限。

## 下一次检索设置

在网站点击“下一次检索设置”，填写两栏关键词、生效日期、近期范围和单日/持续适用。点击提交打开GitHub确认页，再提交Issue。Save search settings工作流只接受仓库所有者xiaoxiao-tiger的结构化设置，写入site/data/search-settings.json并发布。回网站刷新“已保存设置”可核对。仅在浏览器填写不生效；设置公开，不填写密码或私人信息。

日更任务读取当天适用的最新设置，没有适用项时采用默认关键词。设置可更换到任何研究主题。期刊白名单site/data/journals.json由上传CSV的Q1/Q2筛出，保留SSCI/ESCI，不等同中科院分区。

## 收藏与去重

论文卡片“收藏待读”加入收藏栏，可筛选待读/已读并记笔记。收藏保存在当前浏览器，换设备用导出/导入，不会自动跨设备同步。

recommended.json为只追加的历史推荐登记，结合DOI、arXiv基础编号、规范化题名及跨版本别名去重。验证器拒绝跨日期与两栏重复；预印本转期刊还需人工核对版本关系。调整掉的历史文章仍保留登记，原创刊版本在revisions中。

日更步骤与数据格式见[UPDATE_GUIDE.md](UPDATE_GUIDE.md)。

本地检查：
```sh
python3 scripts/rebuild_registry.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
node --test tests/core.test.js
node --check site/app.js
python3 -m http.server 8000 --directory site
```

无需仓库模型API密钥。静态页面用文本节点显示内容，原文链接仅接受HTTPS。GitHub Pages由Actions部署。
