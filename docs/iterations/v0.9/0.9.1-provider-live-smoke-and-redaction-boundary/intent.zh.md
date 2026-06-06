# 意图

## 问题 / 目的

当前 `GET /manifest` 可以报告 public provider environment readiness，但不能证明
WorldEngine 能发起 live provider call。v0.9 在后续包使用 provider 行为进行
LLM-backed world creation 之前，需要一条最小、安全、WorldEngine-owned 的 smoke path。

本包创建后续 LLM-backed validation layers 所需的 provider boundary 和 redaction evidence。

## 为什么现在

`0.9.0` 已完成 v0.9 handoff baseline，并选择本包作为下一条 route。`0.9.2` 不能诚实地
实现 LLM-backed world generation，除非 provider calls 已有 reviewed WorldEngine-owned
entrypoint、安全的 unconfigured behavior 和 redacted evidence semantics。

## 与路线图的关系

本包是 v0.9 layer 1：provider live smoke。它支持 north star 中后续 AI-assisted world
generation，同时把 provider ownership 留在 core engine 内，防止 external Validation
Client 变成 LLM caller 或 evaluator。

## 非目标

- 不实现 LLM-backed world creation。
- 不实现 generated world rules、worldview fidelity、runtime run controls、user
  direction、event legality、Agent continuity、consolidation、narrative projection、
  diagnostic dialogue 或 Validation Client handoff。
- 不执行 provider-backed lifecycle validation。
- 不构建 product UI 或 game client。
- 不添加 concrete world content。
- 不存储或暴露 raw provider inputs 或 outputs。

## 预期交接

`0.9.2-llm-worldview-ingestion-and-generation-contract` 接收：

- 一条 WorldEngine-owned provider smoke call path。
- redacted provider live summary semantics。
- live provider availability 的 failure taxonomy。
- `/manifest` readiness 和 live provider smoke 是不同证据的明确区分。
- provider redaction tests，以及如有的 unresolved provider blockers。
