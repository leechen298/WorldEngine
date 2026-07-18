# 0.12.1 Agent Public State And Runtime Loop

英文源文件：`README.md`。

状态：review complete
类型：mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

新增最小 session-scoped public Agent state 和 runtime-integrated loop，让 Agent 可以观察
public session、选择 action 或 no-action、只执行 WorldEngine-owned public behavior，并记录
public evidence。

本包不得把 client-submitted action 表述成 Agent autonomy。Agent step request 可以选择 session
和 Agent，但最终 observe/intent/action-or-wait/rest evidence 必须由 WorldEngine 从 public
runtime/session state 生成。

## 范围

评审批准后允许：

- 新增 session-scoped Agent status 的 public Agent state schemas。
- 新增 in-memory session Agent store，或把 Agent state attach 到现有 session store。
- 在 `/sessions/{session_id}/agents` 下新增 session Agent read/list/step APIs。
- 新增 deterministic minimal Agent loop，选择 `observe`、`no_intent`、`action`、`wait`
  或 `rest` 之一。
- 记录 public Agent evidence events，例如 `world.agent.observed`、
  `world.agent.intent.recorded`、`world.agent.action.recorded` 或
  `world.agent.rest.recorded`。
- 更新 manifest/public handoff discovery fields。
- 增加聚焦 backend tests，覆盖 state、loop、client-scripted-action rejection、redaction、
  event evidence 和 compatibility。

禁止：

- evidence 不得包含 raw thought、chain-of-thought、private memory、private goals、secrets、
  raw prompts、raw provider responses、provider traces 或 hidden context。
- 不得把 client-submitted action intent 表述成 autonomous Agent behavior。
- 不得直接绕过 v0.11 rule/event legality。
- 不做完整 personality simulation、long-term memory consolidation、sleep implementation、
  narrative projection、diagnostic conversation、checker automation、provider live call、external
  Validation Client automation 或 complete MVP PASS claim。
- 不加入 concrete demo-world seed data 或 product-specific backend behavior。
- 不在 `backend/worldengine/` 下实现。

## 交付物

- Public session Agent state schema 和 response artifacts。
- Session-scoped Agent list/read/step API。
- 带 event IDs 和 runtime refs 的 runtime-linked Agent step evidence。
- Client-scripted-action rejection 或 omission evidence。
- Manifest/public handoff updates。
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

Implementation-scope evaluator review 已通过。本 package 已在 scoped session Agent public
state/runtime loop 范围内完成。
