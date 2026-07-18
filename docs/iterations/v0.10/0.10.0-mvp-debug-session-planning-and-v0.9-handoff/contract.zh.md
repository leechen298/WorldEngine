# Contract

## Public Concepts

本包可以建立或确认以下 documentation-level concepts：

- `parent review complete`：v0.10 parent package 可以路由到第一个 child。这不是
  implementation authorization。
- `active child package`：`CURRENT_STATE.md` 为下一步 goal 选择的具体 child package。
- `v0.9 BLOCKED handoff`：v0.9 以 full LLM-backed lifecycle validation BLOCKED
  closeout，但其架构和 evidence contracts 可以作为 v0.10 输入。
- `MVP debug-session baseline`：v0.10 先做 discoverability 和 runnable session slice，
  而不是完整 Agent autonomy 或 product validation。
- `implementation closed`：runtime、schema、API、frontend、provider、Validation
  Client、checker、fixture、migration 和 evidence execution work 在后续 reviewed child
  package 打开前仍未授权。

## Compatibility Requirements

- 现有 runtime、schema、API、frontend、event、archive、params、Agent loop、memory、
  generation、fixture、migration、checker、provider、Validation Client、generated-result
  和 legacy behavior 均不改变。
- v0.9 final BLOCKED closeout 只作为历史交接上下文。
- v0.10 planned-package semantics 保持兼容：planned package specs 是 route-map
  inputs，不是 implementation authorization。
- 后续 v0.10 schema/API/checker changes 必须 additive，除非 active future child
  明确允许 breaking change。

## Allowed Changes

- 创建或更新
  `docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff/`
  下的文件。
- 创建或更新本 child package 的中文镜像。
- 更新 parent v0.10 status 和 route surfaces：
  - `docs/iterations/v0.10/README.md`
  - `docs/iterations/v0.10/README.zh.md`
  - `docs/iterations/v0.10/v0.10-plan.md`
  - `docs/iterations/v0.10/v0.10-plan.zh.md`
  - `docs/iterations/v0.10/GOAL_RUNNER.md`
  - `docs/iterations/v0.10/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.10/CURRENT_STATE.md`
  - `docs/iterations/v0.10/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.10/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.10/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.10/review.md`
  - `docs/iterations/v0.10/review.zh.md`
- 记录 documentation checks 和 subagent/evaluator findings。
- 保留 v0.9 BLOCKED handoff facts 和 v0.10 non-claims。

## Forbidden Changes

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、
  fixture、migration、external repository、generated result、provider configuration、
  Validation Client 或 `backend/worldengine/` implementation files。
- 不实现或编辑 manifest handlers、session APIs、session stores、worldview creation
  flow、runtime controls、snapshot/diff logic、dashboard UI、validation repair、Agent
  continuity、provider configuration、checker fixtures、scorecards、evidence bundle
  exporters、persistence、migrations 或 product packaging。
- 不在本 documentation-only package 中运行 live provider calls、API smoke、E2E、
  autonomous validation、generated-result rewrites、checker result generation 或
  external Validation Client flows。
- 不加入 concrete demo worlds、maps、characters、locations、resources、story rules、
  seed data、private transcripts、private fixture paths、hidden reset APIs、private
  validation oracle behavior、UI selectors 或 application-specific backend logic。
- 不存储、展示、记录或导出 API keys、authorization headers、raw prompts、raw provider
  requests、raw provider responses、raw provider traces、raw thought、private Agent
  memory、private goals、hidden context 或 private evaluator data。
- 不把 v0.10 manifest、session creation、bounded runtime、dashboard flow、Validation
  Client automation、provider readiness、external validation、product readiness、Agent
  autonomy 或 full MVP lifecycle 标记为 passed。

## North Star Check

本包保持 WorldEngine generic。它准备通往 debuggable MVP session 的路由，不加入 concrete
worlds、product-client behavior、external validator implementation 或 application-specific
backend logic。

## Out-of-Scope Follow-ups

- `0.10.1`：MVP public manifest and debug handoff。
- `0.10.2`：world session contract and state store。
- `0.10.3`：worldview to runtime session creation。
- `0.10.4`：bounded session runtime and snapshot evidence。
- `0.10.5`：dashboard MVP session flow。
- `0.10.6`：v0.10 validation and handoff。
