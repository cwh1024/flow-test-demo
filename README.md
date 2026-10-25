# flow-test-demo

一个极简的 GitHub 测试仓库，用来练习「新建分支 → 提交 → 发起 PR → 合并」这套日常流程。仓库根目录同时提供一个可直接部署的静态首页。

## 目录

| 文件 | 用途 |
| --- | --- |
| `index.html` | 静态网站首页，也是 Cockpit 的部署入口（无需构建） |
| `hello.py` | 一个可以随便改的小脚本，用来产生提交内容 |
| `README.md` | 你正在看的说明 |

## 本地查看网站

直接双击 `index.html` 即可，无需安装依赖或构建。Cockpit 静态托管时，以仓库根目录作为站点根目录。

## 5 分钟完整走一遍

### 1. 新建分支

```bash
git checkout -b test/my-first-change
```

### 2. 修改 index.html

把页面标题或任意一行文案改掉，保存。

### 3. 提交并推送

```bash
git add index.html
git commit -m "test: 修改首页"
git push -u origin test/my-first-change
```

### 4. 发起 Pull Request

回到仓库页面，点击 **Compare & pull request**，填写标题后点 **Create pull request**。

### 5. 合并

点 **Merge pull request** → **Confirm merge**，然后可以顺手删除测试分支。

## 还可以测什么

- 创建一个 Issue，让 PR 描述里写 `Closes #1`，看合并后是否自动关闭
- 在 **Files changed** 页面给自己留一条 Review 意见
- 加一个 GitHub Actions 工作流，体验自动检查

这个仓库没有任何业务代码，放心折腾。

---

## 交付说明

项目名称：flow-test-demo

GitHub 仓库地址：https://github.com/cwh1024/flow-test-demo

实际主分支：main

技术栈与项目类型：原生 HTML + CSS + JavaScript 静态单页（无框架、无第三方依赖）；另附 Python 3 示例脚本

项目目录与入口：仓库根目录；网站部署入口为 `index.html`；辅助脚本为 `hello.py`

安装、运行与构建：无需安装第三方依赖，无需构建，无锁文件、无构建产物；直接用浏览器打开 `index.html`。静态托管时以仓库根目录为站点根目录。

已推送版本：见本仓库最新提交（完整 SHA 在本次交付回复中提供）

检查结果：

- 文件与依赖：通过。仓库包含 3 个受控文件；`index.html` 自包含，无外部资源、无 CDN、无 `node_modules`、无锁文件、无 `.env`、私钥或令牌。
- 部署入口：通过。仓库根目录存在 `index.html`，页面标题为“flow-test-demo · GitHub 流程练习”，主标题为“把 GitHub 流程，完整走一遍。”。
- 桌面渲染：通过。Chrome 无头模式在 1440px 宽下截图正常，布局完整。
- 移动渲染：通过。390px 视口下 `innerWidth=390`、`scrollWidth=390`，为单列布局，无横向滚动。
- 交互：通过。勾选环节后显示 1/5、进度条 20%；全部勾选后显示 5/5、100% 和完成文案；重置后恢复 0/5，重置按钮回到禁用状态。
- 控制台与网络：通过。无 error、warn、assert 消息；无外部网络请求，页面仅使用内联样式、脚本和 data URI 图标。
- 复制按钮：未验证。无头浏览器没有真实用户手势，剪贴板 API 被拒绝；已提供传统复制方式的降级逻辑，建议在真实浏览器中手动点一次确认。
- 构建：无需构建，未执行构建（不适用）。
- HTTPS 直连：本机仍不可用；本次通过已配置的 SSH 推送。

验收方法：打开仓库根目录的 `index.html`（或部署后的站点首页），应看到页面标题、五步清单、部署信息和命令行速查。勾选步骤会更新进度，全部勾选后出现完成提示，点“重置进度”恢复；手机宽度下为单列布局且无横向滚动。点击“查看仓库”可进入 GitHub 仓库。

交付状态：完整源码（含静态入口 `index.html`）已提交到上述仓库的 `main` 分支并通过 SSH 推送。本次仅完成代码修复、检查和 GitHub 交付，未部署、未上线，也未修改服务器；Cockpit 的重新检查与部署需在平台侧发起。
