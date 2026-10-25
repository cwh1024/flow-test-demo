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
