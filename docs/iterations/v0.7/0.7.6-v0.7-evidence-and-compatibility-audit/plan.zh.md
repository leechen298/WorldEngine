# Plan

## Phase 1: Draft Audit Package

1. 创建 package docs 和中文镜像。
2. 创建 `audit-report.md` 和中文镜像。
3. 运行 documentation and evidence traceability checks。

## Phase 2: Review Evidence

1. 确认 completed child review files 存在。
2. 确认 `0.7.5` evidence 只支持 scoped checker/schema claims。
3. 确认 skipped/out-of-scope checks 仍被排除。
4. 确认 changed files 留在 approved v0.7 scope。

## Phase 3: Evaluators

1. Use documentation/audit evaluator。
2. Use mirror/scope evaluator。
3. 修复 blockers 或停止。

## Phase 4: Handoff

1. 更新 review evidence。
2. Evaluator approval 后，更新 parent route/status surfaces 到 `0.7.7`。

## Stop Conditions

- Missing child review evidence。
- Unresolved P1/P2。
- Scope guard reports out-of-scope files。
- Audit text 把 release-candidate recommendation 写成 final release。
