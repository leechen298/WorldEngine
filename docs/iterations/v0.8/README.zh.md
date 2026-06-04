# v0.8 Minimum Proved Working WorldEngine / External Validation Readiness

状态：final / closeout complete
类型：Codex `/goal` development campaign and iteration package root

## 目标

v0.8 准备 WorldEngine 达到一个最小“正常工作”状态，并让仓库外部的 validation
function 可以从外部观察和判断这个状态。

本版本不在本仓库内实现 external validation function，也不实现第一个 external
product application。目标是让 core engine 的 generation、runtime、Agent loop、
memory-context、event 和 projection surfaces 足够一致、可观察，让独立的外部
validator 或 projection application 能判断 WorldEngine 是否正常工作。

v0.8 从 v0.7 历史 closeout evidence 以及当前 `0.7.9` checker/docs repair evidence
之后开始。`0.7.9-v07-cr-checker-schema-repair` 清除了当前 v0.7 checker/docs
validation scope 的 V07-CR checker/docs blocker gate，但它只能作为 handoff evidence。
它不证明 v0.8 clean pass、minimum working-state PASS、external validation readiness
PASS、product readiness、external consumer PASS、runtime/API/frontend/E2E PASS、live
Agent smoke PASS、full autonomous PASS 或 generation-quality PASS。

## Goal Entry

自然语言目标：

```text
完成 v0.8
启动 WorldEngine v0.8：Minimum Proved Working WorldEngine / External Validation Readiness
编写 v0.8 文档
生成 v0.8 文档
```

解释：

- 从 `CURRENT_STATE.md` 开始。
- 按 `GOAL_RUNNER.md` 选择 route、执行 documentation gates、
  implementation authorization、evaluator checkpoints、verification 和 stop
  conditions。
- 按 `CAMPAIGN_PLAN.md` 与 `v0.8-plan.md` 确认 child sequence、
  deliverables、compatibility constraints 和 handoff rules。
- 把 parent v0.8 package 作为当前唯一 authoritative entrypoint。
- 任何未来 child package 开始前，都必须在当时创建或确认完整 package document
  set 并完成 review gate。不得把 planned `0.8.x` roadmap entries 当成
  execution-approved child contracts。

这不是 external validation application、external projection application、
external repository、product packaging workflow、deployment process、concrete
validation scenario 或 application-specific backend。

## External Validation Boundary

WorldEngine 可以知道外部会存在一个 validation function，并由它验证 engine 是否正常
工作。WorldEngine 不拥有该外部 validator 的实现、private scenarios、product UI、
application state、runner internals、oracle logic、private repository paths 或
concrete world content。

本仓库内，v0.8 只可以定义让外部验证成为可能的 core-side public surfaces 和 evidence
expectations：

- stable public API 与 read-model expectations。
- minimum working-state claim taxonomy。
- observable event、runtime、generation、Agent loop 和 memory-context evidence
  boundaries。
- 未来 external evidence 的 redaction 与 no-private-detail rules。
- 防止 internal tests 被过度声明为 external validation PASS 的 stop rules。

## v0.7 交接基线

v0.7 parent route 历史状态是 `final / closeout complete`，且
`docs/testing/results/2026-06-02-v0.7-code-review.md` 曾记录 post-closeout
issues，涉及 checker、schema、manifest 和 projection read-model semantics。

当前 v0.7 状态已记录 `0.7.9-v07-cr-checker-schema-repair` review complete。
`docs/testing/results/2026-06-02-v0.7-overall-validation.md` 记录了当前 v0.7
checker/docs validation scope 的 clean pass，并清除了 V07-CR checker/docs blocker
gate。

该 repair evidence 仍是有边界的 handoff baseline。它不声明 external suite PASS、
projection readiness PASS、product readiness PASS、runtime/API/frontend/E2E PASS、live
Agent smoke PASS、full autonomous runner/full-suite PASS 或 v0.8 readiness。

## 范围

v0.8 允许范围：

- minimum normally working WorldEngine readiness concepts。
- external validation 所需的 engine-side public surface requirements。
- core-side generation/runtime/Agent-loop/memory-context readiness boundaries。
- 只有在 reviewed child package 明确授权实现时，才可 harden generic read-only
  projection 或 read-model payload。
