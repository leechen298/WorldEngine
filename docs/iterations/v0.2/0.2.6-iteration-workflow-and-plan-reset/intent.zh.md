# 意图

英文版本：`intent.md`

## 问题

v0.2 已完成多个基础 packages，包括 boundary cleanup，但 active planning 仍指向
immediate final closeout。现在做 closeout 太早；剩余工作必须先拆成小的、
可 review 的 packages，并在 release-candidate 和 closeout 之前写清边界。

历史 v0.2 iteration documents 里还保留了 superseded fixture direction 中的
concrete demo details。由于后续 agents 可能会读取整个 v0.2 iteration context，
而不只读取 active direction docs，这些 details 会带来自动化跑偏风险。

## 目标

创建一个 documentation-only package，用来重排 v0.2 剩余 sequence，增加自动迭代
workflow，提供 final-review-bundle template，并在保留历史事实的前提下抽象化
historical concrete demo details。

## 非目标

- 不实现 runtime、schema、API、frontend、test、fixture 或 external repository changes。
- 不创建 0.2.7 到 0.2.12 的 package directories。
- 不声明 v0.2 final release。
- 不隐藏历史事实，也不假装 superseded fixture work 没发生过。
- 不把 concrete fixture direction 恢复为 active roadmap target。

## 为什么现在做

0.2.5 已移除 active concrete external-world anchors，并用 generic schema
smoke coverage 替换 fixture tests。下一步是让 v0.2 剩余工作可被 automation
逐包执行，同时避免未来 package 扩张成 loader、runtime bridge、agent loop、
memory、generation 或 product UI work。

## 北极星对齐

本 package 通过保持 WorldEngine 面向 generic recursive world engine，支撑项目北极星。
它强化了后续 packages 构建 schema、event、evidence 和 compatibility foundations
的流程，同时避免 repository 被缩窄成 demo-specific backend。
