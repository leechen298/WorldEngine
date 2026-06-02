# Contract

## 公共概念

- `FinalCloseout`：确认 v0.8 package evidence 和 final verification 足以将 v0.8 campaign
  标记为 final 的文档决策。
- `FinalVerification`：由本包 review 授权、并在 final status changes 前记录的 current-session
  commands。
- `FinalExclusion`：final v0.8 closeout 仍明确不声明的 surfaces。
- `FinalDisposition`：取值为 `final_ready`、`blocked` 或 `defer_pending_review`。

## 允许变更

Documentation stage：

- 创建或更新本包文档和中文镜像。
- 创建 `final-closeout-summary.md` 和 `final-closeout-summary.zh.md`。
- 记录 final evidence references、compatibility review、scope review、exclusions、
  unresolved findings 和 review gates。
- 将父级 v0.8 status surfaces 更新为本包 ready-for-review。

Documentation review 显式授权 final verification 后：

- 只运行 `test-plan.md` 中列出的或 evaluator 批准的 final verification commands。
- 填写 final verification results 和 final disposition。
- 只有 final verification 与 evaluator approval 都通过时，才把 parent v0.8 status 更新为 final。

## 禁止变更

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository、external validator、external application、
  deployment 或 `backend/worldengine/` files。
- 不在 final closeout 中 repair failures。
- 不声明 external validation PASS、external consumer PASS、product readiness、frontend/E2E
  PASS、Agent smoke PASS、autonomous PASS、generation-quality PASS、deployment readiness、
  external app implementation 或 external validator implementation。
- 不把 v0.7 handoff evidence 转换成 v0.8 product 或 external validation evidence。
- 不授权 v0.9 或 future implementation work。

## 必须覆盖的收口面

Final closeout summary 必须包含：

- `0.8.0` 到 `0.8.8` 的 status matrix。
- final verification command matrix。
- compatibility matrix。
- exclusions and non-claims。
- unresolved finding matrix。
- final disposition。

## 收口规则

只有满足以下条件时，v0.8 才可标记 final：

- final verification commands 通过，或被明确分类为 skipped/out of scope 且不影响 final claim。
- 无 unresolved P1 或 blocking P2。
- parent and child status surfaces synchronized。
- evaluator review approves final closeout。
