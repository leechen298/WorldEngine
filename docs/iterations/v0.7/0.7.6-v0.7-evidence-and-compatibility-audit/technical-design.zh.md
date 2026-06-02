# Technical Design

## Audit Artifact

`audit-report.md` 是 primary output，应包含：

- reviewed child package table。
- evidence traceability table。
- compatibility assessment。
- scope assessment。
- unresolved findings。
- handoff recommendation。

## Traceability Checks

使用 file-existence checks 验证 required reviews and evidence：

- parent `review.md`。
- `0.7.0` 到 `0.7.5` 的 child `review.md` files。
- `0.7.5` `evidence-matrix.md`。

使用 status consistency searches，确认 closeout 后 parent 指向下一 child。

使用 changed-file scope guard，确认 active diff 只落在 v0.7 docs、v0.7 public contracts 和已批准的
checker/test files。

## Compatibility Rules

- Audit 只记录 evidence，不改变 behavior。
- Checker/schema PASS 不是 runtime/API/frontend PASS。
- Saved-result checker PASS 不是 live Agent 或 full autonomous PASS。
- Release-candidate recommendation 不是 final release。

## Output Rule

任何 blocker 必须同时记录在 `audit-report.md` 和 `review.md`。
