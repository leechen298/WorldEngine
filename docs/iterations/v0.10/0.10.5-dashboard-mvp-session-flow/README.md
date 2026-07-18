# 0.10.5 Dashboard MVP Session Flow

Chinese mirror: `README.zh.md`.

Status: final / focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Rework the existing dashboard into a compact MVP session flow for creating a
session from worldview input, running bounded session ticks, and inspecting
timeline/snapshot evidence.

This package makes the existing backend session APIs usable by a human through
the dashboard. It does not turn the dashboard into world simulation authority
and does not add provider key management or concrete demo assets.

## Scope

Allowed after review:

- Add frontend API client methods and types for session create-from-worldview,
  session run, pause, resume, status, and snapshots.
- Update the dashboard to show an MVP session shell with worldview input,
  session status, bounded run controls, timeline refresh, and snapshot
  evidence.
- Reuse existing panels where practical and keep existing runtime/world panels
  available unless intentionally integrated.
- Add focused frontend unit tests and targeted dashboard E2E smoke.
- Run frontend unit/build/E2E commands as available, plus backend focused
  tests needed by UI behavior.

Allowed files:

- `frontend/src/api/client.ts`
- `frontend/src/api/client.test.ts`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/pages/DashboardPage.test.ts`
- `frontend/src/components/RuntimeControls.vue`
- `frontend/src/components/RuntimeControls.test.ts`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/src/style.css`
- package and parent v0.10 docs/reviews.

Forbidden:

- No polished game art or concrete demo assets.
- No provider key UI or live provider execution.
- No Validation Client code.
- No checker fixture implementation.
- No durable persistence or migration.
- No raw prompt/response/provider trace display.
- No `backend/worldengine/` changes.

## Deliverables

- Reviewed package docs and mirrors.
- Dashboard MVP session create/run/inspect flow.
- Frontend API client coverage.
- Unit tests and targeted E2E smoke evidence.
- Review evidence and handoff to v0.10 validation.

## Status Checklist

- [x] Package documents drafted.
- [x] Documentation / contract evaluator complete.
- [x] Implementation authorized.
- [x] Implementation complete.
- [x] Focused verification complete.
- [x] Evaluator closeout complete.
- [x] Review evidence updated.

## Final Assessment State

Current value: `PASS`.
