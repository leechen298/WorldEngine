# Technical Design

## Documentation Or Implementation Structure

Establish deterministic docs and keep implementation authorization closed.

For code or mixed packages, implementation must stay in `backend/app/` unless this package contract explicitly widens the scope. New runtime features must not be added under `backend/worldengine/`.

## Affected Files

Allowed file classes for this package:

- Create `docs/iterations/v0.4/**` parent and child documentation.
- Define goal entry `完成 v0.4`.
- Define subagent/evaluator checkpoints and package sequence.
- Record v0.3 post-closeout evidence as handoff context only.

Explicitly out of scope:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

## Data / Control Flow

The v0.4 loop direction is:

1. Build a bounded `PerceptionFrame` from runtime state, recent events, current params, and optional runtime context summary.
2. Produce or accept an `ActionIntent` inside a request-scoped loop step.
3. Validate the intent against the minimal action vocabulary.
4. For `noop`, return a no-effect `ActionResult`.
5. For `params.patch`, convert to `ParamPatchItem`, run static validation, run dry-run validation, and apply only if validation succeeds.
6. Emit or return inspectable result evidence only as authorized by the active package contract.

This package may implement only the subset explicitly allowed in its contract. Later steps in the sequence remain planned until their own packages are reviewed.

## Compatibility Strategy

- `RuntimeEngine` tick and `world_time_seconds` behavior must remain compatible unless the active child explicitly changes it.
- API envelope and error shape must remain compatible.
- `/runtime/state`, `/runtime/step`, `/world/events`, and `/world/event-steps` are compatibility-sensitive.
- World params, params apply behavior, existing ParamsAgent endpoint, archive behavior, and Event.refs optional serialization are compatibility-sensitive.
- Schema changes must be additive unless the active contract explicitly allows a breaking change.

## Anti-Drift Rules

- Stop when a required evaluator checkpoint is missing.
- Stop on P1 or unresolved P2 findings.
- Stop and record a blocker when required file classes are not authorized by the active contract.
- Do not treat historical evidence as current-session pass evidence.
