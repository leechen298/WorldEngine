# Iteration Documentation Agent Rules

Status: process standard

This file governs documentation work under `docs/iterations/`.
Root `AGENTS.md` and `CLAUDE.md` still govern repository-wide behavior.
This file defines the required detail level for version plans, planned
packages, iteration packages, validation plans, evidence, and reviews.

This file does not implement or define an external automation controller.

## Purpose

Use this file whenever creating or modifying files under `docs/iterations/`.
It turns the expected iteration-document detail level into explicit rules so
future agents do not infer scope, evidence requirements, or closeout state from
examples.

These rules apply to:

- version plans.
- planned packages.
- concrete iteration packages.
- validation plans.
- post-closeout validation documents.
- review and evidence records.

## Version Plan Standard

Any `vX.Y-plan.md` that contains multiple planned sub-iterations must describe
each planned package as a quasi-package specification.

Each planned package must include these fields:

```text
Package name
Status
Type
Goal
Why this exists
Inputs / required reading
Allowed changes
Forbidden changes
Expected deliverables
Expected tests / verification
Compatibility constraints
Scope guardrails
Exit criteria
Handoff to next package
```

Hard rules:

- `README.md` may be a package index or summary.
- `vX.Y-plan.md` must be the detailed execution specification.
- A one-line package summary is not enough.
- Later agents must not have to guess scope, allowed files, forbidden files,
  verification, compatibility constraints, or handoff state.
- If any required planned-package field is missing, review must record at
  least a P2 finding.
- If missing `Forbidden changes`, `Compatibility constraints`, or
  `Scope guardrails` could let runtime, API, or schema work exceed scope,
  review must record a P1 finding.

## Iteration Package File Standard

Code and mixed packages must include:

```text
README.md
intent.md
contract.md
technical-design.md
test-plan.md
plan.md
review.md
```

Documentation-only packages must include at least:

```text
README.md
intent.md
contract.md
plan.md
review.md
```

Documentation-only packages may omit `technical-design.md` and `test-plan.md`
only when they do not prepare or change runtime, schema, API, UI, test,
fixture, process, evidence, validation, release, or automation-consumption
behavior.

If a documentation-only package modifies any of these topics, it must include
`test-plan.md` and should include `technical-design.md`:

```text
process rules
version semantics
product boundaries
evidence rules
validation templates
release status
package sequencing
automation consumption contracts
```

## Required Content For Each Package File

Each package file must be specific enough for review. Placeholder headings are
not sufficient.

### README.md

Must include:

```text
Status
Type
Goal
Scope
Deliverables
Final assessment state, if applicable
```

### intent.md

Must include:

```text
Problem / purpose
Why now
Relationship to roadmap
Non-goals
Expected handoff
```

### contract.md

Must include:

```text
Public concepts
Allowed changes
Forbidden changes
Compatibility requirements
Out-of-scope follow-ups
```

### technical-design.md

Must include:

```text
Documentation or implementation structure
Affected files
Data / control flow, if relevant
Compatibility strategy
Anti-drift rules
```

### test-plan.md

Must include:

```text
Exact commands to run
Expected results
Commands not run and why
Blocker recording rule
No unverified claims rule
```

### plan.md

Must include:

```text
Ordered execution steps
Phase boundaries
Stop conditions
Review update step
```

### review.md

Must include:

```text
Changed files
Commands run
Test results
Compatibility review
Scope review
Unresolved P1/P2/P3
Final assessment
```

## Anti-Drift Requirements

Any future version or package planning must state:

```text
where the work lives
what files may change
what files must not change
which current behaviors are compatibility-sensitive
which adjacent tempting features are explicitly out of scope
which later version owns those tempting features
how the next package receives handoff
```

Do not:

- add concrete demo world details.
- use external validation worlds to drive core abstractions.
- implement future-version work in the current package.
- mix documentation planning and implementation unless the current package
  contract explicitly allows it.
- claim tests passed without current-session evidence.

## Validation And Post-Closeout Documentation Standard

Post-closeout validation documents must distinguish these states:

```text
feature closeout complete
independent validation not yet performed
validation planned
validation executed
validation passed / blocked / failed
```

A validation plan must not be written as a validation result.

Post-closeout validation documents should include:

```text
intent
contract
test plan
API smoke plan
E2E / integration plan
autonomous review plan
execution plan
report template
review
```

Hard rules:

- If E2E was not run, record `not executed` or `not configured`.
- If Codex autonomous validation was not run, do not mark it passed.
- If no E2E framework exists, state that the fallback is API smoke plus
  backend integration tests.
- Validation reports must not prefill `passed`.
- Only commands actually run in the current session may be recorded as passed.
- If a command is unavailable, record the blocker.

## Evidence And Review Rules

Evidence and review records must follow these rules:

```text
No unverified test claims.
No hidden blockers.
No vague "tests passed".
Record exact commands.
Record not-run checks and why.
P1 blocks closeout.
Unresolved P2 blocks final unless explicitly accepted.
P3 can be carried only with explicit handoff.
```

Severity definitions:

```text
P1: blocks implementation or closeout.
P2: should be fixed before final review unless explicitly accepted.
P3: non-blocking polish or future handoff.
```

## External Automation Boundary

WorldEngine iteration docs may be consumed by external automation controllers.
WorldEngine does not own agent scheduling, Codex role assignment, retry loops,
or orchestration.

`docs/iterations/` must provide deterministic package specs, not automation
implementation.

## English / Chinese Mirror Rule

If an active English iteration doc has a `.zh.md` mirror, update both.
Chinese mirrors may keep technical terms in English.

Status, scope, conclusion, allowed changes, forbidden changes, evidence, and
review findings must be equivalent across mirrors.

Do not create new mirrors unless the package contract or active task
explicitly allows it.

## Release / Closeout Rules

Do not mark a version complete or released unless the final closeout package
allows it.

Release candidate is not release.

Documentation-only closeout must not claim new runtime behavior.

Final closeout must cite evidence and unresolved findings.

If validation is not executed, say so clearly.
