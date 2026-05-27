# Technical Design

## 当前状态

`RuntimeEngine` 是 v0.1 的内存运行时脚手架。它持有 tick 状态，推进
`world_time_seconds`，发出 `tick.advanced`，运行默认模块树，并调用归档
回调。

`WorldSpec` 和 0.3.2 加载器仍是数据边界。已加载数据还不是运行时上下文。
当前没有运行时桥接层。

## 契约对齐和不变量

桥接契约必须保留这些不变量：

- 只有成功的加载器输出可以进入桥接层。
- 运行时上下文是派生且有边界的，不是原始 `WorldSpec`。
- 如果后续实现上下文存储，它默认必须是可选和惰性的。
- `WorldCell` 是 schema / 世界结构，不是 `WorldModule`。
- tick、事件、参数、归档、API、前端和旧路径行为在本包中都是只读兼容性
  表面。
- 示例和诊断保持领域中立。

## 后续实现形状

后续实现包应新增一个很小的桥接模块，最可能放在 `backend/app/core/` 下，
负责：

1. 接收一个成功的加载器结果。
2. 检查加载器结果是否足够完整，可以派生桥接上下文。
3. 派生一个窄的 `RuntimeContext`。
4. 返回成功结果或结构化桥接错误。
5. 不产生运行时副作用。

如果后续让 `RuntimeEngine` 存储上下文，构造函数变更必须是添加式的，并默认
没有上下文。现有不传上下文的调用必须保持完全相同行为。

本包不创建该模块。

## 受影响表面

本包影响的文档表面：

- `docs/contracts/runtime-context-bridge-contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

明确不受影响的实现表面：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- 测试、fixture、migration、API 路由、schema、运行时服务、归档、参数、
  事件或持久化代码。

## 数据模型 / Schema 变更

本包不做 schema 变更。`RuntimeContext`、`RuntimeContextSummary` 和
`RuntimeContextBridgeError` 在 `0.3.4` 实现前只是概念性桥接边界结构。

提议的上下文形状有意保持很小：

- 已验证的 WorldSpec 身份。
- 已验证的 schema 版本。
- 已验证的根 cell 身份和类型。
- 中立 source metadata。
- 可选且经评审的 metadata。

它不是持久化 schema，也不是本包中的 API 响应模型。

## 运行时 / 服务设计

本包不改变运行时或服务行为。在经评审实现添加可选存储或访问路径前，未来
桥接层只是纯派生边界。

运行时上下文不得驱动：

- tick 推进。
- 事件发出。
- 模块执行。
- 参数校验或应用。
- 归档快照或摘要创建。
- API 响应形状。
- 前端行为。

## 兼容性

现有运行时 tick、`world_time_seconds`、API 包装、`/runtime/state`、
`/runtime/step`、`/world/events`、`/world/event-steps`、参数行为、归档
行为、可选 `Event.refs`、前端可见形状和旧 `backend/worldengine/` 行为必须
保持不变。

后续实现必须通过聚焦测试和范围检查证明旧行为，然后才能声明兼容。

## 验证设计

文档验证应证明：

- 英文和中文必需迭代包文件存在。
- 桥接契约包含必需概念、上下文字段、错误类别、兼容性表面和禁止推断。
- 0.3.3 状态在英文和中文里程碑文档中同步。
- 已触及文档没有引入具体演示世界锚点。
- 未修改实现文件。
- `git diff --check` 通过。

## 风险

- 上下文形状可能过宽，意外变成 API 或事件 payload。契约通过定义很小的
  派生形状并禁止暴露原始 `WorldSpec` 来缓解。
- 0.3.4 对 `RuntimeEngine` 构造函数的变更可能影响现有测试。测试计划要求
  对现有默认行为提供兼容性证据。
- `WorldCell` 可能被误认为 `WorldModule`。契约明确禁止直接等同。
- Metadata 可能变成领域特定。桥接层把 metadata 限制为中立诊断，除非经过
  评审。
