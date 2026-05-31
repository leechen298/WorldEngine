# 契约

状态：final / closeout complete

## Package 决策

`0.5.7` 是 documentation-only final closeout。只有 final verification 和 closeout consistency evaluator approval 通过后，才可更新 final status。

Implementation authorization 保持 `no`。

## Closeout Criteria

只有满足以下条件后，v0.5 才可标记为 `final / closeout complete`：

- Child packages `0.5.1` 到 `0.5.6` 均为 review complete。
- Final docs/mirror checks 通过。
- Final changed-file scope guard 通过。
- Final forbidden-surface sentinel 通过。
- Final focused backend compatibility 通过。
- Final full backend regression 通过。
- Final unresolved finding classification 无 P1/P2。
- Closeout consistency evaluator 通过。

## 最终纳入能力

v0.5 收口时包含：

- Working-memory 和 episodic-memory contracts。
- Additive backend memory schemas。
- Generic in-memory memory substrate。
- Agent Loop perception 中的 bounded read-only memory context。
- Relationship state、self-summary、reflection records 和 personality drift signals 的 refined deferred contracts。
- Final closeout 前已评审 release-candidate bundle。

## 最终排除能力

v0.5 收口时不包含：

- Durable persistence。
- Public memory APIs。
- Vector retrieval 或 indexing。
- Self-summary generation。
- Automatic reflection。
- Relationship behavior。
- Personality drift action modifiers。
- Frontend product behavior。
- World generation。
- External validation readiness 或 report automation。
- Projection application readiness。

## Final Verification Matrix

必需 final commands：

- `git diff --check`
- v0.5 parent 和 child packages 的 required docs/mirrors check。
- Baseline-aware changed-file scope guard。
- 针对 `backend/worldengine`、frontend、alembic 和 migrations 的 forbidden-surface sentinel。
- Focused v0.5 memory/loop/action backend compatibility。
- Full backend regression。

## Status Surfaces

Evaluator approval 后同步：

- `docs/iterations/v0.5/CURRENT_STATE.md`
- `docs/iterations/v0.5/CURRENT_STATE.zh.md`
- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/v0.5-plan.md`
- `docs/iterations/v0.5/v0.5-plan.zh.md`
- `docs/iterations/v0.5/review.md`
- `docs/iterations/v0.5/review.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`

## 允许修改

- 本 package 下的 final closeout docs 和 mirrors。
- Parent v0.5 status surfaces。
- Roadmap 中 v0.5 final handoff 相关 status lines。

## 禁止修改

- 不修改 implementation files。
- 不修改 `backend/worldengine/**`、frontend、migration、fixture、generated result、external repository，不创建 release tag 或 push。
- 不声明未运行的 validation。
