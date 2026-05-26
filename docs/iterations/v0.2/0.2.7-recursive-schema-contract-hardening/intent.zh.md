# Intent

Status: ready for review

英文版本：`intent.md`。

## Problem

v0.2 已引入 recursive schema foundation，包括 EntityRef、WorldCell、WorldSpec 和 generic schema smoke tests。v0.3 开始 loader 或 runtime bridge work 之前，这些 schema contracts 需要更清晰的 documentation 和 focused validation evidence。

当前代码已经验证 basic nested cells、entity references、schema version、invalid empty identifiers、serialization 和 reconstruction。剩余风险是未来 agents 可能从稀疏 schema documentation 中推断 loader behavior、runtime-side semantics 或 domain-specific examples，而不是遵循 explicit contract。

## Goal

为 EntityRef、WorldCell、WorldSpec 定义 documentation 和 implementation plan，使它们成为 generic、additive、recursive schema contracts，并具备 testable acceptance criteria。

Implementation 完成后的状态应满足：

- EntityRef、WorldCell、WorldSpec contract docs 存在。
- Schema tests 证明 recursive nesting、invalid generic values 和 model dump / validate round trips。
- Runtime loading 仍未实现。
- Examples 和 test payloads 保持 domain-neutral。

## Non-goals

- 不实现 WorldSpec loader。
- 不把 WorldSpec 连接到 RuntimeEngine。
- 不改变 runtime behavior。
- 不改变 API response shapes。
- 不修改 frontend behavior。
- 不添加 concrete external-world fixtures、seed data、roles、locations、resources、story rules 或 product UI。
- 不实现 generation、projection、memory、agent loop 或 self-continuity behavior。
- 不创建 external repositories。

## Why Now

0.2.5 移除了 concrete external-world anchors 并恢复 generic schema smoke coverage。0.2.6 重置了剩余 v0.2 plan。0.2.7 是下一步 foundation work，因为 v0.3 loader work 需要 stable schema semantics 和 evidence，之后才能安全消费 WorldSpec data。

## North Star Alignment

本 package 通过澄清 worlds、child worlds 和 referenced entities 的 generic schema language 来支持 recursive world structures。它强化 reusable engine contracts，而不会把 repository 收窄成 demo-specific backend，也不会提前实现未来 runtime surfaces。
