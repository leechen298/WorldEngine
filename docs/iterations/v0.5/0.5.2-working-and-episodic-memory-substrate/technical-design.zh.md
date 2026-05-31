# 技术设计

状态：review complete

## 当前状态

相关 backend files：

- `backend/app/schemas/agent_loop.py` 定义 `PerceptionFrame`、`ActionIntent`、
  `ActionResult`、`LoopStepRequest` 和 `LoopStepResponse`。
- `backend/app/agent/perception.py` 构建 bounded read-only perception frames。
- `backend/app/agent/loop_service.py` 先构建 perception，再应用 action。
- `backend/app/agent/action_adapter.py` 只接受 `noop` 和 `params.patch`。
- `backend/app/api/routes/world_agent.py` 暴露 `POST /world/agent/loop/step`。
- `backend/app/tests/test_agent_perception.py`、`test_agent_loop_service.py` 和
  `test_agent_loop_api.py` 覆盖相邻 compatibility behavior。

当前还没有 memory schema 或 substrate module。

## 契约对齐与不变量

本包必须保持：

- 不修改 existing loop schemas。
- 不修改 action semantics。
- 不添加新 API route。
- 不要求 app factory wiring。
- 不添加 durable persistence。
- 不修改 `backend/worldengine/`。

## Proposed Implementation

新增 `backend/app/schemas/agent_memory.py`，包含 Pydantic models：

- `MemoryEvidenceRef`：generic evidence reference，包含 `type`、`id` 和 optional metadata。
- `WorkingMemoryRecord`：agent/world-scoped current-context record。
- `EpisodicMemoryRecord`：agent/world-scoped event-linked record。

新增 `backend/app/agent/memory.py`，包含：

- `InMemoryAgentMemoryStore`。
- `add_working_memory(record)`。
- `add_episodic_memory(record)`。
- `list_working_memory(agent_id, world_id, limit=None)`。
- `list_episodic_memory(agent_id, world_id, limit=None)`。
- deterministic ordering 和 copy isolation。

store 应刻意保持简单。本包不把它 wired into app state，因为 `0.5.3` 前还没有 public consumer。

## 受影响表面

Implementation surfaces：

- new schema module：`backend/app/schemas/agent_memory.py`。
- new service module：`backend/app/agent/memory.py`。
- new focused tests：`backend/app/tests/test_agent_memory_substrate.py`。

Adjacent verification surfaces：

- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_service.py`
- `backend/app/tests/test_agent_loop_api.py`
- `backend/app/tests/test_agent_action_adapter.py`

## Data Model / Schema Changes

所有 schema changes 都是 additive，因为它们新增 module，不修改 existing models。

Record identifiers 是 strings，timestamps 使用符合 existing schema style 的 strings，
evidence references 是 generic dictionaries 或 typed models。substrate 不得存储 concrete world data。

## Runtime / Service Design

In-memory store 为 working 和 episodic records 维护独立 internal lists。读取按 `agent_id` 和
`world_id` 过滤。

Working memory deterministic ordering：

1. higher `priority` first。
2. 可比较时 newer `updated_at`/`created_at` first。
3. stable `memory_id` tie-breaker。

Episodic memory deterministic ordering：

1. higher `tick` first。
2. higher `world_time_seconds` first。
3. newer `created_at` first。
4. stable `memory_id` tie-breaker。

store 返回 deep model copies，保护 backing state。

## 兼容性

由于本包只新增 module，不接入 loop/API，旧 requests 和旧 responses 保持不变。相邻测试必须确认
perception、loop service、loop API 和 action adapter behavior 仍然通过。

## 防漂移规则

- Implementation 仅限新增 memory schema、新增 memory store 和 focused memory tests。
- 本包不引入 API routes、app factory wiring、loop integration 或 request schema fields。
- 不把 substrate 描述成 durable persistence、vector retrieval 或 summarization。
- 除非后续已评审 package 授权 code，否则 relationship state、self-summary、reflection 和
  personality drift 仍保持 follow-up contract work。
- 将已关闭的 `0.5.0` 和 `0.5.1` status updates 视为 campaign handoff context，
  不当作 `0.5.2` implementation scope。

## 风险

- 风险：memory substrate 变成 public API。
  检测：changed-file review 和 API tests。
- 风险：store 暴露 mutable backing state。
  检测：focused copy-isolation test。
- 风险：deterministic bounds 不稳定。
  检测：ordered bounded-list tests。
- 风险：action behavior 意外变化。
  检测：相邻 loop/action tests。
