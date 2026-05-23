# Technical Design

## Source of Truth

The repository-owned skill source remains:

```text
.agents/skills/<skill-name>/SKILL.md
```

No separate plugin is introduced. A plugin would be useful only if WorldEngine
later needs marketplace distribution, bundled MCP tools, hooks, apps, or
cross-repository packaging.

## Skill Names

```text
.agents/skills/worldengine-iteration-docs/SKILL.md
.agents/skills/worldengine-iteration-dev/SKILL.md
.agents/skills/worldengine-e2e-runner/SKILL.md
.agents/skills/worldengine-agent-smoke-runner/SKILL.md
.agents/skills/worldengine-agent-autonomous-test-runner/SKILL.md
```

## `worldengine-iteration-docs`

Purpose: documentation-stage workflow.

The skill should trigger when a user asks to create, update, review, or prepare
WorldEngine iteration packages, roadmap/process docs, workflow governance docs,
or package review evidence before implementation.

Core behavior:

- confirm repository state with `git status --short --branch`.
- read `AGENTS.md`, `CLAUDE.md` or `CLAUDE.zh.md`, `docs/project-north-star.md`,
  `docs/product-model.md`, `docs/scope-boundaries.md`,
  `docs/roadmap.md`, and `docs/iterations/README.md` as needed.
- classify work as documentation-only, code, or mixed.
- for code or mixed work, draft the full package set:
  `README.md`, `intent.md`, `contract.md`, `technical-design.md`,
  `test-plan.md`, `plan.md`, and `review.md`.
- keep implementation files untouched.
- leave `review.md` in a pre-implementation state until implementation actually
  runs.
- tell the user which docs need review before implementation can start.

## `worldengine-iteration-dev`

Purpose: implementation-stage workflow.

The skill should trigger when a user asks to implement a reviewed WorldEngine
code or mixed iteration package.

Core behavior:

- confirm repository state with `git status --short --branch`.
- read root agent guidance and the active iteration package in this order:
  `README.md`, `intent.md`, `contract.md`, `technical-design.md`,
  `test-plan.md`, `plan.md`, `review.md`.
- verify that the required package exists and is reviewed/approved enough to
  implement.
- keep iteration and planning documents read-only during implementation.
- implement only the approved package scope.
- run verification from `test-plan.md` or explicitly approved package entry
  points.
- report changed files, commands, exit codes, pass/fail counts, unrun items, and
  residual risks in the final response.
- update `review.md` only when the user explicitly asks for closeout or the
  active package contract says implementation closeout includes writing review
  evidence.

If required docs are missing, stale, conflicting, or not reviewed, the skill
must stop and report the blocker. It must not patch docs and continue coding in
the same implementation flow.

## `worldengine-agent-smoke-runner`

Purpose: basic Agent smoke workflow.

This existing skill should remain scoped to the current
`docs/testing/agent-smoke/` protocol. It is an agent-assisted exploratory smoke
check with deterministic validation, not a general Agent autonomous testing
workflow.

The implementation must preserve:

- UI or CLI operation logging only.
- `operation-log.jsonl` as the raw operation record.
- no direct API calls recorded as Agent operations.
- PASS only from `make validate-agent-smoke-result RESULT_DIR=<run-dir>`.

## `worldengine-agent-autonomous-test-runner`

Purpose: broader Agent autonomous test execution workflow.

The skill should trigger when a user asks to run, validate, or report an Agent
autonomous test that is broader than smoke, such as scenario suites,
scorecard-based runs, longer autonomous dashboard tasks, or future agent
runtime evaluation packages.

Core behavior:

- confirm repository state with `git status --short --branch`.
- locate the authoritative scenario, protocol, or test-plan document for the
  requested autonomous test.
- distinguish between fixture/checker validation, live autonomous execution,
  and UI smoke.
- run only documented entry points.
- capture run id or result directory, verdict source, scorecard or checker
  status when available, operation log, transcript/log paths, screenshots or
  artifacts, and unverified items.
- if no broader autonomous test contract exists, stop and report that only
  Agent smoke is currently defined.

This skill must not treat `worldengine-agent-smoke-runner` evidence as full
Agent autonomous test coverage.

## Project Skill Validation

Update the existing skill helper, or replace it with a project-only validator,
so it checks the five repository-owned skills without copying them into personal
skills by default:

```python
PROJECT_SKILLS = (
    "worldengine-iteration-docs",
    "worldengine-iteration-dev",
    "worldengine-e2e-runner",
    "worldengine-agent-smoke-runner",
    "worldengine-agent-autonomous-test-runner",
)
```

`make validate-codex-skills` remains the command surface for checking project
skills.

`make sync-codex-skills` should be removed or deprecated so a normal project
validation run does not recreate duplicate `worldengine-*` entries under
`~/.agents/skills`.

If a user explicitly asks for a one-off local copy in the future, that should be
a separate opt-in command and must report that it will create personal skill
duplicates.

## Entry Guidance

If implementation shows that agents do not discover the project-owned workflow
skills reliably, add a short "Project Workflow Skills" section to root agent
guidance. The section should point to the four skill names and preserve the
two-stage gate.

## Test Matrix

| Area | Required evidence |
|---|---|
| Skill structure | `quick_validate.py` passes for all five skills. |
| Project validation | `make validate-codex-skills` lists all five project skills and exits `0`. |
| Personal copies | No `~/.agents/skills/worldengine-*` directories are created by default validation. |
| Existing skills | E2E and Agent smoke skill files preserve deterministic evidence rules, and smoke remains clearly basic. |
| Autonomous tests | Broader Agent autonomous runner stops when no explicit autonomous scenario/protocol exists. |
| Scope | `git diff --name-only` shows no backend, frontend, runtime fixture, or validator changes. |
