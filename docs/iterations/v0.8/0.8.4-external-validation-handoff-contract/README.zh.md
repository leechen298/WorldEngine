# 0.8.4 External Validation Handoff Contract

状态：review complete
类型：documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## 目的

本 package 定义 WorldEngine 可以交给未来 external validation function 的 public handoff
contract。它说明 core repository 可以命名、分类、引用什么，但不定义 external validator 如何
连接、运行、评判 private scenarios，或保存 private evidence。

Handoff contract 连接：

```text
reviewed v0.8 core readiness surfaces
  -> public handoff surface identifiers
  -> redacted evidence reference rules
  -> blocked/skipped/out-of-scope classification
  -> later core-side smoke evidence
```

## 当前状态

当前 v0.8 已具备：

- `0.8.1` minimum working-state claim taxonomy。
- `0.8.2` observable public surface boundaries。
- `0.8.3` bounded generation -> runtime -> Agent loop core-readiness evidence。
- v0.7 handoff context：redacted validation reports、readiness manifests、
  projection read-model contracts 和 V07-CR checker/docs repair。

当前缺口是 v0.8-specific handoff vocabulary：让 public evidence references 对后续
validation 有用，同时防止 private validator details 进入 core repository。

## Handoff Contract Summary

WorldEngine 只可以暴露或记录 public、generic handoff facts：

- handoff surface ids。
- public contract surface references。
- redacted evidence reference ids 和 repository-relative paths。
- evidence class 和 status values。
- redaction confirmation。
- forbidden-detail review。
- blocker、skipped 和 out-of-scope rationale。
- compatibility notes 和 unresolved finding classification。

WorldEngine 不得暴露或记录：

- external validator connection details。
- external validator commands 或 private runner state。
- private scenarios、oracle internals、product UI selectors、app repository
  layout、private transcripts、screenshots、paths、world data、product content、
  secrets、provider traces、raw prompts 或 non-redacted external event payloads。

## 范围

本 package 是 documentation-only。它可以创建 0.8.4 package documents、Chinese mirrors，
并更新 parent v0.8 status/review。它不添加 schemas、checkers、templates、API routes、
backend tests、frontend code、fixtures、generated artifacts、migrations、external repositories
或 `backend/worldengine/` files。

## Handoff

本 package 将给 `0.8.5-core-working-state-smoke-evidence` 交付一个 public classification
contract，用于后续 core-side evidence。它不交付 external validation PASS、product readiness、
projection application readiness、frontend/E2E PASS、Agent smoke PASS、autonomous PASS、
generation quality PASS 或 final v0.8 readiness。
