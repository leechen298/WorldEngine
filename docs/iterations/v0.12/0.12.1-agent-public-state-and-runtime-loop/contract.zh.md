# Contract

英文源文件：`contract.md`。

## Public Concepts

- `session Agent`：WorldEngine session 内表示的 in-world Agent。
- `public Agent state`：redaction-safe Agent fields，例如 status、last observation
  summary、public intent label、visible action、runtime refs 和 evidence refs。
- `Agent step`：WorldEngine-owned transition；它 observe public state、选择 public
  intent/action-or-wait/rest outcome、记录 events，并更新 public Agent state。
- `client-scripted action`：client-provided concrete action 或 patch，绕过 WorldEngine
  intent selection。它不得被报告为 Agent autonomy。

## Allowed Changes

- 在 `backend/app/schemas/` 新增 public session Agent schemas。
- 在 `backend/app/core/world_session.py` 或小型相邻 core module 中新增 session Agent state
  storage。
- 在现有 session route 边界内的 `backend/app/api/routes/session.py` 下新增 session Agent APIs。
- 更新 `backend/app/api/routes/world.py` 中的 manifest/public handoff discovery。
- 在 `backend/app/tests/` 下新增 focused backend tests。
- 更新 package 和 parent review evidence。

## Forbidden Changes

- schemas、events、API responses、tests 或 review evidence 中不得包含 raw thought、raw
  chain-of-thought、private memory、private goals、hidden context、raw prompts、raw provider
  responses、provider traces 或 secrets。
- session Agent step endpoint 不接受 client-provided action patches/intents。
- 不直接修改 Agent private state、long-term memory、personality、skills、injury、death 或
  inventory。
- public world mutation 不得绕过 rule/event legality。
- 不做 frontend、persistence/migration、provider live、external Validation Client、checker
  automation、narrative/diagnostic 或 complete MVP closeout work。
- 不在 `backend/worldengine/` 下新增 runtime feature。

## Required Behavior

- 新 session 或既有 session 可以暴露至少一个 public Agent record。
- read/list public Agent state 是 redaction-safe 的。
- 不带 client action intent 运行 session Agent step，会产生 public
  observe/intent/action-or-wait/rest evidence。
- Agent evidence 中的 runtime refs 匹配当前 runtime tick/time。
- Agent step evidence append 到 event log，并由 response 引用。
- 如果 client 试图提交 scripted action intent，API 会 reject，或以明确 public diagnostic
  evidence 忽略。
- 现有 request-driven `/world/agent/loop/step` 保持兼容，但不作为 session Agent autonomy
  的证据。

## Compatibility Requirements

- 现有 session create/list/read/status/run/snapshot/rules/directions/evolution APIs 保持
  additive-compatible。
- 现有 agent loop service tests 继续通过。
- Manifest additions 是 additive。
- Event payloads 保持 public 且 redaction-safe。

## Exit Criteria

- Documentation evaluator 记录无 P1/P2 findings。
- 代码变更前记录 `implementation_authorized: yes`。
- Focused tests 证明 public Agent state、WorldEngine-owned step selection、event evidence、
  client-scripted-action rejection、redaction boundary 和 compatibility。
- Closeout 前 implementation-scope evaluator 无 blocking P1/P2。
