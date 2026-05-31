# 0.4.4 Minimal Agent Loop Orchestration And API

Status: review complete
Type: mixed or code

## Goal

Wire a request-driven minimal Agent-in-World loop that builds perception, obtains or accepts an intent, validates and applies the intent, emits inspectable result evidence, and returns a stable API response.

## Scope

Connect the minimal loop and reviewed API boundary without background autonomy.

Allowed changes:

- Add request-driven loop service under approved `backend/app/` modules.
- Extend existing agent-loop schemas additively for loop step request/response models.
- Add one reviewed API route only if contract-authorized.
- Register/wire the loop service through the backend app factory and route dependency state.
- Use deterministic providers or explicit test intents for tests.
- Add focused service/API tests and adjacent compatibility checks.

Forbidden changes:

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.
- Do not replace or break `/world/agent/params/propose-and-apply`.

## Deliverables

- Complete package docs and Chinese mirrors.
- Focused test evidence, compatibility evidence, and required subagent/evaluator checkpoints when implemented.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

## Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

Chinese mirrors are required in this package and are created in the same documentation pass.

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Implementation authorized, when applicable
- [x] Implementation complete, when applicable
- [x] Tests/evidence complete
- [x] Review complete

## Final Assessment State

Current value: `review complete`.
