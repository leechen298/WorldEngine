# 契约

## 公开概念

- 独立 reviewer：直接读取 source inputs，不依赖实现者总结的 Codex reviewer。
- Unsupported claim：缺少当前证据或与代码冲突的 release、compatibility、loader、
  bridge、API、runtime 或 Event.refs statement。
- 自主评审建议：`04` 中记录的最终 reviewer outcome。

## Reviewer 输入

独立 reviewer 必须读取：

- `README.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.3/evidence-index.md`
- `docs/iterations/v0.3/compatibility-audit.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`

## 允许修改

- 创建和更新本包规划文档。
- 定义 autonomous reviewer 输入和检查项。
- 定义 reviewer 应运行或阻塞的命令。
- 定义 `04` 的报告形状。

## 禁止修改

- 本包不执行 autonomous review。
- 不修改代码或测试。
- 不修改 runtime、schema、API、frontend、fixtures、migrations 或外部仓库。
- 不添加 concrete demo-world details 或 private oracle details。
- 不把 autonomous validation 写成成功。
- 不改变 v0.3 发布状态。

## 兼容性要求

后续 review 必须明确检查：

- WorldSpec loader claim。
- runtime context bridge claim。
- RuntimeEngine compatibility。
- Event.refs response compatibility。
- API / schema / runtime compatibility。
- 没有 concrete demo-world regression。

## 范围外后续事项

Autonomous validation execution 属于 `04`。修复属于单独的已评审 package。
