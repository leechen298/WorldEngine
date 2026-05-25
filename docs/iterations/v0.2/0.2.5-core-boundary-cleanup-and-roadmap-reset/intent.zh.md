# 意图

英文版本：`intent.md`

## 问题

WorldEngine 的 core mission 是递归世界生成与运行引擎，包含 event、agent、
memory、feedback、projection 和 pseudo-self continuity substrates。它不是某个
specific concrete demo、concrete demo surface 或 product backend。

此前的 v0.2 documents 和 implementation artifacts 曾把 historical concrete fixture、
concrete demo surface、superseded concrete fixture direction 及相关 concrete terms
作为 fixture 或 validation anchors。这些 anchors 原本是为了让 schema work 更具体，
但现在会带来方向风险：

- Codex、Claude 或其他 coding agents 可能推断 core repository 应该知道 Demo
  world details。
- Future implementation 可能从 generic recursive world infrastructure 漂移成
  application-specific backend。
- Tests 和 fixtures 可能围绕 concrete locations、roles、resources 或 narrative rules
  塑造 engine contracts。
- External fixture worlds 可能误变成 upstream design drivers，而不是 public
  WorldEngine contracts 的 downstream consumers。

## 目标

0.2.5 准备一次 boundary cleanup，从 active WorldEngine planning、fixture data 和
fixture tests 中移除 concrete Demo world anchors，同时保留 v0.2 已建立的 generic
recursive world schema 和 event foundation。

implementation 后，core repository 只应保留：

- generic schema contracts。
- generic runtime contracts。
- generic event contracts。
- generic agent-in-world contracts。
- generic memory and self-continuity contracts。
- generic projection contracts。
- generic smoke tests。
- redacted validation report formats。

Future fixture worlds 和 validation worlds 应位于 core repository 之外，并通过 public
interfaces 消费 WorldEngine。

## 非目标

- 不创建 external fixture repository。
- 不创建 external validation repository。
- 不实现 WorldSpec loader。
- 不实现 runtime bridge。
- 不实现 Agent loop。
- 不实现 memory 或 self-continuity。
- 不实现 world generation。
- 不实现或替换 frontend dashboard。
- 不修改 v0.1 runtime behavior。
- 不引入另一个 concrete Demo world 来替换旧方向。

## 为什么现在做

v0.2 已建立 generic recursive-world schema language 和 event references。在 v0.3
loader 或 runtime bridge work 开始前，这是纠正 project direction 的合适时机。
如果 concrete Demo anchors 继续留在 active docs 和 tests 中，后续代码可能把它们当作
architecture facts。

0.2.5 应在 loader、runtime bridge、agent-in-world、memory、generation、validation
或 projection milestones 基于 v0.2 foundation 继续构建前，把边界写清楚。

## 北极星对齐

本 cleanup 把 concrete worlds 视为 external consumers，而不是 core identity，从而保持
WorldEngine 与 north star 对齐。core repository 继续作为 recursive worlds、event
evidence、agents living in worlds、memory continuity、self-continuity 和 projections
的 generic substrate。

cleanup 保留未来 worlds 需要的 schema vocabulary，同时移除“第一个可理解的 validation
surface 是 core engine 的一部分”这一暗示。
