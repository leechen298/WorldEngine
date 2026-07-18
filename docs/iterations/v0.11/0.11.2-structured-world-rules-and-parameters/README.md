# 0.11.2 Structured World Rules And Parameters

Chinese mirror: `README.zh.md`.

Status: implementation complete / focused verification passed
Type: mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Attach structured public rules, parameters, constraints, and boundaries to a
world session so v0.11 event generation can later reference public legality
evidence.

This package reuses existing rule-parameter schemas and validators. It does
not implement event generation or direction handling.

## Scope

Allowed after review:

- Additive session-scoped rule/parameter attach and summary API.
- Reuse `GeneratedRuleParameterSet`, `validate_generated_rule_parameter_set`,
  and `build_public_world_rule_summary`.
- Store accepted rule summaries in the in-memory session store.
- Manifest discovery updates.
- Focused backend tests for valid attach, invalid refs/types/private markers,
  summary access, and existing params compatibility.

Forbidden:

- No live provider calls.
- No direction queue.
- No event generation or diff application.
- No fidelity scoring.
- No Validation Client implementation or external PASS.
- No durable persistence/migrations.
- No concrete demo-world seed data.
- No `backend/worldengine/` changes.

## Expected Deliverables

- Session rule/parameter attach endpoint.
- Session rule/parameter summary endpoint.
- Public validation diagnostics and redaction-safe summary.
- Focused backend tests and review evidence.

## Status Checklist

- [x] Package documents drafted.
- [x] Documentation / contract evaluator complete.
- [x] implementation_authorized: yes.
- [x] Implementation complete.
- [x] Verification complete.
- [x] Evaluator closeout complete.
