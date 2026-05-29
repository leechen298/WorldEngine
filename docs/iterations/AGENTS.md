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

## Codex Goal Campaign Standard

Runnable parent or umbrella packages may support Codex App `/goal` campaign
execution. They must not rely on memory or chat context as the only entrypoint.

A goal campaign package must provide:

```text
README.md with Goal Entry
GOAL_RUNNER.md
CURRENT_STATE.md
CAMPAIGN_PLAN.md or equivalent parent plan section
child package README / contract / plan / review files
```

`README.md` owns the natural-language goal alias, such as
`完成 <package-name>`.

`GOAL_RUNNER.md` owns the execution state machine, adaptive gate selection,
risk-based gate order, review loops, implementation authorization rule,
verification loop, closeout consistency gate, and stop conditions.

`CURRENT_STATE.md` owns the current active child, current campaign status,
archived evidence policy, and next action.

`CAMPAIGN_PLAN.md` or the parent plan owns child sequence, campaign exit
criteria, and cross-child handoff rules.

`review.md` owns evidence and final status. It must not be the only place where
the goal entry is defined.

If a package is reset to rerun a campaign, historical evidence must remain
visible but be marked as archived or non-current unless explicitly re-accepted
by the current goal.

## English / Chinese Mirror Rule

### Default bilingual output rule

For active iteration documentation, English and Chinese mirrors should be
produced together when the document is part of:

- version index.
- version plan.
- package README.
- package contract.
- package plan.
- package review.
- release candidate or closeout docs.
- post-closeout validation docs.
- validation report templates.
- evidence, compatibility, or boundary audit docs.

If the task creates a new English active iteration document and a Chinese
mirror is expected by the directory convention, package contract, or active
task, create the `.zh.md` mirror in the same pass.

If a mirror is intentionally omitted, the package `review.md` must record why.

### Existing mirror update rule

If an active English iteration doc already has a `.zh.md` mirror, update both
in the same pass.

If only one side is updated, review must record at least a P2 finding unless
the package contract explicitly allows English-only or Chinese-only changes.

### Chinese document quality rule

Chinese mirrors must be real Chinese documents, not English documents with
Chinese punctuation.

Chinese mirrors must use natural Chinese prose for explanations, goals, scope,
conclusions, review findings, and status notes.

It is acceptable to preserve technical identifiers in English only when they
are:

- code symbols.
- file paths.
- command names.
- API routes.
- package names.
- status literals.
- field names.
- established project terms where translating would reduce precision.

Do not leave ordinary explanatory sentences in English.

Do not produce paragraphs that are mostly English with a few Chinese connector
words.

Do not mechanically copy English headings and prose when a natural Chinese
equivalent is clear.

### Structural equivalence rule

Chinese mirrors must preserve the same meaning and review semantics as the
English file.

The following must be equivalent across English and Chinese:

- Status.
- Type.
- Goal.
- Scope.
- Allowed changes.
- Forbidden changes.
- Compatibility requirements.
- Expected deliverables.
- Expected tests / verification.
- P1/P2/P3 findings.
- Final assessment.
- Release / closeout status.
- Validation status.
- Blockers and not-run reasons.

### Heading translation rule

Headings may keep code-like nouns or package names in English, but generic
headings should be translated into readable Chinese.

Examples:

- `Goal` may become `目标`.
- `Scope` may become `范围`.
- `Allowed changes` may become `允许修改`.
- `Forbidden changes` may become `禁止修改`.
- `Expected tests / verification` may become `预期测试 / 验证`.
- `Final assessment` may become `最终评估`.

Do not require literal one-to-one heading translation if a clearer Chinese
heading is available.

### Review enforcement

If a Chinese mirror is missing, stale, semantically weaker, or mostly English
where natural Chinese is expected:

- record P2 for normal documentation.
- record P1 if the mismatch affects release status, validation status,
  forbidden changes, compatibility constraints, or closeout evidence.

## Release / Closeout Rules

Do not mark a version complete or released unless the final closeout package
allows it.

Release candidate is not release.

Documentation-only closeout must not claim new runtime behavior.

Final closeout must cite evidence and unresolved findings.

If validation is not executed, say so clearly.
