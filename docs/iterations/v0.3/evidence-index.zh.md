# v0.3 证据索引

状态：待评审

## 目的

本索引把 v0.3 各迭代包证据映射到发布候选评审前需要确认的兼容性表面。它区分
已有证据支持的内容、仅文档定义的内容，以及仍属于交接风险的内容。

## 证据矩阵

| 迭代包 | 类型 | 状态 | 证据来源 | 关键命令 / 结果 | 兼容性覆盖 | 发现 |
|---|---|---|---|---|---|---|
| 0.3.0 规划基线 | 仅文档 | 评审完成 | `0.3.0.../review.md` | `git diff --check`；文件、状态、措辞检查 | 版本边界、v0.3 包序列、兼容性基线 | 未记录 P1/P2/P3 |
| 0.3.1 加载器契约 | 仅文档 | 评审完成 | `0.3.1.../review.md` | `git diff --check`；契约、状态、范围检查 | 加载器输入、输出、错误、校验、运行时隔离 | 无未解决 P1/P2/P3 |
| 0.3.2 加载器实现 | 文档与代码混合或代码 | 评审完成 | `0.3.2.../review.md` | 后端 venv `python -m pytest` 加载器和 schema smoke 检查通过；仓库根目录 `pytest` 形式因环境/导入路径失败 | 纯 WorldSpec 加载器、schema 校验、无运行时/API 耦合 | P3：根目录直接 pytest 形式在当前环境不可靠。target_package: `0.3.7-v0.3-release-candidate-bundle`。defer_reason: 发布候选验证规划可选择规范的后端 venv 命令形式。 |
| 0.3.3 桥接契约 | 仅文档 | 评审完成 | `0.3.3.../review.md` | `git diff --check`；契约、状态、兼容性检查 | 运行时上下文语义、兼容性证据要求、RuntimeEngine 边界 | 未记录 P1/P2/P3 |
| 0.3.4 桥接实现 | 文档与代码混合或代码 | 评审完成 | `0.3.4.../review.md` | 后端 venv `python -m pytest` 桥接、运行步进、事件、参数、归档、加载器、schema smoke 检查通过 | 可选惰性运行时上下文，运行时/API/事件/参数/归档兼容 | 实现阶段未记录 P1/P2/P3 |
| 0.3.5 外部样例契约准备 | 仅文档 | 评审完成 | `0.3.5.../review.md` | `git diff --check`；契约、脱敏、状态、范围检查 | 公开外部样例运行器边界和脱敏报告要求 | P2 `v0.3-P2-001` 延期到 0.3.6 且已解决；P3：后续可能需要公开 CLI/API 文档和更严格报告 schema。target_package: `v0.7-external-validation-readiness`。defer_reason: 外部运行器/报告加固属于后续验证准备。 |

## 兼容性表面索引

| 表面 | 分类 | 证据 |
|---|---|---|
| WorldSpec 加载器 | 有变更且有证据 | 0.3.2 实现 `backend/app/core/worldspec_loader.py`；后端 venv 聚焦加载器测试通过。 |
| 运行时上下文桥接 | 有变更且有证据 | 0.3.4 实现 `backend/app/core/runtime_context.py` 和可选惰性 `RuntimeEngine` 存储；聚焦桥接测试通过。 |
| 运行 tick 与 `world_time_seconds` | 未改变且有证据 | 0.3.4 运行步进测试通过。 |
| API envelope 和返回形状 | 未改变且有部分证据 | 0.3.4 事件兼容测试通过；加载器和桥接未新增 API route。 |
| `/runtime/step` 或运行步进行为 | 未改变且有证据 | 0.3.4 运行步进测试通过。 |
| `/world/events` | 未改变且有证据 | 0.3.4 事件 API 兼容测试通过。 |
| `/world/event-steps` | 未改变且有证据 | 0.3.4 事件 API 兼容测试通过。 |
| 可选 `Event.refs` 兼容 | 未改变且有证据 | 0.3.4 事件 schema 兼容测试通过。 |
| 世界参数和参数应用行为 | 未改变且有证据 | 0.3.4 world params 和 params agent 测试通过。 |
| 归档 snapshot 和 summary 行为 | 未改变且有证据 | 0.3.4 archive snapshot summary 测试通过。 |
| 前端可见返回形状 | 未触及 | v0.3 加载器和桥接实现包未修改前端文件。后端兼容测试覆盖当前已测试的返回表面。 |
| Schema 兼容 | 未改变且有证据 | 0.3.2 和 0.3.4 schema smoke 测试通过；0.3.6 未修改 schema 文件。 |
| 样例边界 | 仅文档证据 | 0.3.5 定义公开运行器和脱敏报告边界，未添加样例数据。 |
| 旧路径 `backend/worldengine/` 边界 | 未触及 | 各包 review 记录旧路径没有变更。 |

## 假设

- 既有迭代包 review 文件准确记录了对应实现或文档会话运行过的命令。
- 后端 venv `python -m pytest` 是 v0.3 证据中可靠的 pytest 调用方式，因为
  0.3.2 中直接从仓库根目录运行 `pytest` 失败。
- 本审计把前端可见兼容性视为未触及，因为 v0.3 加载器和桥接包没有修改前端文件，
  也没有新增 API 暴露路径。

## 开放风险

- P3：前端可见返回形状证据仍是间接证据，除非后续发布候选包运行更广的后端或前端 smoke 覆盖。target_package:
  `0.3.7-v0.3-release-candidate-bundle`。defer_reason: 更广的 smoke 覆盖属于可选发布候选证据，不是完成本仅文档审计的要求。
- P3：外部样例报告在自动化稳定消费前，可能需要机器可读 schema。target_package:
  `v0.7-external-validation-readiness`。defer_reason: 报告自动化加固属于后续外部验证准备。
- P3：外部运行器在 v0.7 验证准备前，可能需要补充公开 CLI/API 文档。target_package:
  `v0.7-external-validation-readiness`。defer_reason: 面向运行器的文档扩展属于后续验证准备；0.3.6 只审计既有公开边界。

## 交接准备度

v0.3 证据支持进入发布候选准备；`v0.3-P2-001` 解决后已无剩余开放 P1 或 P2
阻塞项。v0.4 只能在 v0.3 发布候选和最终收口门禁完成后，把加载器和惰性运行时上下文桥接作为基础使用。
