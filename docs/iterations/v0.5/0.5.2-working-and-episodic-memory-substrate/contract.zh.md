# 契约

状态：review complete

## 公开概念

本包只实现 `0.5.1` 中的两个概念族：

- `WorkingMemoryRecord`：带 provenance 的 bounded current-context memory。
- `EpisodicMemoryRecord`：带 provenance、world-time/tick evidence 的 event-linked experience memory。

实现也可以定义小型支持类型，例如 memory source enum/value、evidence reference model 或 bounded
context model，只要它们保持 generic 且属于 backend schemas 内部。

## Schema 语义

Working memory records 必须包括：

- stable `memory_id`。
- `agent_id` 和 `world_id`。
- textual `content`。
- `source` 和 provenance/evidence metadata。
- `created_at` 和 `updated_at`。
- bounded-context metadata，例如 `priority` 和 optional expiration/tick window。

Episodic memory records 必须包括：

- stable `memory_id`。
- `agent_id` 和 `world_id`。
- textual `summary`。
- `event_refs`。
- `tick` 和 `world_time_seconds`。
- `source`、optional action/outcome references 和 `created_at`。

如果 technical design 记录了等价语义，精确 Python model names 可以调整。

## Service 语义

In-memory substrate 必须：

- 仅使用 process memory 存储记录。
- 按 `agent_id` 和 `world_id` 限定 reads。
- 返回 deep copies 或 immutable copies，避免 caller 修改 backing state。
- 提供 deterministic ordering 的 bounded working-memory selection。
- 提供 deterministic ordering 的 agent/world-scoped episodic listing。
- 本包不做 app wiring 或 route exposure。

## 兼容性要求

- 现有 v0.4 Agent Loop requests 和 responses 保持不变。
- 本包不得修改 `PerceptionFrame`、`LoopStepRequest`、`ActionIntent`、`ActionResult`
  和 `POST /world/agent/loop/step`。
- 现有 `/world/agent/params/propose-and-apply`、event routes、runtime state/step、
  params behavior、archive behavior、API envelope/error shape 和 optional `Event.refs`
  serialization 必须保持兼容。
- Schema additions 是 additive，不改变 existing models。

## 允许修改

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_*.py`
- 本目录下的 package docs 和 mirrors。
- 仅为准确交接修改父级 v0.5 status/review surfaces。

## 禁止修改

- 不修改 `backend/worldengine/**`。
- 不修改 frontend files。
- 不添加或修改 API routes。
- 不修改 `LoopStepRequest`、`ActionIntent`、`ActionResult`、action adapter semantics、
  `params.patch` validation semantics、event behavior、runtime tick behavior 或
  API envelope/error behavior。
- 不添加 durable persistence、migrations、vector search、summarization、
  relationship state behavior、reflection automation、personality drift action modifiers、
  concrete world content、external validation internals 或 application-specific backend logic。

## Implementation Authorization Criteria

只有满足以下条件后才能实现：

- 全部 package docs 和中文镜像存在。
- documentation/contract evaluator 报告没有 P1 和 blocking P2。
- `review.md` 记录 `implementation_authorized: yes`。
- 第一个 production change 前已有 focused backend failing test。

## North Star 检查

该实现是 agents living inside worlds 的 generic memory substrate work。它保持可检查、有范围且
non-public；不添加 demo-world behavior、projection application behavior 或 consciousness claims。

## 范围外后续工作

- `0.5.3`：Agent Loop perception 中的 bounded read-only memory context。
- `0.5.4`：relationship、self-summary、reflection 和 drift contract follow-up。
- 后续版本：durable persistence、retrieval indexing、generation、external validation readiness 和
  projection application readiness。