- provider-boundary、credential、mock fallback 或 live-smoke semantics 只有在
  reviewed child package 明确拥有该范围时才可处理。
- public engine surfaces 的 core-side smoke 与 compatibility evidence。
- release-candidate、final closeout 和 post-closeout evidence documents。

v0.8 禁止范围：

- 不在本仓库内实现 external validation function 或 external projection application。
- 不添加 concrete app worlds、names、maps、locations、characters、resources、
  story rules、seed data、UI selectors、private transcripts、product routes、
  product packaging、deployment scripts 或 app-specific backend logic。
- 不添加 private external repository paths、private runner state、hidden reset
  APIs、validation oracle internals、prompt/provider traces、secrets 或
  non-redacted external event payloads。
- 没有当前 session 证据时，不声明 external validation PASS、external consumer
  PASS、product readiness、runtime/API/frontend/E2E PASS、Agent smoke PASS、
  autonomous PASS 或 generation-quality PASS。
- 除非 reviewed child package 明确授权该范围，不添加 durable persistence、
  migrations、live provider behavior 或 generated-world active runtime execution。
- 不在 `backend/worldengine/` 下添加新 runtime features。

## 交付物

- Parent goal-campaign documents：`README.md`、`v0.8-plan.md`、
  `GOAL_RUNNER.md`、`CURRENT_STATE.md`、`CAMPAIGN_PLAN.md`、`review.md`，以及
  Chinese mirrors。
- `v0.8-plan.md` 内的 planned `0.8.x` child-package specifications。
- 明确的 v0.7 handoff-risk handling 与 stop rules。
- 明确的 boundary rules：external validation 在本仓库外，core-side readiness
  for that validation 在本仓库范围内。
- Documentation-stage review evidence，证明本次 drafting pass 不修改 runtime、
  schema、API、frontend、test implementation、fixture、migration、external
  repository、generated result 或 `backend/worldengine/` implementation files。

## Planned Package Roadmap

下列 `0.8.x` entries 以及 `v0.8-plan.md` 中的条目是 roadmap-level planned
package specs。它们不是当前 implementation authorization，不是 execution-approved
contracts，也不是不可变脚本。未来 agent 必须在 child 启动时创建或确认 active child
package documents，然后完成 review 才能 implementation。

### `0.8.0-v0.8-planning-and-v0.7-handoff-baseline`

- 类型：documentation-only
- 状态：review complete
- 目的：创建 v0.8 documentation root、goal-campaign controls、v0.7
  handoff-risk baseline、minimum working-state boundary、external-validation
  boundary 和 package sequence。

### `0.8.1-minimum-working-state-contract`

- 类型：documentation-only
- 状态：review complete
- 目的：定义 v0.8 何时可以称为 minimum normally working WorldEngine state，同时不声明
  product readiness 或 external validation PASS。

### `0.8.2-core-observable-surface-boundary`

- 类型：documentation-only
- 状态：review complete
- 目的：定义 external validator 可观察的 public runtime、event、generation、
  Agent loop、memory-context 和 read-model surfaces。

### `0.8.3-generation-runtime-agent-loop-readiness`

- 类型：mixed or code
- 状态：review complete
- 目的：如果 reviewed child package 授权实现，则 harden core-side minimum
  generation -> runtime -> Agent loop readiness slices。

### `0.8.4-external-validation-handoff-contract`

- 类型：documentation-only
- 状态：review complete
- 目的：定义 WorldEngine 为 external validation function 暴露或记录什么，但不定义外部
  validator 如何连接或运行。

### `0.8.5-core-working-state-smoke-evidence`

- 类型：mixed validation package
- 状态：review complete
- 目的：对 in-scope public engine surfaces 运行 core-side smoke 与 compatibility
  evidence，不运行也不实现 external validator。

### `0.8.6-v0.8-evidence-and-boundary-audit`

- 类型：documentation-only
- 状态：review complete
- 目的：在 release-candidate packaging 前 audit evidence、compatibility surfaces、
  unresolved findings 和 external-validation leakage risks。

### `0.8.7-v0.8-release-candidate-bundle`

- 类型：documentation-only
- 状态：review complete
- 目的：基于 reviewed evidence 准备 release-candidate bundle，不超出当前 session
  evidence 声明 final readiness。

### `0.8.8-v0.8-final-closeout`

