# 意图

## 问题 / 目的

v0.8 不能在没有精确、可 review 含义的情况下声明 WorldEngine works。前序版本提供了
generation、runtime、Agent loop、memory 和 projection foundations，但尚未定义组合后的
minimum working-state claim。

本 package 在 observable surface 或 runtime readiness work 启动前，先定义 claim boundary。

## 为什么现在做

`0.8.0` 已完成 planning 与 v0.7 handoff baseline。下一条 route 需要 minimum working-state
contract，让后续 packages 知道哪些 evidence 需要 expose、prove、skip、block 或 exclude。

## 与 roadmap 的关系

v0.8 为 external validation function 准备 core-side readiness。本 package 定义 core-side
readiness 的含义，但不实现 external validator 或 external application。

## 非目标

- 不实现 code、schemas、checkers、tests、APIs、frontend routes 或 evidence artifacts。
- 不运行 runtime/API/frontend/E2E/Agent/autonomous/external validation。
- 不声明 minimum working state 已被证明。
- 不定义 external validator connection workflows 或 private scenarios。

## 预期交接

`0.8.2-core-observable-surface-boundary` 接收 required core slices、claim taxonomy、evidence
classes、exclusions 和 stop conditions，用于定义 observable public surfaces。
