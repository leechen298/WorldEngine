# 完整产品验证覆盖地图

状态：计划中的覆盖地图

英文镜像：`coverage-map.md`。

## 权威来源

覆盖范围来自：

- `docs/project-north-star.md`。
- `docs/product-model.md`。
- `docs/scope-boundaries.md`。
- `docs/roadmap.md`。
- 当前 `docs/testing/` scenario contracts 和 playbooks。

本地图是产品级的。某一次具体验证可以把部分能力标记为 `out_of_scope`，但如果声明完整
产品验证，就不能静默遗漏这些能力。

## 能力分类

| ID | 能力区 | 最终必须可测试什么 | 主要证据类型 |
| --- | --- | --- | --- |
| CPV-01 | Governance 和 scope boundary | 工作符合 North Star、active code path、iteration gates；core 中没有 demo-specific data 或 external validation internals。 | docs audit、scope guard、review evidence。 |
| CPV-02 | Recursive world schema | `WorldCell`、`WorldSpec`、refs、additive event references、schema compatibility 和 invalid payload rejection。 | unit tests、schema smoke、contract docs。 |
| CPV-03 | WorldSpec loader 和 runtime bridge | 有效 generic world specs 能加载到 runtime context，并保持 v0.1 runtime compatibility。 | backend focused tests、API summaries。 |
| CPV-04 | World generation | deterministic templates、structured generation plans、import boundaries、preview、regeneration、runtime-readiness，以及实现后的 LLM-backed generation。 | backend tests、E2E、generation summaries、LLM redacted evidence。 |
| CPV-05 | Runtime progression | ticks 推进时间、rules 被评估、state changes 被应用，runtime 不依赖 hidden side effects。 | backend tests、events、snapshots、lifecycle summaries。 |
| CPV-06 | Event spine 和 timeline | events 可追加、可查询、typed、redacted、支持 references，并作为系统 spine。 | event API tests、timeline E2E、API summary、event artifacts。 |
| CPV-07 | Snapshots、replay 和 recovery | 生成 snapshots，replay 能检查历史状态，branch-like worldlines 不依赖 app-specific assumptions。 | snapshot artifacts、replay summaries、E2E、Validation Client evidence。 |
| CPV-08 | Parameters 和 state diffs | params 可校验、可应用、拒绝 invalid/reserved paths，并产生可复核 diffs。 | backend tests、params-flow E2E、Agent smoke。 |
| CPV-09 | Agent minimal loop | Agents 感知 events，产生 action intents，执行 supported actions，并通过 public contracts 接收结果。 | backend tests、API tests、Agent loop E2E。 |
| CPV-10 | Agent memory substrate | working memory、episodic memory、memory context、isolation 和 read-only perception boundaries 生效。 | backend tests、memory summaries、archive summaries。 |
| CPV-11 | Agent self-continuity 和 pseudo-self | 实现后，public evidence 能展示 identity continuity、self-summary、relationship history、personality drift signals、intent、reflection 和长期 behavior。 | Agent autonomy summaries、snapshots、second-Agent review。 |
| CPV-12 | LLM provider integration | Provider env readiness 和最小 live calls 通过 WorldEngine 工作，而不是通过客户端，并且 evidence 脱敏。 | provider live summary、checker output。 |
| CPV-13 | LLM-backed world creation 和 evolution | 用户 premise 生成 system-digestible public state、parameters、rules、legality constraints，并能 rule-driven evolution。 | LLM-backed lifecycle summaries、scorecard、checker。 |
| CPV-14 | Event legality 和 external guidance | Random events 和用户方向只影响 external environment，outcomes 由 world rules adjudicate。 | event legality summaries、diffs、snapshots。 |
| CPV-15 | Projection 和 read models | public consumers 可检查 bounded read-only projections，且没有 private app state 或 write capability。 | projection schema/checker、API summary、external reports。 |
| CPV-16 | Dashboard 和 local UI | dashboard runtime、params、timeline、archive summary、Agent tools、generation preview 可用。 | frontend unit tests、build、Playwright E2E。 |
| CPV-17 | External Validation Client handoff | 外部客户端可消费 public APIs/contracts、记录操作、导出 evidence，并且不拥有 engine logic。 | cross-repo evidence bundle、public API summary、operation log。 |
| CPV-18 | Agent-assisted testing | Agent smoke 和 autonomous saved-result validation 使用 allowed operations，PASS 来源由 checker 控制。 | operation logs、result.json、scorecard、checker output。 |
| CPV-19 | Evidence、redaction 和 reports | evidence 完整、脱敏、durable、可复核；secrets/private internals 不泄露。 | redaction scan、evidence bundle、result summaries。 |
| CPV-20 | Reliability、compatibility 和 regressions | focused tests 和 broad regressions 保护旧版本、APIs、schemas、dashboard behavior 和 testing tools。 | command matrix、full backend/frontend/E2E outputs。 |

## 完整验证层级

| 层级 | 名称 | 覆盖 |
| --- | --- | --- |
| L0 | Documentation and scope audit | CPV-01、current state、claim boundaries。 |
| L1 | Schema and contract validation | CPV-02、CPV-15、CPV-19。 |
| L2 | Backend unit and API compatibility | CPV-03 到 CPV-10、CPV-20。 |
| L3 | Generation and import validation | CPV-04、CPV-13 preconditions。 |
| L4 | Runtime lifecycle validation | CPV-05 到 CPV-08。 |
| L5 | Agent loop and memory validation | CPV-09 到 CPV-11。 |
| L6 | Frontend and dashboard E2E | CPV-16。 |
| L7 | Agent smoke validation | CPV-18 focused smoke。 |
| L8 | Autonomous saved-result validation | CPV-17 到 CPV-19 recorded evidence。 |
| L9 | LLM-backed lifecycle validation | CPV-12 到 CPV-14 加 CPV-11。 |
| L10 | External client evidence review | CPV-17 到 CPV-19。 |
| L11 | Final verdict audit | 所有 in-scope CPV items。 |

## 最小完整运行要求

后续“完整产品验证”运行必须为每个 CPV row 生成矩阵，并给出以下状态之一：

- `pass`。
- `fail`。
- `blocked`。
- `skipped`。
- `out_of_scope`。

任何 row 都不能省略。如果某个能力属于未来路线图，标记为 `out_of_scope` 并说明原因。
如果它应属于当前范围但没有支持，应标记为 `fail` 或 `blocked`，不能标记为 `pass`。
