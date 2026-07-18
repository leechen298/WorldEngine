# 0.13.0 WorldEngine Runnable Anchor

Chinese mirror: `README.zh.md`.

Status: closed / WorldEngine-side anchor verified
Type: mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## Goal

Implement one deterministic WorldEngine-side vertical slice that can generate
a runnable world package, boot one session, advance exact lockstep ticks, run
one Agent through a causal action loop, judge one accepted and one rejected
operator intervention, expose a generic client projection, and operate the
whole flow through the project administration console.

The package proves the core is runnable. It does not claim complete MVP PASS;
Godot and the external checker remain required v0.13 packages.

## Scope

After review approval this package may add:

- a versioned generic control/runtime/evidence HTTP contract.
- deterministic world-package generation from structured input and fixed seed.
- package readiness validation and immutable `package_hash`.
- process-local session boot and lockstep `step N` execution.
- monotonic event sequence, tick, revision, snapshot, and `state_hash` evidence.
- one WorldEngine-owned Agent perception/decision/action/result loop.
- a bounded public experience link that affects a later Agent decision.
- explicit tick-boundary intervention windows with accepted and rejected
  outcomes.
- generic action and feedback request boundaries for future clients.
- a work-focused administration console that uses only the public/control API.
- focused backend, frontend, and E2E tests.

## Deliverables

- Public capability manifest and versioned API schemas.
- Deterministic `RunnableWorldPackage` and readiness result.
- Runnable session state, event/diff/snapshot spine, and public projection.
- Agent causal-chain evidence and prior-experience-linked later decision.
- Accepted and rejected intervention evidence from the same open window.
- Administration console for generation, session control, Agent inspection,
  intervention, timeline, and evidence export.
- Generic black-box protocol tests and review evidence.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Status Checklist

- [x] Documents drafted
- [x] User review complete
- [x] Documentation/contract evaluator PASS
- [x] Implementation authorized
- [x] Implementation complete
- [x] Focused verification complete
- [x] Independent review checkpoints complete
- [x] Package closeout complete

## Current Assessment

The WorldEngine-side anchor is implemented and closed after focused backend,
frontend, E2E, black-box, real-browser, code-review, validation-evidence, and
closeout-consistency gates. The full backend run remains honestly recorded as
`484 passed, 1 failed` because of an unrelated dirty legacy manifest/test
mismatch; no clean repository-wide PASS is claimed. Complete v0.13, Godot, and
the external checker remain unexecuted later-package work.
