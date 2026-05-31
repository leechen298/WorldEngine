# 目标运行器

状态：final / closeout complete

## 目标入口

本 campaign 覆盖的自然语言目标包括：

```text
完成 v0.6
启动 WorldEngine v0.6：World Generation v1
```

## 路由选择

1. 读取 `CURRENT_STATE.md`。
2. 如果 `CURRENT_STATE.md` 指向某个 child package，按以下顺序读取该 package：
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
3. 使用 `CAMPAIGN_PLAN.md` 和 `v0.6-plan.md` 确认 package sequence 与 handoff
   rules。
4. 直到 active child package review 记录 `implementation_authorized: yes` 前，
   不得 implementation。

## 文档阶段关口

Documentation-only work 可以创建或更新 v0.6 iteration documents、package plans、
contracts、review evidence 和中文镜像。

Documentation-only work 不得修改 runtime、schema、API、frontend、backend test、
fixture、migration、external repository、generated result 或 `backend/worldengine/`
实现文件。

## 实现授权规则

Implementation authorization 默认关闭。

对于 mixed 或 code children：

1. `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md` 必须完成评审。
2. Documentation/contract evaluator 必须报告无 P0/P1 且无 blocking P2。
3. `review.md` 必须记录 `implementation_authorized: yes`。
4. Implementation 必须停留在 active child package contract 内。

如果 implementation 暴露 design gap，必须停止 implementation，更新相关文档，并只在
更新后的 contract/design/test plan/execution plan 通过评审后继续。

## Subagent / Evaluator 要求

因为 v0.6 是 `/goal` campaign，且后续存在 implementation-bearing children，在工具可用且
被授权时应使用 subagent/evaluator checkpoints：

1. 记录 `implementation_authorized: yes` 前，先做 documentation/contract
   evaluator。
2. 文件被修改后、广泛验证前，做 implementation-scope evaluator。
3. focused tests 后、broader regression、E2E、API smoke 或 generation-quality
   claims 前，做 code-review evaluator。
4. 将 tests、E2E、API smoke、Agent smoke、autonomous validation、build 或 release
   claims 记录为 passed 前，做 validation-evidence evaluator。
5. 任一 child 或 parent final assessment 前，做 closeout consistency evaluator。

会改变 process rules、package sequencing、evidence rules、automation-consumption
contracts、release status、validation templates 或 mirror obligations 的
documentation-only children，必须使用 read-only documentation evaluator。如果
subagent/evaluator tooling 不可用或未授权，则记录缺失 checkpoint，并将状态保持为
`planned / ready for review`，不得声称 review complete。

## 报告规则

- 历史 v0.5 evidence 只能作为 handoff evidence 引用。
- 没有 current-session command evidence 时，不得把 v0.6 generation、runtime、API、
  frontend、E2E、build、Agent smoke、autonomous validation、release behavior 或
  generation quality 标记为 passed。
- 在 `review.md` 中记录 exact commands、exit status、pass counts、skipped checks
  和 rationale。
- P1 阻断 implementation 或 closeout。
- 除非 active package contract 与 review 明确接受，否则 unresolved P2 阻断 final
  status。
- P3 只能在明确 handoff 时保留。

## 范围停止条件

如果任务会导致以下情况，必须停止并记录 blocker：

- active child 授权前修改 runtime/schema/API/frontend/test implementation。
- 添加 concrete demo-world data、private external validation oracle details 或
  application-specific backend logic。
- 在 reviewed v0.6 contract 之外实现 external validation readiness、projection app
  readiness、durable persistence 或 live external AI-provider behavior。
- 在 `backend/worldengine/` 下新增 runtime features。
- 将 v0.5 historical evidence 当作当前 v0.6 pass evidence。
- 绕过必需 documentation、implementation authorization、evaluator 或 evidence gates。
