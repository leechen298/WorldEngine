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

External fixture, validation, and projection applications are consumers of
WorldEngine. They are not part of the engine core and must not turn this
repository into application-specific backend code.

## Active Code Path

- `backend/app/` is the active backend code path.
- `frontend/` is the active dashboard code path.
- `backend/worldengine/` is pre-v0.1 legacy code unless a later iteration
  contract explicitly says otherwise.

Do not add new runtime features under `backend/worldengine/`.

## Iteration Documentation Gate

Use `docs/iterations/README.md` as the per-iteration documentation standard.
When creating or modifying files under `docs/iterations/`, also read
`docs/iterations/AGENTS.md`. It defines the required detail level for version
plans, planned packages, iteration packages, validation plans, evidence, and
review documentation.

For broad documentation generation requests, especially `/plan`-style prompts
or requests to create multiple iteration files, follow the Codex Plan-Mode
Document Generation Standard in `docs/iterations/AGENTS.md` before drafting the
documents.

Codex may use subagents only when the user explicitly asks for subagents /
parallel agent work or when the active package `GOAL_RUNNER.md`, contract, or
plan explicitly authorizes them. Subagent work must stay inside the active
package scope, obey the same git safety and evidence rules, and remain
subordinate to the main agent, which owns synthesis, verification, and final
status. For `/goal` development campaigns, subagent / evaluator checkpoints are
required by the iteration rules before implementation-bearing child packages
can close out. Detailed subagent and learning-report rules for iteration work
live in `docs/iterations/AGENTS.md`.

When the user says `完成 <iteration-package>`, `complete
<iteration-package>`, `实现 <iteration-package>`, `开发
<iteration-package>`, `implement <iteration-package>`, `develop
<iteration-package>`, or an equivalent request to implement or develop a named
iteration package, first locate the matching package under
`docs/iterations/**/<iteration-package>/`. If that package contains
`README.md`, `GOAL_RUNNER.md`, `CURRENT_STATE.md`, or `CAMPAIGN_PLAN.md`, read
those files before planning or executing. Do not infer package workflow from
memory or adjacent packages.

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

6. Application surfaces are not the engine goal.
   Do not narrow WorldEngine into demo-specific or application-specific backend
   logic.

7. Agent pseudo-self is core, but not automatic current scope.
   A version may define boundaries without implementing agent self-continuity
   if the roadmap or iteration contract places that implementation later.

8. Keep WorldEngine core generic.
   Do not add concrete demo-world names, maps, characters, locations,
   resources, story rules, seed data, UI code, or game/application-specific
   backend logic to this repository.

9. External validation worlds are consumers.
   Do not use an external validation world to drive internal engine
   abstractions. External fixture and validation applications consume public
   APIs, CLI contracts, schemas, exported contracts, or redacted reports.

10. Review must include evidence.
   Every code iteration must record changed files, commands run, test results,
   compatibility review, scope review, and unresolved findings in `review.md`.

## Verification and Reporting

- Do not claim tests, builds, E2E, UI smoke, or runtime behavior passed unless
  you ran the relevant command or flow in the current work session.
- For docs-only iterations, it is acceptable not to run code tests, but
  `review.md` must state that tests were not run and why.
- Prefer focused verification tied to the iteration contract, then broader
  regression commands when the blast radius requires it.

## Natural-Language Request Routing

Detailed natural-language trigger rules live in `docs/agent-guides/`. Keep this
file as the short router. Before executing a routed request, open the matching
guide and its primary workflow document.

| User request | Route | Primary workflow |
| --- | --- | --- |
| `生成 <version> 文档`, `编写 <version> 文档`, `规划 <version> 每个迭代`, `生成 <version> 迭代包` | `docs/agent-guides/natural-language-iteration-documentation-triggers.md` | `docs/iterations/AGENTS.md` |
| `完成 <iteration-package>`, `实现 <iteration-package>`, `开发 <iteration-package>`, `complete <iteration-package>`, `implement <iteration-package>`, `develop <iteration-package>` | `docs/agent-guides/natural-language-implementation-triggers.md` | `docs/iterations/AGENTS.md` |
| `测试 <version>`, `验证 <version>`, `<version> 是否通过`, `验证当前产品`, `clean pass` | `docs/agent-guides/natural-language-validation-triggers.md` | `docs/testing/product-capability-validation-playbook.md` |
| `编写 <version> 测试方案`, `补充 <iteration-package> 测试文档`, `设计 <feature> 测试用例`, `生成测试矩阵` | `docs/agent-guides/natural-language-test-documentation-triggers.md` | `docs/testing/test-documentation-playbook.md` |
| `审核 <version> 代码`, `review <version> code`, `代码审核 <feature-or-package>` | `docs/agent-guides/natural-language-code-review-triggers.md` | `docs/testing/code-review-playbook.md` |

A trigger phrase is only routing. It does not by itself authorize runtime,
schema, API, frontend, test, fixture, migration, or external repository
implementation, and it does not prove PASS or closeout. If a request combines
documentation, implementation, validation, or review, run the relevant workflows
in guide-defined order and keep evidence claims bounded.

## Git Safety

- Do not revert or overwrite user changes that are already present in the
  working tree.
- Before staging or committing, inspect the changed-file set and keep it scoped
  to the current iteration package unless the user explicitly widens scope.
