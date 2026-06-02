# Review

状态：planned / ready for review

parent_implementation_authorized: no
active_child_package: none
active_child_implementation_authorized: no
active_child_evidence_execution_authorized: no

## Parent Review State

Parent v0.8 documentation package 已修订，等待 review。

本次修订用 “Minimum Proved Working WorldEngine / External Validation Readiness”
替换旧的 external-projection-application framing。修订后的范围把 external validation
function 和 external application 留在本仓库外，同时要求 WorldEngine 定义 core-side
readiness、observable public surfaces、evidence boundaries 和 handoff contracts，
供后续 external validator 消费。

Planned `0.8.x` child packages 只是 route-map specifications。它们不是 active child
contracts，不是 implementation authorization，不是 evidence execution authorization，
也不是 closeout evidence。

## Subagent / Evaluator Findings

- Target/scope reviewer `019e875e-031e-7c73-82d3-18d41fc31784` 未发现 P1。它发现
  P2：v0.7 handoff 中仍有旧 v0.8 目标引用，以及 v0.7 external-validation-readiness
  concepts 与 v0.8 minimum working-state / external-validation handoff readiness
  之间的边界表述存在歧义。收窄范围后，这些 findings 只在 v0.8 parent docs 中处理：
  v0.7 保持 historical closeout material，v0.8 自己声明新目标，不重写已完成的 v0.7
  child packages。
- Mirror/status reviewer `019e875e-3140-73d1-82be-56668572256e` 未发现
  P1/P2/P3。它确认 v0.8 parent 有 12 个 markdown files、无 child directories、
  9 个 planned child package sections 都包含 required fields，status/authorization
  language 一致，且 `git diff --check` clean。

Subagents 没有授权或执行 runtime、schema、API、frontend、checker、fixture、migration、
external validation 或 external application work。

## Changed Files

Authoritative roadmap and boundary files：

- `docs/roadmap.md`
- `docs/scope-boundaries.md`

Version-level v0.8 documentation files：

- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/v0.8-plan.zh.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/review.zh.md`

Working tree 还包含独立的 v0.7 checker/schema repair state，位于 `docs/contracts/`、
`docs/testing/`、`tools/testing/`，以及 untracked
`docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/` package。本 review
不把这些文件当成 v0.8 implementation、validation evidence、external validator work
或 external application work。

本 v0.8 parent revision 故意不更新已完成的 v0.7 child package historical docs。v0.7
旧文档中把 v0.8 描述为 projection-application readiness 的说法，只作为 historical context，
并由当前 v0.8 parent docs supersede。

本 parent revision pass 不意图创建 v0.8 child package directories 或 files。

## Commands Run

```bash
git status --short --branch
```

Result：branch `v0.7-local`；status 显示 v0.8 parent docs、roadmap/scope docs，以及独立的
v0.7 checker/schema repair state。本 parent pass 没有引入 v0.8 runtime、API、frontend、
fixture、migration、external repository、external validator 或 external app files。

```bash
git diff --check
```

Result：passed with no output。

```bash
python3 -c '<v0.8 parent required-file check>'
```

Result：`missing=0`。

```bash
python3 -c '<v0.8 planned package required-field check>'
```

Result：`planned_package_count=9`，`planned_package_missing_fields=0`。

```bash
python3 -c '<v0.8 markdown shape and whitespace check>'
```

Result：`markdown_files=12`，`child_dir_files=0`，`trailing_whitespace=0`，
`tab_lines=0`。

```bash
python3 -c '<v0.8 status and authorization guard>'
```

Result：`required_status_missing=0`，`forbidden_status_lines=0`。

```bash
rg -n 'v0\.8[^\n]*projection application readiness|projection application readiness[^\n]*v0\.8|v0\.8 projection app|first external projection|First External Projection Application|projection-application-readiness' docs/iterations/v0.8 docs/roadmap.md docs/scope-boundaries.md --glob '!review*.md'
```

Result：退出码 `1`，无 matches。

该搜索故意排除已完成的 v0.7 historical docs。v0.7 历史文档中曾把 v0.8 描述为
projection-application readiness 的说法，由当前 v0.8 parent docs supersede，而不是回写改动。

## Compatibility Review

本次只修改 documentation direction，不修改 runtime、schema、API、frontend、backend
tests、fixtures、migrations、generated results、external repositories、external
validator code、external application code 或 `backend/worldengine/`。

修订后的 v0.8 plan 继续把 v0.7 evidence 只当作 handoff context，并保持 v0.7
post-closeout blockers 可见。Historical evidence 不提升为 v0.8 PASS evidence。

## Scope Review

Scope 仍为 documentation-only。

修订后的 v0.8 scope 明确禁止实现 external validation function、external projection
application、product UI、concrete external validation worlds、private runner details、
oracle internals、hidden reset APIs、private repository paths、provider traces、
secrets、app-specific backend logic、durable persistence、migrations 或新的
`backend/worldengine/` runtime features，除非后续 reviewed child package 明确授权更窄的
core-side scope。

## Unresolved Findings

- P3：Parent v0.8 docs 已修订，并经过两个 subagent review passes，但仍需要 human
  review，之后才能开始 child package、implementation 或 evidence execution。
- P3：Working tree 包含独立的 v0.7 checker/schema repair changes。没有后续 reviewed
  handoff 时，不得把它们混入 v0.8 readiness claims 或当作 v0.8 evidence。

## Final Assessment

当前值：`planned / ready for review`。

Parent v0.8 documents 现在将 v0.8 定义为 minimum proved working WorldEngine
readiness 加 external-validation handoff readiness。它们不授权 implementation、
external validation execution、external application work 或 readiness PASS claims。