- 类型：documentation-only
- 状态：final / closeout complete
- 目的：只有在 reviewed package completion、evidence consistency checks、scope
  review、blocker classification 和 evaluator approval 后，才标记 v0.8 final。

### Post-closeout addendum: `0.8.9-external-validation-provider-and-handoff-manifest`

- 类型：documentation-only planning package
- 状态：implemented / `WORLDENGINE_CONTRACT_READY`
- 目的：记录准备 Codex 自主验证时发现的 WorldEngine 侧 public manifest、
  provider-readiness 和 Validation Client world-creation contract 前置条件。
- 边界：该 addendum 不重新打开 `0.8.8` final closeout，也不声明 external
  validation PASS、Codex autonomous validation PASS 或 human validation PASS。

### Implementation child package: `0.8.9.1-public-handoff-manifest-and-world-creation-contract`

- 类型：mixed implementation package
- 状态：implementation complete / `WORLDENGINE_CONTRACT_READY`
- 目的：为实现 `GET /manifest`、OpenAPI 可发现的 `POST /worlds`、public
  world creation response、provider-readiness redaction，以及可选 public director
  guidance status 提供具体 reviewed gate。
- 边界：该 child package 只实现 WorldEngine Gate 1。未修改 Validation Client code、
  未添加 concrete demo-world content、未暴露 secrets 或 private Agent state，也未声明
  external validation PASS。

### Repair package: `0.8.9.2-director-guidance-public-redaction-repair`

- 类型：mixed implementation package
- 状态：implementation complete / focused verification passed
- 目的：修复 public director guidance wording；第一次 full lifecycle autonomous
  validation result 因 evidence integrity redaction 失败。
- 边界：scoped repair 和 focused verification 已完成。live full lifecycle rerun、
  external repository changes、generated result rewrites 和 PASS claims 仍未授权。

## 当前状态

Active child package：none for implementation。

Current route：`final / closeout complete with external validation evidence handoff`。

Implementation authorization：no。

Evidence execution authorization：no。

Audit execution authorization：no。

`0.8.8-v0.8-final-closeout/test-plan.md` 中列出的 final verification commands 已运行，evidence
已记录。Closeout evaluator review 已在 reviewed v0.8 package scope 内通过。这个 parent state
不授权任何 runtime、schema、API、frontend、migration、external repository、generated
result、external validation implementation 或 `backend/worldengine/` implementation work。

Full lifecycle autonomous validation assets 位于 `docs/testing/` 和 `tools/testing/`，
不是 v0.8 iteration packages。第一次正式 full lifecycle validation result 已记录在
`docs/testing/results/` 下，并因 redaction 失败。上面的 repair package 是该失败的
reviewed-product-iteration 路径。

## 交接基线

- v0.7 状态：historical `final / closeout complete`，且 `0.7.9` 已完成当前 v0.7
  checker/docs validation scope 的 checker/docs repair。
- v0.7 `0.7.9` repair evidence 只能作为 handoff evidence，不能作为 current v0.8
  PASS evidence。
- v0.7 不证明 v0.8 minimum working-state readiness、external validation readiness、
  product readiness 或 external consumer PASS。
- v0.8 从自己的 package review gates 开始，不继承 v0.7 implementation
  authorization。

## Final Assessment State

当前值：`final / closeout complete`。

Parent v0.8 campaign docs 已通过 `0.8.8-v0.8-final-closeout` documentation/contract
review。Planned `0.8.x` entries 仍只是 route-map specifications。`0.8.4` 已 review
complete，并把 external-validation handoff contract hand off 给 `0.8.5`。
`0.8.5-core-working-state-smoke-evidence` 已 review complete，并把 core-side smoke evidence
hand off 给 audit package。`0.8.6-v0.8-evidence-and-boundary-audit` 已 review complete，
并推荐 release-candidate packaging。`0.8.7-v0.8-release-candidate-bundle` 已 review
complete，并且只授权 bounded release-candidate bundle handoff to final-closeout review。
`0.8.8-v0.8-final-closeout` documentation/contract review 已通过，final verification
commands 已运行，results 已记录。Closeout evaluator PASS 后，final closeout 已在 reviewed
v0.8 package scope 内授权。
External validation execution、
projection app build、product readiness 和 v0.8 readiness PASS claims 仍未授权。
