# 契约

状态：review complete

## Package 决策

`0.5.6` 是 documentation-only。它准备 release-candidate bundle 供 review，但不声明
final release。

Implementation authorization 保持 `no`。

## 纳入 v0.5 的能力

- Working memory schema semantics 和 additive backend record model。
- Episodic memory schema semantics 和 additive backend record model。
- Process-local generic in-memory agent memory substrate。
- Agent Loop perception 中的 bounded read-only memory context。
- Relationship state、self-summary、reflection records 和 personality drift signals
  的细化 contracts，implementation 继续 deferred。

## Deferred Scope

- Durable persistence。
- Public memory APIs。
- Vector retrieval 或 indexing。
- Self-summary generation。
- Automatic reflection。
- Relationship behavior。
- Personality drift action modifiers。
- World generation。
- External validation readiness 和 report automation。
- Projection application readiness。
- Frontend product behavior。

## 纳入的证据

Bundle 纳入 `0.5.5` audit evidence：

- focused v0.5 memory/loop/action compatibility：`33 passed`。
- full backend regression：`145 passed`。
- docs/mirror checks：`missing=0`。
- changed-file scope guard：`out_of_scope=0`。
- forbidden implementation surface sentinel：无输出。
- evidence/compatibility evaluator PASS，且无 P1/P2/P3 findings。

## Reviewer Checklist

Reviewer 应确认：

- `0.5.1` 到 `0.5.5` 所有 child packages 都是 review complete。
- Implementation-bearing packages 具备 authorization 和 required evaluators。
- 纳入能力未超过 v0.5 scope。
- Deferred capabilities 没有被意外实现。
- 当前 evidence 是 v0.5 evidence，而不是 v0.4 handoff evidence。
- 无 unresolved P1/P2。
- 本 package 未声明 final release。

## Final Closeout 前置条件

`0.5.7` 仍必须：

- 重新检查 parent 和 child status consistency。
- 运行 final docs/mirror/scope checks。
- 运行 required final verification matrix。
- 运行 closeout consistency evaluator。
- 只有 evidence consistency 通过后才更新 final status。

## 允许修改

- 本目录下的 package docs 和 mirrors。
- 仅为准确交接更新 parent v0.5 status/review surfaces。

## 禁止修改

- 不修改 implementation files。
- 不声明 final release。
- 不设置 `final / closeout complete` status。
- 不创建 release tag 或 push。
- 不修改 `backend/worldengine/**`、frontend、migration、fixture 或 external repository。
