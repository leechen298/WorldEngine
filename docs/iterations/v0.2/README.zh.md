# v0.2 Recursive World Foundation

Status: planned / in progress

英文版本：`README.md`。

## Goal

建立 recursive world schema/spec foundation、additive event contract、generic schema smoke
validation、external fixture boundary、legacy boundary、iterative automation workflow 和 release
candidate evidence，同时保留 v0.1 runtime compatibility。

## Version Boundary

v0.2 不能实现 WorldSpec loader、RuntimeEngine-to-WorldCell migration、runtime bridge、Agent-in-World
loop、memory/self-continuity substrate、world generation、projection API、product UI、external
fixture repository、external validation repository 或 concrete demo world fixture。

## Detailed Plan Source

本文件是摘要索引。后续 package 的执行级详细计划见：

- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

## Package Index

### `0.2.1-project-north-star`

Type: documentation-only
Status: review complete
Purpose: 建立 north star、product model、scope、roadmap、iteration templates
和 docs governance。

### `0.2.2-recursive-world-contract`

Type: code
Status: review complete
Purpose: 增加 EntityRef、WorldCell、WorldSpec schemas 和 schema tests。

### `0.2.3-event-contract-extension`

Type: code
Status: review complete
Purpose: 扩展 Event optional structured references，并保持 compatibility。

### `0.2.4-worldspec-reference-fixture`

Type: code
Status: historical artifact
Purpose: historical concrete fixture package；future direction 已被 0.2.5
supersede。

### `0.2.5-core-boundary-cleanup-and-roadmap-reset`

Type: mixed
Status: review complete
Purpose: 清理 concrete external-world anchors、重置 roadmap，并用 generic
schema smoke coverage 替换 fixture tests。

### `0.2.6-iteration-workflow-and-plan-reset`

Type: documentation-only
Status: ready for review
Purpose: 重排 v0.2 剩余计划，增加 iterative automation workflow docs，并抽象化
v0.2 iteration docs 中的 residual concrete demo anchors。

### `0.2.7-recursive-schema-contract-hardening`

Type: mixed
Status: planned
Purpose: 加固 EntityRef、WorldCell、WorldSpec contracts 和 generic schema
tests，不做 runtime loading。

### `0.2.8-event-reference-contract-hardening`

Type: mixed
Status: planned
Purpose: 加固 EventRef 和 Event.refs additive event reference contracts，不做
resolver 或 causality runtime。

### `0.2.9-generic-schema-evidence-and-boundary-audit`

Type: documentation-only or mixed
Status: planned
Purpose: 审计 schema、event、external boundary 和 legacy boundary evidence。

### `0.2.10-legacy-boundary-and-compatibility-review`

Type: documentation-only or mixed
Status: planned
Purpose: 在 v0.3 bridge work 前明确 v0.1 runtime scaffold compatibility 和
legacy boundary。

### `0.2.11-v0.2-release-candidate-bundle`

Type: documentation-only
Status: planned
Purpose: 准备 release-candidate evidence，供 human / ChatGPT review，不声明
final release。

### `0.2.12-v0.2-final-closeout`

Type: documentation-only
Status: planned
Purpose: 仅在 0.2.11 review approval 后执行 final closeout。

## Required Reading

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
