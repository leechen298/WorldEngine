# Technical Design

## Primary Artifact

`final-closeout.md` 是 v0.7 final closeout record，记录 final status decision、evidence、
exclusions 和 v0.8 handoff boundary。

## Final Verification Groups

- checker regression：`tools/testing`。
- CLI validation：readiness manifest 和 projection read-model。
- JSON syntax：v0.7 report schema、readiness manifest schema/json、projection read-model schema。
- evidence links：所有 child reviews 以及 evidence/audit/release-candidate artifacts。
- formatting：`git diff --check`。
- scope：changed-file scope guard。
- status：final update 后 parent and child status consistency。

## Final Output Rule

任何 final command 或 evaluator 报告 blocker 时，final status 必须保持 not complete，并记录 blocker。
