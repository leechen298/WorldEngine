# Test Plan

## Documentation Checks

- Verify repository state before and after documentation edits.
- Verify Markdown diff has no whitespace errors.
- Verify the detailed plan acceptance gate for 0.2.7 through 0.2.12.
- Verify release wording does not claim final release.
- Verify residual concrete demo anchors are removed or abstracted.

## Commands

```bash
git status --short --branch
git diff --check
```

## Concrete Demo Anchor Sweep

Use a temporary, untracked pattern file under `/tmp` or another untracked path.
Do not write the concrete pattern list into tracked Markdown.

The review should record the command purpose and classification only, using
abstract descriptions such as:

- historical concrete fixture wording
- historical concrete fixture pathname
- legacy concrete demo anchor
- concrete demo anchor sweep

## Detailed Plan Acceptance Gate

Before final output, verify that `docs/iterations/v0.2/v0.2-plan.md` and
`docs/iterations/v0.2/v0.2-plan.zh.md` contain all required fields for every
package from 0.2.7 through 0.2.12:

- Package name
- Status
- Type
- Goal
- Why this exists
- Inputs / required reading
- Allowed changes
- Forbidden changes
- Expected deliverables
- Expected tests / verification
- Compatibility constraints
- Scope guardrails
- Exit criteria
- Handoff to next package

If any field is missing, record a P2 finding and do not claim the plan is
ready.

## Acceptance Criteria

- `0.2.6-iteration-workflow-and-plan-reset` exists with the required package
  files and Chinese mirrors.
- `00-chatgpt-plan.md` / `.zh.md`, `development-workflow.md` / `.zh.md`, and
  `final-review-bundle-template.md` / `.zh.md` exist.
- v0.2 index and plan docs point to 0.2.6 as workflow and plan reset, not
  final closeout.
- `v0.2-plan.md` and `v0.2-plan.zh.md` include full quasi-package
  specifications for 0.2.7 through 0.2.12.
- roadmap v0.2 entries match the new package sequence without rewriting v0.3+
  technical direction.
- release docs remain draft / planned / not released.
- No runtime, schema, API, frontend, backend test, or fixture files changed.

## Not Run

Backend and frontend tests are not required for this documentation-only
package. If code, schema, API, frontend, test, or fixture files are modified by
mistake, stop and record a scope violation.
