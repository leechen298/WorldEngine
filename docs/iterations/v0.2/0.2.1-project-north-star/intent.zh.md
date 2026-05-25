# Intent

Status: complete

英文版本：`intent.md`。

## Problem

WorldEngine 在进入 v0.2 schema work 前，需要明确 project direction 和 development discipline。否则
后续 code generation 容易把 concrete demo surface 误解成 engine goal，并把 architecture 收窄成
demo-specific backend。

## Goal

建立：

- root `AGENTS.md` rules for coding agents。
- `docs/project-north-star.md`。
- `docs/product-model.md`。
- `docs/scope-boundaries.md`。
- `docs/roadmap.md`。
- `docs/glossary.md`。
- iteration governance 和 templates。
- v0.2 planning docs。

## Non-goals

- 不修改 backend code。
- 不修改 frontend code。
- 不新增 runtime feature。
- 不实现 WorldCell 或 WorldSpec。
- 不新增 historical concrete fixture。
- 不创建 application repository。

## Why Now

v0.1 是 scaffold baseline。v0.2 将开始 recursive world foundation。如果没有 governance 和 north
star，schema/runtime work 会更容易偏向 application-specific implementation。

## North Star Alignment

本 package 直接建立 north star，确保后续 work 围绕 generate worlds、run worlds、recursive
structures 和 Agent pseudo-self substrate，而不是 demo-specific backend。
