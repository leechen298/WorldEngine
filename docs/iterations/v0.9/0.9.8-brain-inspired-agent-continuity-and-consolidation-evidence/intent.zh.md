# Intent

英文原文：`intent.md`。

## 问题

v0.9 现在已有 provider readiness boundaries、LLM-backed world creation shape、world rule parameters、worldview fidelity checks、bounded runtime controls、world direction boundaries，以及 rule-linked event legality。它仍缺少公开证据来证明 Agent 不只是一次性的 scripted action。

如果没有 public continuity evidence，后续 LLM-backed validation 就无法区分 persistent Agent autonomy、client-supplied action、per-tick mechanical mutation 或 hidden private reasoning。

## 产品意图

本包建立第一版最小 public Agent continuity and consolidation boundary。它要暴露 reviewable artifacts，用于 perception、short-term continuity、long-term summary references、personality and skill summary references、intent/no-intent/rest states、event reactions，以及 sleep/rest/low-activity consolidation phases。

本包不是 consciousness claim、完整 neuroscience model、narrative projection system、diagnostic dialogue bridge、checker fixture package 或 frontend feature。它是 generic engine boundary，用于 public Agent continuity evidence。

## 用户价值

- Validators 可以检查 Agent behavior 是否跨时间持续。
- 后续 checker work 可以判断 public continuity evidence，而不读取 raw prompts、raw thoughts 或 private memory。
- WorldEngine 可以展示 sleep/rest/consolidation cadence，而不会假装 personality、long-term memory 或 skill state 每 tick 都变化。
- 未来 narrative 和 diagnostic surfaces 可以消费 public summaries，而默认不修改 canonical world state 或 Agent memory。

## North Star Alignment

WorldEngine north star 包含 agents 在 worlds 中生活、积累 memory、通过 feedback 改变，并形成 engineered pseudo-self continuity。本包推进这个方向，同时保留 WorldEngine 不声明 real consciousness 的明确边界。

## Non-Goals

- 不输出 raw thought 或 chain-of-thought。
- 不导出 private memory payload。
- 不暴露 private goals 或 hidden context。
- 不执行 live provider interpretation。
- 不执行 checker 或修改 fixtures。
- 不运行 external validation。
- 不修改 frontend 或 Validation Client。
- 不实现 narrative projection 或 diagnostic dialogue。
- 不添加 durable scheduler 或 background worker。
- 不实现 automatic per-tick personality、long-term memory 或 skill mutation。
- 不修改 `backend/worldengine/`。
