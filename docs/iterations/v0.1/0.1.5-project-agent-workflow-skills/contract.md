# Contract

## Public Semantics

This package adds project-local agent workflow guidance only. It must make the
WorldEngine workflow executable by AI coding agents while preserving runtime,
API, UI, schema, fixture, and product behavior.

## Required Skill Set

The repository-owned skill set must include:

- `worldengine-iteration-docs`
- `worldengine-iteration-dev`
- `worldengine-e2e-runner`
- `worldengine-agent-smoke-runner`
- `worldengine-agent-autonomous-test-runner`

## Role Boundaries

### Documentation skill

`worldengine-iteration-docs` may create or update iteration and governance
documents when the active request is documentation-stage work.

It must:

- read project direction and iteration standards before drafting.
- create the required package document set for code or mixed iterations.
- keep runtime, schema, API, UI, fixture, migration, and test implementation
  files untouched.
- leave the package in a reviewable state.
- report that implementation must wait for review and approval.

### Implementation skill

`worldengine-iteration-dev` may implement code or mixed packages only after the
iteration package is reviewed and approved.

It must:

- read the current iteration package before editing.
- treat approved `intent.md`, `contract.md`, `technical-design.md`,
  `test-plan.md`, and `plan.md` as the work contract.
- keep iteration and planning documents read-only during implementation.
- stop and report blockers if required docs are missing, stale, conflicting,
  or not reviewed.
- run only verification allowed by the package and report real evidence.

It must not:

- create, repair, reorder, rewrite, or delete iteration documents.
- silently reinterpret the contract.
- continue coding after discovering a design gap.
- claim E2E, UI smoke, CLI, runtime, or Agent smoke success without fresh
  current-session evidence.

### Basic Agent smoke skill

`worldengine-agent-smoke-runner` is limited to basic Agent smoke execution. It
must not be described or reported as full Agent autonomous testing.

It may:

- run the documented Agent smoke protocol.
- collect `operation-log.jsonl`, `result.json`, transcript, console, API
  summary, and screenshots required by `docs/testing/agent-smoke/`.
- report PASS only through `make validate-agent-smoke-result`.

### Agent autonomous test skill

`worldengine-agent-autonomous-test-runner` is the broader Agent autonomous test
execution workflow.

It may run only when the repository has explicit scenario, protocol, scorecard,
or test-plan documents for the target autonomous test.

It must:

- identify the authoritative scenario or test contract before running.
- distinguish live autonomous runs from fixture/checker validation.
- record invocation surface, run id or result directory, scorecard/verdict when
  available, raw evidence paths, and unverified items.
- stop if only Agent smoke exists for the requested scope.

It must not claim full autonomous test coverage from Agent smoke evidence.

## Allowed Changes

- Add `.agents/skills/worldengine-iteration-docs/SKILL.md`.
- Add `.agents/skills/worldengine-iteration-dev/SKILL.md`.
- Add `.agents/skills/worldengine-agent-autonomous-test-runner/SKILL.md`.
- Update `tools/testing/sync_codex_skills.py` or its replacement so it validates
  all repository-owned WorldEngine skills without copying them into personal
  skills by default.
- Remove or deprecate personal-skill sync command surfaces that would recreate
  duplicate `worldengine-*` entries in `~/.agents/skills`.
- Update `AGENTS.md`, `AGENTS.zh.md`, `CLAUDE.md`, and `CLAUDE.zh.md` only if
  needed to point agents to the project-owned workflow skills.
- Update v0.1 iteration index and plan documents.
- Update this package's `review.md` with actual implementation and validation
  evidence after implementation.

## Forbidden Changes

- Do not add a plugin package or marketplace entry in this package.
- Do not modify `backend/`.
- Do not modify `frontend/`.
- Do not modify runtime data fixtures.
- Do not modify E2E scenarios or Agent smoke validator behavior.
- Do not add broad Agent autonomous test scenarios without a separate iteration
  contract.
- Do not modify `backend/worldengine/`.
- Do not create or recreate personal `~/.agents/skills/worldengine-*` skill
  copies unless the user explicitly asks for that one-off local copy.

## Compatibility

The existing two skills must keep their current evidence semantics. The new
skills coordinate workflow stages; they must not replace deterministic test
commands or validators as sources of truth.

The project copy under `.agents/skills/` is the source of truth. Personal skill
copies are not part of the steady state for this repository.

## North Star Check

This package supports project governance only. It does not narrow WorldEngine
into a game-specific backend and does not add product capability.
