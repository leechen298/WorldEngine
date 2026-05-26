# 0.2.7 Recursive Schema Contract Hardening

Status: review complete

Type: mixed

英文版本：`README.md`。

## Goal

为 EntityRef、WorldCell、WorldSpec 的 generic schema contract hardening 准备可审查的 implementation contract 和验证要求，同时不把 WorldSpec 接入 runtime loading。

## Scope

文档审查通过后，本 package 可以新增 generic schema contract 文档，并按需更新 domain-neutral schema tests。它必须保持 engine core generic，保留 v0.1 runtime behavior，并避免 loader、runtime bridge、generation、projection、frontend、fixture、migration 或 external repository work。

当前 documentation-stage pass 只创建 package documents。Implementation 只能在 package documents 通过 review 和 approval 后开始。

## Documents

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Planned Deliverables After Review

- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`
- 如果 approved contract 需要更多 coverage，则 focused 更新 generic schema tests。
- 在本 package 的 `review.md` 中记录 implementation evidence。

## Assumptions

- 当前 recursive schema source of truth 是 `backend/app/schemas/entity.py` 和 `backend/app/schemas/world_cell.py`。
- 当前 generic schema coverage 从 `backend/app/tests/test_world_cell_schema.py` 和 `backend/app/tests/test_worldspec_schema_smoke.py` 开始。
- 本 package 继续使用 Pydantic model behavior 作为 validation mechanism。

## Open Risks

- 现有 tests 已覆盖部分 recursive 和 round-trip behavior，implementation 必须避免重复低价值 tests。
- Contract docs 可能暴露 `EntityRef.kind` semantics 的 ambiguity；解决该 ambiguity 必须保持 additive 和 domain-neutral。
- 如果 implementation 发现 schema behavior 必须 non-additive change，必须回到 documentation review 后才能继续 code changes。
