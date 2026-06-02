# Contract

## Public Contract

Review 后，本 package 可以引入一个 generic core-readiness probe。该 probe 必须是
additive，且不得替换既有 preview、regeneration、runtime-readiness、runtime-step 或
Agent-loop APIs。

Probe contract：

- input：一个 candidate `WorldSpec`，或一个已评审 generation preview request。
- process：validate/preview，派生 runtime context，运行一次 isolated runtime step，并运行一次
  default Agent loop `noop`。
- output：bounded generation、runtime-readiness、isolated runtime-step 和 Agent-loop
  evidence。
- side effects：不得影响 app runtime、app event log、world params、memory store、archive
  store、external repositories 或 provider systems。

## Review 后允许的代码路径

Implementation 只能触及：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/tests/` 下 focused tests

如果 implementation 需要其他文件，必须停止并先更新本 contract。

## Required Semantics

- Probe 对 application runtime 必须 read-only。
- Runtime execution 必须 isolated 且 process-local。
- Isolated runtime 只可向 isolated in-memory event log 写入 bounded events。
- Agent loop action 必须 default 为 `noop`；probe 内 `params.patch` out of scope。
- 返回 evidence 必须 redacted，不得包含超过既有 public preview payload 的 raw `WorldSpec`
  internals。
- Memory context 必须 absent 或 bounded read-only；不得添加 memory read/write API。
- Failure paths 必须返回 diagnostics，不得包含 accepted runtime/Agent success claims。

## Forbidden Changes

- 不修改 frontend、migrations、fixtures、external repos、product app code 或
  `backend/worldengine/`。
- 不添加 write/reset APIs、persistence、live provider behavior、external validation
  execution、product workflow 或 generated-world active runtime。
- 不暴露 prompt/provider traces、secrets、private transcripts、private app data、UI
  selectors、oracle internals、raw memory 或 external event payloads。
- 不声明 external validation PASS、product readiness、generation-quality PASS、Agent smoke
  PASS、autonomous PASS 或 v0.8 final readiness。

## Evidence Requirements

Implementation evidence 必须包含：

- successful 和 failed probe paths 的 focused schema/core tests。
- read-only route 与 forbidden fields 422 envelope 的 focused API tests。
- 证明 probe 不会 mutate app runtime state、app event log、params 或 memory store 的 tests。
- 证明 returned evidence 不包含 raw private payloads 的 tests。
- 若受影响，运行 adjacent generation runtime-readiness 和 Agent-loop tests。
- `git diff --check` 与 changed-file scope guard。

## Authorization

Implementation 尚未授权。授权条件：

1. 本 full package document set reviewed。
2. documentation/contract evaluator 报告无 P0/P1，且无 blocking P2。
3. `review.md` 记录 `implementation_authorized: yes`。
