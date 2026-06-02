# 0.8.2 Core Observable Surface Boundary

状态：review complete
类型：documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## 目标

定义未来 external validator 可以观察的 core-side public surfaces，覆盖 runtime、event、
generation、Agent loop、memory context、archive 和 read-model，同时不把 validator、
projection application 或 product-specific behavior 纳入 core repository。

本 package 只定义可观察 surface 边界。不实现 schemas、checkers、API routes、frontend
behavior、tests、evidence artifacts、external validation logic 或 external application behavior。

## 可观察 Surface 边界

后续 reviewed packages 可以暴露或 harden 以下 generic、read-only、redacted surface
families：

| Surface family | Public source boundary | Allowed observable summary |
| --- | --- | --- |
| runtime state | `/runtime/state`, `/runtime/step` evidence | tick、world time、public params summary、runtime-context summary、blocker status |
| event timeline | `/world/events`, `/world/event-steps` | event counts、event type summaries、tick ranges、public event refs |
| generation readiness | `/world/generation/*` | generation id、template/plan status、validation diagnostics、runtime-readiness status |
| Agent loop | `/world/agent/loop/step` | perception boundary、intent type、action result status、public evidence refs |
| memory context | 现有 bounded perception context | counts、scope ids、provenance summaries、redacted bounded memory context |
| archive | `/world/snapshots`, `/world/summaries` | snapshot/summary ids、tick ranges、summary text、event counts |
| projection/read-model | v0.7 projection contracts | read-only family ids、allowed fields、redaction notes、no-write capability |
| handoff/readiness | v0.7 report/manifest contracts 和后续 v0.8 handoff docs | public surface ids、evidence refs、status taxonomy、blockers、redaction confirmation |

未来每个 observable surface 都必须：

- 保持 generic to WorldEngine core。
- public 且 redacted。
- 默认 read-only；只有后续 reviewed package 明确授权 generic write contract 时才可例外。
- 实现时必须 additive 且 versioned。
- 任何 pass claim 前都必须绑定 current-session evidence。

## 禁止暴露

Observable surfaces 不得暴露：

- concrete validation worlds、app names、maps、locations、characters、resources、story
  rules、seed data、product routes、UI selectors 或 private transcripts。
- hidden reset APIs、private runner state、private repository paths、oracle internals、
  provider traces、prompts、secrets 或 non-redacted external event payloads。
- raw memory records、unrestricted memory export、pseudo-self internals、relationship
  history、reflection records，或超出当前 reviewed contracts 的 personality drift internals。
- write APIs、reset APIs、migrations、persistence、product UI、projection app behavior 或
  consumer-specific backend behavior。

## 范围

允许范围：

- 创建本 package document set 和中文镜像。
- 定义 generic observable surface families、public source boundaries、allowed summary
  classes、forbidden exposure、versioning rules，以及后续 packages 的 implementation
  authorization criteria。
- Review 后同步 parent v0.8 route/status surfaces。
- 记录 documentation checks 和 evaluator findings。

禁止范围：

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository 或 `backend/worldengine/` implementation files。
- 不新增或编辑 `docs/contracts/` schemas、`tools/testing` checkers、API routes、service helpers、
  frontend routes、E2E tests 或 evidence artifacts。
- 不声明 core observable surface readiness、runtime/API/frontend pass、minimum working-state
  evidence、external validation PASS、product readiness、projection readiness 或 release readiness。

## 最终评估状态

当前值：`review complete`。

本 package 定义 observable surface boundary，并 handoff 到
`0.8.3-generation-runtime-agent-loop-readiness`，用于后续 reviewed implementation planning
以及任何 future core-readiness hardening。
