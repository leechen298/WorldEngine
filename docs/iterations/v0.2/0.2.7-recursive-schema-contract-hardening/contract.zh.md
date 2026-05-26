# Contract

Status: ready for review

英文版本：`contract.md`。

## Public Concepts

- EntityRef：通过非空 `id`、非空 `kind`、optional `label` 和 free-form `metadata` 引用 generic entity。
- WorldCell：recursive world unit，包含非空 `id`、optional `label`、literal `kind = "world"`、entity references、child cells 和 metadata。
- WorldSpec：versioned recursive world specification，包含 `schema_version = "0.2"`、非空 `id`、optional `label`、required root WorldCell 和 metadata。
- Generic schema contract docs：human-readable contract documents，用于解释 schema fields、compatibility expectations、validation boundaries 和 non-runtime semantics。

## Compatibility Constraints

- Existing runtime behavior 必须保持不变。
- Existing API response shapes 必须保持不变。
- Existing frontend behavior 必须保持不变。
- Existing EventRef / Event.refs compatibility 不得受影响。
- Schema changes 必须 additive，除非本 package 回到 documentation review 并获得 explicitly approved breaking-change contract。
- Current tests 覆盖的 existing valid EntityRef、WorldCell 和 WorldSpec payloads 必须继续 validate。
- Current tests 覆盖的 existing invalid generic values 必须继续 rejected。

## Allowed Changes

- 新增 `docs/contracts/entity-ref-contract.md`。
- 新增 `docs/contracts/worldcell-contract.md`。
- 新增 `docs/contracts/worldspec-contract.md`。
- 如果阅读 existing tests 后仍有 coverage gaps，可用 domain-neutral schema tests 更新 `backend/app/tests/test_world_cell_schema.py`。
- 如果阅读 existing tests 后仍有 coverage gaps，可用 domain-neutral schema tests 更新 `backend/app/tests/test_worldspec_schema_smoke.py`。
- 只有在 approved contract 要求且有 tests 覆盖时，才可在 `backend/app/schemas/entity.py` 或 `backend/app/schemas/world_cell.py` 中进行 additive validation clarifications。
- 用 actual implementation evidence 更新本 package 的 `review.md` 和 `review.zh.md`。

## Forbidden Changes

- 不实现 WorldSpec loader。
- 不把 WorldSpec 连接到 RuntimeEngine。
- 不修改 runtime services、runtime state flow、event log persistence 或 tick behavior。
- 不修改 API routes 或 API response shapes。
- 不修改 frontend dashboard files。
- 不修改 fixtures 或添加 fixture data。
- 不添加 migrations。
- 不修改 `backend/worldengine/`。
- 不添加 concrete external-world names、characters、locations、resources、roles、story rules、seed data、UI concepts 或 product-specific backend logic。
- 不实现 generation、projection、memory、agent loop、self-continuity、resolver 或 causality behavior。
- 不创建 external repositories。

## Acceptance Requirements

- 三个 contract documents 存在，并描述 field semantics、compatibility behavior、validation boundaries 和 explicit non-goals。
- Focused schema tests 通过 documented assessment 证明已经 sufficient，或被更新以覆盖 recursive children、invalid generic values 和 model_dump / model_validate round trips。
- 如果 schema 或 test files 被修改，`make check-backend` 必须通过。
- 如果 schema 或 test files 被修改，focused schema pytest commands 必须通过。
- Package docs 和 contract docs 的 documentation checks 必须通过。
- Review evidence 记录每条 command，不得把未运行 tests 声称为 passed。
- Changed-file set 不包含 runtime、API、frontend、fixture、migration 或 external-repository implementation files。

## North Star Check

本 package 强化 reusable recursive world schema contracts。它不引入 concrete world、product-specific backend 或 application surface。Runtime loading 以及未来 agent、memory、generation、projection work 都保持 out of scope。

## Out-of-Scope Follow-ups

- 0.2.8 hardens EventRef and Event.refs。
- 0.2.9 audits schema、event、external boundary 和 legacy boundary evidence。
- v0.3 可以把 validated generic WorldSpec data load 到 runtime context。
- 后续 milestones 可以添加 generation、projection、agent loop、memory 和 self-continuity。
