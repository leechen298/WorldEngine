# Contract

状态：`archived evidence only / not executed in current campaign`

## Public concepts

- Reviewed branch：execution 期间记录的 branch。
- Reviewed commit：execution 期间记录的精确 commit。
- Command evidence：command、purpose、exit code 和 output summary。
- Blocker：validation 无法运行或完成的原因。
- Final assessment：`passed`、`passed with P3`、`blocked`、`failed` 或
  `not executed` 之一。

## 允许修改

后续 execution pass 期间，除非 separate approved plan 允许更广的 documentation updates，
只能更新本 package 的 report 和 review。

validation-fix pass 期间，只能更新本 package 的 validation evidence、status fields，
以及记录 blocker 或 rerun result 所需的 milestone finding rows。

如果 prior blocker 是 validation infrastructure 或 execution environment 导致，而不是
已确认的 v0.2 product failure，本 package 可以在 runner 或 execution-environment correction
后重新执行。历史 evidence 必须保留可见，不得改写为 passed。

## 禁止修改

- 不从本 execution package 修改 runtime、schema、API、frontend、backend tests、
  fixtures 或 migrations。
- 不在 execution 前硬编码 branch 或 commit。
- 不把 Playwright config 的存在当成 browser E2E 可运行的证明。
- 不为未运行的 checks 声明 success。
- 不隐藏 blockers。

## 兼容性要求

execution 必须把 observed behavior 与 v0.2 release claims 对比，但不改变 v0.2 status。
claim conflicts 应成为 findings，而不是静默编辑 release docs。

## 范围外 follow-ups

- 修复 failed checks。
- 增加 E2E infrastructure。
- 改变 v0.2 implementation 或 release status。
