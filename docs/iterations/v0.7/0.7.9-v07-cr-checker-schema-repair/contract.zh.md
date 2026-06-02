# 契约

## 公共概念

- `ClosedFindingStatus`：对 pass report 来说真正关闭的发现项状态。本包中，
  对 P1/P2 pass 阻断项只有 `resolved` 属于关闭。
- `CheckerSemanticAuthority`：当 JSON Schema 只能表达结构形状时，Python 检查器逻辑
  是语义验证的权威。
- `GenericLeakPattern`：抽象、非特定消费者的泄漏标记，例如本地绝对路径、
  `file://` 路径、UI 选择器标记、隐藏重置术语、判题器术语、
  转录文本术语、种子数据术语和事件载荷术语。
- `PrivateApplicationStateField`：即使字段后缀表面合法，也会暴露私有或
  应用状态语义的投影读模型字段语言。

## 允许的变更

- `tools/testing/validate_external_validation_report.py`
- `tools/testing/test_validate_external_validation_report.py`
- `tools/testing/validate_readiness_manifest.py`
- `tools/testing/test_validate_readiness_manifest.py`
- `tools/testing/validate_projection_read_model_contract.py`
- `tools/testing/test_validate_projection_read_model_contract.py`
- `docs/testing/external-validation-report-schema.json`
- `docs/contracts/v0.7-readiness-manifest-schema.json`
- `docs/validation-report-template.md`
- `docs/contracts/projection-read-model-contract.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md`
- 本包目录下的文件。

## 禁止的变更

- 运行时、API 路由、前端、持久化、迁移、夹具运行器、
  生成结果产物、外部仓库、产品 UI、投影应用实现或 `backend/worldengine/`。
- 具体外部验证世界、具体世界名称、角色、地点、地图、资源、故事规则、
  种子数据、私有转录文本、私有运行器路径、隐藏重置 API 细节、
  私有判题器内部信息、UI 选择器转储或未脱敏外部事件载荷示例。
- `docs/iterations/v0.8/**`。

## 必须满足的修复语义

- V07-CR-01：`pass` 外部验证报告必须拒绝状态为 `accepted`、
  `deferred`、`open` 或其他未关闭状态的 P1/P2 发现项。
- V07-CR-02：外部验证报告检查器必须拒绝通用真实泄漏模式，包括本地绝对路径、
  `file://` 路径、`data-testid`、类似 CSS 选择器的文本、隐藏重置术语、
  判题器术语、转录文本术语、种子数据术语和事件载荷术语。
- V07-CR-03：就绪清单检查器必须对 `evidence_references[*].command`
  以及全部清单文本表面应用公开命令和禁止细节检查。
- V07-CR-04：投影读模型检查器必须拒绝 `private_application_state_summary`
  这类私有 / 应用状态字段术语，即使它有允许后缀。
- V07-CR-05：公共 Schema 必须在 JSON Schema 能表达的地方收紧，或通过文档 / 测试
  明确证明检查器语义权威，并保留“Schema 有效但检查器无效”的回归用例。
- P3：验证报告模板字段映射提示和投影读模型契约状态文本必须同步。

## 兼容性要求

- 现有有效报告、清单和投影 Schema 输入必须继续通过。
- 现有 Agent smoke 和 Agent autonomous saved-result 检查器必须继续通过。
- 变更必须保持通用，不要求私有消费者数据。
- 运行时 / API / 前端行为必须保持不变。

## 审查门禁

只有满足以下条件后，才可以开始实现：

- 包文档和中文镜像存在。
- 文档 / 契约评估器报告无 P0/P1 且无阻断性 P2。
- `review.md` 记录 `implementation_authorized: yes`。

只有满足以下条件后，才可以收尾：

- V07-CR-01 到 V07-CR-05 的红灯测试在修复前被观察到失败。
- 修复后聚焦检查器测试通过。
- 相邻 Agent smoke / autonomous 检查器测试通过。
- `test-plan.md` 中最终 v0.7 验证命令通过。
- 子代理 / 评估器检查点没有阻断性 P1/P2。
- 验证结果已更新且没有夸大声明。

## 范围外后续工作

- live 外部套件执行。
- 完整自主运行器 / 完整套件实现。
- v0.8 投影应用就绪。
