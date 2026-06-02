# Test Plan

Status: documentation-stage audit plan

## Documentation Gate

```bash
git diff --check
```

Expected result: passed with no output.

```bash
python3 -c '<0.8.0 through 0.8.6 required child docs and mirrors check>'
```

Expected result: `missing_child_docs=0`.

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result before audit execution: parent status
`in progress / 0.8.6 ready for review`, active child
`0.8.6-v0.8-evidence-and-boundary-audit`, route
`documentation-review-needed`, and implementation/evidence/audit execution
authorization `no`.

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Expected result: changed files are limited to `docs/iterations/v0.8/**` plus
already reviewed `0.8.3` backend/app schema/helper/route/test files.

```bash
python3 -c '<v0.8 Markdown whitespace check>'
```

Expected result: no trailing whitespace and no tab characters.

## Audit Execution Authorization

Do not fill final audit results until `review.md` records
`audit_execution_authorized: yes`.

After documentation review, authorized documentation-only audit checks may
include:

```bash
python3 -c '<evidence reference existence check for 0.8.0 through 0.8.5 reviews and named result docs>'
```

```bash
python3 -c '<package status and unresolved finding matrix check>'
```

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Allowed matches must be in forbidden, non-claim, redaction-check, or
historical handoff contexts.

## Code Tests

This package is documentation-only. It should not run runtime, schema, API,
frontend, E2E, Agent smoke, autonomous, checker implementation, fixture,
migration, external validator/app, or `backend/worldengine/` tests. It may
reference already executed evidence from reviewed packages.

## Audit Closeout Criteria

Audit closeout requires:

- evidence references resolve.
- no unresolved P1 or blocking P2 remains.
- skipped/out-of-scope checks remain visible.
- status surfaces stay synchronized.
- release-candidate recommendation is `recommended`, `blocked`, or
  `defer_pending_review` with explicit rationale.
