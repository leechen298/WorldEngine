# Plan

## Files

- Create:
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/intent.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/intent.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/contract.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/contract.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/technical-design.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/technical-design.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/test-plan.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/test-plan.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/plan.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/plan.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.zh.md`
- Modify during documentation stage:
  - `docs/iterations/v0.3/README.md`
  - `docs/iterations/v0.3/README.zh.md`
  - `docs/iterations/v0.3/v0.3-plan.md`
  - `docs/iterations/v0.3/v0.3-plan.zh.md`
- Modify only after closeout review approval:
  - `docs/releases/v0.3.md`
  - `docs/releases/v0.3.zh.md`
  - `docs/iterations/v0.3/findings.md`, if finding status changes.
- Do not touch:
  - runtime, schema, API, frontend, fixture, migration, or test implementation
    files.
  - `backend/worldengine/`.
  - external repository content.

## Steps

1. Read repository guidance, v0.3 milestone docs, 0.3.7 release-candidate
   evidence, findings, templates, and prior closeout examples.
2. Create the mirrored 0.3.8 package docs.
3. Mark 0.3.8 `ready for review` in the package README and v0.3 milestone
   index; synchronize v0.3 plan docs to avoid status drift.
4. Run documentation-stage verification from `test-plan.md`.
5. Record current-session evidence in `review.md` and `review.zh.md`.
6. Wait for human / ChatGPT review approval before applying final closeout
   release wording or review-complete status.

## Verification

Documentation-stage verification is limited to docs checks:

- `git diff --check`
- mirrored package file presence checks.
- status consistency grep for package README, milestone index, and plan docs.
- closeout gate wording grep.
- unresolved P1/P2 blocker guard.
- concrete demo anchor sweep.
- changed-file scope guard.
- trailing whitespace grep.

Runtime, backend, frontend, schema execution, fixture, migration, and test
implementation checks are intentionally not part of the documentation-stage
pass unless final reviewers request fresh evidence later.
