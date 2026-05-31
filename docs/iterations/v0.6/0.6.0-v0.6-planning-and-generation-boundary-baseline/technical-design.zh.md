# 技术设计

状态：review complete

## 文档结构

`0.6.0` 创建一个 v0.6 campaign root 和第一个 child package：

```text
docs/iterations/v0.6/
├── README.md
├── README.zh.md
├── v0.6-plan.md
├── v0.6-plan.zh.md
├── GOAL_RUNNER.md
├── GOAL_RUNNER.zh.md
├── CURRENT_STATE.md
├── CURRENT_STATE.zh.md
├── CAMPAIGN_PLAN.md
├── CAMPAIGN_PLAN.zh.md
├── review.md
├── review.zh.md
└── 0.6.0-v0.6-planning-and-generation-boundary-baseline/
    ├── README.md
    ├── README.zh.md
    ├── intent.md
    ├── intent.zh.md
    ├── contract.md
    ├── contract.zh.md
    ├── technical-design.md
    ├── technical-design.zh.md
    ├── test-plan.md
    ├── test-plan.zh.md
    ├── plan.md
    ├── plan.zh.md
    ├── review.md
    └── review.zh.md
```

## 受影响文件

允许受影响文件仅限 `docs/iterations/v0.6/**`。

本 package 不影响 backend、frontend、API、migration、fixture、generated result、
external repository 或 `backend/worldengine/` files。

## 生成边界模型

Parent plan 将 v0.6 拆成可评审的 child packages：

1. boundary 和 campaign planning。
2. contract 和 template semantics。
3. deterministic template generator core。
4. structured generation plan compiler。
5. AI-assisted plan import boundary。
6. validation、metadata 和 preview API。
7. regeneration 和 runtime-readiness integration。
8. dashboard preview 和 E2E smoke。
9. evidence audit。
10. release candidate。
11. final closeout。

本 package 只记录 sequence，不实现任何 generator。

## 兼容性策略

Campaign 在写代码前识别 compatibility-sensitive surfaces：

- `WorldSpec`、`WorldCell` 和 `EntityRef`。
- `load_worldspec` 和 loader errors。
- `RuntimeContext` 和 runtime-context summaries。
- `RuntimeEngine` tick/time behavior 和 context storage。
- v0.4 Agent Loop contracts。
- v0.5 memory context surfaces。
- existing API envelope 和 error shape。

后续 children 必须用 current-session commands 证明 compatibility，才能声明 pass。

## 防漂移规则

- Active child package 是唯一 implementation scope。
- Documentation-only packages 不得修改 implementation files。
- Generated examples 必须保持 generic，不得嵌入 concrete demo-world content。
- 除非后续已评审 child 明确授权 live provider behavior，否则 AI-assisted generation 表示
  structured plan import。
- 历史 v0.5 evidence 只是 handoff context。
- Review status 不得超过已有 evidence。

## 风险

- 风险：v0.6 planning 意外变成 product-specific world authoring。
  缓解：明确 forbidden changes 和 scope guardrails。
- 风险：AI-assisted generation 被理解为 live provider integration。
  缓解：使用 provider-independent structured plan boundary。
- 风险：generated `WorldSpec` output 破坏 loader/runtime-context behavior。
  缓解：后续 child packages 必须运行 focused loader 和 runtime-context tests。
- 风险：缺少 evaluator evidence 却被误认为 review complete。
  缓解：evidence 缺失时状态保持 `planned / ready for review`；evidence 记录后可以将
  `0.6.0` 标记为 complete，但继续保持 `implementation_authorized: no`。
