# Scope Boundaries

Status: authoritative boundary guide

英文版本：`scope-boundaries.md`。

## Global Rules

- WorldEngine 必须与 `docs/project-north-star.md` 保持一致。
- WorldEngine core repository 不能包含 concrete demo worlds。
- External fixture 和 validation worlds 不能作为 core repository 内的 fixtures、
  acceptance targets、loader test inputs 或 projection targets 保存。
- External fixture 和 validation worlds 只能通过 public APIs、CLI commands、schemas、
  exported contracts 和 redacted validation reports 消费 WorldEngine。
- Core repository 可以定义 schemas、runtime contracts、event contracts、agent contracts、
  memory/self-continuity contracts、projection contracts 和 redacted report formats。
- Core repository 不能保存 external-world seed data、characters、locations、story rules、
  validation oracle internals 或 application-specific backend logic。
- 当 core capabilities 需要 LLM behavior 时，WorldEngine 拥有 provider configuration 和
  provider calls。External clients 不得成为 provider calls、provider keys 或 evaluator
  decisions 的 authority。
- 允许 redacted public summaries。API keys、authorization headers、raw prompts、raw provider
  responses、raw provider traces、raw thought、private memory payloads、private goals 和 hidden
  context 不得成为 public evidence。
- Agent memory、personality 和 skill changes 不得被假定为每 tick 自动 mutate。Package 拥有该
  behavior 时，sleep、rest 或 low-activity phases 中的 consolidation 必须 explicit。
- Narrative projection、replay views 和 out-of-world diagnostic conversations 默认是 external
  inspection surfaces。除非 reviewed package 明确创建 bridge，否则它们不得修改 canonical world
  state、world timelines 或 Agent memory。
- Code work 必须限定在一个 iteration package 内。
- Schema changes 必须 additive，除非当前 contract 允许 breaking changes。
- Runtime behavior 必须保留，除非当前 contract 明确改变它。

## v0.2 Does

v0.2 Recursive World Foundation 可以：

- 增加 north star 和 documentation governance。
- 在 schema/spec layer 定义 WorldCell 和 WorldSpec。
- 定义 EntityRef 等 shared references。
- 增加 optional event structure fields。
- 增加 generic schema smoke validation。
- 定义 external fixture 和 validation consumers 的边界。
- 标记 `backend/worldengine/` 为 legacy。
- 保留现有 runtime behavior。

## v0.2 Does Not

v0.2 不能：

- 完整迁移 RuntimeEngine 到 WorldCell。
- 把 Agent inner-world 实现为 WorldCell。
- 实现完整 world generation。
- 实现 demo-specific runtime。
- 创建单独的 game repository。
- 增加 vector memory。
- 增加 multi-agent society simulation。
- 实现 Agent pseudo-self continuity。
- 修改 frontend dashboard，除非 iteration contract 明确要求。

## Future Boundaries

- v0.3 可以把 generic WorldSpec 桥接进 runtime loading。
- v0.3.5 可以定义 external fixture contract readiness。
- v0.4 可以加入 minimal agent-in-world loop。
- v0.5 可以加入 memory 和 self-continuity。
- v0.6 可以加入 world generation v1。
- v0.7 可以准备 external validation 和 projection consumer readiness。
- v0.8 可以准备 core-side minimum working-state boundary，以及 external validation function
  需要的 public surfaces。
- v0.9 可以准备 first LLM-backed lifecycle foundation，包括 WorldEngine-owned provider calls、
  generated world rules、bounded runtime control、world-level direction、rule-linked event
  legality、brain-inspired Agent continuity/consolidation evidence，以及 external
  narrative/diagnostic projection boundaries。
