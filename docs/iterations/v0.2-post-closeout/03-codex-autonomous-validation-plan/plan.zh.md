# Plan

状态：package complete / plan accepted current campaign

## 执行步骤

1. 定义 autonomous reviewer role。
2. 列出 required inputs。
3. 定义要运行或记录为 blocked 的 commands。
4. 定义 release claim checks。
5. 定义 API、schema、runtime 和 compatibility finding categories。
6. 定义 concrete demo-world regression checks。
7. 定义 unsupported-claim handling。
8. 定义 final recommendation values。
9. hand off 到 execution package。
10. 记录本 package 没有执行 autonomous validation。

## 阶段边界

- 本 package 定义 reviewer instructions。
- `04-codex-autonomous-validation-execution/` 负责 execution 和 review verification。

## 停止条件

如果 plan 出现以下问题，停止并记录 P2：

- 允许 reviewer 只依赖 summaries。
- 允许 code changes。
- 允许 unverified success claims。
- 省略 P1/P2/P3 classification。
- 省略 concrete demo-world regression checks。

## 审查记录更新步骤

用 documentation-only scope 和 final assessment 更新 `review.md`。
