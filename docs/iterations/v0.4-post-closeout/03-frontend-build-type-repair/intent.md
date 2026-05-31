# Intent

## Problem

The v0.4 post-closeout validation matrix is blocked by one P1 failure:

```bash
cd frontend && pnpm build
```

The build fails during TypeScript checking in frontend component tests and in
the Ant Design Vue table `customRow` binding for `TimelinePanel.vue`.

## Goal

Make the frontend build pass through minimal type-correct edits, preserve the
existing selector assertions, and rerun the validation matrix required for a
clean-pass decision.

## Why Now

Package `02-overall-product-capability-validation` already found backend,
Vitest, E2E, Agent smoke, and minimal autonomous saved-result checks passing.
The frontend build failure is the only recorded P1 clean-pass blocker.

## Relationship To Roadmap

This package supports v0.4 quality validation for the first in-world Agent loop
without changing the runtime model, public API, or later roadmap scope.

## Non-goals

- Do not change backend runtime, schemas, API behavior, migrations, or legacy
  `backend/worldengine/**`.
- Do not change frontend product behavior beyond type-correct selector/test
  support.
- Do not implement a full autonomous runner.
- Do not reclassify the minimal autonomous checker as full autonomous coverage.

## Expected Handoff

If the required commands pass, this package hands off a clean-pass validation
assessment to the parent v0.4 post-closeout campaign. If any command fails, it
records the new blocker with exact command evidence.
