# 0.6.0 v0.6 规划与生成边界基线

状态：review complete
类型：documentation-only
implementation_authorized: no

## 目标

创建 v0.6 documentation root、`/goal` campaign controls、version plan、generation
boundary、compatibility baseline 和 v0.5 handoff mapping，且不修改 implementation
files。

## 范围

允许：

- 在 `docs/iterations/v0.6/` 下创建 parent v0.6 campaign docs。
- 在
  `docs/iterations/v0.6/0.6.0-v0.6-planning-and-generation-boundary-baseline/`
  下创建本 child package。
- 定义 v0.6 capability split：templates、structured generation plans、AI-assisted
  plan import、validation、metadata、preview、regeneration、dashboard preview、audit、
  release candidate 和 final closeout。
- 定义 planned child sequence 和 review gates。
- 将 v0.5 final closeout 只记录为 handoff evidence。

禁止：

- 不得修改 runtime、schema、API、frontend、backend test、fixture、migration、
  generated result、external repository 或 `backend/worldengine/` implementation
  files。
- 不得实现 generation schemas、services、APIs、UI、persistence、regeneration、
  runtime readiness 或 tests。
- 不得添加 concrete world data、application-specific backend logic、private
  validation oracle details、live AI-provider dependencies、external validation
  readiness 或 projection app readiness。

## 交付物

- v0.6 parent campaign docs 和中文镜像。
- `0.6.0` child package docs 和中文镜像。
- Documentation-stage verification plan 和 review evidence。
- 明确交接给 `0.6.1-world-generation-contracts-and-template-semantics`。

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

## 当前评估

本 documentation-only package 已 review complete。它交接给
`0.6.1-world-generation-contracts-and-template-semantics`，且 v0.6 implementation
authorization 仍关闭，直到后续 implementation-bearing child package 明确记录
`implementation_authorized: yes`。
