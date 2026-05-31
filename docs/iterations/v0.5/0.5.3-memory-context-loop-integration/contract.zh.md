# 契约

状态：review complete

## 公开概念

- `MemoryContext`：由 working-memory 和 episodic-memory records 组装而成的 bounded、
  read-only perception data。
- `working_memory`：perception 中包含的 current-context memory entries。
- `episodic_memory`：perception 中包含的 event-linked memory entries。

Memory context 只属于 perception data，不是 action modifier。

## 允许修改

- 在 `backend/app/schemas/agent_loop.py` 添加 additive memory context schema models 或 fields。
- 扩展 `backend/app/agent/perception.py`，接受 optional memory store，并构建 bounded
  read-only memory context。
- 仅把 `InMemoryAgentMemoryStore` wired into `backend/app/api/app_factory.py`，作为 perception
  使用的 internal app state。
- 更新 `backend/app/tests/` 下的 loop/perception/API tests。
- 为 handoff 更新 package docs 和 parent v0.5 status/review surfaces。

## 禁止修改

- 不修改 `ActionIntent`、`ActionResult`、accepted action types、action adapter behavior
  或 params patch semantics。
- 不添加 public memory APIs。
- 不添加 loop request memory selectors。
- 不在 `AgentLoopService.step` 中写 memory。
- 不添加 durable persistence、migrations、frontend behavior、concrete world content、
  external validation internals、relationship behavior、self-summary generation、
  automatic reflection 或 personality drift action modifiers。
- 不修改 `backend/worldengine/**`。

## 兼容性要求

- Existing loop callers 在不发送新字段时必须继续可用。
- Existing loop request validation 对 unknown request fields 仍保持 strict。
- Existing action 和 result schemas 保持不变。
- API envelope 和 error behavior 保持不变。
- Memory context 必须有边界，并且不得暴露 mutable backing store state。
- Default app 可以暴露 empty memory context，除非 tests 直接 seed store。

## 实现授权条件

只有满足以下条件后才能实现：

- 全部 package docs 和中文镜像存在。
- documentation/contract evaluator 报告没有 P1 和 blocking P2。
- `review.md` 记录 `implementation_authorized: yes`。
- production code changes 前存在 focused failing test，并已运行。

## North Star 检查

本包支持 memory-shaped perception，同时保持 WorldEngine generic。它不添加 concrete world data、
application behavior 或 consciousness claims。

## 范围外后续工作

- `0.5.4`：relationship、self-summary、reflection 和 drift contract follow-up。
- 后续 package：基于 memory 的 behavior changes、persistence、retrieval indexing、generation、
  validation readiness 和 projection readiness。
