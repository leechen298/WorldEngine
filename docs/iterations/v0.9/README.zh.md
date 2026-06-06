# v0.9 LLM-backed World Lifecycle Foundation

英文镜像：`README.md`。

Status：reviewed / ready for child package development
Type：Codex `/goal` development campaign and iteration package root
implementation_authorized：no
evidence_execution_authorized：no

## 目标

v0.9 要把 WorldEngine 从“基础生命周期已验证”推进到“第一版 LLM-backed 生命周期基础”。

这个版本的目标是：由 WorldEngine 自己调用 live provider，把用户输入的基础世界观生成成
公开、可运行的世界模型；世界运行要可控；用户可以用自然语言引导世界层面的方向，但不能
直接强行改 Agent 私有状态或最终事实；世界参数和事件要按规则演化；Agent 要有公开的连续性
证据，并且这种连续性要参考类脑结构和睡眠/休息沉淀节奏；最后这些都要能被 checker-backed
evidence 验证。

人话说：v0.9 要让 WorldEngine 第一次真正用 LLM 创建并驱动世界，同时保证运行可控、
证据可查、边界安全。

## 来自 v0.8 的交接

v0.8 已关闭 basic lifecycle 和 external-validation readiness boundary。当前交接事实是：

- basic `worldengine-full-lifecycle-autonomous` 在 public provider metadata redaction
  checker repair 后，可以通过官方 checker。
- basic flow 已证明创建世界、tick 推进、事件、快照、一次 WorldEngine-backed Agent
  action、自然语言方向边界和 evidence export。
- LLM-backed suite 当前是 `BLOCKED`。这不是 basic product flow 坏了，而是 provider
  live smoke、LLM-backed world creation、rule-linked evolution、event legality、
  persistent Agent autonomy evidence 和 LLM-backed checker/schema support 还不存在。

v0.9 从这些 blocker 开始。它不得重新打开 `0.8.9.3`，也不得把 planned LLM-backed
testing docs 当成当前可 PASS 的覆盖。

## 范围

reviewed child authorization 后，v0.9 允许处理：

- WorldEngine-owned provider configuration 和 live smoke calls。
- redacted provider evidence 和 provider readiness semantics。
- LLM-backed worldview ingestion 和 public world model generation。
- generated world parameters、rules、constraints、boundaries 和 validation metadata。
- 生成后立即验证和运行后验证的 worldview fidelity checks。
- bounded runtime controls，例如 run N ticks、run for world-time duration、pause、
  resume 和 max-run limits。
- natural-language world direction，只影响 external events 和 world environment
  trends，不直接改 Agent private state。
- rule-linked parameter evolution 和 event legality checks。
- brain-inspired public Agent continuity contracts：perception、working 或 short-term
  memory、long-term memory summaries、personality summaries、skill summaries、intent
  states、behavior 和 event reactions，不泄露 raw chain-of-thought 或 private memory。
- sleep、rest 或 low-activity consolidation cadence，用于 memory、personality 和 skill
  updates。Consolidation 可以跨多个 ticks，不得被建模成每 tick 强制更新 personality 或
  long-term memory。
- external narrative projection 和 out-of-world diagnostic conversation boundaries。这些
  surface 可以帮助人类或 validator 理解运行情况，但默认不得成为 in-world events 或 Agent memories。
- LLM-backed autonomous checker、fixtures、result schema、scorecard 和 second-Agent
  review support。
- WorldEngine 到 Validation Client 的 evidence handoff contracts。

除非后续 reviewed package 明确改变 roadmap，否则 v0.9 禁止：

- 不让 Validation Client 拥有 provider calls 或 provider keys。
- 不存储、展示或导出 API keys、authorization headers、raw prompts、raw provider
  responses、raw provider traces、private Agent memory、raw thought 或 hidden context。
- 不允许用户 direction 直接设置最终世界事实，例如“Agent X 死亡”；用户 direction 必须被
  转换成 bounded world-level pressure、constraints、probability shifts 或 external event
  candidates。
- 不把 Agent personality、long-term memory 或 skill drift 设计成 automatic per-tick updates。
- 不把外部 player-to-Agent diagnostic conversation 当成 in-world dialogue、world timeline
  content 或 Agent memory，除非未来 reviewed package 明确建立这种 bridge。
- 不允许 narrative text generation 修改 canonical world state。
- 不在本仓库加入 concrete demo worlds、maps、characters、locations、resources、
  story rules、app-specific backend behavior 或 product packaging。
- 不在 `backend/worldengine/` 下新增 runtime features。
- 没有 current-session checker 或 scorecard evidence 时，不声明 product readiness、
  human-quality simulation、consciousness、full selfhood、external validation PASS 或
  LLM-backed lifecycle PASS。

## Planned Package Roadmap

`v0.9-plan.md` 是详细 planned-package specification。里面的 planned packages 只是
route-map specs，不是 active implementation authorization，也不是完整 child package docs。

计划顺序：

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

## 当前状态

Active child package：none。

Current route：

```text
0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed
```

Implementation authorization：no。

Evidence execution authorization：no。

Audit execution authorization：no。

Implementation 必须等 concrete child package 在 documentation/contract/design/test-plan review 后
记录 positive implementation authorization。

## Goal Entries

自然语言 goal：

```text
完成 v0.9
开发 v0.9
生成 v0.9 文档
编写 v0.9 文档
启动 WorldEngine v0.9：LLM-backed World Lifecycle Foundation
```

通过 `GOAL_RUNNER.md`、`CURRENT_STATE.md`、`CAMPAIGN_PLAN.md` 和 `v0.9-plan.md`
路由。

## 验证边界

v0.9 不允许靠 UI smoke 或主观 review 通过。PASS 必须来自 documented checker output、
scorecard summary，以及 active package 要求时的 second-Agent read-only review。

Validation Client 可以操作和导出 evidence，但真正被验证的是 WorldEngine，LLM 行为也由
WorldEngine 拥有。

## Final Assessment State

当前值：`reviewed / ready for child package development`。

这个 parent documentation package 定义 v0.9 方向和 planned package sequence。它本身不授权任何
runtime、schema、API、checker、fixture、frontend、evidence、provider、Validation Client 或
`backend/worldengine/` implementation work。

下一条合法 route 是创建或 review concrete `0.9.0` child package documents。后续 `0.9.x`
package completion 必须只由对应 reviewed child package 和 current-session evidence 声明。
