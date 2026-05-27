# Technical Design

## 当前状态

v0.3 目前已有截至 0.3.7 发布候选包的包证据。发布占位文档仍声明 v0.3 为
planned / not released；在本文件包之前，里程碑索引中 0.3.8 仍是 planned /
gated。

最终收口包只触及文档状态和证据表面。它不触及加载器代码、运行时上下文代码、
schema、API 路由、前端代码、fixture、migration 或测试实现文件。

## 契约对齐与不变量

最终收口必须保持这些不变量：

- 修改最终状态前，必须取得发布候选评审批准。
- 最终收口时不得存在未解决 P1/P2 问题。
- 0.3.0 到 0.3.7 的历史证据不得被表述为 0.3.8 当前会话测试执行。
- 开放 P3 项只能作为明确接受的交接项保留。
- v0.4 仍是未来里程碑，需要自己的已评审包。

## 计划实现

文档阶段创建本包，并将本包标记为 ready for review。

评审批准后，实现阶段可以：

1. 根据评审支持的内容，把 `docs/releases/v0.3.md` 和
   `docs/releases/v0.3.zh.md` 从 planned / not released 调整为最终收口措辞。
2. 更新 v0.3 里程碑索引和详细计划状态文档。
3. 仅在最终评审需要阻塞项分类、接受 P3 交接或记录新问题时，更新
   `docs/iterations/v0.3/findings.md`。
4. 更新本包 README 清单和评审证据。
5. 运行 `test-plan.md` 中的文档验证命令。

如果最终评审发现未解决 P1/P2 阻塞项，收口必须停止并记录阻塞项，不能改变
最终状态。

## 受影响表面

- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`
- `docs/iterations/v0.3/findings.md`，仅在问题状态变化时。
- `docs/releases/v0.3.md`
- `docs/releases/v0.3.zh.md`

## 数据模型 / Schema 变更

无。本包不得改变 schema、校验行为、数据库模型、事件字段、API 模型、fixture
或 migration。

## 运行时 / 服务设计

无。本包不得改变运行时服务、加载器行为、桥接行为、API 路由、事件日志行为、
归档行为、参数行为或前端行为。

## 兼容性

通过范围控制保持兼容：

- 不修改运行时、schema、API、事件、归档、参数、前端、fixture、migration 和
  测试实现文件。
- 最终状态声明是由历史包证据和当前会话文档检查支撑的文档声明。
- 当前会话命令必须与历史证据分开列出。

## 风险

- 状态更新可能在评审批准前暗示 v0.3 已最终发布。测试计划会检查发布和状态
  措辞。
- 可能遗漏 P1/P2 阻塞项。测试计划会扫描 `findings.md` 和收口文档中的未解决
  P1/P2。
- 文档镜像可能漂移。测试计划会检查英文和中文文件存在性及状态措辞。
- 未来 v0.4 交接可能被过度表述成实现许可。契约和测试计划要求 v0.4 保持为
  单独评审包。
