# 技术设计

状态：review complete

## 当前状态

`0.5.2` 已添加：

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`

当前 loop/perception code：

- `PerceptionFrame` 包含 runtime、params、recent events 和 optional runtime context summary。
- `PerceptionBuilder` 从 runtime state、world params、recent events 和 runtime context 构建
  read-only frame。
- `AgentLoopService.step` 在应用 action intent 前构建 perception。
- `ActionResultAdapter` 拥有 action semantics，必须保持不变。

## 契约对齐与不变量

- Memory context 是 read-only perception data。
- Loop action selection 和 action result behavior 不改变。
- 不添加 public API route。
- 不添加 loop request field。
- Loop step 内不写 memory。
- Existing request validation 和 API envelope behavior 保持兼容。

## 拟议实现

在 `backend/app/schemas/agent_loop.py` 添加 schema models：

- `MemoryContextSummary` 或等价模型，包含 bounded working 和 episodic memory record lists。
- `PerceptionFrame` 上的 optional `memory_context` field。

扩展 `PerceptionBuilder`：

- 接受 optional `memory_store`、`agent_id`、`world_id` 和 memory limits。
- 当 store 可用时，调用 `list_working_memory` 和 `list_episodic_memory`。
- 把 model data deep-copy 到 perception frame。
- 在不要求 caller seed memory 的情况下，默认返回 empty context 或 `None`。

在 `create_app()` 中把 `InMemoryAgentMemoryStore` wired 为 internal state，使 route 可以在
tests 中暴露 seeded memory context，而不新增 route。

## 受影响表面

- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_api.py`
- 可能包括 `backend/app/tests/test_agent_loop_service.py`

## 数据模型 / Schema 变更

唯一 existing schema change 是 additive：`PerceptionFrame` 增加 optional memory context。
Existing request schemas 和 action/result schemas 不变。

## Runtime / Service 设计

Perception 使用 deterministic default agent/world scope 从 in-memory store 读取 memory。
本包中 scope 可以固定为 generic identifiers，除非 test design 证明存在更安全的 existing source。
该 scope 必须记录，并且不得变成新的 public request parameter。

## 兼容性

旧 loop requests 仍有效。忽略额外 response fields 的旧 clients 仍兼容。Unknown loop request
fields 的 strict validation 保持不变。

## 防漂移规则

- 不添加 write paths。
- 不改变 action adapter behavior。
- 不引入 public memory route。
- 用 constants 或 constructor defaults 保持 memory context bounded。
- `0.5.4` concepts 在本包中保持 contract-only。

## 风险

- 风险：memory context 改变 action semantics。
  检测：action adapter 和 loop service tests。
- 风险：mutable backing store 泄漏到 perception。
  检测：perception copy-isolation test。
- 风险：response shape changes 变成 breaking。
  检测：loop API compatibility tests。
