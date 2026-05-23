# Intent

## Problem

0.1.6 defined current-code E2E and Agent smoke scenario contracts, but two
Agent smoke scenarios are still not executable:

- `dashboard-params-flow`
- `dashboard-invalid-param`

The blocker is not product behavior. The blocker is test infrastructure:
missing stable selectors for future UI assertions, a validator that only
accepts `dashboard-basic-runtime`, a result schema pinned to one scenario, and
no deterministic helper that can produce or verify `api-summary.json` for live
Agent smoke.

Without this package, a later live Agent smoke run would either fail validator
support or risk letting Codex hand-author API evidence.

## Goal

After this package is implemented and reviewed:

- dashboard selectors exist for Auto-Tune, MemoryPanel, and timeline expanded
  details.
- the Agent smoke validator supports three scenarios:
  `dashboard-basic-runtime`, `dashboard-params-flow`, and
  `dashboard-invalid-param`.
- the Agent smoke result schema accepts the same three scenarios.
- valid and invalid validator fixtures cover the new scenario branches.
- project tooling can generate deterministic API checker artifacts for live
  Agent smoke instead of relying on handwritten `api-summary.json`.
- `dashboard-params-flow` and `dashboard-invalid-param` can be marked
  validator-supported, with no live run recorded yet.

## Non-goals

- Do not run live Agent smoke.
- Do not create or update live smoke result artifacts under
  `test-results/agent-smoke/latest/`.
- Do not implement `dashboard-archive-summary` E2E.
- Do not run Codex/test-runner autonomous scenarios.
- Do not add API curl smoke.
- Do not change runtime, API, product, schema, or dashboard user-visible
  behavior.
- Do not modify `backend/worldengine/`.
- Do not start 0.1.8 implementation or execution.

## Why Now

0.1.6 closed the current-code test map. The next safe step is to make the
documented Agent smoke contracts mechanically executable before any agent tries
to run and report live smoke evidence.

This package is the bridge from "scenario contract exists" to "validator can
accept deterministic evidence."

## North Star Alignment

WorldEngine needs reliable evidence for runtime projection behavior before it
can evolve toward recursive worlds and agent continuity. This package improves
test observability and evidence quality for the dashboard projection without
turning WorldEngine into a game-specific backend or expanding product scope.
