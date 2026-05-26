# Technical Design

Status: ready for review

英文版本：`technical-design.md`。

## Current State

`backend/app/schemas/entity.py` 将 EntityRef 定义为 Pydantic model，包含非空 `id`、非空 `kind`、optional `label` 和 default empty metadata。

`backend/app/schemas/world_cell.py` 将 WorldCell 定义为 recursive Pydantic model，包含非空 `id`、optional `label`、literal `kind = "world"`、default empty `entity_refs`、default empty `child_cells` 和 default empty metadata。它还定义 WorldSpec，包含 literal `schema_version = "0.2"`、非空 `id`、optional `label`、required `root` 和 default empty metadata。

`backend/app/tests/test_world_cell_schema.py` 已覆盖 imports、defaults、nested child cells、entity references、required root WorldCell、empty-id rejection、non-world kind rejection、unsupported schema version rejection、invalid child/entity input rejection、model_dump serialization 和 model_validate reconstruction。

`backend/app/tests/test_worldspec_schema_smoke.py` 已覆盖 domain-neutral in-memory schema smoke payload、recursive children、EntityRef integration、WorldSpec validation 和 round trips。

## Contract Alignment and Invariants

- 保持 EntityRef generic。`kind` 标识 reference category，但本 package 不把它绑定到 runtime registries 或 resolver behavior。
- WorldCell 只在 schema layer 保持 recursive。
- WorldSpec 是 validated specification object，不是 runtime loader input path。
- Examples 保持 domain-neutral。
- 保留 current valid payload compatibility。
- 保留 runtime、API、frontend、fixture、migration 和 legacy directory behavior。

## Proposed Implementation

Documentation review approval 后，执行最小 scoped hardening pass：

1. 新增 `docs/contracts/entity-ref-contract.md`，说明 EntityRef fields、accepted generic semantics、metadata boundary、compatibility guarantees、validation behavior 和 non-goals。
2. 新增 `docs/contracts/worldcell-contract.md`，说明 recursive WorldCell structure、child cell semantics、entity reference semantics、metadata boundary 和 non-runtime status。
3. 新增 `docs/contracts/worldspec-contract.md`，说明 WorldSpec versioning、root semantics、serialization expectations、compatibility behavior 和 v0.3 handoff boundary。
4. 对照 `test-plan.md` 中的 accepted coverage list 检查 existing schema tests。
5. 只添加缺失的 domain-neutral tests。优先扩展现有 schema test files；只有 separate file 明显更清晰时才新增 test file。
6. 用 actual changed files、commands、results、compatibility review、scope review 和 unresolved findings 更新 `review.md` 和 `review.zh.md`。

## Affected Surfaces

Documentation:

- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/**`

Possible tests:

- `backend/app/tests/test_world_cell_schema.py`
- `backend/app/tests/test_worldspec_schema_smoke.py`

Possible schemas, only if additive clarification is required:

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`

## Data Model / Schema Changes

默认不需要 schema change。Expected implementation 是 contract documentation 加任何 missing generic tests。

如果 implementation 发现真实 schema ambiguity，allowed schema changes 仅限 `contract.md` 已批准的 additive validation clarifications。Breaking changes 需要回到 documentation review。

## Runtime / Service Design

None。本 package 不得添加 loader、resolver、runtime bridge、service flow、background task、persistence behavior、API route 或 frontend behavior。

## Compatibility

Existing v0.1 runtime behavior、event behavior、API response shapes、frontend behavior 和 legacy `backend/worldengine/` behavior 保持不变。

Current tests 覆盖的 existing valid EntityRef、WorldCell 和 WorldSpec payloads 必须继续 validate。Current tests 覆盖的 existing invalid payloads 必须继续 validation failure。

## Assumptions

- Pydantic 继续作为本 package 的 schema validation layer。
- Contract docs 可以 clarify semantics，而不要求 schema code changes。
- Current generic tests 是 baseline；凡已覆盖 acceptance criteria 的地方可以复用为 evidence。

## Risks

- Risk: tests 重复 existing coverage，而不是 harden meaningful gaps。Mitigation: implementation 必须先把 current tests 映射到 acceptance criteria，只添加 missing tests。
- Risk: contract docs 意外暗示 runtime loader behavior。Mitigation: 每个 contract doc 必须包含 explicit non-runtime boundaries。
- Risk: generic examples 漂移到 external validation world details。Mitigation: 使用 neutral identifiers，并对 touched docs and tests 运行 concrete demo anchor sweep。
- Risk: additive schema clarification 可能影响 existing payloads。Mitigation: 运行 focused schema tests 和 `make check-backend`，然后记录 compatibility evidence。
