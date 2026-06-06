# Project North Star

Status: authoritative project direction

英文版本：`project-north-star.md`。

## Core Mission

WorldEngine 是 recursive world generation 与 runtime engine。它也是 Agent 在 world 中通过
lived experience 形成 continuity、memory、feedback-shaped behavior 和 pseudo-self 的
runtime substrate。

WorldEngine 存在是为了支持五个长期能力：

1. 从 structured inputs、templates 和 AI-assisted generation 生成 worlds。
2. 让 worlds 作为 stateful systems 随时间运行，拥有 events、rules、timelines、resources、
   history、snapshots 和 recovery。
3. 支持 recursive world structures：worlds 可以包含 child worlds、projected worlds、
   subjective worlds 和 specialized runtime cells。
4. 让 Agent 在 worlds 中生活，perceive events、act、accumulate memory、update goals，并通过
   feedback 变化。
5. 让 Agent 发展出 sustained pseudo-self：identity continuity、self-narrative、
   relationship history、personality drift，以及由 prior experience 塑造的 decision
   patterns。

## LLM-backed Execution Direction

AI-assisted generation 和 reasoning 是 engine-owned capabilities。External clients 可以提供 user
input、展示 projections、导出 evidence，但 WorldEngine 拥有 provider configuration、provider
calls、redaction boundaries、structured outputs，以及验证这些 outputs 所需的 public evidence。

LLM output 不能被当作 hidden truth 接受。它必须被转换成 public、structured、inspectable 的
world models、rules、events、summaries、projections 或 validation artifacts，让 runtime 和
checker 可以 reason about。

## Agent Continuity Direction

Agent continuity 应设计成 cognition substrate，而不是 per-tick status updater 或 chat wrapper。
Memory、personality、skill、intent 和 self-narrative 应通过 explicit state、experience、
feedback 和 consolidation processes 演化。

长期 Agent 设计可以使用 sleep、rest 或 low-activity phases，让 working memory、long-term
memory、personality summaries 和 skill summaries 跨多个 ticks 沉淀。WorldEngine 不得假定
meaningful memory、personality 或 skill changes 每个 tick 都发生。

## What This Does Not Claim

WorldEngine 不宣称 real consciousness。`pseudo-self` 指可工程化、可检查、可测试、可改进的
continuity model。它是 product 和 engineering target，不是 metaphysical claim。

## External Projection Applications

External projection applications 是 WorldEngine 的 consumers 和 validation surfaces。它们通过
public engine contracts 验证 engine，但不是 core repository 的一部分。

它们是：

- engine 的 public consumers。
- runtime、events、memory 和 Agent continuity 的 external validation consumers。
- product-specific UI 与 application behavior 在 core repository 外部落地的位置。
- narrative、replay、diagnostic 和 inspection surfaces，可以帮助人类理解 running world，但
  不是 world 本身。

它们不是：

- WorldEngine 的 purpose。
- 让 engine 变成 demo-specific 的理由。
- 用 application-only state 替代 recursive world architecture 的理由。
- 拥有 provider behavior、Agent private memory、canonical world mutation 或 authoritative
  evaluation 的位置。

Narrative projections 和 out-of-world diagnostic conversations 可以是有用的 external views。
默认情况下，它们必须读取 public world evidence，且不得修改 canonical world state、world
timelines 或 Agent memory。

## Architecture Anchor

World 是 recursive runtime unit。一个 world 可以包含 child worlds、locations、agents、rules、
resources、timelines、event streams、projection config 和 external connectors。后续
milestones 可能把 Agent 的 subjective memory 或 self-narrative space 建模为 specialized
world cells，但 v0.2 只为这个方向建立 foundation。

## Decision Rule

当 proposed feature 与本文档冲突时，proposal 必须修改或被拒绝。如果 north star 本身需要改变，
先更新本文档，并在 iteration package 中记录该 decision。
