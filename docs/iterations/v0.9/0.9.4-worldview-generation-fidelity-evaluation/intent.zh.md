# Intent

英文原文：`intent.md`。

## 问题 / 目的

`0.9.2` 引入了 non-live public worldview generation surface，`0.9.3` 引入了
generated rule/parameter schema。这些输出可以是结构化且已脱敏的，但仍可能没有满足用户的
premise。v0.9 因此需要一个 deterministic public evaluation layer，用来判断
generation evidence 是 faithful、missing important premise coverage、
contradictory、blocked，还是尚不可运行。

## 为什么现在做

父级 v0.9 campaign 需要在 bounded runtime control、natural-language
direction、rule-linked evolution、Agent continuity 和 full LLM-backed
validation 之前获得 fidelity evidence。否则后续 runtime evidence 可能看起来在运行，
但实际已经偏离原始 worldview。

## 与路线图的关系

本包通过把 worldview quality 转化为 public、checker-compatible contract，推进 v0.9
LLM-backed lifecycle foundation。它支撑 North Star：generated worlds 必须可检查、
由规则和证据驱动，而不是依赖主观印象。

## 非目标

- 不运行 live provider calls。
- 不创建 generated result artifacts。
- 不实现 bounded runtime controls。
- 不实现 rule-linked event legality 或 parameter evolution。
- 不实现 Agent continuity、consolidation、narrative projection 或 diagnostic dialogue。
- 不修改 Validation Client code 或 external repositories。
- 不存储 concrete validation-world fixtures、raw prompts、raw provider responses、
  private evaluator oracles、private Agent memory、raw thought 或 hidden context。

## 预期交接

`0.9.4` 应向 `0.9.5` 交接 public immediate 和 bounded-run fidelity artifact
schemas，以及 deterministic helper behavior。`0.9.5` 会提供 actual bounded
runtime controls，从而支持更强的 run-based evidence。

