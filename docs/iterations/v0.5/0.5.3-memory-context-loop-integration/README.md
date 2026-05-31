# 0.5.3 Memory Context Loop Integration

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Add bounded read-only memory context into the Agent Loop perception path using
the `0.5.2` in-memory substrate, without changing action semantics.

The integration must be additive: existing loop requests continue to work,
existing action types and result behavior stay unchanged, and memory context is
visible only as read-only perception data.

## Scope

Allowed:

- add an additive memory context schema field to `PerceptionFrame`.
- extend `PerceptionBuilder` to optionally read bounded memory context from
  the in-memory substrate.
- wire the in-memory store into the backend app only as an internal dependency
  needed for perception context.
- add focused perception/loop/API compatibility tests.
- update package docs and Chinese mirrors.

Forbidden:

- do not modify `ActionIntent`, `ActionResult`, accepted action types, action
  adapter behavior, or `params.patch` semantics.
- do not add public memory APIs or loop request fields.
- do not make memory write during a loop step.
- do not implement relationship behavior, self-summary generation, automatic
  reflection, personality drift action modifiers, durable persistence,
  migrations, frontend behavior, concrete world content, or private validation
  oracle details.
- do not modify `backend/worldengine/`.

## Deliverables

- Additive perception memory context schema.
- Read-only bounded memory context assembly in the perception path.
- Focused tests proving old loop requests remain compatible, memory context is
  bounded and copied, and action semantics are unchanged.
- Review evidence with required evaluator checkpoints.

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

Documentation/contract gate passed and implementation is authorized.
Implementation must start with the required TDD red run before production code
changes.
