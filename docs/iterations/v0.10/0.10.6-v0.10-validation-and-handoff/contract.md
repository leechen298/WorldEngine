# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- **Runnable session MVP slice**: the reviewed v0.10 surface where a user can
  create a public session from worldview input, run bounded ticks, inspect
  timeline/snapshot evidence, and use dashboard controls.
- **Closeout result**: one of `PASS`, `PARTIAL`, `BLOCKED`, or `FAIL`, backed
  only by current-session evidence.
- **Handoff to v0.11**: documentation state that lets v0.11 begin rule-bound
  world evolution from the runnable session slice; it is not v0.11
  implementation.

## Allowed Changes

- Run and record validation commands listed in `test-plan.md`.
- Inspect public manifest/discovery output.
- Update this package's review and parent v0.10 closeout/handoff docs.
- Mark v0.11 as the next campaign route only through status/handoff docs.
- Record a narrowly scoped defect repair only if validation reveals an
  in-scope P1/P2 defect and the repair stays inside the reviewed v0.10
  contract.

## Forbidden Changes

- No new runtime, API, schema, frontend, provider, checker, fixture,
  Validation Client, persistence, migration, or `backend/worldengine/`
  implementation unless a reviewed P1/P2 defect repair is recorded first.
- No live provider calls.
- No external Validation Client execution or automated PASS claim.
- No v0.11 or v0.12 feature implementation.
- No Agent autonomy claim.

## Compatibility Requirements

- Existing v0.10 public API and dashboard behavior must remain compatible with
  the evidence recorded by 0.10.1 through 0.10.5.
- Existing backend and frontend tests remain authoritative for their reviewed
  scope.
- v0.10 closeout must not rename replay/worldline branches into parent/source
  world semantics.

## Out-of-Scope Follow-Ups

- Rule-bound world evolution belongs to v0.11.
- Agent continuity and pseudo-self formation belong to v0.12.
- External Validation Client automation remains outside WorldEngine.
- Provider-backed quality validation requires a later provider/live evidence
  gate.

## Validation Contract

Run and record current-session evidence for:

- focused backend session/public handoff/bounded runtime tests.
- frontend unit tests.
- frontend build.
- targeted dashboard E2E.
- public manifest/discovery inspection.
- `git diff --check`.

If a command cannot run because of environment/sandbox/server limitations,
record the exact failure and classify the package as PARTIAL or BLOCKED unless
an approved rerun resolves it.

## Closeout Contract

The package must produce one of:

- `PASS`: v0.10 runnable session MVP slice is evidenced for reviewed scope.
- `PARTIAL`: core slice works, but a non-core or environment-limited evidence
  item is missing.
- `BLOCKED`: an external environment/permission/tool/provider limitation
  prevents required evidence.
- `FAIL`: in-scope evidence ran and found an unresolved defect.

## Handoff Contract

If v0.10 closes PASS or acceptable PARTIAL, v0.11 may start from a runnable
session and add rule-bound world evolution. Agent continuity remains v0.12
scope.

## Forbidden Claims

Do not claim:

- live provider quality PASS.
- external Validation Client automated PASS.
- Agent autonomy.
- durable persistence.
- v0.11 rule evolution implemented.
- v0.12 Agent continuity implemented.
