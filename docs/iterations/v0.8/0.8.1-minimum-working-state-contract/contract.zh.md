# Contract

## 公共概念

- `minimum working-state`：一个有边界的 core-side claim，表示 generation、runtime、event
  evidence、Agent loop、memory context、projection/read-model observability 和 blocker
  classification 足够一致，可由后续 current-session evidence 证明。
- `required core slice`：在提出 claim 前，必须明确为 pass、blocked、skipped with rationale
  或 out of scope 的领域。
- `claim taxonomy`：允许使用的状态词汇，用于防止 contract、observable surface、evidence、
  handoff 和 external validation PASS 被混淆。
- `evidence class`：documentation、schema/checker、API、backend、frontend、E2E、Agent smoke、
  autonomous、external validation 或 manual review evidence；每类 evidence 都有自己的授权和
  non-claim boundary。

## 允许修改

- 创建或更新
  `docs/iterations/v0.8/0.8.1-minimum-working-state-contract/` 下的文件。
- 创建或更新本 package 的中文镜像。
- 更新 parent v0.8 status 和 route surfaces。
- 为 `0.8.2` 到 `0.8.5` 定义 claim taxonomy、required core slices、evidence classes、
  exclusions 和 authorization criteria。

## 禁止修改

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository 或 `backend/worldengine/` implementation
  files。
- 不实现 schemas、checkers、services、APIs、UI、persistence、tests、smoke runners、
  external validation behavior、external application behavior 或 evidence artifacts。
- 不添加 concrete world content、private external repository paths、UI selectors、hidden reset
  APIs、private transcripts、oracle internals、provider traces、secrets 或 product-specific
  backend logic。
- 不把 runtime、API、frontend、E2E、Agent smoke、autonomous、external validation、projection
  readiness、product readiness、minimum working-state 或 release behavior 标记为 passed。

## 兼容性要求

- Existing runtime、event、archive、params、Agent loop、memory、generation、API envelope、
  dashboard、readiness manifest 和 projection read-model behavior 保持 unchanged。
- v0.7 `0.7.9` checker/docs repair evidence 只能作为 handoff context。
- 未来 implementation 必须 additive，除非后续 reviewed child package 明确授权 breaking
  change。

## 范围外后续

- `0.8.2`：定义 observable public surfaces。
- `0.8.3`：只有 reviewed 后才实现或 harden core readiness slices。
- `0.8.4`：定义 external-validation handoff contract。
- `0.8.5`：运行 core-side smoke evidence。
