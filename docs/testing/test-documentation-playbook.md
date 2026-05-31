# Test Documentation Playbook

Status: reusable test-documentation guide

Chinese mirror: `test-documentation-playbook.zh.md`.

This playbook standardizes how agents write or update test documentation,
test plans, scenarios, and test cases for WorldEngine versions and iteration
packages. It is a documentation and design workflow; it does not by itself
prove tests passed.

Use `product-capability-validation-playbook.md` when the user asks to execute
validation and report a PASS/FAIL verdict.

## When To Use

Use this playbook when the user asks to write, supplement, organize, review, or
prepare testing documentation.

Examples:

```text
/goal 编写 <version> 测试方案
/goal 补充 <iteration-package> 测试文档
/goal 设计 <feature-or-scenario> 测试用例
/goal 为当前 package 写 E2E / Agent 测试场景
/goal 生成当前产品的测试矩阵和测试计划
```

A one-line request is a valid trigger. It starts this documentation workflow.
It does not mean validation has run or passed.

## Required Reading

Before drafting test documentation, read:

- `AGENTS.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- the active version/package `README.md`, `intent.md`, `contract.md`,
  `technical-design.md`, `test-plan.md`, `plan.md`, and `review.md` when they
  exist.
- relevant existing docs under `docs/testing/`.

## Package Boundary

If the request only writes or updates test documentation, keep it
documentation-only and record that no code tests were run unless explicitly
requested.

If the request will add or modify test code, checker code, fixtures, schemas,
runtime/API/frontend behavior, or result artifacts, use the repository
iteration package gate before implementation.

Do not write test documentation that implies product behavior was validated
unless validation was actually run and recorded.

## Required Outputs

Depending on the request scope, produce or update the relevant artifacts:

- test strategy or test approach.
- capability/test matrix.
- `test-plan.md` for the active iteration package.
- E2E scenario documents under `docs/testing/e2e-scenarios/`.
- Agent smoke scenario documents under `docs/testing/agent-smoke/scenarios/`.
- Codex/test-runner autonomous scenario documents under
  `docs/testing/agent-autonomous/scenarios/`.
- result schema or checker contract documentation.
- fixture requirements.
- command matrix.
- evidence and artifact expectations.
- negative cases, boundary cases, and failure-path cases.
- traceability from contract requirements to tests.

## Test Documentation Matrix

Every substantial test documentation pass should cover:

- capability or requirement being tested.
- risk or failure mode.
- test level: unit, integration/API, E2E, Agent smoke, autonomous, manual
  observation, or documentation audit.
- automation status: implemented, planned, blocked, not applicable, or out of
  scope.
- command or future command.
- expected assertion.
- evidence source.
- fixture or data requirement.
- pass/fail owner: test runner, deterministic checker, scorecard checker, or
  human review.
- unresolved gaps.

## Test Case Template

Use this structure for concrete test cases:

```text
ID:
Capability:
Priority:
Type:
Preconditions:
Steps:
Expected assertions:
State/event/log evidence:
Artifacts:
Negative or boundary coverage:
Automation target:
Current status:
```

Keep test cases specific enough that another agent can implement or run them
without inventing missing assertions.

## Unit Test Documentation

Unit-test documentation must identify:

- focused unit-test files or future files.
- logic under test.
- positive cases.
- negative and boundary cases.
- fixture or mock data.
- expected command.
- reason broader E2E or Agent checks cannot replace the unit test.

## E2E Documentation

E2E documentation must identify:

- user path or API path.
- setup and data reset requirements.
- UI assertions, API assertions, and event/log cross-checks.
- failure-path assertions.
- artifact/report path expectations.
- sandbox or local-server requirements.

Do not document E2E as "open page only" unless the explicit goal is a smoke
navigation check.

## Agent Test Documentation

Agent test documentation must distinguish:

- Agent smoke: UI/CLI operation plus deterministic checker.
- minimal autonomous saved-result validation: saved result directory plus
  deterministic or scorecard checker.
- full autonomous runner/full suite: autonomous runner plus scorecard/checker.
- manual observation: supporting evidence only.

Document required `operation-log.jsonl`, `result.json`, transcripts, console
logs, screenshots, API summaries, and checker commands where applicable.

## Review And Closeout

Test documentation closeout should record:

- changed documentation files.
- whether code, tests, checkers, fixtures, or product behavior changed.
- documentation consistency checks run, such as `git diff --check`.
- tests not run and why.
- unresolved P1/P2/P3 documentation or coverage gaps.
- handoff to implementation or validation when applicable.

If the user later asks to run validation, switch to
`product-capability-validation-playbook.md`.
