# Technical Design

状态：documentation-only design

## Design Boundary

本 package 设计 contract vocabulary，不实现 runtime 或 checker。设计刻意写在 documentation 中，
让后续 package 可以选择是否实现 schemas、templates 或 checkers，而不会把这些工作夹带进本阶段。

## Handoff Record Shape

如果未来 package 实现 machine-checkable handoff record，应使用这个 conceptual shape：

```text
ExternalValidationHandoff
  handoff_id
  version
  engine_reference
  surface_id
  contract_surface_path
  evidence_class
  status
  evidence_reference
  redaction_confirmation
  forbidden_detail_review
  unresolved_findings
  rationale
  compatibility_notes
  scope_review
```

本 package 不创建 schema file。该 shape 只是后续 review 的 design target。

## Status Design

允许的 handoff statuses：

- `contract_ready`：contract surface 已存在并 review。
- `core_evidence_ready`：后续 package 已为 core-side surface 提供 current-session evidence。
- `blocked`：在 blocker 被修复或由后续 reviewed package 接受前，该 surface 不能支持目标 claim。
- `skipped`：该 check 未运行，并有明确 rationale。
- `out_of_scope`：该 surface 超出 active package 或 repository boundary。

禁止的 status behavior：

- `blocked`、`skipped` 和 `out_of_scope` 不得计为 PASS。
- `contract_ready` 不得计为 runtime/API/product/external validation PASS。
- 除非后续 external workflow 提供 reviewed public evidence，`core_evidence_ready` 不得计为
  external validation PASS。

## Redaction Design

每个 public handoff record 必须同时包含：

- redaction confirmation statement。
- forbidden-detail review，对 forbidden classes 给出明确 false/none values。

未来 machine checks 应拒绝明显 private paths、UI selector markers、hidden reset markers、
oracle-internal markers、seed-data markers、transcript markers、secrets、provider trace
terms、raw prompt terms 和 non-redacted external event payload markers。

## Compatibility Design

本设计组合既有 public baselines：

- v0.7 redacted report semantics 定义 report safety。
- v0.7 readiness manifest semantics 定义 public evidence references。
- v0.7 projection read-model semantics 定义 read-only/no-write boundaries。
- v0.8 `0.8.1` 定义 claim taxonomy。
- v0.8 `0.8.2` 定义 observable surfaces。
- v0.8 `0.8.3` 提供 bounded core-readiness evidence。

本 package 不修改这些 files 或 behaviors。

## Review Design

Review 必须确认本 package：

- 命名 handoff vocabulary，但不实现它。
- implementation authorization 保持关闭。
- 保留 forbidden detail classes。
- v0.7 repair evidence 仍只作为 handoff context。
- 让 `0.8.5` 负责 current-session core smoke evidence。
