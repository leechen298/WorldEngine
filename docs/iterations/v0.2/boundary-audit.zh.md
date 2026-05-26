# v0.2 Boundary Audit

状态：0.2.9 audit evidence

本 audit 检查 active v0.2 documentation 和 evidence 是否仍在 generic
recursive-world foundation boundary 内。它不改变 runtime、schema、API、
frontend、fixture、migration 或 test implementation behavior。

## Audit Inputs

- `AGENTS.md`
- `CLAUDE.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/external-fixture-boundary.md`
- `docs/validation-report-template.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`
- `docs/contracts/event-ref-contract.md`
- completed v0.2 package reviews through 0.2.8
- `docs/iterations/v0.2/findings.md`

## Boundary Results

| Boundary | Result | Evidence | Notes |
|---|---|---|---|
| External consumer boundary | pass | `docs/external-fixture-boundary.md`、`docs/validation-report-template.md`、0.2.5 review | Core 可定义 public contracts 和 redacted report formats；concrete validation-world internals 仍在仓库外。 |
| Concrete fixture boundary | pass | 0.2.5 review 与当前 v0.2 scope docs | Active concrete external-world fixture data 已移除，并由 generic schema smoke coverage 替代。Historical 0.2.4 artifacts 仅保持 historical。 |
| Generic schema boundary | pass | EntityRef、WorldCell、WorldSpec contract docs，以及 0.2.2 和 0.2.7 reviews | Schemas 已实现并测试，但不声明 loader、runtime bridge、persistence migration、generation 或 projection behavior。 |
| Event reference boundary | pass | EventRef contract，以及 0.2.3 和 0.2.8 reviews | Event refs 是 additive 且 event-local。未声明 resolver、causality engine、runtime binding、memory link 或 projection behavior。 |
| Runtime compatibility boundary | pass with handoff | `docs/current-implementation.md`、`docs/backend-implementation.md`、completed code-package reviews | Reviews 记录没有有意改变 runtime/API/frontend behavior。完整 legacy compatibility review 仍属 0.2.10。 |
| Legacy directory boundary | pass with handoff | `AGENTS.md`、`docs/current-implementation.md`、`docs/backend-implementation.md` | `backend/worldengine/` 仍为 legacy，0.2.9 不修改它。0.2.10 将更详细记录该 boundary。 |
| Future-scope boundary | pass | `docs/scope-boundaries.md`、`docs/roadmap.md`、`docs/iterations/v0.2/v0.2-plan.md` | Loader、runtime bridge、agent loop、memory、self-continuity、generation、projection API、product UI、external fixture repository 和 external validation repository 仍是 planned 或 not implemented。 |
| Status consistency | pass after 0.2.9 updates | v0.2 index 和 detailed plan 的 English/Chinese mirrors | 0.2.7 与 0.2.8 plan/index drift findings 通过把 detailed plan statuses 同步为 `review complete` 关闭；本 audit 后 0.2.9 标记为 `review complete`。 |
| Changed-file scope | pass | 0.2.9 verification commands | Changed files 限于批准的 v0.2 documentation 和本 package review evidence。 |

## Path Sanity Checks

本 audit 使用既有文件作为 evidence，不创建新的 runtime surfaces。必要路径类别存在：

- `docs/` 下的 active direction docs。
- `docs/contracts/` 下的 contract docs。
- `docs/iterations/v0.2/` 下的 v0.2 package docs。
- `docs/current-implementation.md` 和 `docs/backend-implementation.md`
  中的 active backend map docs。

0.2.9 不需要 external repository path、fixture repository、validation
runner internals、frontend implementation path、migration path 或
`backend/worldengine/` changes。

## Concrete Anchor Sweep Summary

0.2.9 verification 使用 temporary untracked pattern file，并只在本文档中记录
abstract result categories。Sweep 范围包括 active direction docs、contract
docs、0.2.9 audit docs、v0.2 plan/index docs，以及 0.2.9 package docs。

Result：完整 v0.2 plan/index sweep 只在 milestone index 中发现被取代的
0.2.4 package 的 historical-artifact references。针对 active direction、
contract、audit 和 0.2.9 package docs 的 sweep 以 no matches 退出。

允许的 residual categories 位于本 audit active-doc sweep 范围之外：

- historical v0.1 与 v0.2 package evidence。
- 0.2.4 historical artifact documentation。
- 描述既往 cleanup work 或 abstract sweep categories 的 review text。

这些 residual categories 不是 active direction，不能成为 future
implementation inputs。

## Status Drift Review

0.2.9 implementation 前，`findings.md` 跟踪：

- `v0.2-P2-001`：detailed v0.2 plan 仍将 0.2.7 标记为
  `ready for review`，而 milestone index 已标记为 `review complete`。
- `v0.2-P2-002`：detailed v0.2 plan 仍将 0.2.8 标记为
  `ready for review`，而 milestone index 已标记为 `review complete`。

0.2.9 通过把 English 和 Chinese detailed v0.2 plan status fields 同步为
`review complete` 解决这两个问题。`findings.md` 现在记录这些 items 已关闭。

## Handoff Limits

- 0.2.10 应执行 detailed v0.1 runtime scaffold compatibility 和 legacy
  boundary review。
- 0.2.11 只能在 0.2.10 review 后准备 release-candidate evidence。
- v0.3 loader 或 runtime bridge work 不能把本 audit 当作隐含 implementation
  approval；它仍需要 reviewed package contract。
