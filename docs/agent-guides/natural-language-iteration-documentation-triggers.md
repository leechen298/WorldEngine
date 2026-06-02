# Natural-Language Iteration Documentation Triggers

Status: reusable agent routing guide

Chinese mirror: `natural-language-iteration-documentation-triggers.zh.md`.

Use this guide when a user makes a short iteration-documentation request such
as:

```text
生成 <version> 文档
编写 <version> 文档
规划 <version> 每个迭代
生成 <version> 迭代包
创建 <version> iteration docs
```

## Primary Workflow

Run the Codex Plan-Mode Document Generation Standard in
`docs/iterations/AGENTS.md`.

Before drafting project-direction work, also respect the required reading in
`AGENTS.md` and `docs/iterations/README.md`, especially:

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`

## Boundary

This trigger creates or updates reviewable iteration documentation only. It
does not authorize runtime, schema, API, frontend, test, fixture, migration, or
external repository implementation.

If a user combines iteration documentation with implementation, finish the
documentation stage first and report that implementation waits for review and
approval of the relevant package documents.

## Default For New Versions

For a new version, a short version-documentation request defaults to the
version-level package only:

- parent generation plan.
- version index.
- version plan.
- campaign state docs.
- child package sequence.
- planned-package specifications inside the version plan.

Do not create full documentation directories for every planned child iteration
by default.

## Planned Child Package Rule

Planned child packages in a version plan are route-map specifications. They are
not approved execution contracts and not implementation authorization.

Create a concrete child package document set only when one of these is true:

- the user explicitly names that child package.
- the user asks to create or complete that child package.
- a reviewed active package explicitly authorizes creating the next child
  package documents.

## Required Output Discipline

When generating or updating iteration documentation:

- keep package status honest: proposed, planned, ready-for-review, or equivalent
  until review actually approves the next stage.
- make child-package sequence, boundaries, and stop rules explicit.
- list generated or updated files.
- record documentation checks such as `git diff --check`.
- state that code tests were not run when the request is docs-only.
- do not imply implementation, validation, or closeout from documentation alone.

## Existing Package Handling

If matching version or package files already exist:

1. Read the current `README.md`, `GOAL_RUNNER.md`, `CURRENT_STATE.md`,
   `CAMPAIGN_PLAN.md`, and `review.md` when present.
2. Preserve the active package boundary.
3. Update existing docs instead of creating duplicate authority surfaces.
4. If status text drifts across files, treat that as a documentation finding and
   fix it before reporting the package ready.
