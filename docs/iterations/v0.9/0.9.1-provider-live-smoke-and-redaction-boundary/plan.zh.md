# Plan

英文原文：`plan.md`。

## 有序步骤

1. 阅读 v0.9 parent docs 和本 package document set。
2. 运行 `test-plan.md` 中的 documentation checks。
3. 把本包交给 read-only documentation/contract evaluator。
4. 修复或记录 evaluator findings。
5. 如果没有 P0/P1/blocking P2，更新 `review.md` 为
   `implementation_authorized: yes`；否则在 code changes 前停止。
6. 在 `backend/app/` 实现最小 provider smoke path。
7. 添加 public provider summary schemas 和 redaction tests。
8. 保持 `/manifest` compatibility 和 existing public handoff tests。
9. 运行 focused backend tests。
10. 只有当 checker support 被修改时运行 checker tests。
11. 如果 code changes 触及 shared backend surfaces，运行 backend regression。
12. 更新 `review.md`，记录 commands、results、compatibility review、scope review、
    unresolved findings、final assessment 和 handoff to `0.9.2`。

## 阶段边界

Documentation phase：

- 创建并 review package documents。
- authorization 前不得修改 runtime、API、schema、test、checker、provider 或 fixture files。

Implementation phase：

- 只有本 package review 记录 `implementation_authorized: yes` 后才可开始。
- 必须留在 allowed backend/checker/test scope 内。

Evidence execution phase：

- Live provider calls 是 optional 且必须 bounded。
- 如果没有 provider key 或 network，记录 `not_configured` 或 `blocked`，不是 PASS。

## Stop Conditions

如出现以下情况则停止：

- package docs 缺失或冲突。
- evaluator 报告 unresolved P0/P1/blocking P2。
- implementation 需要 Validation Client changes。
- implementation 需要 concrete world content。
- smoke evidence 会暴露 keys、raw prompts、raw responses、raw traces 或 private account details。
- provider behavior 扩展成 world generation。
- tests 无法证明 unconfigured behavior 和 redaction。

## Review Update Step

closeout 前，`review.md` 必须记录：

- changed files。
- commands run。
- test results。
- live provider status 或 blocked/not-configured status。
- compatibility review。
- scope review。
- unresolved P1/P2/P3 findings。
- final assessment 和 handoff。
