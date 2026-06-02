# Contract

## Public Concepts

本 package 可以建立或确认这些 documentation-level concepts：

- `parent review complete`：v0.7 parent package 可以 route 到第一个 child。这不是
  implementation authorization。
- `active child package`：`CURRENT_STATE.md` 中为下一步 goal 选择的具体 child package。
- `historical handoff evidence`：v0.6 evidence 可用于 v0.7 scope 背景，但不算当前 v0.7 pass
  evidence。
- `external validation boundary`：external suites 通过 public contracts、schemas、exported bundles、
  redacted reports 或 APIs 消费 WorldEngine，不把 private validation worlds 导入本仓库。
- `projection consumer boundary`：projection applications 消费 generic WorldEngine read models 和
  contracts，不把 product-specific backend behavior 放进 core repository。

## Compatibility Constraints

- Existing runtime、schema、API、frontend、event、archive、params、Agent loop、memory、generation、
  fixture、migration、checker 和 legacy behavior 保持不变。
- Parent v0.7 planned-package semantics 保持兼容：planned package specs 是 route-map inputs，
  不是 implementation authorization。
- Historical v0.6 evidence 仅保持 handoff context。
- 任何 future schema/API/checker change 都必须 additive，除非 active future child 明确允许 breaking
  change。

## Allowed Changes

- 创建或更新
  `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/`
  下的文件。
- 创建或更新本 child package 的中文镜像。
- 更新 parent v0.7 status 和 route surfaces：
  - `docs/iterations/v0.7/README.md`
  - `docs/iterations/v0.7/README.zh.md`
  - `docs/iterations/v0.7/v0.7-plan.md`
  - `docs/iterations/v0.7/v0.7-plan.zh.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.7/CURRENT_STATE.md`
  - `docs/iterations/v0.7/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.7/review.md`
  - `docs/iterations/v0.7/review.zh.md`
- 记录 documentation checks 和 subagent/evaluator findings。

## Forbidden Changes

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、migration、
  external repository、generated result 或 `backend/worldengine/` implementation files。
- 不实现或编辑 report schemas、redaction checkers、contract bundle generators、readiness manifest
  generators、projection endpoints、API handlers、frontend UI、persistence、migrations 或 product
  packaging。
- 不加入 concrete external validation world data、concrete world names、maps、characters、locations、
  resources、story rules、seed data、private transcripts、UI selectors、private fixture paths、hidden
  reset APIs 或 private validation oracle behavior。
- 不将 v0.7 标记为 final、release-ready、product-ready、projection application-ready、
  external-suite-passed、Agent-smoke-passed、autonomous-passed、E2E-passed、API-passed、
  frontend-passed 或 runtime-passed。

## North Star Check

本 package 保持 WorldEngine generic。它为 external consumers 定义 campaign boundary，但不加入
consumer-specific state、private validation fixtures、product UI 或 application backend logic。

## Out-of-Scope Follow-ups

- `0.7.1`：public validation and projection contract semantics。
- `0.7.2`：report schema and redaction checker。
- `0.7.3`：contract bundle and readiness manifest。
- `0.7.4`：projection consumer read model contracts and any approved read-only implementation。
- `0.7.5`：quality regression and compatibility evidence。
- `0.7.6` through `0.7.8`：audit、release-candidate、final closeout。
