# Contract

## Public Concepts

本包可以建立或确认以下文档级概念：

- `parent review complete`：v0.9 父包可以路由到第一个子包。这不是
  implementation authorization。
- `active child package`：`CURRENT_STATE.md` 中为下一步 goal 选择的具体子包。
- `v0.8 basic lifecycle handoff`：v0.8 修复序列之后，basic full-lifecycle
  autonomous validation 可以通过官方 checker。这只是 handoff context。
- `LLM-backed lifecycle blocked`：provider live smoke、LLM-backed world
  creation、rule-linked evolution、event legality、persistent Agent autonomy and
  consolidation evidence、checker/schema support，以及 Validation Client
  LLM-backed evidence handoff 仍需要未来子包处理。
- `provider live-call closed`：live provider calls 保持未授权，直到 reviewed
  child package 明确授权。
- `redacted provider evidence`：未来 provider evidence 只能暴露已批准的 public
  summaries，绝不能暴露 secrets、raw prompts、raw responses 或 raw provider
  traces。

## 兼容性要求

- 既有 runtime、schema、API、frontend、event、archive、params、Agent loop、
  memory、generation、fixture、migration、checker 和 legacy behavior 不变。
- 父级 v0.9 planned-package semantics 保持兼容：planned package specs 是 route-map
  inputs，不是 implementation authorization。
- v0.8 basic lifecycle PASS 仅保持为 historical handoff context。
- LLM-backed testing docs 仍是 validation specifications，不是当前 pass-capable
  evidence。
- 任何未来 schema/API/checker 变更必须是 additive，除非 active future child 明确允许
  breaking change。

## 允许变更

- 创建或更新
  `docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline/` 下的文件。
- 创建或更新本子包中文镜像。
- 更新父级 v0.9 status 和 route surfaces：
  - `docs/iterations/v0.9/README.md`
  - `docs/iterations/v0.9/README.zh.md`
  - `docs/iterations/v0.9/v0.9-plan.md`
  - `docs/iterations/v0.9/v0.9-plan.zh.md`
  - `docs/iterations/v0.9/GOAL_RUNNER.md`
  - `docs/iterations/v0.9/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.9/CURRENT_STATE.md`
  - `docs/iterations/v0.9/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.9/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.9/review.md`
  - `docs/iterations/v0.9/review.zh.md`
- 记录 documentation checks 和 subagent/evaluator findings。
- 保留 v0.8 handoff facts 和 v0.9 non-claims。

## 禁止变更

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、
  fixture、migration、external repository、generated result、provider
  configuration、Validation Client 或 `backend/worldengine/` implementation 文件。
- 不实现或编辑 provider smoke paths、LLM-backed world generation、rule schemas、
  runtime controls、direction queues、event legality、Agent continuity、
  consolidation、narrative projection、diagnostic dialogue、checker fixtures、
  scorecards、evidence bundle exporters、API handlers、frontend UI、persistence、
  migrations、product packaging 或 external validation behavior。
- 不在本 documentation-only package 中运行 live provider calls、API smoke、E2E、
  autonomous validation、generated-result rewrites 或 external Validation Client
  flows。
- 不添加 concrete demo worlds、maps、characters、locations、resources、story
  rules、seed data、private transcripts、private fixture paths、hidden reset APIs、
  private validation oracle behavior、UI selectors 或 application-specific backend
  logic。
- 不存储、展示、记录或导出 API keys、authorization headers、raw prompts、raw
  provider requests、raw provider responses、raw provider traces、raw thought、
  chain-of-thought、private Agent memory、private goals、hidden context 或 private
  evaluator data。
- 不把 provider live smoke、LLM-backed world creation、rule evolution、event
  legality、Agent autonomy、Agent consolidation、narrative projection、diagnostic
  dialogue、checker support、Validation Client handoff、full lifecycle validation、
  product readiness 或 external validation 标记为 passed。

## North Star Check

本包保持 WorldEngine 的通用性。它准备 engine-side LLM-backed lifecycle campaign
route，而不添加 concrete worlds、product-client behavior、external validator
implementation 或 application-specific backend logic。

## Out-of-Scope Follow-ups

- `0.9.1`：provider live smoke and redaction boundary。
- `0.9.2`：LLM-backed worldview ingestion and generation contract。
- `0.9.3`：world model rule and parameter schema。
- `0.9.4`：worldview generation fidelity evaluation。
- `0.9.5`：bounded runtime control and run budget。
- `0.9.6`：natural-language world direction boundary。
- `0.9.7`：rule-linked evolution and event legality。
- `0.9.8`：brain-inspired Agent continuity and consolidation evidence。
- `0.9.9`：external narrative and diagnostic dialogue boundary。
- `0.9.10`：LLM-backed autonomous checker and fixtures。
- `0.9.11`：Validation Client evidence handoff contract。
- `0.9.12`：LLM-backed full-lifecycle validation execution。
- `0.9.13`：v0.9 release-candidate and closeout。
