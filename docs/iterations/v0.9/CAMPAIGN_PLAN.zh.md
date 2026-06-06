# Campaign Plan

英文镜像：`CAMPAIGN_PLAN.md`。

Status：reviewed / 0.9.9 implementation complete / verification passed

## 目标

以 review-gated `/goal` campaign 方式运行 v0.9，建立 WorldEngine 第一版 LLM-backed
world lifecycle foundation。

这个 campaign 的目标不是做完整游戏或外部产品客户端，而是让 WorldEngine 具备：

- 通过 WorldEngine-owned configuration 调用 live provider。
- 从用户基础世界观生成 public runnable world model。
- 在生成后立即验证和 bounded runtime execution 后验证世界观生成是否准确。
- 通过 tick count、world-time duration、pause、resume 和 provider/cost bounds 控制
  世界运行。
- 把用户 natural-language direction 接收为 bounded world-level guidance。
- 通过 explicit rules 和 legality checks 演化 parameters 和 events。
- 暴露 brain-inspired public Agent continuity evidence，且不泄露 private internals。
- 把 Agent consolidation cadence 和 per-tick runtime progression 分开，让 memory、personality
  和 skill updates 可以在 sleep、rest 或 low-activity phases 中沉淀。
- 定义 external narrative projection 和 out-of-world diagnostic player-to-Agent conversation
  为 inspection surfaces，而不是 canonical world mutation。
- 通过 checker-backed LLM-backed lifecycle validation 证明上述能力。

## Parent Drafting 已读取的权威输入

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`

## Campaign Rules

- Parent v0.9 package 是 authoritative campaign entrypoint。
- `v0.9-plan.md` 中 planned `0.9.x` entries 是 roadmap-level planned package specs。
  它们不授权 implementation，也不是不可变 execution scripts。
- 每个 child 的 implementation authorization 初始都是 no。
- 每个 child 的 provider live-call authorization 初始都是 no。
- Mixed/code packages 必须先完成 documentation review，之后才可 implementation。
- Historical v0.8 evidence 只能作为 handoff context。
- Planned LLM-backed testing docs 是 validation specs，不是 current PASS evidence。
- 声明 v0.9 provider live smoke、LLM-backed world creation、rule evolution、event
  legality、Agent autonomy、checker support、Validation Client evidence export、full
  lifecycle validation 或 release claims 前，必须有 current-session command evidence。
- Chinese mirrors 必须保留 status、type、goal、scope、forbidden changes、
  compatibility requirements、findings 和 final assessment 语义。
- Readiness claims 必须区分 `planned`、`blocked`、`implemented`、`checker-supported`、
  `evidence-ready`、`validation-pass` 和 `out of scope`。

## Planned Child Sequence

1. `0.9.0-v0.9-planning-and-v0.8-handoff-baseline`
2. `0.9.1-provider-live-smoke-and-redaction-boundary`
3. `0.9.2-llm-worldview-ingestion-and-generation-contract`
4. `0.9.3-world-model-rule-parameter-schema`
5. `0.9.4-worldview-generation-fidelity-evaluation`
6. `0.9.5-bounded-runtime-control-and-run-budget`
7. `0.9.6-natural-language-world-direction-boundary`
8. `0.9.7-rule-linked-evolution-and-event-legality`
9. `0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`
10. `0.9.9-external-narrative-and-diagnostic-dialogue-boundary`
11. `0.9.10-llm-backed-autonomous-checker-and-fixtures`
12. `0.9.11-validation-client-evidence-handoff-contract`
13. `0.9.12-llm-backed-full-lifecycle-validation-execution`
14. `0.9.13-v0.9-release-candidate-and-closeout`

这个 sequence 是 route proposal，可由 reviewed child package documents 修订。如果
implementation 或 evidence 暴露设计问题，不得机械执行。

## Cross-Child Handoff Rules

- `0.9.0` hand off reviewed v0.9 campaign structure 和 v0.8 blocker baseline。
- `0.9.1` hand off provider live smoke 和 redacted provider evidence。
- `0.9.2` hand off LLM-backed world creation output shape 和 generation metadata。
- `0.9.3` hand off world parameters、rule schema、constraints 和 boundary semantics。
- `0.9.4` hand off worldview fidelity evaluation before and after bounded run。
- `0.9.5` hand off bounded runtime 和 provider/cost run controls。
- `0.9.6` hand off natural-language world direction semantics 和 queueing。
- `0.9.7` hand off rule-linked parameter evolution 和 event legality。
- `0.9.8` hand off brain-inspired public Agent continuity 和 consolidation evidence。
- `0.9.9` hand off external narrative projection 和 diagnostic dialogue boundaries。
- `0.9.10` hand off LLM-backed checker、fixtures、schema 和 scorecard。
- `0.9.11` hand off Validation Client 需要的 public evidence artifacts，但不在本仓库实现客户端。
- `0.9.12` hand off live 或 explicitly blocked full lifecycle validation evidence。
- `0.9.13` 只在 evidence consistency 和 review gates 通过后关闭 v0.9。

## Campaign Exit Criteria

v0.9 只有在以下条件满足后才可标记为 `final / closeout complete`：

- 所有 active child packages review complete 或由 contract 明确 deferred。
- implementation-bearing children 记录 current-session command evidence。
- provider live-call evidence 已 redacted 且 checker-validated，或 remaining provider
  blockers 已明确分类。
- generated world output 是 public、system-digestible、premise-specific，并且不是
  deterministic generic fallback。
- worldview fidelity checks 验证 generated output 和 bounded runtime behavior，或 blocker
  已分类。
- runtime controls 防止 unbounded tick、duration、provider-call 和 cost execution。
- user direction 是 world-level guidance，不能直接 mutate Agent private state 或 final facts。
- event generation 绑定 rules、state、probability、causality、location、time 和 legality
  evidence。
- Agent continuity evidence 是 public，且不暴露 raw thought、chain of thought、private
  memory、hidden context 或 private goals。
- Agent memory、personality 和 skill consolidation 不建模成 automatic per-tick mutation；
  sleep/rest/low-activity consolidation evidence 必须 explicit，或 blocker 已分类。
- narrative projection 和 diagnostic player-to-Agent conversation 保持在 canonical world state
  外，除非 reviewed future bridge 明确改变该边界。
- LLM-backed checker/schema/fixtures 可以判断 required artifacts。
- Validation Client handoff 通过 public evidence contracts 定义。
- unresolved findings 已分类，且没有未明确接受的 P1/P2。

## Stop Conditions

出现以下情况必须在 implementation 或 closeout 前停止：

- active child package docs 缺 required files 或 mirrors。
- planned package 尚未转换为 current child package docs。
- provider call work 在没有 explicit active child authorization 时开始。
- required evaluator checkpoint 不可用或报告 blocking P1/P2。
- implementation 触碰 active package contract 外文件。
- implementation 发现 design gap，但 active child docs 尚未 update 并 re-reviewed。
- tests、checkers 或 provider calls 失败，且 package 不能诚实记录 pass evidence。
- user direction 绕过 rules 并直接写 final facts。
- Validation Client 开始拥有 LLM behavior。
- core repository 出现 concrete application content 或 product-specific backend behavior。
- README、current state、plan、review 和 closeout docs 之间 status surfaces drift。
