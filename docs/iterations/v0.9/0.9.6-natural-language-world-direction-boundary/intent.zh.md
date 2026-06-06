# Intent

英文原文：`intent.md`。

## 本包存在原因

v0.9 需要让用户能引导运行中的世界，但不能把用户文本变成 direct state mutation。现有 public
director guidance endpoint 已证明 basic redacted handoff surface，但它只是把 guidance 作为
简单 public event 接收，还没有定义 allowed world-level pressure 和 forbidden direct final
outcomes 之间的结构化边界。

`0.9.6` 要在 `0.9.7` rule-linked evolution and event legality 之前建立这个边界。Direction
必须成为 queued guidance，供后续 rule/evolution packages adjudicate；它自己不得决定 illegal
events，也不得强制 Agent outcomes。

## 用户价值

用户可以表达希望世界考虑的 pressure、risk、trend、constraint 或 environmental direction，
同时 WorldEngine 保留 rule-led causality 和 Agent autonomy boundaries。

## 工程价值

本包为后续 packages 提供 public、structured direction artifact：

- 哪些内容作为 world-level guidance 被接受。
- 哪些内容作为 direct mutation 被拒绝。
- guidance 何时可以被考虑。
- 哪些 public rule references 或 future adjudication hooks 可以消费它。
- redaction status 如何保护 evidence 不泄露 private internals。

## 范围内

- 定义并实现 public direction intake semantics。
- 区分 allowed environmental/event-bias guidance 和 forbidden final outcomes。
- 将 accepted guidance queue 到 bounded future consideration。
- 保持现有 public director guidance endpoint compatibility。
- 添加 focused tests 和 review evidence。

## 范围外

- Natural language 的 live provider interpretation。
- Generated result directories。
- Checker execution 或 external validation。
- Rule-linked event legality 或 final event adjudication。
- Agent private memory、goal、personality、relationship、inventory 或 life state mutation。
- Frontend UI 和 Validation Client changes。
- Durable scheduling 或 background processing。
- `backend/worldengine/` changes。

## 交接

交接给 `0.9.7` 的内容是 external world guidance 的 public queue 和 summary contract。
`0.9.7` 后续可以消费该 contract，评估 events 和 parameter changes 是否符合 world rules。
