# 0.4.1 Agent-in-World Loop Contract

Status: planned
Type: documentation-only

## Goal

Define the public v0.4 Agent-in-World loop concepts, event semantics, API boundary, error model, and implementation authorization criteria before code changes.

## Scope

Define PerceptionFrame, ActionIntent, ActionResult, and loop-step semantics.

Allowed changes:

- Define `PerceptionFrame`, `ActionIntent`, `ActionResult`, and `LoopStep` semantics.
- Define event and error model contracts as documentation only.
- Define allowed action vocabulary: `noop` and validated `params.patch`.
- Define API boundary without adding a route in this package.

Forbidden changes:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

## Deliverables

- Complete package docs and Chinese mirrors.
- Documentation-only verification and rationale for not running code tests.
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
- [ ] Contract reviewed
- [ ] Technical design reviewed
- [ ] Test plan reviewed
- [ ] Implementation authorized, when applicable
- [ ] Implementation complete, when applicable
- [ ] Tests/evidence complete
- [ ] Review complete

## Final Assessment State

Current value: `planned`.
