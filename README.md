# flow-test-demo

一个极简的 GitHub 测试仓库，用来练习「新建分支 → 提交 → 发起 PR → 合并」这套日常流程。

## 目录

| 文件 | 用途 |
| --- | --- |
| `hello.py` | 一个可以随便改的小脚本，用来产生提交内容 |
| `README.md` | 你正在看的说明 |

## 5 分钟完整走一遍

### 1. 新建分支

```bash
git checkout -b test/my-first-change
```

### 2. 修改 hello.py

把 `Hello, GitHub!` 改成任意一句话，保存。

### 3. 提交并推送

```bash
git add hello.py
git commit -m "test: 修改问候语"
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

技术栈与项目类型：Python 3 命令行示例脚本（用于练习和测试 GitHub 流程）

项目目录与入口：仓库根目录；入口为 `hello.py`

安装、运行与构建：无需安装依赖、无需构建；需 Python 3，运行命令 `python hello.py`

已推送版本：见本仓库最新提交（完整 SHA 在本次交付回复中提供）

检查结果：

- 文件检查：通过。仓库仅包含 `README.md` 与 `hello.py`，均为 UTF-8 编码；无第三方依赖、无锁文件、无 `.env`、私钥、证书或明显令牌。
- 运行检查：未验证。本机未安装可用的 Python 解释器，无法执行 `python hello.py` 或语法编译检查。
- 网络推送：本机直连 `github.com` 的 HTTPS 连接被重置，`git push` 未成功；本次源码通过 GitHub API 提交到远程 `main` 分支。

验收方法：打开仓库应能看到 `README.md` 和 `hello.py`。在装有 Python 3 的电脑上运行 `python hello.py`，预期输出 `Hello, GitHub! 试着修改这一行，然后提交一个 PR。`。也可以按上方“5 分钟完整走一遍”新建分支、修改文件并合并一个测试 PR。

交付状态：完整源码已提交到上述仓库的 `main` 分支（本次通过 GitHub API 提交，未使用 `git push`）。
