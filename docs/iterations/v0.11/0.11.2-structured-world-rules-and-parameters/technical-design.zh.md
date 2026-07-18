# Technical Design

英文版本：`technical-design.md`。

## Affected Files

评审后允许修改的 implementation files：

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_session_rule_parameters_api.py`
- 只有在需要补 compatibility assertions 时，才修改 existing rule-parameter tests。

## API Shape

新增：

```text
POST /sessions/{session_id}/rules
GET /sessions/{session_id}/rules
```

`POST` 接收 `GeneratedRuleParameterSet`，返回 validation result 和 public summary。
Accepted rule sets 会 attach 到 session。Rejected sets 返回 public rejection diagnostics，
但不修改 session 当前已 accepted 的 summary。

`GET` 返回 session 当前 attached rule summary，或者 public `not_attached` status。

## Storage

扩展 in-memory session record，增加 optional：

- last accepted `PublicWorldRuleSummary`。
- last `RuleParameterValidationResult`。

不增加 persistence 或 migration。

## Redaction

使用现有 validator behavior。如果存在 private markers，可能 echo ids/paths 的 public summary
fields 必须为空，redaction status 必须是 `failed`。
