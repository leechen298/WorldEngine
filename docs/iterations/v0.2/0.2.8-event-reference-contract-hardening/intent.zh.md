# Intent

英文版本：`intent.md`

## 问题

v0.2 已通过 `EventRef` 和 `Event.refs` 引入 optional structured event
references。未来 memory、causality、projection 和 agent-in-world systems 会需要
清晰的 reference contract，但 v0.2 不能提前实现这些系统。

当前 schema 已支持无 refs 的 event construction、带 generic `id` / `kind`、
optional `role`、default metadata 的 refs、nested event pages，以及 model dump /
validate round trips。剩余风险是：未来工作可能从不充分的 additive field 文档中
推断出 resolver behavior、timeline causality、runtime WorldCell binding 或
domain-specific reference kinds。

## 目标

为加固 EventRef 和 Event.refs 定义 documentation 与 implementation plan，使其
成为 additive、event-local、domain-neutral reference structures，并具备可测试的
acceptance criteria。

成功的 implementation 状态是：

- `docs/contracts/event-ref-contract.md` 文档化 EventRef 和 Event.refs。
- focused compatibility tests 证明 optional refs、default behavior、
  validation boundaries、nested event containers 和 serialization round trips。
- existing event dictionaries without refs 仍能 validate。
- 不引入 resolver、causality engine、runtime binding、memory behavior、
  projection behavior 或 domain-specific reference catalog。

## 非目标

- 不实现 referential integrity resolver。
- 不实现 timeline causality engine。
- 不把 refs 绑定到 live WorldCell runtime state。
- 不实现 Agent action consequence logic。
- 不实现 memory、self-continuity、projection、generation 或 world loading
  behavior。
- 不修改 API routes 或 API response shapes。
- 不修改 frontend behavior。
- 不增加 concrete external-world fixtures、seed data、roles、locations、
  resources、story rules、product UI 或 application-specific backend logic。
- 不创建 external repositories。

## 为什么现在做

0.2.7 已加固 recursive schema contracts。0.2.8 是匹配的 event contract
hardening step，位于 0.2.9 审计 schema、event、external boundary 和 legacy
boundary evidence 之前。稳定的 event reference semantics 能降低 v0.3 loader 以及
后续 agent / memory / projection 工作开始前的风险。

## North Star 对齐

本 package 通过明确 events 如何为未来 world、agent、memory 和 projection systems
携带 structured references，支撑 WorldEngine 的 event spine。它保持 engine
generic，不把 repository 收窄为 demo-specific backend，也不提前实现未来 runtime
behavior。
