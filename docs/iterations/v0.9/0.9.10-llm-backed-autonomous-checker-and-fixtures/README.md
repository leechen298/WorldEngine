# 0.9.10 LLM-backed Autonomous Checker And Fixtures

Chinese mirror: `README.zh.md`.

Status: implementation complete / verification passed
Type: mixed testing/tooling package
implementation_authorized: yes
provider_live_call_authorized: no
evidence_execution_authorized: no
external_validation_authorized: no

## Package

Name: `0.9.10-llm-backed-autonomous-checker-and-fixtures`

## Goal

Implement checker, schema, fixture, and focused test support so LLM-backed
autonomous scenarios can be judged from structured public artifacts as
`pass`, `fail`, `blocked`, or `not_run` without subjective review or runtime
provider execution in this package.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Scope Summary

This package may extend the existing saved-result autonomous checker in
`tools/testing/validate_agent_autonomous_result.py`, its tests, fixture
directories, and LLM-backed testing documentation. It must not change
WorldEngine runtime behavior, provider call paths, frontend UI, Validation
Client code, generated results, or `backend/worldengine/`.

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Current Route

```text
0.9.10-llm-backed-autonomous-checker-and-fixtures-implementation-complete
```

Implementation is complete for the reviewed `tools/testing`, fixtures,
LLM-backed testing docs, package docs, and necessary parent routing/review docs
scope. Provider live calls, evidence execution, external validation, frontend,
Validation Client, `backend/app/**`, and `backend/worldengine/**` remain
unauthorized.
