# v0.2 递归世界基础

状态：`planned / in progress`

英文版本：`README.md`

## 目标

v0.2 的目标是建立可继续演进的递归世界基础：通用的 schema/spec 基础、
增量式事件契约、通用 schema 冒烟验证、外部 fixture 边界、legacy boundary、
自动迭代工作流，以及 release candidate 所需的证据框架。

v0.2 仍保持对 v0.1 runtime scaffold 的兼容，不把当前 runtime 改造成
WorldCell runtime。

## 版本边界

v0.2 不实现以下内容：

- WorldSpec loader。
- RuntimeEngine 到 WorldCell 的迁移。
- runtime bridge。
- Agent-in-World loop。
- memory / self-continuity substrate。
- world generation。
- projection API。
- product UI。
- external fixture repository。
- external validation repository。
- concrete demo world fixture。

## 详细计划来源

本文件只是 v0.2 的摘要索引。后续 package 的执行级计划以以下文件为准：

- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

## 包索引

### `0.2.1-project-north-star`

类型：`documentation-only`
状态：`review complete`
目的：建立项目北极星、产品模型、范围边界、路线图、迭代模板和文档治理规则。

### `0.2.2-recursive-world-contract`

类型：`code`
状态：`review complete`
目的：增加 EntityRef、WorldCell、WorldSpec schemas 和 schema tests。

### `0.2.3-event-contract-extension`

类型：`code`
状态：`review complete`
目的：扩展 Event 的可选结构化引用，并保持兼容性。

### `0.2.4-worldspec-reference-fixture`

类型：`code`
状态：`historical artifact`
目的：保留 historical concrete fixture package 的历史事实；后续方向已由
0.2.5 取代。

### `0.2.5-core-boundary-cleanup-and-roadmap-reset`

类型：`mixed`
状态：`review complete`
目的：清理 concrete external-world anchors、重置路线图，并用通用 schema
冒烟覆盖替换旧 fixture tests。

### `0.2.6-iteration-workflow-and-plan-reset`

类型：`documentation-only`
状态：`review complete`
目的：重排 v0.2 剩余计划，增加自动迭代工作流文档，并抽象化 v0.2
iteration docs 中残留的 concrete demo anchors。

### `0.2.7-recursive-schema-contract-hardening`

类型：`mixed`
状态：`review complete`
目的：加固 EntityRef、WorldCell 和 WorldSpec contract，并补强通用 schema
tests；不做 runtime loading。

### `0.2.8-event-reference-contract-hardening`

类型：`mixed`
状态：`review complete`
目的：加固 EventRef 和 Event.refs 的增量式事件引用契约；不实现 resolver
或 causality runtime。

### `0.2.9-generic-schema-evidence-and-boundary-audit`

类型：`documentation-only`
状态：`review complete`
目的：审计 schema、event、external boundary 和 legacy boundary 的 evidence。

### `0.2.10-legacy-boundary-and-compatibility-review`

类型：`documentation-only`
状态：`review complete`
目的：在 v0.3 bridge work 前明确 v0.1 runtime scaffold 的兼容性和 legacy
boundary。

### `0.2.11-v0.2-release-candidate-bundle`

类型：`documentation-only`
状态：`review complete`
目的：准备 release-candidate evidence，供 human / ChatGPT review；不声明
final release。

### `0.2.12-v0.2-final-closeout`

类型：`documentation-only`
状态：`ready for review`
目的：仅在 0.2.11 review approval 后执行 final closeout。

## 必读文件

- `AGENTS.md`
- `AGENTS.zh.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
