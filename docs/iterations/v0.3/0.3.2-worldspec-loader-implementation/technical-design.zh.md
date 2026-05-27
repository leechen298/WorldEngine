# 技术设计

## 当前状态

`WorldSpec` 定义在 `backend/app/schemas/world_cell.py`，并已有 schema smoke
测试覆盖。`0.3.1` 在 `docs/contracts/worldspec-loader-contract.md` 中新增了加载
器契约，但没有实现加载器代码。目前还没有运行时桥接层。

## 契约对齐和不变量

实现必须保持这些不变量：

- 使用现有 `WorldSpec` schema，或其已评审包装器，进行校验。
- 将输入分发、解析和校验失败规范化为稳定加载器结果对象。
- 已加载数据仍只是规格数据。
- 避免导入 `RuntimeEngine`、API 路由模块、持久化、归档、参数、事件写入、前端、
  fixture 和旧运行时代码。
- 测试数据保持领域中立。

## 实现方案

新增 `backend/app/core/worldspec_loader.py`，提供小型同步 API。具体名称可遵循
本地 Python 风格，但模块应暴露一个清晰的加载函数，以及符合已评审契约的结构化
结果类型。

建议形状：

- 用不可变或普通结构化对象表示成功和错误结果。
- 支持 mapping、JSON 文本、JSON bytes，以及可选 JSON 文件路径的输入分发。
- 通过标准库解析 JSON。
- 通过 `WorldSpec` 做 schema 校验。
- 将异常规范化为 `unsupported_input`、`parse_error`、
  `schema_validation_error` 或 `io_error`。

加载器不应做现有 schema 校验之外的深层语义检查，不解析引用，也不派生运行时
上下文。

## 受影响表面

实现表面：

- `backend/app/core/worldspec_loader.py`
- `backend/app/tests/test_worldspec_loader.py`

文档表面：

- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

只读兼容性表面：

- `backend/app/schemas/world_cell.py`
- 现有 schema smoke 测试。
- 运行时、API、事件、归档、参数、前端可见、fixture、迁移和旧路径测试。

## 数据模型 / Schema 变更

不允许 schema 变更。`LoadedWorldSpec`、`WorldSpecLoaderError` 和
`WorldSpecLoaderResult` 是加载器边界结构，不是持久化 schema 对象，也不是本包
的 API 响应模型。

## 错误路径风格

当输入内部的失败位置已知时，`WorldSpecLoaderError.path` 必须使用确定性的
JSON Pointer 风格字符串：

- 根级校验失败使用 `/`。
- 对象字段使用斜杠分隔的段，例如 `/schema_version` 或 `/root/id`。
- 列表索引使用数字段，例如 `/cells/0/id`。
- 路径段中的字面量 `~` 和 `/` 分别转义为 `~0` 和 `~1`。
- 不支持输入、文件 I/O 失败，以及无法绑定到稳定输入位置的解析失败使用
  `path = None`。

Schema 校验规范化必须先把框架校验位置转换成此风格，再返回
`WorldSpecLoaderError` 对象。测试必须断言不支持 `schema_version` 和无效 root
cell 数据的代表性路径，不依赖 Pydantic 私有错误消息格式。

## 运行时 / 服务设计

加载器是纯数据边界工具：

1. 接收一个输入值。
2. 分类输入来源。
3. 仅在需要时解析 JSON。
4. 用 `WorldSpec` 校验得到的 mapping。
5. 返回成功或失败结果。

它不得启动、修改、包装或配置运行时服务。

## 兼容性

现有运行时 tick、`world_time_seconds`、API envelope、`/runtime/step`、
`/world/events`、`/world/event-steps`、参数行为、归档行为、可选 `Event.refs`、
前端可见形状和旧目录 `backend/worldengine/` 行为必须保持不变。

由于加载器不会接入这些表面，实现应主要通过范围、导入和聚焦回归检查证明这一点。

## 风险

- 错误规范化可能隐藏过多校验细节。聚焦测试必须断言稳定错误码和足以定位无效
  字段的 path / detail。
- 文件输入可能暗示 fixture 策略。如果实现，测试必须使用临时单个 JSON 文档和
  中立内容。
- 便利 API 可能漂移成运行时桥接行为。导入检查和禁止变更评审必须捕获
  runtime / API / event / persistence 耦合。
- 如果代码修改 `world_cell.py`，可能改变现有 schema 预期；本包禁止该行为，并
  要求现有 schema smoke 测试继续通过。
