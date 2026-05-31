# Product Capability Validation Playbook

Status: reusable validation guide

Chinese mirror: `product-capability-validation-playbook.zh.md`.

This playbook standardizes the post-closeout validation pattern used after
v0.4 and makes it reusable for later versions. It is version-agnostic: each
version or package must still define its own scope, commands, evidence, and
PASS criteria.

## When To Use

Use this playbook when a user asks whether a version, release candidate, or
current product state is really validated, ready, clean, or passing.

Examples:

```text
/goal 测试 <version>
/goal 验证 <version> 是否达到 clean pass
/goal 测试 <iteration-package>
/goal 对当前产品能力做完整验证
/goal run post-closeout validation for vX.Y
```

A one-line request is a valid trigger. A one-line verdict is valid only after
current-session evidence proves it.

## Non-Negotiable Rules

- Read `AGENTS.md`, `docs/iterations/README.md`, and the active version or
  package documents before claiming scope.
- Do not claim tests passed unless the command or checker ran in the current
  work session, or a durable result file explicitly records the current
  session evidence being relied on.
- Do not use Agent observation, manual observation, or a plan as a PASS source.
- Do not repair product code inside a validation package unless the package
  explicitly authorizes repair.
- Do not widen a version into future roadmap scope.
- If a check is out of scope, skipped, blocked, or absent, say so directly.

## Package Requirement

If validation will add or change tests, checker code, fixtures, result schema,
product code, runtime behavior, API behavior, or frontend behavior, create a
mixed or code iteration package before implementation.

If validation only audits existing evidence and updates documentation, a
documentation-only package may be enough, but it must still record the no-code
boundary and no-test rationale where applicable.

## Capability Matrix

Every full product capability validation must produce or update a matrix that
covers at least:

- version and scope boundaries.
- core user paths.
- API/backend behavior.
- backend and frontend unit test coverage.
- frontend pages and interactions.
- data state changes, events, logs, persistence, and evidence surfaces.
- invalid inputs, permission boundaries, limits, and failure paths.
- E2E scenarios and gaps.
- Agent smoke scenarios and deterministic checker support.
- Codex/test-runner autonomous scenarios, saved-result checker support, and
  whether a broad autonomous runner exists.
- existing test coverage and missing coverage.

## Command Profile

The exact commands are version-specific. A product-level clean-pass profile
normally includes:

```bash
make check-backend
make check-frontend
cd backend && .venv/bin/python -m pytest <version-focused-unit-tests> -q
cd backend && .venv/bin/python -m pytest app/tests tests -q
cd frontend && pnpm test
cd frontend && pnpm build
make test-e2e
make validate-agent-smoke-fixtures
make validate-agent-smoke-result RESULT_DIR=<smoke-result-dir>
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=<autonomous-result-dir>
git diff --check
```

Version-specific backend focused tests should be added before the broad backend
regression. If frontend code is in scope, include focused frontend unit tests
or the full frontend unit suite before build and E2E. Documentation-only
packages should not pretend to run this profile; they should record that
product-level validation was not in scope.

## Unit Test Evidence

Unit tests are required for product-level validation when the version or
package includes backend logic, frontend logic, schemas, adapters, validators,
or test/checker tooling.

Record:

- focused unit-test commands tied to the version or package risk.
- broad backend unit/regression command results.
- frontend unit-test command results when frontend code or dashboard behavior
  is in scope.
- test file count or pass/fail count when the runner reports it.

Do not use E2E, Agent smoke, or autonomous checker results as a substitute for
unit tests when unit-testable logic changed.

## E2E Evidence

E2E PASS requires explicit assertions, not only successful navigation. For
state-changing flows, cross-check at least two evidence surfaces when possible:

- UI result.
- API state.
- event or log evidence.
- artifact or report output.

Record the command, exit code, pass/fail count, and report or artifact paths.

## Agent Test Categories

Keep these categories separate:

- Agent smoke: the Agent operates UI/CLI, and PASS/FAIL comes from a
  deterministic checker.
- Minimal autonomous saved-result validation: a result directory is checked by
  a deterministic or scorecard checker.
- Full autonomous runner/full suite: an autonomous runner plans and executes
  multi-step tasks and a scorecard/checker judges the result.
- Manual observation: useful supporting evidence, never a PASS source.

Do not describe Agent smoke or saved-result validation as full autonomous.

## Required Evidence Artifacts

A full validation closeout should record:

- scenario or capability matrix.
- command table with exit code and pass/fail counts.
- focused and broad unit-test results.
- artifact paths.
- result directories.
- operation logs for Agent tests.
- `result.json` for Agent smoke or autonomous saved-result validation.
- checker command used for PASS/FAIL.
- subagent or evaluator findings when the goal or package requires them.
- P1/P2/P3 unresolved findings.
- final verdict: `clean pass`, `partial pass`, `failed`, or `blocked`.

Durable summaries belong in `docs/testing/results/`.

## Verdict Rules

Use `clean pass` only when all required in-scope commands and checkers pass.

Use `partial pass` when some meaningful required surfaces pass but at least one
required in-scope check fails, is blocked, or is missing.

Use `failed` when core required behavior is contradicted by evidence.

Use `blocked` only when validation cannot proceed and the blocker is recorded
with exact reproduction evidence.

For future-scope or intentionally skipped checks, say `out of scope` or
`skipped`, not `passed`.

## One-Line Validation Requests

The project may accept a one-line request such as:

```text
/goal 验证 <version> 是否达到 clean pass
```

That sentence starts this playbook. It does not complete it.

The final response may be short only after the evidence already exists or has
just been produced. A safe one-line final verdict must still cite the evidence
source, for example:

```text
<version> clean pass is verified by its iteration review and the current-session command matrix recorded there.
```

If the evidence does not cover frontend, E2E, Agent smoke, autonomous, external
validation, or product readiness, the final verdict must name those exclusions.
