# 意图

状态：planned / ready for review

## 问题 / 目的

v0.6 是第一个可以拥有 world generation 的 WorldEngine 版本。Roadmap 已命名目标，但不能从
一行 roadmap entry 直接开始 implementation。任何 schema、service、API、frontend 或 test
implementation 变更前，都必须先有 reviewable campaign root、child-package sequence、
compatibility baseline、generation boundary 和 explicit non-goals。

## 为什么现在做

v0.5 final closeout 已完成，并明确只允许 v0.6 通过自己的 reviewed iteration package 启动。
现有 `WorldSpec` loader 和 runtime-context bridge 为 v0.6 提供了 validation 和 readiness
baseline，但 generation contracts 必须在代码使用前定义。

## 与 Roadmap 的关系

v0.6 实现 roadmap 项 "World Generation v1"：从 templates 和 structured AI-assisted
generation 生成 runnable `WorldSpec` data，并提供 validation、metadata、preview 和
regeneration support。

本 package 不实现该能力。它只创建后续 child packages 安全实现该能力所需的 documentation
和 review path。

## 非目标

- `0.6.0` 不实现 generation schemas、services、APIs、UI、tests、persistence、runtime
  readiness、preview 或 regeneration。
- 不添加 external validation readiness；v0.7 负责该范围。
- 不添加 first external projection application readiness；v0.8 负责该范围。
- 不添加 concrete world content、private validation details、application-specific backend
  behavior、live AI-provider calls 或 `backend/worldengine/` runtime features。
- 不声明 runtime、API、E2E、frontend、Agent smoke、autonomous、external validation、
  projection、product readiness 或 release checks 已通过。

## 预期交接

评审后，本 package 将 v0.6 campaign structure 和 generation boundary 交接给
`0.6.1-world-generation-contracts-and-template-semantics`。在后续 mixed/code child 记录
`implementation_authorized: yes` 前，implementation 仍未授权。

## North Star 对齐

本 package 通过准备从 structured inputs、templates 和 AI-assisted plans 进行 generic
world generation，支持 north star；同时保留 recursive world architecture，避免
application-specific backend logic。
