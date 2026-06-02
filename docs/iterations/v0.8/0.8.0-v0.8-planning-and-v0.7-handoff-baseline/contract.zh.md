# Contract

## 公共概念

本 package 可以建立或确认以下 documentation-level concepts：

- `parent review complete`：v0.8 parent package 可以 route 到第一个 child。这不是
  implementation authorization。
- `active child package`：`CURRENT_STATE.md` 为下一步 goal 选择的具体 child package。
- `current v0.7 checker/docs handoff evidence`：`0.7.9` 和
  `2026-06-02-v0.7-overall-validation.md` 为 v0.7 清除了 V07-CR checker/docs
  blocker gate。它们不证明 v0.8 readiness。
- `historical handoff evidence`：v0.7 和 v0.6 evidence 只影响 v0.8 scope，不算 current
  v0.8 pass evidence。
- `minimum working-state boundary`：v0.8 必须先定义 minimum normally working
  WorldEngine state 所需的 core slices，之后才可声明该状态。
- `external validation boundary`：external validation 只消费 public、redacted、
  generic core-side surfaces，不成为本仓库的一部分。

## 兼容性约束

- Existing runtime、schema、API、frontend、event、archive、params、Agent loop、
  memory、generation、fixture、migration、checker 和 legacy behavior 保持 unchanged。
- Parent v0.8 planned-package semantics 保持兼容：planned package specs 是 route-map
  inputs，不是 implementation authorization。
- 当前 v0.7 checker/docs clean pass 只能作为 handoff context。
- 未来 schema/API/checker changes 必须 additive，除非 active future child 明确允许
  breaking change。

## 允许修改

- 创建或更新
  `docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/` 下的文件。
- 创建或更新本 child package 的中文镜像。
- 更新 parent v0.8 status 和 route surfaces：
  - `docs/iterations/v0.8/README.md`
  - `docs/iterations/v0.8/README.zh.md`
  - `docs/iterations/v0.8/v0.8-plan.md`
  - `docs/iterations/v0.8/v0.8-plan.zh.md`
  - `docs/iterations/v0.8/GOAL_RUNNER.md`
  - `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.8/CURRENT_STATE.md`
  - `docs/iterations/v0.8/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.8/review.md`
  - `docs/iterations/v0.8/review.zh.md`
- 记录 documentation checks 和 subagent/evaluator findings。
- 在 v0.8 文档内部更新 v0.7 handoff wording，以反映当前 `0.7.9` repair 状态。

## 禁止修改

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、
  fixture、migration、external repository、generated result 或 `backend/worldengine/`
  implementation files。
- 不实现或编辑 minimum working-state schemas、external-validation handoff schemas、
  redaction checkers、contract bundle generators、readiness manifest generators、
  projection endpoints、API handlers、frontend UI、persistence、migrations 或 product
  packaging。
- 不添加 concrete external validation world data、concrete world names、maps、
  characters、locations、resources、story rules、seed data、private transcripts、UI
  selectors、private fixture paths、hidden reset APIs、private validation oracle
  behavior 或 private external repository paths。
- 不把 v0.8 标记为 final、release-ready、product-ready、external-suite-passed、
  external-consumer-passed、minimum-working-state-passed、Agent-smoke-passed、
  autonomous-passed、E2E-passed、API-passed、frontend-passed 或 runtime-passed。

## North Star 检查

本 package 保持 WorldEngine generic。它准备 core-side readiness 和
external-validation handoff boundaries，不添加 consumer-specific state、private
validation fixtures、product UI 或 application backend logic。

## 范围外后续

- `0.8.1`：minimum working-state contract 和 claim taxonomy。
- `0.8.2`：core observable surface boundary。
- `0.8.3`：generation、runtime 和 Agent-loop readiness。
- `0.8.4`：external-validation handoff contract。
- `0.8.5`：core-side working-state smoke evidence。
- `0.8.6` 到 `0.8.8`：audit、release-candidate 和 final closeout。
