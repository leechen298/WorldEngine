# Technical Design

## Current State

The active v0.2 index and plan still require a remaining-package reset. The
roadmap also needs to point at 0.2.6 as workflow and plan reset instead of
final closeout. The release docs are draft planning artifacts and must remain
not released.

Historical v0.2 packages may contain superseded concrete fixture detail. The
new automation workflow will cause future agents to read broad v0.2 context,
so those details must be abstracted to reduce scope drift while preserving
historical evidence.

## Contract Alignment and Invariants

- Keep all changes in documentation.
- Keep v0.2 status planned / in progress.
- Keep release docs draft / planned / not released.
- Keep existing v0.3 and later technical roadmap direction intact except for
  the v0.2 handoff wording needed by this package.
- Preserve historical facts in abstract form.

## Proposed Implementation

1. Add the 0.2.6 package document set with English / Chinese mirrors.
2. Add `00-chatgpt-plan.md` and `00-chatgpt-plan.zh.md` as the seed plan for
   later automation.
3. Add `development-workflow.md` and `development-workflow.zh.md` with the
   ChatGPT / Codex A / Codex B loop,
   gates, severity model, evidence rules, and WorldEngine boundaries.
4. Add `final-review-bundle-template.md` and
   `final-review-bundle-template.zh.md` with required review fields.
5. Update v0.2 index and plan docs so 0.2.7 through 0.2.12 have stable planned
   names, types, boundaries, deliverables, verification expectations, and
   handoffs.
6. Update roadmap v0.2 entries to match the new package sequence.
7. Update release docs to remain draft / planned / not released and to point
   final closeout after 0.2.12 approval.
8. Abstract residual historical concrete demo details in v0.2 iteration docs.

## Affected Surfaces

- `docs/iterations/v0.2/**`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`

## Data Model / Schema Changes

None.

## Runtime / Service Design

None.

## Compatibility

This package does not change runtime behavior, API response shape, schema
validation behavior, frontend behavior, tests, fixtures, or external consumer
contracts.

## Risks

- Risk: remaining-package planning is too shallow for later automation.
  Mitigation: enforce the Detailed Plan Acceptance Gate.
- Risk: historical concrete detail remains and influences later agents.
  Mitigation: run a concrete demo anchor sweep with a temporary untracked
  pattern file and classify residuals abstractly.
- Risk: release docs overclaim final status.
  Mitigation: run release-status wording checks and keep final closeout behind
  0.2.12 review approval.
