# 技术设计

## 当前状态

`backend/app/core/worldspec_loader.py` 暴露 `LoadedWorldSpec` 和
`load_worldspec()`。`docs/contracts/runtime-context-bridge-contract.md` 定义了
可接受桥接输入、上下文形状、错误类别和兼容要求。

`RuntimeEngine` 仍然是 v0.1 内存运行时脚手架。它拥有 `RuntimeState`，推进
tick 和 `world_time_seconds`，发出 `tick.advanced`，在提供默认模块树时执行
它，调用归档回调，并返回复制后的运行时状态。

## 契约对齐和不变量

实现必须保持这些不变量：

- 只有成功的加载器输出或已评审等价输入可以进入桥接。
- 派生上下文是有界的，不暴露原始 `WorldSpec` payload。
- 上下文是可选且惰性的。
- `WorldCell` 仍是 schema 结构，不是 `WorldModule`。
- 既有运行时、API、事件、参数、归档、前端可见、fixture、migration 和遗留行为
  都是兼容表面。
- 示例和测试只使用领域中性标识符。

## 建议实现

添加 `backend/app/core/runtime_context.py`，包含小型结构化类型和纯派生函数。
具体命名可遵循本地 Python 风格，但模块应暴露：

- `RuntimeContext`
- `RuntimeContextSummary`
- `RuntimeContextBridgeError`
- result wrapper 或清晰的成功/错误返回。
- 一个明显的派生函数，例如 `build_runtime_context()`。

派生函数应当：

1. 接收一个候选输入。
2. 确认它是成功的 `LoadedWorldSpec` 或已评审等价输入。
3. 只读取已验证的身份、schema version、root cell 身份/类型和中性加载器来源元数据。
4. 返回 `RuntimeContext` 或结构化桥接错误。
5. 不产生运行时副作用。

如果 `RuntimeEngine` 存储上下文，应使用默认值为 `None` 的新增可选构造参数。
既有构造调用点和 `RuntimeEngine.from_env()` 不应需要改变，除非只是透传可选值且
默认值不变。任何上下文访问器都必须只读，并且不得改变 `get_state()` 或 `step()`
响应语义，除非评审明确批准新增诊断 helper。

## 受影响表面

实现表面：

- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`，仅在需要可选惰性存储时触及。
- `backend/app/tests/test_runtime_context_bridge.py`

只读兼容表面：

- `backend/app/core/worldspec_loader.py`
- `backend/app/core/event_bus.py`
- `backend/app/world/modules/*`
- 运行时、事件 API、参数、归档、schema、前端可见和遗留测试。

文档表面：

- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

## 数据模型 / Schema 变更

不允许 schema 变更。`RuntimeContext`、`RuntimeContextSummary` 和
`RuntimeContextBridgeError` 是内部桥接边界结构，不是持久化 schema，也不是 API
响应模型。

允许的运行时上下文字段：

- `worldspec_id`
- `schema_version`
- `root_cell_id`
- `root_cell_type`
- `source_type`
- `source_label`
- `metadata`

Metadata 必须保持领域中性且有界。如果实现无法证明 metadata 中性，本包应省略
metadata。

## 错误模型

桥接错误必须使用稳定 code：

- `unsupported_input`
- `invalid_loaded_worldspec`
- `context_derivation_error`

错误应包含简短 message、可选 path，并在可用时包含中性来源元数据。桥接错误不得
重新解释属于加载器职责的 schema 验证错误。

## 运行时 / 服务设计

桥接是纯本地边界。它不得：

- 启动或改变运行时服务。
- 发出事件。
- 应用参数。
- 创建归档快照。
- 写入持久化记录。
- 调用 API route handler。
- import 前端或遗留运行时模块。

如果添加运行时存储，`step()` 必须继续像以前一样递增 tick 和 world time，在相同
条件下发出相同事件形状，并用相同参数调用既有 callback。

## 兼容性

实现必须提供当前会话证据：

- 默认 `RuntimeEngine` 构造。
- `RuntimeEngine.from_env()`。
- `RuntimeEngine.step()` 状态推进。
- `/world/events` 和 `/world/event-steps` 的事件 API 兼容性。
- `/runtime/state` 和 `/runtime/step` 的运行时 API 兼容性。
- 参数和参数应用行为。
- 归档快照和摘要行为。
- 可选 `Event.refs` 兼容性。
- 前端可见响应形状。
- 遗留 `backend/worldengine/` 边界。

## 风险

- 运行时上下文存储可能意外成为序列化公共状态。
- 便利 summary 可能被误认为产品 UI 或投影 API。
- 测试可能证明纯桥接，但漏掉默认运行时构造兼容性。
- Metadata 若不排除或严格限制，可能变成应用特定内容。
