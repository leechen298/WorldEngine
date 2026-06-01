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
- Planned-package specifications in `vX.Y-plan.md` do not by themselves create
  concrete child package directories, package files, or implementation
  authorization.
- A one-line package summary is not enough.
- Later agents must not have to guess scope, allowed files, forbidden files,
  verification, compatibility constraints, or handoff state.
- A broad request to generate or plan a version must not create full document
  sets for every planned child iteration by default. Create a concrete child
  package document set only when the user explicitly requests that child
  package, asks to create or complete a child package, or a reviewed active
  package explicitly authorizes the next child package documentation.
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

## Codex Plan-Mode Document Generation Standard

Use this standard when the user asks for `/plan`, asks for a plan before
iteration documentation, or gives a broad request that would create or revise
multiple `docs/iterations/` files.

Plan-mode documentation work must produce a reviewable generation plan before
large-scale drafting. The plan may live in the chat response for a small
docs-only change. For a new version plan, new iteration package, validation
chain, goal campaign, or multi-file rewrite, the plan must be recorded in the
relevant `plan.md`, `CAMPAIGN_PLAN.md`, parent `vX.Y-plan.md`, or package
`review.md` before closeout.

The generation plan must include:

```text
Objective
Authoritative inputs read
Documentation type
Files to create or update
Files explicitly out of scope
Required package status values
Allowed changes
Forbidden changes
Review gates
Verification commands
Open questions or assumptions
Stop conditions
Handoff after plan approval
```

Hard rules:

- Do not modify runtime, schema, API, frontend, backend tests, fixtures,
  migrations, or external repositories during plan-mode documentation drafting.
- Do not create implementation-ready claims until the package documents have
  been reviewed and the review evidence records approval.
- Do not generate a full package from memory alone. Read the relevant roadmap,
  version plan, parent package, current package docs, and governing `AGENTS.md`
  files first.
- If the plan reveals missing scope, contradictory status, missing required
  inputs, or unclear implementation authorization, stop the plan as
  `NEEDS_USER_INPUT` or record the blocker in `review.md`.
- If the user asks for `/plan` only, stop after the plan unless they explicitly
  authorize drafting or execution.
- If the user asks `/goal` to complete a package, the goal may execute the
  selected plan-mode gates inside the same goal, but the plan and gates must
  still be visible in package docs or review evidence.
- For broad version-level documentation requests, create or update the version
  root and version plan first. Do not pre-create every planned child package's
  `README.md`, `intent.md`, `contract.md`, `technical-design.md`,
  `test-plan.md`, `plan.md`, or `review.md` unless the user or reviewed active
  package explicitly authorizes those concrete child package documents.
- Keep the plan tied to the active package. Do not include adjacent future
  versions or convenient follow-on work unless the parent plan explicitly owns
  that scope.

## Concept Learning / Research Synthesis Gate

Use this gate when iteration work depends on an unfamiliar concept, dense
source material, research paper, course, external framework, or internal design
area that the active package does not already explain.

The output must be a durable, reviewable artifact, not only transient chat
notes. Use the active package `plan.md`, `technical-design.md`, `review.md`, or
a package-local `notes/*.md` file when the learning result needs to support
later implementation or review.

Required learning report content:

```text
Learning objective
Sources read
Source reliability / authority
Glossary and prerequisite concepts
Concept walkthrough
Evidence table mapping claims to sources
Diagrams when they clarify the concept
Claims from the source material
Agent interpretation / synthesis
Caveats and weak evidence
Open questions
Follow-up reading or experiments
Impact on the active package
```

Hard rules:

- Separate what the source claims from what the agent infers.
- Cite source sections, headings, pages, figures, tables, files, or symbols
  whenever possible.
- If exact page or figure references are unavailable, say so and use the most
  precise available section, heading, file, or symbol reference.
- Do not treat a paper, course, external article, generated summary, or
  subagent output as ground truth when evidence is weak or disputed.
- Prefer Markdown-native Mermaid diagrams for concept maps, method flows, and
  evidence maps. Use generated or binary visual assets only when a
  Markdown-native diagram is insufficient and the active package allows the
  asset.
- Do not implement code based only on the learning report. Implementation still
  requires the normal iteration package contract, design, test plan, and review
  gates.

Subagent split for dense material:

- one subagent may map the problem statement, contribution, method, evidence,
  limitations, and claimed results.
- one subagent may gather prerequisite context from approved sources.
- one subagent may inspect figures, tables, notation, algorithms, code paths,
  or claims needing careful verification.
- one subagent may act as a skeptical reviewer and identify unsupported claims,
  missing baselines, unclear assumptions, or follow-up questions.

The main agent must wait for the requested subagents, reconcile
contradictions, and write the final learning report. Do not paste disconnected
subagent notes as the final artifact.

