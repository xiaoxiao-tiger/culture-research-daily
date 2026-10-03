# 文化传播文献日报

中文文化传播研究简报，每期两个tab：跨学科精选10篇、传播学与社会科学期刊10篇，合计20篇。开头显示实际检索记录，每篇展示原文摘要或明确标注的节选、完整摘要链接、原创中文概述，以及理论、数据、方法、结果和研究启示。理论与数据按可核验信息充分展开，不设500字上限。

网站：https://xiaoxiao-tiger.github.io/culture-research-daily/

原文摘要完整转载须有明确许可，否则展示简短原文摘录与来源链接。公开摘要核验与全文核验分开标记，未确认的样本、系数和识别细节明确注明。创刊期收录经典与近年研究，不表示当天新发表。

所有内容保存在site/data，以Git提交历史保留版本。支持日期归档、两个文献tab、键盘切换、可展开解读与JSON下载。

由已连接GitHub的ChatGPT定时任务每天北京时间10:00启动检索、核验和写入；GitHub Actions在提交后验证并部署。10:00是任务启动时间，任务完成后内容上线。连接及权限须保持可用，失败时保留历史期次。不需要仓库模型API密钥。

日常操作与schemaVersion 2格式见[UPDATE_GUIDE.md](UPDATE_GUIDE.md)。

本地检查：
```sh
python3 scripts/validate.py
node --check site/app.js
python3 -m http.server 8000 --directory site
```

网站为无依赖静态页面，文献文本用文本节点呈现，原文链接仅接受HTTPS。GitHub Pages发布源为GitHub Actions。
