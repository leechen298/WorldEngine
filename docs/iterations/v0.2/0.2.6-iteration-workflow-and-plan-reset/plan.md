# Plan

## Files

Create:

- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/README.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/intent.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/contract.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/technical-design.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/test-plan.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/plan.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/review.md`
- `docs/iterations/v0.2/00-chatgpt-plan.md`
- `docs/iterations/v0.2/development-workflow.md`
- `docs/iterations/v0.2/final-review-bundle-template.md`

Modify:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- historical `docs/iterations/v0.2/**` files only to abstract concrete demo
  details.

Do not touch:

- runtime code.
- schema code.
- API code.
- frontend code.
- backend tests.
- fixtures.
- external repositories.
- 0.2.7 through 0.2.12 package directories.

## Steps

1. Read the required active docs and 0.2.5 review evidence.
2. Create the 0.2.6 package documents.
3. Add the automation workflow, ChatGPT seed plan, and review bundle template.
4. Rewrite the v0.2 index and plan so 0.2.6 is workflow/reset and 0.2.7
   through 0.2.12 are planned quasi-package specifications.
5. Update roadmap v0.2 entries only.
6. Update release docs as draft / planned / not released.
7. Abstract historical concrete demo details inside v0.2 iteration docs and
   v0.2 release docs.
8. Run the documentation verification commands.
9. Record evidence in this package's `review.md`.

## Verification

- `git status --short --branch`
- `git diff --check`
- Detailed Plan Acceptance Gate for 0.2.7 through 0.2.12.
- concrete demo anchor sweep using a temporary untracked pattern file.
- release-status wording check.
