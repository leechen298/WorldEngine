# 技术设计

英文版本：`technical-design.md`

## 当前状态

active v0.2 index 和 plan 仍需要一次 remaining-package reset。roadmap 也需要把
0.2.6 指向 workflow and plan reset，而不是 final closeout。release docs 是 draft
planning artifacts，必须保持 not released。

历史 v0.2 packages 可能包含 superseded concrete fixture detail。新的 automation
workflow 会让未来 agents 读取更广的 v0.2 context，因此这些 details 必须被抽象化，
以降低 scope drift 风险，同时保留历史 evidence。

## 契约对齐与不变量

- 所有变更都保持在 documentation 内。
- v0.2 状态保持 `planned / in progress`。
- release docs 保持 `draft / planned / not released`。
- 除本 package 必需的 v0.2 handoff wording 外，保持现有 v0.3 及之后的
  technical roadmap direction。
- 以抽象形式保留历史事实。

## 实现方案

1. 增加 0.2.6 package document set，并补齐中文镜像。
2. 增加 `00-chatgpt-plan.md` / `00-chatgpt-plan.zh.md`，作为后续 automation
   seed plan。
3. 增加 `development-workflow.md` / `development-workflow.zh.md`，记录
   ChatGPT / Codex A / Codex B loop、gates、severity model、evidence rules
   和 WorldEngine boundaries。
4. 增加 `final-review-bundle-template.md` /
   `final-review-bundle-template.zh.md`，记录 required review fields。
5. 更新 v0.2 index 和 plan docs，让 0.2.7 到 0.2.12 具有稳定的 planned names、
   types、boundaries、deliverables、verification expectations 和 handoffs。
6. 更新 roadmap v0.2 entries，匹配新的 package sequence。
7. 更新 release docs，让它们继续保持 draft / planned / not released，并把
   final closeout 放在 0.2.12 approval 之后。
8. 抽象化 v0.2 iteration docs 中残留的 historical concrete demo details。

## 影响范围

- `docs/iterations/v0.2/**`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`

## Data Model / Schema 变更

无。

## Runtime / Service 设计

无。

## 兼容性

本 package 不改变 runtime behavior、API response shape、schema validation behavior、
frontend behavior、tests、fixtures 或 external consumer contracts。

## 风险

- 风险：remaining-package planning 对后续 automation 来说不够细。
  缓解：执行 Detailed Plan Acceptance Gate。
- 风险：historical concrete detail 残留并影响后续 agents。
  缓解：使用 temporary untracked pattern file 做 concrete demo anchor sweep，
  并只以抽象分类记录 residuals。
- 风险：release docs 过度声称 final status。
  缓解：运行 release-status wording checks，并把 final closeout 放在
  0.2.12 review approval 之后。
