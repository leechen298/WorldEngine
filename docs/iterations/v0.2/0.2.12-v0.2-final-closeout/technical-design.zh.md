# Technical Design

英文版本：`technical-design.md`

## Design Summary

0.2.12 是 documentation-only status and evidence closeout。它没有 runtime
architecture、schema migration、API design、frontend design、fixture design 或 test
implementation design。

Review approval 之后的 implementation stage 只应更新用于表达 final milestone status
和 final review evidence 的 documentation surfaces。

## Documentation Surfaces

Closeout implementation 可以更新：

- release docs：`docs/releases/v0.2.md`、`docs/releases/v0.2.zh.md`。
- milestone index docs：`docs/iterations/v0.2/README.md`、
  `docs/iterations/v0.2/README.zh.md`。
- detailed plan docs：`docs/iterations/v0.2/v0.2-plan.md`、
  `docs/iterations/v0.2/v0.2-plan.zh.md`。
- findings ledger：`docs/iterations/v0.2/findings.md`，仅在 final review 改变 finding
  state 或 handoff classification 时更新。
- package review docs：
  `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.md` 和
  `review.zh.md`。

## Status Model

Documentation-stage status：

- package README：`ready for review`。
- v0.2 milestone index：0.2.12 `ready for review`。
- v0.2 plan：0.2.12 `ready for review`。
- v0.2 release docs：在 implementation approval 前保持 release-candidate / not final。

Post-review implementation status，只有在 approved 后：

- 0.2.12 package 可变为 `review complete`。
- v0.2 milestone 可变为 final / complete。
- release docs 可带 closeout evidence 声明 final status。
- open P3 findings 可作为 accepted v0.3 handoffs 保留。

如果 final review rejects 或 conditionally blocks closeout：

- v0.2 保持 not final。
- unresolved P1/P2 blockers 保持 visible。
- 本包 review 记录 blocker，且不标记 final status。

## Evidence Model

Final closeout 必须区分：

- 0.2.1 到 0.2.11 package reviews 的 historical evidence。
- 0.2.12 中运行的 current-session documentation checks。
- reviewer decision evidence：approve、reject 或 condition closeout。

Documentation checks 不推导 implementation behavior。

## Mirror Requirements

每个 English package document 都有 Chinese mirror。Release、milestone、plan 或 review
docs 中 implementation-stage status wording 的变更，也必须同步到对应 Chinese document
中。

## Failure Handling

如果发现 P1/P2 blocker：

- 在 `review.md` 和 `review.zh.md` 中记录。
- 如 blocker 应持续到 session 之后，更新 `docs/iterations/v0.2/findings.md`。
- 保持 v0.2 not final。
- 在 final release wording 前停止。
