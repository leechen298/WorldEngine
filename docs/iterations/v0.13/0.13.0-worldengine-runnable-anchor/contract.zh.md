# 契约

英文源文件：`contract.md`。

## 公共概念

- `WorldBrief`：与 provider 无关的结构化世界方向，包含固定 seed、规模边界、前提和约束。
- `RunnableWorldPackage`：不可变生成交接物，包含 public world spec、rules、actions、Agent
  seeds、projection manifest 和 evidence policy。
- `package_hash`：对规范化 runnable package 计算的正典 hash；Session boot 必须引用自己
  实际加载的准确 hash。
- `WorldSession`：一场进程内正典运行，包含 lifecycle state、source package hash、tick、
  world time、revision 和 state hash。
- `InterventionWindow`：由 `window_id` 和 `open_tick` 标识的明确 tick-boundary window，
  用户只能在窗口内提交方向。
- `BoundedDirection`：不直接指定最终世界事实的外部压力或约束。
- `DirectionDecision`：accepted、translated、rejected 或 deferred 结果，包含稳定 reason
  code、rule refs 和可能存在的 applied-diff refs。
- `ActionRequest`：Agent 或客户端提出世界变更的类型化请求，本身不应用变更。
- `FeedbackEvent`：客户端观察到的、可能具有历史意义的局部结果；WorldEngine 接受之前仍只是
  candidate。
- `PublicProjection`：脱敏安全的 Session read model，包含 session ID、tick、revision、
  state hash、公开实体和 Agent、allowed actions 与 event cursor。
- `AgentExperienceRef`：后续 Agent 决策对先前 accepted event/action result 的公开引用；
  它不是 private memory 或 raw thought。
- `EvidenceBundle`：供外部 checker 使用的 public package、event、diff、snapshot、Agent、
  direction、projection 和 request-correlation evidence。

## 协议操作

文档评审期间可以细化 resource 名称，但必须保留以下通用操作：

```text
GET  /health
GET  /api/v1/capabilities
GET  /openapi.json
POST /api/v1/world-packages
GET  /api/v1/world-packages/{package_id}
POST /api/v1/sessions
GET  /api/v1/sessions/{session_id}
POST /api/v1/sessions/{session_id}/steps
POST /api/v1/sessions/{session_id}/directions
POST /api/v1/sessions/{session_id}/actions
POST /api/v1/sessions/{session_id}/feedback
GET  /api/v1/sessions/{session_id}/projection
GET  /api/v1/sessions/{session_id}/events?after_sequence={sequence}
GET  /api/v1/sessions/{session_id}/evidence
```

Capability manifest 必须声明 engine/build identity、instance identity、contract/schema
version，以及每个 public operation 的 `operation_id`、method、path 和 maturity。

公共 contract 不得包含 Godot node、scene tree、animation、collision shape、frame 或其他
engine-specific type。

## 必须行为

1. 相同规范化 `WorldBrief` 和 seed 生成相同 `RunnableWorldPackage.package_hash`。
2. Ready Session 记录准确 `source_package_hash`；初始 snapshot、canonical state 和 public
   projection 具有相同 revision/state hash。
3. `step N` 精确推进 N 个 tick；tick、world time、event sequence 和 revision 单调递增。
4. 每个 accepted canonical mutation 都有 accepted event 和非空 applied diff；rejected
   request 有公开原因且没有 applied diff。
5. 至少一个 Agent cycle 记录 perception、decision/intent、`ActionRequest`、rule judgment、
   `ActionResult`、event 和 diff refs。
6. 后续 Agent decision 至少包含一个引用先前 public event/action result 的
   `AgentExperienceRef`，并以机器可观察方式改变 public decision evidence。
7. 同一个 `InterventionWindow` 接受一条 bounded direction，并拒绝一条直接指定最终事实的
   请求。拒绝原因必须是语义非法，不能只是“window closed”。
8. Accepted direction 只能进入 queue 或 candidate path，并在后续规则判断中应用，不能直接
   patch canonical state。
9. `ActionRequest` 和 `FeedbackEvent` 使用 request ID；重复 ID 幂等返回原始公开结果。
10. Stale expected revision 返回稳定 conflict result，不得静默覆盖新状态。
11. 管理控制台所有 mutation 都通过这些 API，并显示 public projection 返回的相同 session
    ID、tick、revision 和 state hash。
12. 只知道 base URL 和 capability manifest 的黑盒客户端可以完成生成、boot、step、提交
    两种 direction、检查 Agent、轮询事件和导出 evidence。

## 允许修改

- 在 `backend/app/` 下新增通用 engine modules。
- 在 `backend/app/schemas/` 下新增版本化 schemas。
- 在 `backend/app/api/routes/` 下新增版本化 router，并注册到 active app factory。
- 新增 deterministic MVP 所需的 process-local stores。
- 在 `frontend/src/` 下新增管理控制台 API client、page、components 和 navigation。
- 在 `backend/app/tests/` 与 `frontend/` 下新增 focused backend/frontend/E2E tests。
- 更新本 package review 列出的 v0.13 docs 和 project entrypoints。

## 禁止修改

- 不在 `backend/worldengine/` 下新增 runtime feature。
- WorldEngine source/tests 中不加入 concrete demo/validation world、character、map、location、
  item、story rule 或 visual asset。
- WorldEngine 中不加入 Godot code、scene、project 或 engine-specific schema。
- `0.13.0` 不修改外部仓库。
- Public state/evidence 不依赖或包含 live provider、provider key、raw prompt/response、
  provider trace、raw thought、chain-of-thought、private memory、private goal 或 hidden context。
- 不接受 client-provided state patch、final fact、Agent thought、action result 或 checker verdict
  作为 canonical truth。
- Frontend 不直接访问 storage 或 core Python object。
- 不做 production persistence、migration、distributed execution、deployment 或完整 v0.13 PASS
  声明。
- 不为了让新 package 更容易实现而删除或回滚既有脏改动。

## 兼容性要求

- 新 contract 是 design-first，可以使用新的 `/api/v1` surface，不继承当前 endpoint 形状。
- `0.13.0` 期间保留既有 public surfaces，除非 contract 经重新评审明确允许 deprecate。
- 既有脏文件属于用户，必须兼容或不触碰。
- 复用代码必须通过 v0.13 tests；历史 tests 不足以证明通过。
- Event 和 evidence additions 必须 public、deterministic 且 redaction-safe。

## 范围外后续

- Godot executor 和 external checker：`0.13.1`。
- 完整 cross-client run 和 final classification：`0.13.2`。
- Live LLM 生成/决策质量、持久化、恢复、branch、递归世界、多 Agent 行为和更深 pseudo-self：
  锚点通过后的后续已评审版本。

## 退出条件

- 用户批准 contract、design、test plan 和 plan。
- 只读 documentation/contract evaluator 无 P1/P2。
- 代码修改前记录 `implementation_authorized: yes`。
- 当前 focused verification 证明本 package 拥有的所有 required behavior。
- Review 记录准确 changed files、commands、tests、compatibility、scope 和 evaluator evidence，
  且没有未解决 P1/P2。
