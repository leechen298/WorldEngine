# Natural-Language Test Documentation Triggers

Status: reusable agent routing guide

Chinese mirror: `natural-language-test-documentation-triggers.zh.md`.

Use this guide when a user makes a short test-documentation request such as:

```text
编写 <version> 测试方案
补充 <iteration-package> 测试文档
设计 <feature> 测试用例
写 E2E 测试场景
生成测试矩阵
```

## Primary Workflow

Run `docs/testing/test-documentation-playbook.md`.

This trigger is separate from validation. It produces or updates test
documentation, plans, scenarios, and cases. It does not claim tests ran or
passed.

## Broad Version-Level Output

For broad version-level requests such as `编写 v0.7 测试方案`, do not stop at a
single brief plan, checklist, or capability matrix. Produce or update a
reviewable test-documentation suite that is detailed enough for another agent
to implement or run without inventing missing assertions.

A complete version test-documentation suite must include the following unless a
layer is explicitly scoped out by the active request or package, and the
exclusion is recorded as an unresolved gap:

- an overall test strategy and evidence boundary.
- concrete unit / backend integration / API test cases.
- concrete E2E cases.
- E2E scenario contracts under `docs/testing/e2e-scenarios/`.
- Agent smoke cases and evidence requirements.
- Codex/test-runner Agent autonomous cases.
- Agent autonomous scenario contracts under
  `docs/testing/agent-autonomous/scenarios/`.
- traceability from requirements, contracts, known risks, and review findings to
  test cases.
- command, artifact, fixture, pass/fail owner, current automation status, and
  unresolved gap fields for every substantial layer.
- README or index updates that make the suite discoverable.

## Existing Document Handling

If a relevant test plan or scenario set already exists:

1. Review it against `docs/testing/test-documentation-playbook.md` before
   extending it.
2. Treat missing concrete test cases, missing E2E scenario contracts, missing
   Agent autonomous scenario contracts, mismatched command matrices, overbroad
   PASS claims, and unclear evidence ownership as documentation findings.
3. Fix P1/P2 documentation gaps before saying the test plan is complete.
4. Update indexes so future agents can find the test suite without relying on
   chat history.

## Recommended Version-Level File Pattern

For version-level test suites, prefer this discoverable split unless the active
package defines a narrower structure:

```text
docs/testing/<version>-overall-test-plan.zh.md
docs/testing/<version>-unit-api-test-cases.zh.md
docs/testing/<version>-e2e-test-cases.zh.md
docs/testing/<version>-agent-test-cases.zh.md
docs/testing/e2e-scenarios/<scenario>.md
docs/testing/agent-smoke/scenarios/<scenario>.md
docs/testing/agent-autonomous/scenarios/<scenario>.md
```

Keep the overall plan as the strategy and index. Put concrete cases and
scenario details in the split documents or scenario contracts.

## E2E Documentation Requirements

For E2E documentation:

- distinguish implemented Playwright coverage from planned coverage.
- do not claim a UI-only spec covers request-level API assertions unless the
  spec actually performs those assertions.
- record local-server assumptions.
- record serial state and reset boundaries.
- include UI assertions, API assertions, and event/log cross-checks.
- include failure-path assertions.
- include artifact/report paths.
- identify planned gaps separately from implemented coverage.

## Agent Autonomous Documentation Requirements

In this documentation, "Agent" means Codex or a test-runner agent acting as an
ordinary test user. It does not mean a future WorldEngine in-world Agent.

Full user-style autonomous tests use a user-action layer and an evidence layer.
The user-action layer must include at least one ordinary-user operation, such as
dashboard operation or public product API calls. Checker CLI commands and raw
artifacts belong to the verdict/evidence layer; they do not by themselves
replace the user-action layer.

The autonomous user-action layer may:

- operate the dashboard.
- call public product APIs.

The verdict/evidence layer may:

- run public checker CLI commands.
- record raw artifacts.

PASS must come from deterministic checker, scorecard checker, or a future full
autonomous suite checker. Distinguish full user-style autonomous tests from
Agent smoke and from the current minimal saved-result checker, especially when
the current checker rejects direct API operations as Agent operations.

## Authorization Boundary

Writing test documentation does not authorize adding or changing test code,
checker code, fixtures, schemas, runtime/API/frontend behavior, or durable
result artifacts.

If the user asks to implement tests or execute validation, use the required
iteration package gate before those changes, then run the appropriate
validation flow.

If a request combines test documentation with validation, write or update the
test documentation first, then switch to
`docs/testing/product-capability-validation-playbook.md` for execution and
verdict.
