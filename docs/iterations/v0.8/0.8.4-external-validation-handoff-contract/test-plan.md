# Test Plan

Status: documentation-only verification plan

## Documentation Shape

```bash
python3 -c '<0.8.4 required child docs and mirrors check>'
```

Expected result: `0.8.4-external-validation-handoff-contract missing_child_docs=0`.

Required files:

- `README.md` / `README.zh.md`
- `intent.md` / `intent.zh.md`
- `contract.md` / `contract.zh.md`
- `technical-design.md` / `technical-design.zh.md`
- `test-plan.md` / `test-plan.zh.md`
- `plan.md` / `plan.zh.md`
- `review.md` / `review.zh.md`

## Status Consistency

Check parent and child surfaces for:

- parent status `in progress / 0.8.4 ready for review`.
- active child `0.8.4-external-validation-handoff-contract`.
- route `documentation-review-needed`.
- package status `planned / ready for review`.
- implementation and evidence execution authorization `no`.

After review, the expected next state is:

- parent status `in progress / 0.8.5 child selected`.
- `0.8.4` status `review complete`.
- `0.8.5-core-working-state-smoke-evidence` status
  `selected / child docs not created`.
- implementation and evidence execution authorization `no`.

## Scope Guard

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Expected result: changed files are limited to:

- `docs/iterations/v0.8/**`.
- already reviewed `0.8.3` backend/app schema/helper/route/test files.

No new runtime, schema, API, frontend, backend test, checker, fixture,
migration, generated result, external repository, or `backend/worldengine/`
files may be introduced by this package.

## Text Guard

Search for forbidden overclaims and private-detail terms in the 0.8.4 package
and parent status files:

- external validation PASS.
- product readiness PASS.
- projection application readiness PASS.
- frontend/E2E PASS.
- Agent smoke PASS.
- autonomous PASS.
- final v0.8 readiness PASS.
- private repository path examples.
- UI selectors.
- oracle internals.
- raw prompts.
- provider traces.
- secrets.

Allowed matches must appear only in forbidden, non-claim, redaction, or test
guard contexts.

## Formatting

```bash
git diff --check
python3 -c '<v0.8 markdown whitespace check>'
```

Expected result: no diff whitespace errors, no trailing whitespace, and no tab
characters in v0.8 Markdown files.

## Runtime / Implementation Tests

No runtime, schema, API, frontend, E2E, Agent smoke, autonomous, external
validation, checker, fixture, migration, generated-artifact, or
`backend/worldengine/` tests are run by this documentation-only package.

Existing `0.8.3` backend test evidence remains recorded in that package; this
package does not broaden or rerun it.
