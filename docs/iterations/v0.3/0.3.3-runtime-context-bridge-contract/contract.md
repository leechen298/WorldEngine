# Contract

## Public Concepts

- `RuntimeContextBridge`: future boundary that derives optional runtime
  context from validated loader output.
- `RuntimeContextInput`: successful `LoadedWorldSpec` or reviewed equivalent.
- `RuntimeContext`: optional, inert runtime context derived from generic
  `WorldSpec` data.
- `RuntimeContextSummary`: small diagnostic view for tests and review
  evidence.
- `RuntimeContextBridgeError`: structured bridge error.

The normative public contract is
`docs/contracts/runtime-context-bridge-contract.md`.

## Compatibility Constraints

- Existing runtime tick, `world_time_seconds`, `step_seconds`, and
  `updated_at` behavior must stay compatible.
- Existing API response envelopes and error shapes must stay compatible.
- Existing event, archive, params, frontend-facing, fixture, migration, and
  legacy path behavior must stay compatible.
- Existing `WorldSpec`, `WorldCell`, loader, and event schema behavior must be
  preserved.
- Schema changes are forbidden in this package.
- Runtime context must remain optional and inert until a later reviewed
  implementation proves otherwise.

## Allowed Changes

- Add `docs/contracts/runtime-context-bridge-contract.md`.
- Create the 0.3.3 package documentation and Chinese mirrors.
- Update the v0.3 milestone index and mirrors to mark 0.3.3 `ready for
  review` / `待评审`.
- Update the v0.3 package plan and mirrors only for 0.3.3 status consistency.
- Define bridge input, context shape, error, compatibility, and evidence
  semantics.
- Record documentation-stage verification evidence in `review.md`.

## Forbidden Changes

- Do not implement bridge code.
- Do not modify `RuntimeEngine`, event bus, world modules, API routes,
  schemas, tests, fixtures, migrations, frontend, archive, params,
  persistence, or legacy `backend/worldengine/` implementation files.
- Do not add API response fields or event payload fields.
- Do not place raw `WorldSpec` into event payloads.
- Do not map `WorldCell` directly to runtime modules.
- Do not create concrete world logic, concrete fixtures, or external
  validation-world internals.
- Do not implement world generation, Agent-in-World loop, memory,
  self-continuity, projection, story generation, or NPC chat behavior.

## Acceptance Requirements

- The bridge contract explicitly states accepted input.
- The bridge contract explicitly states derived runtime context fields.
- The bridge contract states that runtime context is optional and inert.
- The bridge contract preserves tick, world time, event log, params, archive,
  API, frontend-facing, and legacy behavior.
- The bridge contract states that `WorldCell` is not automatically a runtime
  module.
- The bridge contract forbids raw `WorldSpec` event payloads and unreviewed API
  exposure.
- The bridge contract includes structured error categories.
- The package documents include assumptions, open risks, verification
  commands, and docs-only no-test rationale.
- English and Chinese milestone mirrors keep the 0.3.3 status synchronized.

## North Star Check

This package keeps WorldEngine generic. It defines an engine-level bridge
boundary for validated world specification data and explicitly forbids
demo-specific backend behavior, external validation-world internals, and
agent or generation behavior.

## Out-of-Scope Follow-ups

- `0.3.4` may implement the minimal optional runtime context bridge after this
  package is reviewed.
- `0.3.5` may define external fixture contract readiness without adding
  external repositories inside core.
- Later milestones may implement runtime module mapping, Agent loops, memory,
  self-continuity, generation, projection, and external product validation.
