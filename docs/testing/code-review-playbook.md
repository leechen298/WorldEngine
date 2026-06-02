# Code Review Playbook

Status: reusable code-review guide

Chinese mirror: `code-review-playbook.zh.md`.

This playbook standardizes how agents review implementation reliability for a
WorldEngine version, iteration package, feature, or current code surface. It is
version-agnostic: each target still defines its own contracts, files, commands,
and review boundaries.

Use `product-capability-validation-playbook.md` when the user asks to execute
validation and report a PASS/FAIL verdict. Use
`test-documentation-playbook.md` when the user asks to write or update test
documentation.

## When To Use

Use this playbook when a user asks to review code, audit implementation logic,
or assess whether implementation is reliable.

Examples:

```text
审核 <version> 代码
review <version> code
审核 <iteration-package> 代码
代码审核 <feature-or-package>
```

A one-line request is a valid trigger. It starts a code review. It is not a PASS
verdict and it is not equivalent to final closeout.

## Non-Negotiable Rules

- Read `AGENTS.md`, `docs/iterations/README.md`, and
  `docs/iterations/AGENTS.md` before claiming review scope.
- Read the target version or package state before reviewing code:
  `README.md`, `CURRENT_STATE.md`, `GOAL_RUNNER.md`, `CAMPAIGN_PLAN.md`,
  version plan, and code-bearing child package docs when they exist.
- Do not treat `final / closeout complete` or `final-closeout-complete` as a
  code-review result.
- Do not claim tests passed unless the command ran in the current work session.
- Do not fix implementation issues inside a review-only request unless the user
  explicitly authorizes repair and the required iteration package permits it.
- Keep findings grounded in current files, line references, commands, and
  contract text.

## Review Scope Selection

For a version target, review only implementation-bearing children unless the
user explicitly asks for documentation governance review. Documentation-only
closeout packages may be used to find evidence and exclusions, but they are not
the code surface.

Build the code-surface map from:

- child package `contract.md`, `technical-design.md`, `test-plan.md`,
  `plan.md`, and `review.md`.
- parent `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and version plan.
- current git state and changed-file lists.
- implementation files, test files, API/frontend files, migrations, fixtures,
  and generated artifacts named by the package.

Classify each surface as in scope, out of scope, skipped, blocked, or evidence
only.

## Review Workflow

1. Confirm target and route.
   - Determine whether the user named a version, package, feature, or current
     working tree.
   - Identify active package state and code-bearing child packages.
   - State that final closeout is only evidence context when applicable.

2. Read contracts before code.
   - Extract allowed changes, forbidden changes, compatibility constraints,
     schema/API semantics, test expectations, and explicit exclusions.
   - Note any ambiguity as a review risk before judging implementation.

3. Inspect implementation.
   - Check runtime/schema/API/frontend behavior against the contract.
   - Check compatibility with existing event, runtime, Agent, memory, archive,
     params, loader, and frontend boundaries when touched.
   - Check failure paths, invalid inputs, edge cases, data leakage, mutable
     state, hidden side effects, persistence, migration, network/provider calls,
     and concrete application-specific content.
   - Check that public errors, diagnostics, envelopes, and response shapes match
     the package contract.

4. Inspect tests and evidence.
   - Check whether focused tests cover the highest-risk behavior and failure
     paths.
   - Check whether broader regression evidence matches the claimed blast
     radius.
   - Run focused commands only when needed to confirm a finding or claim, then
     record exact commands and results.
   - If commands are not run, state that explicitly.

5. Use independent review when available.
   - When subagents/evaluators are available and authorized, use a read-only
     code-review subagent or evaluator.
   - Superpowers `requesting-code-review` may be used for feature or package
     review. Provide the reviewer with the target, contracts, code surfaces,
     base/head or current tree context, and expected findings format.
   - The main agent remains responsible for verifying reviewer claims against
     source files and command evidence.

6. Report findings first.
   - Lead with P0/P1/P2/P3 findings ordered by severity.
   - Each finding must include file/line references, impact, triggering
     scenario, and why the contract or existing behavior is violated.
   - Then list open questions, tests run or not run, scope exclusions, and
     residual risk.
   - If there are no findings, say so clearly and still report test gaps or
     residual risk.

## Severity Guide

- P0: data loss, security exposure, destructive runtime behavior, or a broken
  core workflow with no workaround.
- P1: contract violation, serious compatibility regression, incorrect public
  API/schema behavior, or a likely production-blocking bug.
- P2: missing important edge-case handling, weak test coverage for meaningful
  risk, confusing diagnostics, or non-blocking scope drift.
- P3: minor maintainability, wording, polish, or low-risk evidence issue.

## Output Template

```text
Findings
- [P1] <title> -- <file>:<line>
  Impact:
  Evidence:
  Suggested direction:

Open Questions
- ...

Verification
- Commands run:
- Not run:

Scope And Residual Risk
- ...
```

## Durable Evidence

If the review is part of an iteration closeout, record material findings and
commands in the relevant package `review.md`.

If the review is a standalone post-closeout or version-level audit, create a
summary under `docs/testing/results/` only when the user asks for durable
evidence or when the review result is needed by later packages. Use:

```text
YYYY-MM-DD-<target>-code-review.md
```

The summary must not imply product validation passed unless validation was
separately run through `product-capability-validation-playbook.md`.
