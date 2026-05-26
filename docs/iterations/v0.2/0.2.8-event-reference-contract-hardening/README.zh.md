# 0.2.8 Event Reference Contract Hardening

状态：`review complete`

类型：`mixed`

英文版本：`README.md`

## 目标

为加固 `EventRef` 和 optional `Event.refs` 准备已审核的 implementation
contract，使其作为 additive event reference structures，同时保持 existing
event compatibility。

## 范围

本 package 在 documentation review 通过后，可以新增 EventRef contract 文档，
并按需更新 focused、domain-neutral event schema compatibility tests。refs
必须保持 event-schema-local；不得实现 referential integrity resolver、
causality engine、runtime bridge、memory link、projection behavior、frontend
behavior、fixture data、migration 或 external repository。

当前 documentation-stage pass 只创建 package documents。Implementation 只能在
package documents 被 review 和 approve 后开始。

## 文档

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

## 状态清单

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [ ] Implementation complete
- [x] Documentation-stage evidence complete
- [x] Review complete

## Review 通过后的计划交付

- `docs/contracts/event-ref-contract.md`
- 如果 approved acceptance requirements 尚未被覆盖，focused updates to
  `backend/app/tests/test_event_schema_compat.py`。
- 本 package `review.md` 中的 implementation evidence。

## 假设

- 当前 event schema source of truth 是 `backend/app/schemas/event.py`。
- 当前 focused compatibility coverage 从
  `backend/app/tests/test_event_schema_compat.py` 开始。
- `Event.refs` 保持 list，默认 `[]`，并对 existing event dictionaries 保持
  optional。
- v0.2 中 `EventRef.kind` 和 `EventRef.role` 是 generic strings，不是
  enumerated runtime semantics。

## 未决风险

- 当前 tests 已覆盖多项 compatibility cases，implementation 必须避免新增重复
  且价值低的 tests。
- Contract wording 可能误导为 resolver、causality、memory 或 projection
  behavior；implementation contract 必须把这些明确列为 non-goals。
- 如果 implementation 发现需要 non-additive schema behavior change，必须先回到
  documentation review，再继续 code changes。
