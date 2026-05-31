# 意图

状态：review complete

## 问题

v0.4 明确排除了 memory、episodic memory、relationship state、self-summary、
reflection 和 personality drift。v0.5 负责这个 roadmap scope，但如果没有已评审
package 就启动，容易把 product-boundary decisions 与 runtime implementation 混在一起。

项目需要一个 deterministic v0.5 `/goal` package，在任何 code changes 前固定 scope、
review gates、compatibility baseline、handoff evidence 和第一个 implementation slice。

## 目标

本 package 完成后，WorldEngine 会拥有可评审的 v0.5 campaign root 和第一个 child
package：

- 定义 v0.5 memory/self-continuity boundary。
- 将六个 capabilities 拆分为 contract-first 和 implementation-later work。
- 将 working memory 和 episodic memory 识别为第一批 implementation candidates。
- 在 behavior 前，把 relationship state、self-summary、reflection records 和
  personality drift signals 保持为 schema/contract semantics。
- 将 v0.4 final closeout 和 post-closeout clean pass 只记录为 handoff evidence。
- 保持 implementation authorization closed。

## 非目标

- 不实现 runtime、schema、API、frontend、backend tests、fixtures、migrations 或
  external repository changes。
- 本 package 不创建 `backend/app/schemas/agent_memory.py`、
  `backend/app/agent/memory.py` 或 `backend/app/tests/test_agent_memory_*.py`。
- 不添加 public runtime APIs。
- 不把 memory 连接到 Agent Loop perception 或 action。
- 不实现 relationship behavior、self-summary generation、automatic reflection 或
  personality drift action modifiers。
- 不添加 world generation、external validation readiness、projection app readiness、
  concrete world content 或 private validation details。

## 当前原因

Roadmap 声明 v0.5 接在已评审 v0.4 request-driven minimal loop 后，引入 working
memory、episodic memory、relationship state、self-summary、reflection records 和
personality drift signals，并使其未来可以影响 action。Post-closeout validation pass
为 v0.5 提供了更强 baseline，但这些 evidence 在 v0.5 产生 fresh command evidence 前
只能作为 handoff context。

## North Star 对齐

本 package 为 north star 中的 engineered pseudo-self substrate 做准备：identity
continuity、self-narrative、relationship history、personality drift，以及由 prior
experience 塑造的 decision patterns。它保持设计 generic 且 inspectable，并拒绝 concrete
demo-world 或 application-specific backend behavior。

## 预期交接

如果评审通过，本 package handoff 到 `0.5.1-memory-self-continuity-contracts`。该
package 应先定义 public concepts 和 schema semantics，再由 `0.5.2` 实现 substrate。
