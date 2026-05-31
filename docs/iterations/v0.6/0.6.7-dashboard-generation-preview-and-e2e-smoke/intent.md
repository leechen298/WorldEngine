# Intent

Status: review complete

## Problem

`0.6.6` exposes stable backend/API semantics for generation preview,
regeneration, and loader/runtime-context readiness. v0.6 still needs a
dashboard-facing way to exercise those APIs and a browser smoke test proving
the operator workflow is visible and wired end to end.

## Goals

- Add a focused dashboard generation preview workflow using existing backend
  generation routes.
- Keep the workflow generic and inspectable, without concrete world content or
  hidden provider behavior.
- Show validation status, bounded metadata, preview summary, diagnostics, and
  runtime-readiness status without leaking raw prompts or private provenance.
- Preserve existing dashboard runtime, timeline, world-params, agent, memory,
  backend API, and E2E behavior.
- Add focused frontend and E2E evidence for the dashboard preview smoke.

## Non-Goals

- No backend generation API redesign.
- No full editor, template catalog UI, persistence, save/publish/install flow,
  runtime activation, or projection application.
- No live AI provider behavior or prompt execution.
- No external validation readiness, product readiness, release readiness,
  generation-quality approval, Agent smoke, or autonomous validation claim.

## North Star Alignment

This package makes generated worlds inspectable through the dashboard while
keeping the engine boundary generic. It proves the preview loop is operable
without promoting generated worlds into live runtime state.

## Handoff

When complete, `0.6.8-v0.6-evidence-and-compatibility-audit` receives
dashboard preview and E2E smoke evidence for the v0.6 audit package.
