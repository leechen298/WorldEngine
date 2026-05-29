# 契约

## 公开概念

- 收口后验证：v0.3 收口之后补充的独立证据。
- E2E 可用性：当前 checkout 和环境中是否存在可运行的浏览器 E2E setup。
- Fallback validation：当 E2E 未配置或无法运行时，用 API smoke 加后端集成测试兜底。
- Loader 验证：聚焦检查 `load_worldspec`。
- Runtime context bridge 验证：聚焦检查 `build_runtime_context` 和 `RuntimeEngine`
  的惰性 context 存储。
- Event.refs 兼容性：检查 event APIs 对空 refs 和非空 refs 的响应兼容性。

## 允许修改

- 创建和更新本包规划文档。
- 定义后续执行的命令和证据要求。
- 定义 fallback 和 blocker 规则。
- 定义 release claim 和 compatibility claim 检查。

## 禁止修改

- 本包不执行验证命令。
- 不修改 runtime、schema、API、frontend、backend tests、fixtures 或 migrations。
- 不创建外部仓库。
- 不加入具体 demo-world details、UI selectors、seed data 或 private oracle details。
- 不改变 v0.3 发布状态。
- 不声明 E2E、集成、loader、bridge、API smoke 或后端验证已经成功。

## 兼容性要求

本计划必须保持：

- v0.3 `final / closeout complete` 状态。
- loader 和 bridge 作为通用引擎基础设施的边界。
- `RuntimeEngine` tick 和 `world_time_seconds` 兼容性。
- Event.refs 响应兼容性。
- 外部 fixture 边界和脱敏证据策略。

## 范围外后续事项

- 实际验证执行属于 `02-e2e-validation-execution`。
- 独立 Codex review 规划属于 `03-codex-autonomous-validation-plan`。
- 最终汇总属于 `05-final-validation-bundle`。
- 任何修复工作都需要单独的已评审 package。
