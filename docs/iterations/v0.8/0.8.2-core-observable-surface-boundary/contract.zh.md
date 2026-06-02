# Contract

## 公共概念

- `observable surface family`：一组 generic、public、read-only、redacted 的 evidence 或
  state summaries，供未来 validator 检查。
- `public source boundary`：可以被引用的 existing API、contract、report、manifest 或 evidence
  surface，但不得暴露 private details。
- `allowed observable summary`：未来 payload 可以暴露的有边界 summary class。
- `forbidden exposure`：不得出现在 public surfaces 中的数据或行为。
- `implementation authorization criteria`：后续 package 在添加 schemas、checkers、APIs 或
  helpers 前必须满足的条件。

## 允许修改

- 创建或更新
  `docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/` 下的文件。
- 创建或更新本 package 的中文镜像。
- 更新 parent v0.8 status 和 route surfaces。
- 定义 observable surface families、public source boundaries、allowed summaries、forbidden
  exposure、compatibility rules，以及后续 packages 的 implementation authorization criteria。

## 禁止修改

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository 或 `backend/worldengine/` implementation files。
- 不新增 `docs/contracts/` schemas、`tools/testing` checkers、API routes、frontend UI、
  E2E tests、generated artifacts 或 report templates。
- 不实现 write APIs、reset APIs、persistence、migrations、product UI、external validation
  behavior、projection application behavior 或 consumer-specific backend behavior。
- 不暴露 raw memory、prompt traces、private transcripts、provider secrets、UI selectors、
  private app data、oracle internals 或 concrete world content。
- 不把 runtime、API、frontend、E2E、Agent smoke、autonomous、external validation、projection
  readiness、product readiness、minimum working-state 或 release behavior 标记为 passed。

## 兼容性要求

- Existing runtime、event、archive、params、Agent loop、memory、generation、API envelope、
  dashboard、readiness manifest 和 projection read-model behavior 保持 unchanged。
- v0.7 projection read-model 与 external-validation readiness contracts 仍是 public redaction
  和 read-only baseline。
- 未来 observable surfaces 必须 additive、versioned、redacted、read-only；除非后续 reviewed
  package 明确授权，否则不得例外。

## 实现授权条件

后续 package 只有在 reviewed contract 记录以下内容后，才可实现 observable schemas、
checkers、helpers 或 API surfaces：

- exact surface family ids。
- exact file classes 和允许修改的 paths。
- payload fields 和 redaction rules。
- no-write/no-reset side-effect rules。
- focused tests 和 adjacent compatibility checks。
- 对 external validation PASS、product readiness 和 projection application readiness 的明确
  non-claims。

## 范围外后续

- `0.8.3`：如果 reviewed，负责 generation/runtime/Agent-loop readiness implementation
  planning 和 hardening。
- `0.8.4`：external-validation handoff contract。
- `0.8.5`：core-side working-state smoke evidence。
