# Contract

英文原文：`contract.md`。

## Public Concepts

`AgentContinuityArtifact`

- 描述某个 Agent 在一个 runtime tick 上 continuity state 的 public artifact。
- 包含 world id、agent id、tick、world time、perception summary refs、working 或 short-term memory summary、long-term memory summary refs、personality summary refs、skill summary refs、current state、event reaction refs、redaction status 和 evidence refs。
- 不得包含 raw thoughts、chain-of-thought、private memory payloads、private goals、hidden context、raw prompts、raw provider responses、provider traces、API keys、authorization headers 或 private evaluator data。

`AgentConsolidationArtifact`

- 描述 sleep/rest/low-activity consolidation phase 的 public artifact。
- 包含 phase id、world id、agent id、start/end tick 或 active tick window、consolidation status、source short-term summary refs、emitted long-term summary refs、personality/skill summary stability 或 bounded-drift markers、event refs 和 redaction status。
- Consolidation 可以跨多个 ticks。它不得暗示 personality、long-term memory 或 skill mutation 每 tick 都强制发生。

`AgentContinuityState`

- Public state vocabulary：
  - `observe`
  - `intent`
  - `action`
  - `no_intent`
  - `wait`
  - `rest`
  - `sleep`
  - `consolidating`
  - `reacting`
- 这些 states 是 public evidence classifications，不是 private cognition dumps。

`AgentEventReactionEvidence`

- 表示 Agent 对 canonical public world event 产生反应的 public evidence。
- 包含 public event refs、reaction summary、selected public state、continuity artifact refs 和 redaction status。
- 不得创建 fake in-world dialogue、private memory mutation 或 final world fact。

`AgentAutonomousActionEvidence`

- 表示 Agent action 是由 WorldEngine-backed Agent loop behavior 选择，而不是由 client、fixture 或 external validation script 直接提供的 public evidence。
- 包含 action event refs、action result refs、continuity artifact refs、public action summary、input provenance classification 和 redaction status。
- 不得暴露 raw prompts、raw thoughts、private goals、private memory、hidden context、provider traces 或 private evaluator data。

`ClientScriptedAutonomyRejection`

- 当 action 直接由 client、fixture 或 external validation script 提供，却被声称为 autonomy 时，返回 public diagnostic。
- Rejection diagnostics 必须是 public，并且不得 echo unsafe client input。

## Required Checks

Continuity evidence 必须 deterministically reject 或 diagnose：

- raw thought 或 chain-of-thought。
- private memory payloads、private goals、hidden context、private evaluator data、raw prompts、raw provider traces、API keys、authorization headers 和 secrets。
- client-scripted action represented as Agent autonomy。
- personality、long-term memory 或 skill changes represented as automatic per-tick mutation。
- 没有 bounded tick/time evidence 的 consolidation phases。
- 没有 public event refs 的 event reactions。
- 没有 public action event refs、action result refs 或 WorldEngine-owned provenance 的 accepted autonomous action evidence。
- 没有 public Agent id、tick/time、state 或 evidence refs 的 continuity artifacts。

Continuity evidence 只有满足以下条件时才可以被接受：

- 所有 evidence 都是 public 且 redacted。
- state vocabulary 属于 allowed public states。
- event reactions 指向 public canonical event refs。
- action state evidence 指向 public canonical Agent action/result event refs，且不是 client-scripted。
- short-term、long-term、personality 和 skill summaries 以 public summaries 或 public refs 表示，而不是 private payloads。
- consolidation cadence 明确，并且可以跨多个 ticks。

## Allowed Changes

Documentation review authorization 之后，本包可以修改：

- `backend/app/schemas/` 中用于 public Agent continuity、consolidation、autonomous action、event reaction 和 scripted-autonomy rejection evidence 的 additive schemas。
- `backend/app/core/` 或 `backend/app/agent/` 下用于 public continuity/consolidation artifact construction 的 narrow deterministic helpers。
- 如 public inspection 需要，可添加 additive active-backend route behavior 或 manifest/OpenAPI exposure。
- Agent continuity 和 consolidation records 的 additive public event payload evidence。
- `backend/app/tests/` 下的 focused backend tests。
- package `review.md` 和 `review.zh.md`。
- review 或 implementation closeout 后，只为 route/status handoff 更新 v0.9 parent status/review docs。

## Forbidden Changes

本包不得：

- 修改 `backend/worldengine/`。
- 修改 frontend code。
- 修改 Validation Client 或 external repositories。
- 执行 live provider calls 或 LLM interpretation。
- 创建 generated worlds 或 generated-result artifacts。
- 执行 checkers 或修改 checker fixtures。
- 运行 external validation 或 autonomous validation。
- 实现 durable scheduling、background workers、cron、queue services 或 deployment infrastructure。
- 实现 narrative projection 或 diagnostic dialogue。
- 存储或导出 raw thought、chain-of-thought、private memory payloads、private goals、hidden context、raw prompts、raw provider requests、raw provider responses、provider traces、API keys、authorization headers、secrets 或 private evaluator data。
- 声明 consciousness、human-quality simulation、full selfhood、checker PASS、external validation PASS、product readiness 或 full v0.9 closeout。

## Compatibility Requirements

- Existing Agent loop APIs 必须保持 additive-compatible，除非本包 review 明确批准 narrow additive extension。
- Existing v0.5 memory schemas 和 stores 必须保持兼容，只能 additive extension。
- Existing event、runtime、snapshot/archive、world direction 和 rule-linked event legality surfaces 必须保持兼容。
- Public handoff manifest behavior 必须保持兼容。
- New schemas 必须 reject extra fields 和 private markers。
- Continuity evidence 不得依赖 checker support 才有用。
- Continuity evidence 应该能被后续 `0.9.10` checker/schema/fixture work 消费，但本包不实现 checker fixtures，也不执行 checkers。
- Rejected scripted-autonomy evidence 不得 append canonical accepted Agent autonomy events。

## North Star Check

本包支持 engineered pseudo-self continuity，同时让模型保持 inspectable、testable，并明确不声明 consciousness。

## Out-of-Scope Follow-ups

- `0.9.9`：external narrative projection 和 diagnostic dialogue boundaries。
- `0.9.10`：LLM-backed checker fixtures、schema、scorecard support 和 checker execution。
- `0.9.12`：live 或 blocked full lifecycle validation execution。

## Exit Criteria

本包只有在以下条件满足时才可 close：

- required package docs 和 mirrors 存在。
- documentation/contract evaluator 报告 no P0/P1 且 no blocking P2。
- code changes 前已记录 implementation authorization。
- focused tests 证明 continuity artifacts、consolidation artifacts、multi-tick cadence、accepted autonomous action evidence、no-intent/rest states、event reactions、scripted-action rejection、redaction、extra-field rejection，以及与 Agent loop、memory、event、runtime 和 public handoff surfaces 的兼容。
- relevant backend regressions 在当前 session 通过。
- `review.md` 记录 exact commands、changed files、subagent findings、compatibility review、scope review、unresolved findings 和 final route。