## Goal Development Campaign Subagent Gate

WorldEngine `/goal` development campaigns must use independent subagent or
evaluator checkpoints. This applies when a goal campaign, full child-package
cycle, code package, mixed package, migration, refactor, deployment retry loop,
or implementation-bearing validation repair can change runtime behavior,
schemas, APIs, frontend behavior, backend tests, fixtures, migrations, or
release claims.

This gate adapts Codex follow-goals behavior to this repository's iteration
model:

- North Star and scope boundaries remain first.
- The active iteration package is the only implementation scope.
- Documentation, contract, design, test-plan, and review gates still control
  implementation authorization.
- Runtime claims require current-session command evidence.
- Closeout still requires changed-file consistency and `review.md` evidence.
- The main agent owns synthesis, verification, final status, and conflict
  resolution.

Mandatory checkpoints for implementation-bearing child packages:

1. Documentation / contract evaluator before recording
   `implementation_authorized: yes`.
2. Implementation-scope evaluator after files are changed and before broad
   verification.
3. Code-review subagent or evaluator after focused tests and before E2E,
   API smoke, autonomous validation, or final status.
4. Validation-evidence evaluator before marking tests, E2E, API smoke,
   autonomous validation, deployment, or release claims as passed.
5. Closeout consistency review before package `review.md` records a final
   route status.

Mandatory checkpoints for documentation-only goal campaign children:

- A read-only documentation evaluator is required when the child changes
  process rules, goal routing, evidence rules, package sequencing, validation
  templates, release status, automation-consumption contracts, or English /
  Chinese mirror obligations.
- Trivial text-only edits may skip subagents only when they do not affect any
  gate, contract, status, claim, or automation route.

Failure handling:

- If subagent tooling is unavailable in a required `/goal` development
  checkpoint, record the missing checkpoint as `BLOCKED` or `NEEDS_USER_INPUT`;
  do not silently downgrade it to optional.
- If a required subagent or evaluator returns P0 / P1 findings, fix them or
  stop before closeout.
- If P2 findings remain, either fix them, downgrade with rationale, carry them
  only where the package contract allows, or stop before a clean pass.
- If subagent output conflicts with source files, command evidence, or git
  state, the main agent must resolve the conflict with authoritative evidence
  before final status.

## Subagent / Evaluator Use Standard

Subagents are allowed for iteration work only when the user explicitly requests
subagents / parallel agent work or when the active package `GOAL_RUNNER.md`,
contract, or plan explicitly authorizes them. They are optional tools for
review, evaluation, exploration, and clearly separable worker tasks. They are
not mandatory ceremony and do not relax package gates.

For `/goal` development campaigns, the Goal Development Campaign Subagent Gate
above is an explicit authorization and makes the listed checkpoints mandatory.

Use subagents when they materially improve reliability, for example:

- learning or summarizing unfamiliar dense source material.
- independent review of broad or risky documentation changes.
- code review for implementation-bearing packages.
- compatibility, scope, security, release-claim, or evidence-honesty checks.
- English / Chinese mirror quality checks.
- autonomous validation or black-box validation review.
- parallel inspection of independent files or subsystems.

Default mode:

- Subagents are read-only evaluators by default.
- Prefer subagents for read-heavy exploration, tests, triage, log analysis,
  learning reports, and summarization.
- Be cautious with parallel write-heavy workflows because concurrent edits can
  create conflicts and coordination overhead.
- A subagent may edit files only when the active package contract explicitly
  allows worker implementation and the main agent has recorded why delegation is
  in scope.
- Subagents must not modify runtime, schema, API, frontend, backend tests,
  fixtures, migrations, external repositories, or out-of-scope documents unless
  the active contract explicitly authorizes that file class.

Main-agent responsibilities:

- define each subagent's scope, inputs, and expected output before dispatch.
- state whether the main agent should wait for all subagents before continuing.
- keep subagent tasks inside the active package and current goal.
- synthesize results instead of pasting disconnected subagent output into
  final status.
- classify subagent findings as P0 / P1 / P2 / P3.
- fix, downgrade with rationale, carry where allowed, or record blockers for
  every P0 / P1 / P2 finding.
- verify any claimed fix or pass with current-session evidence.
- record material subagent reviews in `review.md`, including what was reviewed,
  findings, commands run or not run, and unresolved risks.

Hard stops:

- If a subagent reports a P0 / P1 that cannot be fixed inside the active
  contract, stop as `BLOCKED`, `FAILED`, or `NEEDS_USER_INPUT`.
- If subagent output conflicts with source files, command evidence, or actual
  git state, trust current source/evidence and resolve the conflict before
  closeout.
- Do not use subagents to bypass review gates, implementation authorization,
  Closeout Consistency Gate, or evidence requirements.

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
