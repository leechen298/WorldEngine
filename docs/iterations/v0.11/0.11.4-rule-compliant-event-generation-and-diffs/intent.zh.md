# 意图

英文源文件：`intent.md`。

状态：文档已起草 / 等待评审

## 问题 / 目的

v0.11 已有公开 session rules 和公开 direction guidance，但世界仍需要通过可检查的 event/diff 路径变化。本包把 rule 和 direction 输入连接到一个小型、公开、受 legality gate 约束的 evolution step。

## 为什么现在做

`0.11.2` 让 session rules 可附加，`0.11.3` 把用户 direction 做成有边界的队列。`0.11.4` 是第一个允许把这些公开输入转成 legal event candidates 和 applied public diffs 的 package。

## Roadmap 关系

本包推进 v0.11 rule-bound world evolution 里程碑。它仍不关闭完整 MVP，不证明 provider-backed generation quality，也不实现 Agent autonomy。它为 `0.11.5` 的 worldview fidelity validation 准备 public evolution evidence。

## 非目标

- 不实现完整 narrative simulation。
- 不实现 autonomous Agent loop 或 pseudo-self。
- 不调用 provider。
- 不实现 Validation Client，也不执行外部验证。
- 不实现 frontend。
- 不新增持久化或迁移。
- 不增加具体 demo-world fixtures。
- 不修改 `backend/worldengine/`。

## 预期交接

`0.11.5-worldview-fidelity-and-v0.11-validation` 将接收 rule-linked accepted/rejected event evidence、public state diffs、direction refs、可 replay event records，以及 session/runtime compatibility evidence。
