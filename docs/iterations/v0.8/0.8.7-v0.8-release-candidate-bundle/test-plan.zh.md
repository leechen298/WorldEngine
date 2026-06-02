# Test Plan

状态：documentation-stage test plan

## Documentation Gate

```bash
git diff --check
```

Expected result：passed with no output。

```bash
python3 -c '<0.8.0 through 0.8.7 required child docs and mirrors check>'
```

Expected result：`missing_child_docs=0`。

```bash
python3 -c '<release-candidate evidence reference existence check>'
```

Expected result：`release-candidate-summary.md` 中命名的 package reviews、audit report、testing
result docs 和 contract artifacts 全部存在。

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result before review：parent status
`in progress / 0.8.7 ready for review`，active child
`0.8.7-v0.8-release-candidate-bundle`，route
`documentation-review-needed`，implementation/evidence/audit/release authorization 均为
`no`。

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Expected result：changed files 限制在 `docs/iterations/v0.8/**` 加已 review 的 `0.8.3`
backend/app schema/helper/route/test files。

```bash
python3 -c '<v0.8 Markdown whitespace check>'
```

Expected result：无 trailing whitespace，无 tab characters。

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Allowed matches 必须处于 forbidden、non-claim、redaction-check、audit、release-candidate 或
historical handoff contexts。不得把任何 match 接受为 current v0.8 readiness、external
validation PASS、product readiness、private detail 或 final-readiness evidence。

## Code Tests

本 package 是 documentation-only。不得运行 runtime、schema、API、frontend、E2E、Agent smoke、
autonomous、checker implementation、fixture、migration、external validator/app、deployment、
generated-result 或 `backend/worldengine/` tests。

Release-candidate summary 可以引用 reviewed v0.8 packages 中已执行的 current-session evidence，
但必须标注原 package boundary。

## Review Criteria

Review 通过条件：

- required docs and mirrors exist。
- release-candidate evidence references resolve。
- parent 和 child status surfaces synchronized。
- summary claims stay inside reviewed evidence。
- exclusions remain explicit。
- no unresolved P1 or blocking P2 remains。
- 不创建 final v0.8 release 或 readiness claim。
