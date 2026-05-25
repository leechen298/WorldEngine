# 0.2.5 Core Boundary Cleanup And Roadmap Reset

英文版本：`README.md`

状态：`review complete`

类型：`mixed`

## 目标

从 WorldEngine core planning 中移除 concrete Demo world anchors，并为后续 cleanup
奠定边界，使 repository 继续聚焦在 generic recursive world runtime substrate。

本 package 存在的原因是：早期 v0.2 work 曾把 historical concrete fixture、
concrete demo surface 和 historical concrete fixture wording 用作 fixture 或
validation language。现在这些 wording 会带来风险，因为 future coding agents
可能把 WorldEngine 理解成 Demo application-specific backend，而不是通用引擎。

0.2.5 通过清理 active project direction、roadmap language、fixture data 和 fixture
tests 来重置边界。它也为未来 external fixture worlds 和 external validation consumers
保留 public interfaces，但本 package 不创建这些 repositories。

## 范围

最初的 documentation-planning pass 只创建本 iteration package，不修改 active roadmap、
north star、scope、README、AGENTS、runtime、schema、API、frontend、tests、
fixtures 或 release files。

之后的 implementation pass 按本 contract 清理 active docs、fixtures 和 tests。
closeout evidence 见 `review.md`。

implementation stage 覆盖：

- 从 active project direction documents 中移除 historical concrete fixture、
  concrete demo surface 和 historical concrete fixture anchors。
- 用 domain-neutral schema smoke fixture 替换 concrete Demo world fixture data。
- 用 generic WorldSpec schema smoke tests 替换 concrete fixture tests。
- 增加 external fixture boundaries 和 redacted validation reports 的 core-repository docs。
- 围绕 generic engine consumers 重置 v0.3 及之后的 roadmap language。

implementation stage 不得创建 external fixture repository、external validation
repository、concrete Demo world、application UI、runtime bridge、WorldSpec loader、
Agent loop、memory substrate 或 world generation system。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 状态检查表

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Ready for implementation
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## 路线图重置摘要

本 package 之后的 proposed roadmap direction：

- v0.2.5：core boundary cleanup and roadmap reset。
- v0.2.6：iteration workflow and plan reset。
- v0.3：generic WorldSpec data 的 WorldSpec loader and runtime bridge。
- v0.3.5：external fixture contract readiness。
- v0.4：Agent-in-World minimal loop。
- v0.5：memory and self-continuity substrate。
- v0.6：world generation v1。
- v0.7：external validation readiness / projection consumer readiness。
- v0.8：first external projection application readiness。

Concrete Demo worlds 保持在 WorldEngine core repository 之外，并通过 public
contracts 消费 engine。
