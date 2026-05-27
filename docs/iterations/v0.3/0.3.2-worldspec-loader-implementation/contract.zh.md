# 契约

## 公共概念

- `WorldSpecLoader`：加载一个受支持的通用输入来源并返回已校验加载结果的实现
  组件。
- `WorldSpecInput`：受支持的领域中立输入，限于已解析 mapping、JSON 字符串或
  bytes，以及可选的调用方提供 JSON 文件路径。
- `LoadedWorldSpec`：成功结果，包含已校验 `WorldSpec`、`source_type`、可选
  中立 `source_label` 和 `schema_version`。
- `WorldSpecLoaderError`：稳定结构化错误，包含 `code`、`message`、可选
  `path`、`source_type` 和可选 `source_label`。
- `WorldSpecLoaderResult`：加载器返回的成功或失败包装。

规范性公共契约仍是 `docs/contracts/worldspec-loader-contract.md`。

## 兼容性约束

- 现有运行时行为必须保持兼容。
- 现有 API 响应形状必须保持兼容。
- 现有事件、归档、参数、前端可见行为和旧路径行为必须保持兼容。
- 现有 `WorldSpec`、`WorldCell` 和 `EntityRef` schema 行为必须保留。
- 本包禁止 schema 变更。
- 加载器实现不得成为运行时上下文。

## 允许变更

- 新增 `backend/app/core/worldspec_loader.py`。
- 新增 `backend/app/tests/test_worldspec_loader.py`。
- 新增或更新仅为聚焦加载器测试所需的导入。
- 创建本包文档和中文镜像。
- 更新 v0.3 里程碑索引和计划中 0.3.2 的评审就绪状态。
- 用文档阶段和后续实现阶段证据更新 `review.md` 与 `review.zh.md`。

## 禁止变更

- 不修改 `RuntimeEngine`，不改变 `RuntimeEngine.step` 行为。
- 加载器不得导入 `RuntimeEngine`。
- 不把加载器连接到 API 路由或响应 envelope。
- 不发出事件，不创建归档快照，不应用参数，不写持久化记录，不改变运行时状态。
- 不修改 schema、迁移、前端文件、fixture 或旧目录 `backend/worldengine/`
  运行时代码。
- 不新增具体演示世界名称、地图、角色、地点、资源、故事规则、外部验证世界
  数据或私有 oracle 细节。
- 不实现运行时桥接、世界生成、世界内 Agent 闭环、记忆、自我连续性、投影、
  剧情生成或 NPC 聊天行为。

## 验收要求

- 加载器接收有效最小 mapping，并返回成功的 `LoadedWorldSpec`。
- 加载器接收有效 JSON 字符串或 bytes 输入，并返回与 mapping 输入语义一致的
  结果。
- 如果实现文件加载，加载器接收一个 JSON 文档路径，并对不可读输入报告
  `io_error`。
- 加载器对不支持的输入类型或来源形式返回 `unsupported_input`。
- 加载器对格式错误的 JSON 输入返回 `parse_error`。
- 加载器对无效 `WorldSpec` schema 数据返回 `schema_validation_error`，包括
  不支持的 `schema_version` 和无效 root cell 数据。
- 加载器错误 `path` 值使用 `technical-design.zh.md` 定义的 JSON Pointer 风格
  约定，包括当失败位置是该字段时，不支持 schema 版本返回 `/schema_version`。
- 成功输出包含中立 `source_type`、可选 `source_label` 和已校验
  `schema_version`。
- 测试证明没有改变运行时、API、事件、归档、参数、持久化、前端、fixture、
  迁移或旧路径实现行为。
- 英文和中文 package / 里程碑镜像保持 0.3.2 状态同步为
  `ready for review` / `待评审`。

## North Star 检查

本包保持 WorldEngine 的通用性。它只实现结构化世界规格的可复用引擎级加载器，
并明确禁止演示专用后端行为、外部验证世界内部细节和运行时执行语义。

## 范围外后续工作

- `0.3.3` 可定义已校验加载数据如何进入运行时上下文。
- `0.3.4` 可在桥接契约评审后实现最小可选运行时上下文桥接。
- 后续里程碑可实现 Agent 闭环、记忆、自我连续性、生成、投影和外部产品验证。
