# Technical Design

## Documentation Or Implementation Structure

Connect the minimal loop and reviewed API boundary without background autonomy.

For code or mixed packages, implementation must stay in `backend/app/` unless this package contract explicitly widens the scope. New runtime features must not be added under `backend/worldengine/`.

## Affected Files

Allowed file classes for this package:

- Add request-driven loop service under approved `backend/app/` modules.
- Extend existing agent-loop schemas additively for loop step request/response models.
- Add one reviewed API route only if contract-authorized.
- Register/wire the loop service through the backend app factory and route dependency state.
- Use deterministic providers or explicit test intents for tests.
- Add focused service/API tests and adjacent compatibility checks.

Explicitly out of scope:

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.
- Do not replace or break `/world/agent/params/propose-and-apply`.

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
