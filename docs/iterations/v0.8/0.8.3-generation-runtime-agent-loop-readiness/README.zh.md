# 0.8.3 Generation Runtime Agent Loop Readiness

状态：review complete
类型：mixed/code candidate
implementation_authorized: yes
evidence_execution_authorized: yes

## 目的

本 package 准备 v0.8 所需的最小 generic core loop，让未来 external validation
function 可以通过 public engine surfaces 判断 WorldEngine：

```text
candidate WorldSpec
  -> runtime context readiness
  -> isolated runtime step evidence
  -> default Agent loop perception/action evidence
```

本 package 不是 external validator，也不实现 product application。Documentation/contract
review 和 implementation review 已完成，范围仅限下文定义的 generic、read-only、isolated
core-readiness probe。

## 当前状态

当前实现已经具备：

- `/world/generation` 下的 generation preview 和 regeneration APIs。
- runtime-readiness checks：校验 candidate `WorldSpec`，并派生 bounded runtime context
  summary。
- `RuntimeEngine` 可以携带 inert runtime context。
- `AgentLoopService` 具有 bounded perception、default deterministic `noop`，以及已评审的
  `params.patch` action boundary。
- Perception 中有 bounded memory context，但没有 public memory API。

v0.8 仍缺少一条单一 generic evidence path，证明 candidate `WorldSpec` 可以被 inspection，
可以作为 inert runtime context，被 isolated runtime 推进一步，并被 default Agent loop
观察，同时不修改 app runtime state，也不暴露 private detail。

## Review 后允许的实现

如果本 package review 记录 `implementation_authorized: yes`，implementation 可添加：

- `backend/app/schemas/world_generation.py` 中的 additive schemas。
- `backend/app/core/world_generation.py` 中的 generic helper logic。
- `backend/app/api/routes/world_generation.py` 下一个 read-only API route。
- `backend/app/tests/` 下的 focused backend/API tests。

预期 route 是 core-side readiness probe，例如
`POST /world/generation/core-readiness`，返回 bounded preview、runtime-readiness、
isolated runtime-step 和 default Agent-loop probe evidence。

## 禁止范围

- 不改 frontend。
- 不实现 external validator、external app、product UI、app routing、packaging 或
  deployment。
- 不加入 concrete validation world、seed data、character、location、resource、story
  rule、UI selector、private transcript、private repo path、oracle detail、provider
  trace、prompt、secret 或 external event payload。
- 不添加 durable persistence、migration、live provider behavior、public memory API、
  reset API 或 write API。
- 不在 `backend/worldengine/` 下添加新 runtime feature。
- 不把 generated world 作为 app live runtime state 执行。
- 不声明 external validation PASS、product readiness、generation quality、Agent smoke
  PASS、autonomous PASS 或 v0.8 final readiness。

## Handoff

本 package 将 bounded core readiness evidence 交给
`0.8.4-external-validation-handoff-contract`。它不声明 external validation PASS、product
readiness、generation quality、Agent smoke PASS、autonomous PASS、frontend/E2E PASS 或
final v0.8 readiness。
