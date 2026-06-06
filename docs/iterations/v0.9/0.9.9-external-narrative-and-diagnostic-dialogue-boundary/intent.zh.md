# Intent

英文原文：`intent.md`。

## 问题

WorldEngine 现在已有 public Agent continuity 和 consolidation evidence，但未来 validator 和
clients 还需要 readable projection surfaces：

- narrative projection，用 external prose 或 public read model 总结世界。
- diagnostic Agent dialogue，让 user 或 validator 可以询问 Agent，但不把这次 exchange 变成
  world timeline 的一部分。

这些 surface 对 inspection 有用，但如果被误认为 canonical world state 就会很危险。Narrative
paragraph 不应因为存在就变成 event；diagnostic questions 默认也不应写入 Agent memory。

## 目的

在 LLM-backed checker 或 Validation Client handoff 依赖这些 outputs 前，本包先建立 reviewed
boundary。

## 期望结果

Implementation 后，WorldEngine 应能公开 artifacts，并明确说明：

- 使用了哪些 canonical public evidence。
- artifact 是否在 canonical world state 之外。
- 是否修改了 canonical events、snapshots、Agent memory 或 Agent continuity。
- redaction 是否通过。

本包不得声明 narrative quality、in-world chat、human-like Agent interiority、product readiness、
checker PASS 或 full v0.9 validation PASS。

## 非目标

- 不做 frontend chat UI。
- 不做 product-specific narrative/game content。
- 不做 live provider narrative generation。
- 不做 diagnostic-to-memory bridge。
- 不做 checker fixture implementation。
- 不做 Validation Client implementation。
