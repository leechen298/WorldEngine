# v0.4 Post-Closeout Validation And Test Expansion

Status: implementation complete / validation passed with P3
Type: post-closeout mixed validation campaign

## Goal

Add and run executable validation coverage for the current v0.4 product
surface after v0.4 final closeout, without reopening v0.4 product scope.

This campaign covers:

- v0.4 Agent Loop API Playwright E2E coverage.
- existing dashboard Auto-Tune compatibility E2E coverage.
- Agent UI/CLI smoke coverage for dashboard-operated flows.
- current-session evidence for whether the current product passes those
  checks.

## Boundary

Allowed:

- add or update E2E tests and E2E scenario documentation.
- add or update Agent smoke scenario docs, checker/helper support, fixtures,
  and validated result artifacts.
- record durable validation summaries.
- update package review evidence.

Forbidden:

- do not change v0.4 runtime, schema, API implementation, backend services,
  frontend product UI, migrations, external repositories, concrete world data,
  or `backend/worldengine/`.
- do not call basic Agent smoke a full scorecard-based autonomous suite.
- do not change v0.4 final release status.

## Package Index

| Package | Type | Status | Purpose |
| --- | --- | --- | --- |
| `01-e2e-agent-test-expansion` | mixed | passed with P3 | Define, implement, and run v0.4 Agent Loop E2E plus Agent UI/CLI smoke coverage. |

## Current State

Active child package: `01-e2e-agent-test-expansion`.

Current route: final review complete.

Implementation was authorized after read-only package review and then limited
to the active package's test/evidence surfaces. Current validation passed with
one non-blocking P3 around a stale unreferenced screenshot file in the latest
Agent smoke evidence directory.
