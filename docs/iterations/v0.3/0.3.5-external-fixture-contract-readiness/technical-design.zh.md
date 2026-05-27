# Technical Design

## 设计摘要

本包是仅文档包。设计输出是一个公开契约，说明外部运行器如何通过已评审表面调用
WorldEngine，以及脱敏报告如何作为证据返回。

本包不引入代码设计、schema 设计、API 实现、样例实现或测试实现。

## 契约结构

`docs/contracts/external-fixture-runner-contract.md` 包含：

- 目的和消费者边界。
- 公开概念。
- 允许的公开消费表面。
- v0.3 契约链。
- 脱敏验证报告形状。
- 必需脱敏规则。
- 兼容性约束。
- 禁止推断。
- 验收要求。
- 交接规则。

## 外部运行器流程

文档化流程为：

1. 外部运行器选择一个公开 WorldEngine 契约表面。
2. 外部运行器在本仓库之外调用 WorldEngine。
3. 外部运行器记录观察到的公开行为。
4. 外部运行器脱敏消费者特定内部细节。
5. 外部运行器使用 `docs/validation-report-template.md` 生成报告。
6. WorldEngine 只保存或评审脱敏报告和通用引擎 follow-up。

## 脱敏模型

报告可以包含抽象标识符：

- `external-suite-001`
- `target-redacted-001`
- `scenario-001`

报告不得包含具体外部世界名称、角色、地点、剧情规则、seed data、判定器内部细节、
UI 选择器、隐藏重置 API、私有仓库路径或未脱敏 payload。

## 验证设计

文档验证基于：

- 文件存在检查。
- 状态同步检查。
- 契约标题和必需术语检查。
- 对照 `docs/validation-report-template.md` 的脱敏字段检查。
- 具体锚点 sentinel no-match 检查。
- 实现范围无变更检查。

后端、前端、运行时、API、E2E、Agent smoke 和构建测试不属于本包，因为本包只修改文档。
