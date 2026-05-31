# Contract

## Public Concepts

- `PerceptionFrame`: bounded agent-facing input assembled from runtime state, recent events, world params, and optional runtime context summary. It must not persist memory or infer self-continuity.
- `ActionIntent`: an inspectable requested action from an agent loop step. v0.4 allows only the reviewed minimal action vocabulary.
- `ActionResult`: the accepted, rejected, or no-op outcome of validating and applying an action intent.
- `LoopStep`: one request-scoped perceive -> intent -> validate/apply -> result cycle. It is not background autonomy.

## Allowed Changes

- Add request-driven loop service under approved `backend/app/` modules.
- Extend existing agent-loop schemas additively for loop step request/response models.
- Add one reviewed API route only if contract-authorized.
- Register/wire the loop service through the backend app factory and route dependency state.
- Use deterministic providers or explicit test intents for tests.
- Add focused service/API tests and adjacent compatibility checks.

## Forbidden Changes

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.
- Do not replace or break `/world/agent/params/propose-and-apply`.

## Compatibility Requirements

- `RuntimeEngine` tick and `world_time_seconds` behavior must remain compatible unless the active child explicitly changes it.
- API envelope and error shape must remain compatible.
- `/runtime/state`, `/runtime/step`, `/world/events`, and `/world/event-steps` are compatibility-sensitive.
- World params, params apply behavior, existing ParamsAgent endpoint, archive behavior, and Event.refs optional serialization are compatibility-sensitive.
- Schema changes must be additive unless the active contract explicitly allows a breaking change.

## Implementation Authorization

Implementation authorization is closed until this package records all review gates required by `GOAL_RUNNER.md`. For documentation-only packages, authorization remains limited to documentation changes. For mixed or code packages, `review.md` must record `implementation_authorized: yes` only after the required documentation/contract evaluator reports no blocking findings.

## Out-of-Scope Follow-ups

- v0.5 memory and self-continuity substrate.
- v0.6 world generation.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
- concrete product, game, or validation-world behavior.
