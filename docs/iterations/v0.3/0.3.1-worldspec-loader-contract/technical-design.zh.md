# 技术设计

## 当前状态

`WorldSpec` 由 `backend/app/schemas/world_cell.py` 定义，并在
`docs/contracts/worldspec-contract.md` 中记录。v0.2 明确没有实现加载器行为。
v0.3 计划先完成加载器包，再进入运行时桥接包。

## 契约对齐和不变量

加载器契约必须保持这些不变量：

- schema 校验仍委托给 `WorldSpec` 或已评审包装器。
- 已加载数据仍是规格数据。
- 本包不触碰运行时、API、事件、归档、参数、前端、fixture、迁移、测试和旧
  路径实现文件。
- 示例保持领域中立。

## 后续实现形状

后续实现包应新增一个很小的数据边界模块，位置很可能在 `backend/app/core/`，
职责是：

1. 接收一个受支持输入来源。
2. 仅在需要时解析。
3. 通过 `WorldSpec` 校验得到的 mapping。
4. 返回结构化成功或失败结果。
5. 不产生运行时副作用。

本包不创建该模块。

## 受影响表面

本包影响的文档表面：

- `docs/contracts/worldspec-loader-contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

有意不影响的实现表面：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- 测试、fixture、迁移、API 路由、schema、运行时服务。

## 数据模型 / Schema 变更

没有 schema 变更。契约中的后续加载器结果名称在 `0.3.2` 实现前都是概念。

## 运行时 / 服务设计

本包没有运行时或服务行为变更。契约禁止已加载数据拥有运行时权力，并把运行时
上下文语义留给后续桥接契约。

## 验证设计

文档验证应证明：

- 迭代包文件存在。
- 加载器契约存在必需标题和错误类别。
- 英文和中文里程碑索引状态同步。
- 已触及文档没有引入具体演示世界锚点。
- 未修改实现文件。
- `git diff --check` 通过。

## 风险

- 后续实现可能过度依赖校验库错误文本。契约通过稳定错误码和可测试路径降低此
  风险，避免依赖私有异常格式。
- 文件输入可能被误解成 fixture 目录。契约把文件输入限制为单个 JSON 文档，
  并禁止外部仓库或 fixture bundle。
- 桥接需求可能泄漏进加载器范围。契约明确已加载数据不是运行时上下文。
