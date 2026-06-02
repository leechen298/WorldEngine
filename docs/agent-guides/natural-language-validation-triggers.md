# Natural-Language Validation Triggers

Status: reusable agent routing guide

Chinese mirror: `natural-language-validation-triggers.zh.md`.

Use this guide when a user makes a short validation request such as:

```text
测试 <version>
验证 <version>
<version> 是否通过
测试 <iteration-package>
验证当前产品
clean pass
```

## Primary Workflow

Run `docs/testing/product-capability-validation-playbook.md`.

The trigger phrase is only a request to execute or classify validation. It is
not itself a PASS verdict.

## Boundary

Before reporting a result:

- read the active version or package state.
- determine the in-scope validation surface.
- identify which surfaces are out of scope or unsupported.
- create or use the required iteration package if validation will change tests,
  checkers, fixtures, result schemas, runtime/API/frontend behavior, or durable
  evidence rules.

Do not silently modify implementation or test infrastructure in response to a
validation trigger. If repair or new tests are required, route that work through
the package gate.

## Required Classification

Every in-scope command, checker, suite, or workflow must be classified as one of:

- passed.
- failed.
- blocked.
- skipped.
- out of scope.

Do not collapse blocked, skipped, or out-of-scope into pass-equivalent language.

## Required Distinctions

Validation reports must distinguish:

- backend/unit/checker tests.
- frontend unit/build checks.
- Browser E2E.
- Agent smoke.
- minimal autonomous saved-result validation.
- full autonomous runner/full suite.
- manual observation.
- external validation suite evidence.
- projection readiness.
- product readiness.

If current evidence does not cover one of these surfaces, name the exclusion
instead of implying broader PASS.

## Evidence Requirements

Before reporting a validation verdict, record:

- current branch, commit, and worktree state.
- exact commands or workflows run.
- exit status and result summary for every command.
- raw artifact paths for E2E, Agent smoke, autonomous, external reports, or
  generated summaries.
- unresolved P1/P2/P3 findings.
- skipped, blocked, and out-of-scope items with reasons.
- final verdict source.

Use `docs/testing/results/` or the relevant package `review.md` for durable
summaries.

## Verdict Discipline

Do not claim tests, builds, E2E, UI smoke, Agent smoke, autonomous, external
suite, projection readiness, product readiness, or clean pass unless the
relevant command or checker was run in the current work session and the result
supports the claim.

When old evidence exists, treat it as historical context until it is refreshed
or explicitly scoped as historical.
