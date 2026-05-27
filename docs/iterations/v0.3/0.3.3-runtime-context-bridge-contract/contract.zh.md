# Contract

## 公开概念

- `RuntimeContextBridge`：未来从已验证加载器输出派生可选运行时上下文的边界。
- `RuntimeContextInput`：成功的 `LoadedWorldSpec` 或经评审的等价物。
- `RuntimeContext`：从通用 `WorldSpec` 数据派生出的可选、惰性运行时上下文。
- `RuntimeContextSummary`：用于测试和评审证据的小型诊断视图。
- `RuntimeContextBridgeError`：结构化桥接错误。

规范性公开契约是
`docs/contracts/runtime-context-bridge-contract.md`。

## 兼容性约束

- 现有运行时 tick、`world_time_seconds`、`step_seconds` 和 `updated_at`
  行为必须保持兼容。
- 现有 API 响应包装和错误形状必须保持兼容。
- 现有事件、归档、参数、前端可见、fixture、migration 和旧路径行为必须保持
  兼容。
- 现有 `WorldSpec`、`WorldCell`、加载器和事件 schema 行为必须保留。
- 本包禁止 schema 变更。
- 运行时上下文必须保持可选和惰性，直到后续经评审实现证明其他行为。

## 允许变更

- 新增 `docs/contracts/runtime-context-bridge-contract.md`。
- 创建 0.3.3 迭代包文档和中文镜像。
- 更新 v0.3 里程碑索引及镜像，把 0.3.3 标记为 `ready for review` /
  `待评审`。
- 仅为 0.3.3 状态一致性更新 v0.3 包计划及镜像。
- 定义桥接输入、上下文形状、错误、兼容性和证据语义。
- 在 `review.md` 中记录文档阶段验证证据。

## 禁止变更

- 不实现桥接代码。
- 不修改 `RuntimeEngine`、事件总线、世界模块、API 路由、schema、测试、
  fixture、migration、前端、归档、参数、持久化或旧
  `backend/worldengine/` 实现文件。
- 不新增 API 响应字段或事件 payload 字段。
- 不把原始 `WorldSpec` 放进事件 payload。
- 不把 `WorldCell` 直接映射为运行时模块。
- 不创建具体世界逻辑、具体 fixture 或外部验证世界内部细节。
- 不实现世界生成、世界内 Agent 闭环、记忆、自我连续性、投影、剧情生成或
  NPC 聊天行为。

## 验收要求

- 桥接契约明确说明可接受输入。
- 桥接契约明确说明派生运行时上下文字段。
- 桥接契约说明运行时上下文是可选和惰性的。
- 桥接契约保留 tick、世界时间、事件日志、参数、归档、API、前端可见和旧
  路径行为。
- 桥接契约说明 `WorldCell` 不会自动成为运行时模块。
- 桥接契约禁止原始 `WorldSpec` 事件 payload 和未经评审的 API 暴露。
- 桥接契约包含结构化错误类别。
- 迭代包文档包含假设、未决风险、验证命令和仅文档不运行测试的理由。
- 英文和中文里程碑镜像保持 0.3.3 状态同步。

## 北极星检查

本包保持 WorldEngine 的通用性。它为已验证世界规格数据定义引擎级桥接边界，
并明确禁止演示专用后端行为、外部验证世界内部细节，以及 Agent 或生成行为。

## 范围外后续工作

- `0.3.4` 可在本包评审后实现最小可选运行时上下文桥接层。
- `0.3.5` 可定义外部 fixture 契约准备，但不在核心代码内添加外部仓库。
- 后续里程碑可以实现运行时模块映射、Agent 闭环、记忆、自我连续性、生成、
  投影和外部产品验证。
