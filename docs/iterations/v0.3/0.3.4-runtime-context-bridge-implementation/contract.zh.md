# 契约

## 公共概念

- `RuntimeContextBridge`：从成功加载器结果派生上下文的实现边界。
- `RuntimeContextInput`：可接受输入，仅限成功的 `LoadedWorldSpec` 或已评审
  的等价输入。
- `RuntimeContext`：从通用 `WorldSpec` 数据派生的可选惰性上下文。
- `RuntimeContextSummary`：用于测试和评审证据的确定性诊断视图，不是产品 UI。
- `RuntimeContextBridgeError`：针对不支持输入、不完整加载器输出或派生失败的
  结构化桥接错误。

规范性公共契约仍然是
`docs/contracts/runtime-context-bridge-contract.md`。

## 兼容约束

- 不带上下文的既有 `RuntimeEngine` 构造必须保持兼容。
- 既有 tick、`world_time_seconds`、`step_seconds` 和 `updated_at` 行为必须保持
  兼容。
- 运行时和世界事件端点的既有 API envelope 和响应形状必须保持兼容。
- 既有事件 payload、参数行为、归档行为、前端可见形状、fixture、migration、
  测试和遗留 `backend/worldengine/` 行为必须保持兼容。
- 既有 `WorldSpec`、`WorldCell`、加载器和事件 schema 不得改变。
- 运行时上下文必须保持可选且惰性。

## 允许变更

- 添加 `backend/app/core/runtime_context.py`。
- 在 `backend/app/tests/test_runtime_context_bridge.py` 中添加聚焦桥接测试。
- 仅在默认行为不变时，为 `RuntimeEngine` 添加可选 `runtime_context` 构造参数
  或等价只读持有者。
- 添加供测试和评审证据使用的只读 summary helper。
- 添加桥接和聚焦测试所需的窄范围 import。
- 实现后更新本包 `review.md` 和 `review.zh.md` 的实现证据。

## 禁止变更

- 不改变默认运行时脚手架行为。
- 不改变 `/runtime/state`、`/runtime/step`、`/world/events`、
  `/world/event-steps` 或遗留 `/world/step` 响应形状。
- 不发出新的桥接事件，不把原始 `WorldSpec` 数据放入事件 payload。
- 不让运行时上下文驱动 tick 推进、模块执行、参数读写、归档快照或 API 响应。
- 不修改 schema、migration、fixture、前端代码、持久化模型或遗留
  `backend/worldengine/` 代码。
- 不把 `WorldCell` 转换为 `WorldModule` 语义。
- 不实现生成、Agent-in-World 循环、记忆、自连续性、投影、故事生成、NPC
  聊天、外部仓库或具体演示世界行为。

## 验收要求

- 桥接能从成功的 `LoadedWorldSpec` 派生 `RuntimeContext`。
- 派生上下文只包含 `worldspec_id`、`schema_version`、`root_cell_id`、
  `root_cell_type`、`source_type`、可选 `source_label` 和已评审的中性
  `metadata`。
- 桥接对不支持输入返回 `unsupported_input`。
- 桥接对不完整或内部不一致的加载输出返回 `invalid_loaded_worldspec`。
- 桥接对加载器 schema 验证之外的派生失败返回 `context_derivation_error`。
- 无上下文时 `RuntimeEngine()` 和 `RuntimeEngine.from_env()` 行为不变。
- 如果支持向 `RuntimeEngine` 提供上下文，不能改变 `step()` 状态推进或事件输出。
- 聚焦测试证明不会发出原始 `WorldSpec` 事件 payload。
- 兼容测试证明被触及表面的运行时、事件 API、参数、归档和前端可见响应形状保持兼容。
- 英文和中文包及里程碑镜像保持 0.3.4 状态同步为 `ready for review` / `待评审`。

## 北极星检查

本包保持 WorldEngine 通用。它只实现从已验证世界规格数据到可选运行时上下文
的有界桥接，并明确禁止具体世界行为、外部验证内部细节、Agent 行为、记忆、
生成和投影。

## 后续范围外工作

- `0.3.5` 可以定义外部 fixture runner 契约就绪性。
- `0.3.6` 可以审计加载器和桥接兼容证据。
- 后续里程碑可以定义运行时模块映射、Agent 循环、记忆、自连续性、生成、投影和
  外部产品验证。
