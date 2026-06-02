# Test Plan

Status: documentation-stage test plan

## Documentation Gate

```bash
git diff --check
```

Expected result: passed with no output.

```bash
python3 -c '<0.8.0 through 0.8.7 required child docs and mirrors check>'
```

Expected result: `missing_child_docs=0`.

```bash
python3 -c '<release-candidate evidence reference existence check>'
```

Expected result: all package reviews, audit report, testing result docs, and
contract artifacts named in `release-candidate-summary.md` exist.

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result before review: parent status
`in progress / 0.8.7 ready for review`, active child
`0.8.7-v0.8-release-candidate-bundle`, route
`documentation-review-needed`, and implementation/evidence/audit/release
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

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Allowed matches must be in forbidden, non-claim, redaction-check, audit,
release-candidate, or historical handoff contexts. No match may be accepted as
current v0.8 readiness, external validation PASS, product readiness, private
detail, or final-readiness evidence.

## Code Tests

This package is documentation-only. It must not run runtime, schema, API,
frontend, E2E, Agent smoke, autonomous, checker implementation, fixture,
migration, external validator/app, deployment, generated-result, or
`backend/worldengine/` tests.

The release-candidate summary may reference already executed current-session
evidence from reviewed v0.8 packages. It must label those references with the
original package boundary.

## Review Criteria

Review passes only if:

- required docs and mirrors exist.
- release-candidate evidence references resolve.
- parent and child status surfaces are synchronized.
- summary claims stay inside reviewed evidence.
- exclusions remain explicit.
- no unresolved P1 or blocking P2 remains.
- no final v0.8 release or readiness claim is made.
