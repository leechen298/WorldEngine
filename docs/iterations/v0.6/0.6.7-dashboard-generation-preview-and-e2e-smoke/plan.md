# Plan

Status: review complete

## Objective

Create and review the `0.6.7` dashboard generation preview and E2E smoke
package, then implement only after `implementation_authorized: yes`.

## Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration/review.md`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/api/client.ts`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/e2e/agent-loop.spec.ts`
- `frontend/package.json`
- `frontend/playwright.config.ts`

## Execution Steps

1. Create the seven required package docs and Chinese mirrors.
2. Keep initial status at `ready for review` and
   `implementation_authorized: no`.
3. Run documentation checks.
4. Request documentation/contract evaluator review.
5. After evaluator PASS, record `implementation_authorized: yes` and sync
   parent status surfaces.
6. Implement only the approved frontend/API-client/E2E files.
7. Run focused frontend, build, backend generation API, E2E, diff, and scope
   checks.
8. Request implementation-scope, code-review, validation-evidence, and
   closeout consistency evaluators.
9. If all checks pass, mark `0.6.7` review complete and hand off to `0.6.8`.

## Files To Create Or Update

Documentation stage:

- `docs/iterations/v0.6/0.6.7-dashboard-generation-preview-and-e2e-smoke/**`
- parent v0.6 status and review files.

Implementation stage after authorization:

- `frontend/src/api/client.ts`
- `frontend/src/api/client.test.ts`
- `frontend/src/components/GenerationPanel.vue`
- `frontend/src/components/GenerationPanel.test.ts`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/pages/DashboardPage.test.ts`
- `frontend/src/style.css`
- `frontend/e2e/dashboard-generation.spec.ts` or focused additions to
  `frontend/e2e/dashboard.spec.ts`.
- this package review files and parent status surfaces.

## Files Explicitly Out Of Scope

- backend implementation files.
- `backend/worldengine/**`
- persistence/repository modules.
- migrations.
- fixtures.
- generated output artifacts.
- external repositories.
- provider SDKs, prompt libraries, network clients, or background workers.
- external validation runner or projection application files.

## Stop Conditions

- Implementation starts before authorization.
- Dashboard preview requires backend API/schema/runtime changes.
- UI stores, publishes, activates, or mutates generated specs.
- E2E smoke becomes external validation, autonomous validation, product
  readiness, or generation-quality validation.
- Concrete demo-world/story data is introduced.
- Implementation needs files outside the approved list.

## Handoff

After closeout, `0.6.8-v0.6-evidence-and-compatibility-audit` receives
dashboard generation preview and E2E smoke evidence.
