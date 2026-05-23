# Project North Star

Status: authoritative project direction

英文版本：`project-north-star.md`。

## Core Mission

WorldEngine 是 recursive world generation 与 runtime engine。它也是 Agent 在 world 中通过
lived experience 形成 continuity、memory、feedback-shaped behavior 和 pseudo-self 的
runtime substrate。

WorldEngine 存在是为了支持五个长期能力：

1. 从 structured inputs、templates 和 AI-assisted generation 生成 worlds。
2. 让 worlds 作为 stateful systems 随时间运行，拥有 events、rules、timelines、resources、
   history、snapshots 和 recovery。
3. 支持 recursive world structures：worlds 可以包含 child worlds、projected worlds、
   subjective worlds 和 specialized runtime cells。
4. 让 Agent 在 worlds 中生活，perceive events、act、accumulate memory、update goals，并通过
   feedback 变化。
5. 让 Agent 发展出 sustained pseudo-self：identity continuity、self-narrative、
   relationship history、personality drift，以及由 prior experience 塑造的 decision
   patterns。

## What This Does Not Claim

WorldEngine 不宣称 real consciousness。`pseudo-self` 指可工程化、可检查、可测试、可改进的
continuity model。它是 product 和 engineering target，不是 metaphysical claim。

## First User Surface

第一款 village-like electronic-pet game 是 WorldEngine 的 surface、reference world 和
validation interface。

它是：

- engine 的第一个 user-facing projection。
- 普通用户能理解的第一个 reference world。
- world runtime、events、memory 和 Agent continuity 的 practical acceptance harness。

它不是：

- WorldEngine 的 purpose。
- 让 engine 变成 village-specific 的理由。
- 用 game-only state 替代 recursive world architecture 的理由。

## Architecture Anchor

World 是 recursive runtime unit。一个 world 可以包含 child worlds、locations、agents、rules、
resources、timelines、event streams、projection config 和 external connectors。后续
milestones 可能把 Agent 的 subjective memory 或 self-narrative space 建模为 specialized
world cells，但 v0.2 只为这个方向建立 foundation。

## Decision Rule

当 proposed feature 与本文档冲突时，proposal 必须修改或被拒绝。如果 north star 本身需要改变，
先更新本文档，并在 iteration package 中记录该 decision。
