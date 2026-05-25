# 技术设计

英文版本：`technical-design.md`

## 概览

0.2.5 是一次 boundary reset。implementation 应让 core repository 重新保持
domain-neutral，同时保留 generic recursive-world schema language。

implementation stage 有两个工作面：

- active documentation cleanup。
- fixture and test cleanup。

本 package 不包含 runtime behavior、API behavior、frontend behavior、loader behavior、
Agent behavior、memory behavior 或 generation behavior changes。

## 活跃文档清理

把 active docs 中的 concrete Demo world language 替换为 generic consumer language：

- 将 concrete demo surface wording 替换为 external projection application。
- 将 superseded concrete fixture direction wording 替换为 external validation world
  或 external fixture world。
- 将 validation interface wording 替换为 external validation consumer。
- 保留 external consumers 通过 public contracts 验证 WorldEngine 的原则。
- 保留 concrete Demo worlds 不得存在于 core repository 或塑造 core repository 的原则。

cleanup 应保留已有的 English / Chinese mirrors。如果 active English doc 被修改，
且存在 `.zh.md` mirror，必须在同一 implementation pass 中更新镜像。

## Fixture 策略

移除 concrete fixture：

- 删除 `backend/data/world_specs/historical concrete fixture path`；或
- 用 `backend/data/world_specs/schema_smoke_world.json` 替换。

如果选择替换，新 fixture 必须 domain-neutral。可以使用以下 generic identifiers 和 labels：

- `schema-smoke-world`
- `Schema Smoke World`
- `root`
- `child-a`
- `child-b`
- `entity-a`

fixture 不得编码 concrete Demo world、role、location、resource、plot rule、
narrative rule、schedule、inventory 或 UI concept。

## 测试策略

替换 concrete fixture test：

- 删除或重写 `backend/app/tests/test_worldspec_fixture.py`。
- 如新文件名更清楚，可创建 `backend/app/tests/test_worldspec_schema_smoke.py`。

schema smoke test 可以直接用 `json` 和 `pathlib` 读取 JSON，但不得实现 production
WorldSpec loader。

test 只验证 generic schema behavior：

- `WorldSpec.model_validate(...)` 接受 fixture dictionary。
- `schema_version` 是 `"0.2"`。
- `root` 存在且是 `WorldCell`。
- `root.kind` 是 `"world"`。
- `root.child_cells` 支持 recursive child worlds。
- nested child cells 可递归 validate。
- `EntityRef` 通过 `entity_refs` 支持 generic entity references。
- `model_dump()` 后再 `WorldSpec.model_validate(...)` 可以 round-trip。

test 不得断言 concrete Demo semantics。active test file 不得包含具体 demo anchor terms。

## External Fixture 边界文档

implementation 期间增加 `docs/external-fixture-boundary.md`。该文档定义 future
external fixtures 的 core-repository boundary：

- external fixtures 通过 public WorldEngine schemas、APIs、CLI commands 或
  validation contracts 消费 WorldEngine。
- external fixtures 不得要求 core repository 知道它们的 world entities、
  locations、resources、story rules 或 UI。
- core repository 可以存放 redacted evidence、contract examples 和 validation
  report formats。
- core repository 不得存放 external fixture seed data 或 internal validation world
  implementation details。

## Validation Report 模板

implementation 期间增加 `docs/validation-report-template.md`。它应记录 redacted
validation evidence，同时不嵌入 external world details：

- validation target name 或 redacted identifier。
- WorldEngine version 或 commit。
- exercised public contract。
- commands 或 runner invocation。
- pass/fail result。
- redacted evidence summary。
- compatibility notes。
- unresolved findings。

template 不得要求 external-world seed data、concrete entity names、locations、
resources、plot rules 或 internal validation implementation files。

## 路线图重置

更新 active roadmap docs，移除 superseded concrete fixture direction，改用 generic
engine milestones：

- v0.2.5：core boundary cleanup and roadmap reset。
- v0.2.6：iteration workflow and plan reset。
- v0.3：WorldSpec loader and runtime bridge，只加载 generic WorldSpec。
- v0.3.5：external fixture contract readiness，定义 external runners 如何调用 main
  repository，但不创建这些 repositories。
- v0.4：Agent-in-World minimal loop，包含 perception、action intent、validated
  action result 和 event consequence。
- v0.5：memory and self-continuity substrate。
- v0.6：world generation v1。
- v0.7：external validation readiness / projection consumer readiness。
- v0.8：first external projection application readiness。

## 兼容性

implementation 必须保留 generic schema compatibility。它可以移除或替换 concrete
fixture data 和 concrete fixture assertions，但不得移除或收窄 WorldSpec、WorldCell、
EntityRef 或 EventRef。

Runtime、API、frontend 和 legacy backend behavior 必须保持不变。
