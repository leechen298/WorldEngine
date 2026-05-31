# 0.5.0 v0.5 规划与连续性边界基线

状态：planned / ready for review
类型：documentation-only
implementation_authorized：no

## 目标

创建 v0.5 documentation root、`/goal` campaign controls、version plan、
memory/self-continuity boundary、compatibility baseline 和 v0.4 handoff mapping，
且不修改 implementation files。

## 范围

允许：

- 在 `docs/iterations/v0.5/` 下创建 parent v0.5 campaign docs。
- 在
  `docs/iterations/v0.5/0.5.0-v0.5-planning-and-continuity-boundary-baseline/`
  下创建本 child package。
- 定义 v0.5 在 working memory、episodic memory、relationship state、
  self-summary、reflection records 和 personality drift signals 之间的 capability
  split。
- 定义 planned child sequence 和 review gates。
- 将 v0.4 final closeout 与 v0.4 post-closeout clean pass 只记录为 handoff
  evidence。

禁止：

- 不修改 runtime、schema、API、frontend、backend test、fixture、migration、
  generated result、external repository 或 `backend/worldengine/` implementation
  files。
- 不实现 memory、self-continuity、loop integration、public APIs、frontend
  behavior、durable persistence、migrations 或 tests。
- 不添加 concrete world data、application-specific backend logic、private
  validation oracle details、world generation、external validation readiness 或
  projection app readiness。

## 交付物

- v0.5 parent campaign docs 和中文镜像。
- `0.5.0` child package docs 和中文镜像。
- Documentation-stage verification plan 和 review evidence。
- 明确 handoff 到 `0.5.1-memory-self-continuity-contracts`。

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

本 package 仅处于 documentation stage。在 `review.md` 记录 documentation
verification 后，可进入评审。

