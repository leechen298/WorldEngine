# AGENTS.md

Guidance for Codex and other AI coding agents when working in this repository.

## Project Overview

WorldEngine is a recursive world generation and runtime engine. Its long-term
purpose is to generate worlds, run worlds over time, support recursive world
structures, and let agents live inside those worlds with memory, continuity,
feedback, action, and pseudo-self formation.

Read these documents before proposing or implementing project-direction work:

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`

Chinese mirror: `AGENTS.zh.md`.

The first village-like game or electronic-pet surface is only the first
user-facing projection of WorldEngine. It is not the engine goal and must not
turn the repository into a game-specific backend.

## Active Code Path

- `backend/app/` is the active backend code path.
- `frontend/` is the active dashboard code path.
- `backend/worldengine/` is pre-v0.1 legacy code unless a later iteration
  contract explicitly says otherwise.

Do not add new runtime features under `backend/worldengine/`.

## Iteration Documentation Gate

Use `docs/iterations/README.md` as the per-iteration documentation standard.

Code or mixed iterations require an iteration package before implementation:

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`

Documentation-only iterations may omit `technical-design.md` and `test-plan.md`
only when they do not prepare runtime, schema, API, UI, or test implementation.
They must still include `contract.md` if they change process rules, version
semantics, product boundaries, concepts, evidence rules, or templates.

Iteration work is a two-stage gate:

1. Documentation stage: draft or update the required iteration package
   documents first. Keep runtime, schema, API, UI, test, and fixture files
   untouched unless the active request is explicitly documentation-only and the
   file is part of that documentation scope.
2. Implementation stage: start only after the iteration package has been
   reviewed and approved. Treat the approved documents as the work contract.

Do not draft or revise iteration documents and implement their runtime/code
changes side by side. Documentation must be separately reviewable before code
work starts. If implementation reveals a design gap, stop implementation,
update the relevant documents, and resume only after the updated contract,
design, test plan, or execution plan is reviewed.

When implementing code, read the current iteration documents first and follow:

1. `intent.md`
2. `contract.md`
3. `technical-design.md`
4. `test-plan.md`
5. `plan.md`
6. `review.md`

If implementation reveals a design problem, stop, update the relevant
iteration documents, and continue only after the updated contract/design is
reviewed.

## Hard Rules

1. North Star first.
   Any feature proposal must be checked against `docs/project-north-star.md`.

2. No implementation without iteration docs.
   Code or mixed iterations require intent, contract, technical design, test
   plan, execution plan, and review evidence. These documents are a reviewed
   gate before implementation, not paperwork to create while coding.

3. Current package only.
   Implement only the active iteration package. Do not implement adjacent
   future versions or convenient follow-on capabilities.

4. Preserve compatibility.
   Schema extensions must be additive unless the current iteration contract
   explicitly allows breaking changes.

5. Event is the system spine.
   World, agent, memory, runtime, and external projection work should converge
   through event contracts and evidence, not hidden side effects.

6. Game surface is not engine goal.
   Do not narrow WorldEngine into a village game backend.

7. Agent pseudo-self is core, but not automatic current scope.
   A version may define boundaries without implementing agent self-continuity
   if the roadmap or iteration contract places that implementation later.

8. Review must include evidence.
   Every code iteration must record changed files, commands run, test results,
   compatibility review, scope review, and unresolved findings in `review.md`.

## Verification and Reporting

- Do not claim tests, builds, E2E, UI smoke, or runtime behavior passed unless
  you ran the relevant command or flow in the current work session.
- For docs-only iterations, it is acceptable not to run code tests, but
  `review.md` must state that tests were not run and why.
- Prefer focused verification tied to the iteration contract, then broader
  regression commands when the blast radius requires it.

## Git Safety

- Do not revert or overwrite user changes that are already present in the
  working tree.
- Before staging or committing, inspect the changed-file set and keep it scoped
  to the current iteration package unless the user explicitly widens scope.
