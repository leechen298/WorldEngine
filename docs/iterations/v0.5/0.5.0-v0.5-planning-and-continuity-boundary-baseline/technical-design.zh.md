# 技术设计

状态：review complete

## 当前状态

v0.4 已 final / closeout complete。它交付了 minimal request-driven
Agent-in-World loop，包括 bounded perception、action intent/result contracts、
validated `noop` 与 `params.patch`，以及 `POST /world/agent/loop/step`。

v0.4 明确没有实现 memory、episodic memory、relationship state、self-summary、
reflection 或 personality drift。v0.4 post-closeout validation 在 scoped frontend
build type repair 后记录 clean pass。该 evidence 只作为 baseline 和 handoff context。

本次工作前不存在 `docs/iterations/v0.5/` package。

## 契约对齐与不变量

本 package 是 documentation-only。它必须保持以下 invariants：

- implementation authorization 保持 `no`。
- 所有 changes 都留在 `docs/iterations/v0.5/**` 下。
- 不修改 runtime、schema、API、frontend、backend test、fixture、migration、
  generated result、external repository 或 `backend/worldengine/` implementation
  files。
- 六个 v0.5 capabilities 都先作为已评审 contracts 进入，再实现 behavior。
- Working memory 和 episodic memory 是唯一的首批 implementation candidates。
- Historical v0.4 evidence 不得提升为 v0.5 pass evidence。

## 文档结构

Parent campaign docs：

- `README.md`：version root、goal entry、scope、deliverables、package index、
  current state 和 handoff baseline。
- `v0.5-plan.md`：所有 planned children 的 detailed version plan 和 quasi-package
  specs。
- `GOAL_RUNNER.md`：route selection、implementation authorization、
  subagent/evaluator gates、reporting rules 和 stop conditions。
- `CURRENT_STATE.md`：current campaign status、active child、route、next action 和
  evidence snapshot。
- `CAMPAIGN_PLAN.md`：campaign sequence、cross-child handoff、exit criteria 和
  stop conditions。
- `review.md`：parent-level documentation evidence 和 subagent/evaluator findings。

Child package docs：

- `README.md`：package status、goal、scope、deliverables 和 document list。
- `intent.md`：problem、goal、non-goals、why now、north-star alignment 和 handoff。
- `contract.md`：public concepts、capability split、compatibility constraints、
  allowed changes、forbidden changes 和 follow-ups。
- `technical-design.md`：本 documentation design 和 invariants。
- `test-plan.md`：exact documentation verification commands 和 not-run
  implementation checks。
- `plan.md`：ordered execution steps 和 stop conditions。
- `review.md`：changed files、commands、test results、compatibility review、scope
  review、subagent evidence、findings 和 final assessment。

每份 active doc 都有 `.zh.md` 镜像。

## 未来计划实现接口

本 package 可以命名 future implementation paths，但不得创建它们：

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py` 或等价的已批准路径
- `backend/app/tests/test_agent_memory_*.py`

未来任何 implementation package 都必须在 implementation 前定义 exact schemas、
services、interfaces、data flow、tests 和 compatibility checks。

## 兼容性策略

`0.5.0` 不改变 product behavior。未来 implementation packages 必须将以下 v0.4
surfaces 视为 compatibility-sensitive：

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- request-scoped `LoopStep`
- `POST /world/agent/loop/step`
- `/world/agent/params/propose-and-apply`
- runtime tick 和 world time
- API envelope 和 error shape
- event routes 和 optional `Event.refs`
- params behavior
- archive behavior

## 防漂移规则

- 保持 parent `README.md`、`CURRENT_STATE.md`、`v0.5-plan.md`、
  `CAMPAIGN_PLAN.md` 和 `review.md` status values 一致。
- 保持英文和中文镜像语义等价。
- 精确记录 command evidence。
- 对本 docs-only package，将 implementation checks 记录为 not run。
- 如果 changed-file set 出现任何 implementation file class，必须停止。

## 风险

- 风险：文档暗示 implementation authorization。
  缓解：在 package docs 和 review 中记录 `implementation_authorized: no`。
- 风险：v0.4 evidence 被误读为 v0.5 validation。
  缓解：将所有 v0.4 evidence 标记为 handoff only。
- 风险：v0.5 扩展成 application-specific behavior。
  缓解：在 parent 和 child contracts 中重复 concrete-world、external-validation、
  projection 和 `backend/worldengine/` 禁止项。
- 风险：mirror drift。
  缓解：同一轮创建英文和中文文件，并在 review 中包含 mirror checks。
