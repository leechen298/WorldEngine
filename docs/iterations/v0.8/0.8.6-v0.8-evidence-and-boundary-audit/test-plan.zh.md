# Test Plan

状态：documentation-stage audit plan

## Documentation Gate

```bash
git diff --check
```

Expected result：passed with no output。

```bash
python3 -c '<0.8.0 through 0.8.6 required child docs and mirrors check>'
```

Expected result：`missing_child_docs=0`。

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result before audit execution：parent status 为
`in progress / 0.8.6 ready for review`，active child 为
`0.8.6-v0.8-evidence-and-boundary-audit`，route 为
`documentation-review-needed`，implementation/evidence/audit execution authorization 均为
`no`。

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Expected result：changed files 限制在 `docs/iterations/v0.8/**` 加 already reviewed
`0.8.3` backend/app schema/helper/route/test files。

```bash
python3 -c '<v0.8 Markdown whitespace check>'
```

Expected result：无 trailing whitespace，无 tab characters。

## Audit Execution Authorization

`review.md` 记录 `audit_execution_authorized: yes` 前，不得填写 final audit results。

Documentation review 后，authorized documentation-only audit checks 可包括：

```bash
python3 -c '<evidence reference existence check for 0.8.0 through 0.8.5 reviews and named result docs>'
```

```bash
python3 -c '<package status and unresolved finding matrix check>'
```

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Allowed matches 必须处于 forbidden、non-claim、redaction-check 或 historical handoff
contexts。

## Code Tests

本 package 是 documentation-only。不得运行 runtime、schema、API、frontend、E2E、Agent
smoke、autonomous、checker implementation、fixture、migration、external validator/app 或
`backend/worldengine/` tests。它可以 reference reviewed packages 中 already executed
evidence。

## Audit Closeout Criteria

Audit closeout 需要：

- evidence references resolve。
- no unresolved P1 或 blocking P2 remains。
- skipped/out-of-scope checks remain visible。
- status surfaces stay synchronized。
- release-candidate recommendation 是 `recommended`、`blocked` 或
  `defer_pending_review`，并有 explicit rationale。
