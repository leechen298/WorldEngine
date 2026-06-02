# Technical Design

## 文档结构

本 documentation-only package 定义 contract 和 taxonomy。它包含 `technical-design.md`
和 `test-plan.md`，因为它改变 version semantics、evidence rules、package sequencing 和
automation-consumption vocabulary。

## 受影响文件

允许文件：

- 本 package 的七个英文文档和七个中文镜像。
- parent v0.8 route/status files。

不影响 runtime、schema、API、frontend、backend test、checker implementation、fixture、
migration、generated result、external repository 或 legacy implementation file。

## Data / Control Flow

1. `CURRENT_STATE.md` route 到 `0.8.1-documentation-package-needed`。
2. 本 package 定义 required core slices 和 claim taxonomy。
3. Parent state 移动到 `0.8.2-documentation-package-needed`。
4. `0.8.2` 使用 taxonomy 定义 observable public surfaces。

## 兼容策略

- 保持所有 current behavior unchanged。
- 把本 package 视为 contract vocabulary only。
- 将 runtime/API/frontend/E2E/Agent/autonomous/external validation checks 全部记录为
  not run。
- 防止 v0.7 handoff evidence 变成 v0.8 pass evidence。

## 防漂移规则

- `core contract ready` 不得写成 runtime pass。
- `external validation handoff ready` 不得写成 external validation PASS。
- `blocked`、`skipped` 和 `out of scope` 不得计为 pass。
- 任何未来 implementation package 都必须说明它被允许改变哪些 exact claim taxonomy values。
