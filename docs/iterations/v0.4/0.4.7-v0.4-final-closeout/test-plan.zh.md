# 测试计划

## 要运行的精确命令

本包必需文档命令：

```bash
git status --short --branch
git diff --check
```

本包特定验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 记录 backend/frontend/API/E2E/runtime tests 不由本 documentation-only package 强制要求；如果 final evaluator 重新运行 backend/API 命令，必须在 `review.md` 和 `final-closeout.md` 中记录命令和结果。

如果本包在未来执行中修改 backend 实现文件，必须在 `backend/` 下用 `.venv/bin/python -m pytest ...` 运行聚焦 backend tests，然后运行 active implementation review 中指定的相邻兼容性测试。

## 预期结果

- 文档检查退出 `0`。
- 必需文件和镜像存在。
- 没有变更文件超出 active package contract。
- 任何 backend/API/E2E/runtime pass claim 都有当前会话命令支撑，或记录为 not run。

## 未运行命令及原因

文档草拟期间不强制运行 backend、frontend、API smoke、E2E、Agent smoke、runtime behavior、build、schema execution、fixture、migration 或 test implementation 命令。如果 final closeout repair 或 evaluator review 重新运行 backend/API checks，必须在 `review.md` 和 `final-closeout.md` 记录当前会话结果。

## Blocker 记录规则

如果命令无法运行、evaluator checkpoint 不可用或缺失必需文件，必须在 `review.md` 中记录 `blocked` 或 `needs-user-input`，并写明精确命令、缺失文件或不可用 checkpoint。

## 不得未验证声明规则

除非命令或评审在当前会话运行，或 active contract 带理由明确接受，否则不得把 tests、API smoke、E2E、backend checks、frontend checks、runtime behavior、migration、fixture behavior、release status 或 closeout status 标记为 passed。
