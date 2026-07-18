# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Affected Files

Allowed implementation files after review:

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_session_rule_parameters_api.py`
- existing rule-parameter tests only if compatibility assertions need updates.

## API Shape

Add:

```text
POST /sessions/{session_id}/rules
GET /sessions/{session_id}/rules
```

`POST` accepts `GeneratedRuleParameterSet` and returns validation result plus
public summary. Accepted rule sets are attached to the session. Rejected sets
return public rejection diagnostics without mutating the session's accepted
summary.

`GET` returns the current attached rule summary for a session or a public
`not_attached` status.

## Storage

Extend the in-memory session record with optional:

- last accepted `PublicWorldRuleSummary`.
- last `RuleParameterValidationResult`.

No persistence or migration is added.

## Redaction

Use existing validator behavior. If private markers are present, public
summary fields that could echo ids/paths must be empty and redaction status
must be `failed`.
