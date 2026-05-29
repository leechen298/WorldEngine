# Contract

## Public Concepts

- Post-closeout validation: independent evidence gathered after v0.3 closeout.
- E2E availability: whether a runnable browser E2E setup exists in the current
  checkout and environment.
- Fallback validation: API smoke plus backend integration tests when E2E is
  not configured or cannot run.
- Loader validation: focused checks for `load_worldspec`.
- Runtime context bridge validation: focused checks for `build_runtime_context`
  and inert `RuntimeEngine` context storage.
- Event.refs compatibility: response compatibility for empty and non-empty
  refs across event APIs.

## Allowed Changes

- Create and update planning docs in this package.
- Define commands and expected evidence for future execution.
- Define fallback and blocker rules.
- Define release-claim and compatibility-claim checks.

## Forbidden Changes

- Do not execute validation commands in this package.
- Do not change runtime, schema, API, frontend, backend tests, fixtures, or
  migrations.
- Do not create external repositories.
- Do not include concrete demo-world details, UI selectors, seed data, or
  private oracle details.
- Do not alter v0.3 release status.
- Do not state that E2E, integration, loader, bridge, API smoke, or backend
  validation already succeeded.

## Compatibility Requirements

The plan must preserve:

- v0.3 final / closeout complete status.
- loader and bridge boundaries as generic engine infrastructure.
- `RuntimeEngine` tick and `world_time_seconds` compatibility.
- Event.refs response compatibility.
- external fixture boundary and redacted evidence policy.

## Out-Of-Scope Follow-Ups

- Actual validation execution belongs to `02-e2e-validation-execution`.
- Independent Codex review planning belongs to `03-codex-autonomous-validation-plan`.
- Final synthesis belongs to `05-final-validation-bundle`.
- Any repair work requires a separate reviewed package.
