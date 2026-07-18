# 0.12.2 Agent Memory And Rest Consolidation MVP

英文源文件：`README.md`。

状态：review complete
类型：mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

为 `0.12.1` 引入的 session Agent 增加最小 public memory summaries 和
rest/consolidation evidence。

本包应展示 Agent 可以跨 tick 携带 public memory，并通过 rest 沉淀 observations。它不得暴露
private memory payloads、raw thought、private goals、personality mutation、skill mutation
或 deep cognition claims。

## 范围

评审批准后允许：

- 新增 public session Agent memory summary schemas 和 response artifacts。
- 通过现有 in-memory memory substrate 存储 short-term public working summaries 和 episodic
  summaries。
- 在 `/sessions/{session_id}/agents/{agent_id}/memory` 下新增 session Agent memory read API。
- 扩展 session Agent step 或新增 consolidation endpoint，在 Agent rests 时记录 rest /
  consolidation evidence。
- 记录 public evidence events，例如 `world.agent.memory.recorded` 和
  `world.agent.consolidation.recorded`。
- 增加 focused backend tests，覆盖 public memory creation、multi-tick rest consolidation、
  redaction、no per-tick personality/skill mutation、evidence refs 和 compatibility。

禁止：

- public evidence 不得包含 raw private memory payloads、raw thought、chain-of-thought、
  private goals、hidden context、provider traces、raw prompts、raw provider responses 或
  secrets。
- 不做 automatic per-tick personality、skill、relationship、injury、death、inventory 或
  long-term memory mutation。
- 不把 diagnostic conversation 插入 Agent memory。
- 不做 frontend、persistence/migration、provider live、external Validation Client、checker
  automation、narrative/diagnostic 或 complete MVP closeout work。
- 不在 `backend/worldengine/` 下实现。

## 交付物

- Public Agent memory summary API/artifacts。
- 与 session Agent runtime refs 绑定的 rest/consolidation evidence。
- Public event evidence 和 memory evidence refs。
- Focused backend tests 和 review evidence。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## 状态清单

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Implementation authorized
- [x] Implementation complete
- [x] Tests complete
- [x] Review complete

## 最终评估

Implementation-scope evaluator review 已通过。本 package 已在 scoped Agent memory 和
rest consolidation MVP 范围内完成。
