# Test Plan

状态：documentation-only verification plan

## Documentation Shape

```bash
python3 -c '<0.8.4 required child docs and mirrors check>'
```

预期结果：`0.8.4-external-validation-handoff-contract missing_child_docs=0`。

Required files：

- `README.md` / `README.zh.md`
- `intent.md` / `intent.zh.md`
- `contract.md` / `contract.zh.md`
- `technical-design.md` / `technical-design.zh.md`
- `test-plan.md` / `test-plan.zh.md`
- `plan.md` / `plan.zh.md`
- `review.md` / `review.zh.md`

## Status Consistency

检查 parent 和 child surfaces：

- parent status `in progress / 0.8.4 ready for review`。
- active child `0.8.4-external-validation-handoff-contract`。
- route `documentation-review-needed`。
- package status `planned / ready for review`。
- implementation 和 evidence execution authorization 均为 `no`。

Review 后预期 next state：

- parent status `in progress / 0.8.5 child selected`。
- `0.8.4` status `review complete`。
- `0.8.5-core-working-state-smoke-evidence` status
  `selected / child docs not created`。
- implementation 和 evidence execution authorization 均为 `no`。

## Scope Guard

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

预期结果：changed files 限制在：

- `docs/iterations/v0.8/**`。
- already reviewed `0.8.3` backend/app schema/helper/route/test files。

本 package 不得新增 runtime、schema、API、frontend、backend test、checker、fixture、
migration、generated result、external repository 或 `backend/worldengine/` files。

## Text Guard

在 0.8.4 package 和 parent status files 中搜索 forbidden overclaims 与 private-detail terms：

- external validation PASS。
- product readiness PASS。
- projection application readiness PASS。
- frontend/E2E PASS。
- Agent smoke PASS。
- autonomous PASS。
- final v0.8 readiness PASS。
- private repository path examples。
- UI selectors。
- oracle internals。
- raw prompts。
- provider traces。
- secrets。

允许的命中只能位于 forbidden、non-claim、redaction 或 test guard contexts。

## Formatting

```bash
git diff --check
python3 -c '<v0.8 markdown whitespace check>'
```

预期结果：无 diff whitespace errors，无 trailing whitespace，v0.8 Markdown files 中无 tab
characters。

## Runtime / Implementation Tests

本 documentation-only package 不运行 runtime、schema、API、frontend、E2E、Agent smoke、
autonomous、external validation、checker、fixture、migration、generated-artifact 或
`backend/worldengine/` tests。

既有 `0.8.3` backend test evidence 仍记录在该 package；本 package 不扩大或重跑它。
