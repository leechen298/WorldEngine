# 计划

英文源文件：`plan.md`。

状态：closed / 执行完成

## 目标

准备并在明确授权后实现 WorldEngine 侧最小可运行锚点，不依赖当前实现设计、live provider、
Godot 或外部基础设施。

## 已读取的权威输入

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/project-plan.md`
- `docs/roadmap.md`
- `docs/living-world-development-flow.zh.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- v0.13 parent documents

## 文档类型

在 documentation stage 准备的完整 mixed implementation package。

## Documentation Stage 创建或更新的文件

- v0.13 parent index、campaign state/runner/plan 和 version plan，以及中文镜像。
- 完整 `0.13.0-worldengine-runnable-anchor` package 和中文镜像。
- `docs/project-plan(.zh).md` 与 `docs/roadmap(.zh).md` 路由更新。

## Documentation Stage 明确不修改

- `backend/`
- `frontend/`
- Tests、fixtures、migrations、generated evidence 和 runtime data。
- `/Users/leechen/projects/WorldEngine-Validation-Client`。

## 有序执行步骤

### 阶段 A：文档 Gate

1. 起草 parent v0.13 campaign 和详细 package sequence。
2. 起草本 package 的 intent、contract、technical design、test plan、plan 和 documentation-stage
   review，并完成中英文镜像。
3. 整合只读子代理关于纵向切片完整性和防假通过边界的发现。
4. 运行 package completeness、mirror、authorization、terminology 和 `git diff --check`。
5. 请求独立只读 documentation/contract evaluator。
6. 修复所有 P1/P2 finding。
7. 把 package 交给用户评审，并停在实现之前。

### 阶段 B：授权

8. 用户批准且 evaluator PASS 后，只把 `0.13.0` authorization 改为 `yes`，并同步 parent、
   current-state 和 review mirrors。
9. 读取 active code/tests，把它们当成 implementation inventory。
10. 如果审计发现 contract gap，停止并更新/重审文档。

### 阶段 C：Test-first 实现

11. 为 AC-01 至 AC-10 新增 failing focused tests。
12. 实现通用 manifest 和 schemas。
13. 实现 deterministic package generation/readiness/hash。
14. 实现 Session boot、atomic lockstep step、event/diff/snapshot/state hash、projection 和
    evidence export。
15. 实现 deterministic Agent causal loop 和引用经历的后续 decision。
16. 实现明确 intervention window 和 accepted/rejected direction path。
17. 实现通用 action/feedback、idempotency 和 revision boundaries。
18. 在同一组 API 上实现管理控制台。

### 阶段 D：验证与评审

19. 运行 focused backend tests。
20. 请求 implementation-scope evaluator 并修复 P1/P2。
21. 运行 frontend unit/build 和 focused E2E。
22. 请求 code-review evaluator 并修复 P1/P2。
23. 运行 regression 和 black-box API smoke。
24. 请求 validation-evidence evaluator。
25. 用准确当前证据更新 `review.md`/`review.zh.md`。
26. 请求 closeout-consistency evaluator。
27. 所有 gate 通过后，关闭 `0.13.0`，但不声明完整 MVP PASS，并路由到外部 `0.13.1`
    documentation package。

## 授权后允许修改

只允许 `contract.md` 和 `technical-design.md` 列出的 backend/frontend/test/doc surfaces。

## 禁止修改

- External repository、Godot、provider live、concrete fixture world、production
  persistence/deployment 或 legacy `backend/worldengine/`。
- 未经重审的 contract change。
- 回滚无关 dirty files。

## Review Gates

- 授权前 documentation/contract evaluator。
- 实现修改后 implementation-scope evaluator。
- Focused tests 后 code-review evaluator。
- Runtime/E2E claim 前 validation-evidence evaluator。
- Package PASS 前 closeout-consistency evaluator。

## 验证命令

准确命令定义在 `test-plan.md`。当前 package session 没有实际运行的命令不能标记 passed。

## 假设

- 第一锚点使用 process-local persistence 足够。
- Deterministic generation 和 Agent policy 是合法 MVP execution path。
- 带 event cursor 的 HTTP polling 足以支持第一种通用客户端。
- 既有 Web 管理技术可以保留，但 validation-client Web code 不约束本 package。

## Stop Conditions

- 用户或 evaluator 拒绝 contract。
- Required behavior 只能通过 live provider、core concrete fixture、private state 或
  client-owned canonical mutation 实现。
- 既有 dirty work 使 scoped implementation 无法在不破坏覆盖的情况下进行。
- 仍有未解决 P1/P2。

## 批准后交接

在批准的 `0.13.0` scope 内使用 `worldengine-iteration-dev`。本 package 发布 verified
contract bundle 之前，不启动 `0.13.1`。
