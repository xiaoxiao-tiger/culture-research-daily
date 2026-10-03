# 文化传播文献日报

中文文化传播研究简报，每期推荐10篇文章，每篇正文约500字，包含文献信息、理论、数据、方法、结果与研究启示。

## 网站

页面包含最新一期、日期归档、可展开的完整解读和原文链接。所有内容保存在 `site/data/`，以提交历史保留版本。

首次启用：进入本仓库 **Settings → Pages → Build and deployment → Source**，选择 **GitHub Actions**。然后在 **Actions → Publish daily briefing website → Run workflow** 运行发布。

默认项目地址为 `https://xiaoxiao-tiger.github.io/culture-research-daily/`，只有成功部署后才能访问。

## 每日更新

由已连接GitHub的ChatGPT定时任务每天北京时间10:00启动文献检索、核验和写入。GitHub Actions在网站内容提交后验证JSON并部署页面。10:00是任务启动时间，内容会在任务完成后上线。

不需要在仓库中配置模型API密钥。定时任务的连接及权限须保持可用；任务失败时保留上一期，不覆盖已发布简报。

日常操作与数据格式见 [UPDATE_GUIDE.md](UPDATE_GUIDE.md)。邮件推送尚未配置。

## 本地检查

```sh
python3 scripts/validate.py
node --check site/app.js
python3 -m http.server 8000 --directory site
```

网站是无依赖静态页面，全部文献文本以文本节点呈现，原文链接仅接受HTTPS。
