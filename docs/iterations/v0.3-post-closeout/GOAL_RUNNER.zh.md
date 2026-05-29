# GOAL_RUNNER.md

用途：为 `v0.3-post-closeout` 定义 Codex App `/goal` prompt 和 campaign 指引。

这不是 WorldEngine 运行时行为，也不是自动化控制器实现。调度、编排、重试基础设施
和 Codex 角色分配属于 Codex 环境或其他外部工具。

本文件只定义本验证 campaign 的可读入口、状态机、停止条件、证据规则和 review 更新规则。

## Campaign 入口

当用户说：

```text
完成 v0.3-post-closeout
```

Codex 应按本文件、`CURRENT_STATE.md` 和 `CAMPAIGN_PLAN.md` 运行 campaign。

默认行为：

- 从 `CURRENT_STATE.md` 记录的当前子包开始。
- 选择路由前先读取当前子包文档。
- 只有当前子包达到所需退出状态后，才推进到下一包。
- 遇到阻塞、失败证据、必需文件缺失、source conflict 或越界修改时停止。

## 优先阅读文件

先读取这些父级文件：

- `README.md`
- `CURRENT_STATE.md`
- `CAMPAIGN_PLAN.md`
- `validation-master-plan.md`
- `validation-report-template.md`
- `review.md`
- `docs/iterations/AGENTS.md`
- 根目录 `AGENTS.md`

然后读取当前子包：

- `README.md`
- `intent.md`
- `contract.md`
- `plan.md` 或 `execution-plan.md`
- 如存在，读取 `test-plan.md`
- 如存在，读取相关报告或评审模板
- `review.md`

执行验证和自主评审时，还要读取 `validation-master-plan.md` 中列出的 v0.3 输入文件。

## 子包顺序

1. `01-e2e-validation-plan`
2. `02-e2e-validation-execution`
3. `03-codex-autonomous-validation-plan`
4. `04-codex-autonomous-validation-execution`
5. `05-final-validation-bundle`

`03` 只规划自主验证。`04` 才负责执行自主验证。`05` 只汇总当前证据、明确接受的历史证据
或已记录阻塞。

## 允许的路由类型

- `goal-entry`
- `documentation-planning`
- `human-review`
- `validation-execution`
- `autonomous-review-planning`
- `autonomous-review-execution`
- `repair-loop`
- `blocker-recording`
- `final-bundle-synthesis`
- `needs-user-input`

父 campaign 不授权 runtime、schema、API、frontend、fixture、migration、
backend test 或外部仓库变更。

## 停止条件

出现下列情况时停止，并记录为 `blocked` 或 `failed`：

- 后端确定性测试失败。
- API smoke 失败。
- loader 验证失败。
- runtime context bridge 验证失败。
- runtime compatibility claim 与实际行为冲突。
- release claim 与实际行为冲突。
- Codex autonomous reviewer 报告 P1。
- 出现具体 demo-world 回归。
- 命令无法运行且没有记录 blocker。
- 必需文件缺失。
- 当前子包需要执行契约未授权的实现变更。
- 缺少验证证据但报告试图写成功结论。
- git state 出现越界修改。

## 证据要求

任何后续执行结论都必须记录：

- reviewed branch。
- execution branch。
- evidence commit。
- 如可用，final documentation commit。
- validation date。
- executor。
- 实际运行的完整命令。
- 命令输出或结果摘要。
- 未运行的检查及原因。
- P1/P2/P3 findings。
- blockers。
- 使用当前报告允许词汇写出的最终评估。

历史 v0.3 包证据可以作为 archived context 引用，但除非当前 campaign 明确重跑或带理由接受，
否则不能算作 fresh validation。

## Review 更新规则

每个子包收口时，都要更新自己的 `review.md`，记录：

- changed files。
- files read。
- commands run。
- commands not run。
- test results。
- compatibility review。
- scope review。
- unresolved P1/P2/P3。
- final assessment。

只有子包达到已评审路由状态后，才可以更新父级 `CURRENT_STATE.md`。父级 `review.md`
记录本文档创建轮次以及后续 campaign 级修改。

## 修复循环规则

如果验证执行发现 P1 或 P2：

- 先分类 finding。
- 除非未来已有评审 repair package 明确授权，否则不要修改实现。
- 把 blocker 或 failure 记录到当前执行报告。
- 更新子包 `review.md`。
- 除非子包契约明确允许带记录 carry，否则不要进入下一子包。

P3 只有在写明交接目标和理由后才可以 carry。

## 不得声明未验证结果

测试、API smoke、E2E、Codex 自主评审、后端回归、前端构建、migration、fixture run、
loader 验证、bridge 验证或兼容性结论，只有在当前 campaign 真实执行过，或明确记录为
已接受历史证据时，才可以写成成功。

模板必须从 `not executed` 开始，不能预填成功结果。

## 不扩大范围

本 campaign 不得：

- 重新打开 v0.3 实现。
- 改变 v0.3 发布状态。
- 实现 v0.4 工作。
- 添加 demo-world 内容。
- 创建外部仓库。
- 添加 private validation oracle details。
- 修改 runtime、schema、API、frontend、backend tests、fixtures、migrations
  或 legacy `backend/worldengine/` 文件。
