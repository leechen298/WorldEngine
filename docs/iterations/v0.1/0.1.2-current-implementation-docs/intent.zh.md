# Intent

Status: review complete

英文版本：`intent.md`。

## Problem

v0.1 closeout 已记录 release boundary 和 test evidence，但还需要更完整的 current implementation map。
否则未来 agent 容易只从代码猜测 current state，或把 v0.2 planned capabilities 误当成已实现能力。

## Goal

补齐 v0.1 current implementation docs，覆盖：

- active backend assembly。
- runtime/event/world params/archive/params-agent behavior。
- active frontend dashboard。
- current API surface。
- current test coverage map。
- known limits。

## Non-goals

- 不修改 backend code。
- 不修改 frontend code。
- 不新增 tests。
- 不实现 v0.2 schemas。
- 不把 planned recursive WorldCell behavior 写成 existing behavior。

## Why Now

v0.2 开始前需要一个准确的 v0.1 baseline，让后续 schema/runtime work 能以当前事实为依据。

## North Star Alignment

本 package 通过记录真实 current state，防止后续工作把 params-agent、heartbeat/counter 或 dashboard
误解为已经完成 recursive world 和 Agent pseudo-self。
