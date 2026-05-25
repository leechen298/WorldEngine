# 契约

英文版本：`contract.md`

## 公共概念

- Core boundary cleanup：从 active WorldEngine core docs、fixture data 和 fixture
  tests 中移除 concrete Demo world anchors。
- Generic schema smoke fixture：domain-neutral WorldSpec JSON file，仅用于证明
  schema validation、recursion、entity references 和 round-trip behavior。
- External fixture world：未来位于 repository 外部的 consumer，通过 public contracts
  验证 WorldEngine，而不塑造 core repository internals。
- External validation report：redacted report format，用于记录 external validation
  evidence，同时不把 external world implementation details 存入 core repository。
- Historical iteration artifact：prior iteration documentation，只有在明确标注为
  historical context 时，才可以保留 concrete Demo language。

## 兼容性约束

- Existing runtime behavior 必须保持 compatible。
- Existing API response shapes 必须保持 compatible。
- Existing frontend behavior 必须保持 compatible。
- Existing generic schema contracts 必须保留。
- 本 package 不要求 schema changes；后续如提出 schema cleanup，除非 reviewed contract
  明确允许 breaking change，否则必须是 additive。
- WorldCell、WorldSpec、EntityRef、EventRef 和其他 generic schema names 不得因本
  cleanup 被移除。

## 允许变更

经 documentation gate review 和 approval 后，implementation 可以：

- 更新 `docs/project-north-star.md` 和 `.zh.md`，把 concrete Demo world wording
  替换成 external projection application、external validation world 和 external
  fixture world language。
- 更新 `docs/product-model.md` 和 `.zh.md`，保持 WorldEngine 是 generic recursive
  world runtime substrate。
- 更新 `docs/scope-boundaries.md` 和 `.zh.md`，移除 core repository 内允许 concrete
  Demo fixtures 的表达。
- 更新 `docs/roadmap.md` 和 `.zh.md`，移除 v0.7 superseded concrete fixture direction
  milestone，改为 external validation readiness / projection consumer readiness。
- 更新 `AGENTS.md` 和 `AGENTS.zh.md`，移除 current guidance 中的 concrete demo
  surface wording。
- 更新 `README.md` 和 `README.zh.md`，移除运行 superseded concrete fixture direction
  的描述。
- 更新其他包含相同 concrete Demo anchors 的 active core docs，包括 architecture、
  glossary、release planning、v0.2 index 或 plan docs。
- 将 `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/` 标记为不再定义
  future direction 的 historical iteration artifact。
- 删除 `backend/data/world_specs/historical concrete fixture path`，或用
  `backend/data/world_specs/schema_smoke_world.json` 替换。
- 删除或重写 `backend/app/tests/test_worldspec_fixture.py` 为
  `backend/app/tests/test_worldspec_schema_smoke.py`。
- 增加 `docs/external-fixture-boundary.md`。
- 增加 `docs/validation-report-template.md`。
- 将 later roadmap direction 重置为 generic engine milestones。
- 在 closeout 时更新本 package 的 `review.md`。

## 禁止变更

- 不创建 external fixture repository。
- 不创建 external validation repository。
- 不实现 WorldSpec loader。
- 不实现 runtime bridge。
- 不实现 Agent loop。
- 不实现 memory 或 self-continuity。
- 不实现 world generation。
- 不修改 frontend dashboard。
- 不修改 v0.1 runtime behavior。
- 不修改 API routes 或 response shapes。
- 不修改 production event log storage。
- 不修改 `backend/worldengine/` runtime behavior。
- 不删除 WorldCell、WorldSpec、EntityRef、EventRef 或其他 generic schema contracts。
- 不用另一个 concrete Demo world 替换 historical concrete fixture。
- 不引入任何 new concrete world、role、location、resource、plot rule、narrative
  rule、application UI、seed data 或 internal external-validation world
  implementation detail。
- 不保留与 concrete Demo world words、entities、locations、resources 或 assertions
  耦合的 active tests 或 active fixtures。
- 不把 historical iteration artifacts 当作 current roadmap direction。

## 活跃文档锚点清理

implementation 必须把以下文件视为 active-doc cleanup candidates：

- `AGENTS.md`
- `AGENTS.zh.md`
- `README.md`
- `README.zh.md`
- `docs/project-north-star.md`
- `docs/project-north-star.zh.md`
- `docs/product-model.md`
- `docs/product-model.zh.md`
- `docs/scope-boundaries.md`
- `docs/scope-boundaries.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/architecture.md`
- `docs/architecture.zh.md`
- `docs/glossary.md`
- `docs/glossary.zh.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

implementer 必须先搜索 concrete Demo world anchors，不能假设此列表完整。

## 历史文档规则

historical iteration packages 只有在新的 0.2.5 cleanup 明确标注旧 wording 是
historical 的情况下，才可以保留旧 wording。package close 后，historical documents
不得作为 future roadmap authority。

## 北极星检查

本 package 通过从 core repository 中移除 concrete Demo world semantics，强化 north
star。WorldEngine 继续聚焦 recursive world generation、runtime、event contracts、
agent-in-world behavior、memory、self-continuity 和 projections。

## 范围外 follow-ups

- 创建 external fixture repository。
- 创建 external validation repository。
- Runtime loading of WorldSpec data。
- Runtime bridge from WorldSpec to v0.1 runtime。
- Agent-in-world loop。
- Memory and self-continuity substrate。
- World generation v1。
- User-facing projection application implementation。
