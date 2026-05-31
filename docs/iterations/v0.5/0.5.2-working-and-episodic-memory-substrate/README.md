# 0.5.2 Working And Episodic Memory Substrate

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Implement the first additive generic working-memory and episodic-memory
substrate for WorldEngine agents.

The implementation is intentionally non-public and in-memory only. It adds
generic schemas, a small in-memory substrate service/store, and focused
backend tests. It does not add public APIs, loop integration, persistence,
frontend behavior, relationship behavior, self-summary generation,
reflection, or personality drift behavior.

## Scope

Allowed:

- add `backend/app/schemas/agent_memory.py`.
- add `backend/app/agent/memory.py`.
- add focused backend tests under `backend/app/tests/test_agent_memory_*.py`.
- update this package's docs, review evidence, and Chinese mirrors.
- run focused backend memory tests and adjacent v0.4 loop/perception/API
  compatibility tests.

Forbidden:

- do not modify `backend/worldengine/`.
- do not add public runtime APIs or routes.
- do not integrate memory into `POST /world/agent/loop/step`; `0.5.3` owns
  that scope.
- do not modify `ActionIntent`, `ActionResult`, accepted action types, or
  `params.patch` semantics.
- do not implement relationship behavior, self-summary generation, automatic
  reflection, personality drift action modifiers, durable persistence,
  migrations, frontend behavior, concrete world content, or private validation
  oracle details.

## Deliverables

- Additive working-memory and episodic-memory schema models.
- Generic in-memory memory substrate/store.
- Focused backend tests proving schema semantics, bounded working-memory
  selection, episodic event references, copy isolation, and generic scoping by
  `agent_id`/`world_id`.
- Adjacent compatibility evidence for existing Agent Loop and perception
  behavior.
- Review evidence with documentation/contract evaluator, TDD red/green
  evidence, implementation-scope evaluator, code-review evaluator,
  validation-evidence evaluator, and closeout consistency evaluator.

## Documents

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## Current Assessment

This package is review complete. The memory substrate implementation stayed
inside the approved new schema/store/test files, and focused plus adjacent
compatibility evidence is recorded in `review.md`.
