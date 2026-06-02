# Contract

## Public Concepts

本 package 定义 documentation-level public concepts：

- external validation readiness。
- projection consumer readiness。
- readiness claim taxonomy。
- redacted validation report semantics。
- projection read-only consumer boundary。
- authorization criteria for schema/checker implementation。

## Compatibility Constraints

- Existing runtime、event、archive、params、Agent loop、memory、generation、API envelope 和
  dashboard behavior 保持不变。
- Existing `docs/contracts/external-fixture-runner-contract.md` 保持兼容，只通过 documentation-level
  readiness semantics additive 扩展。
- Future schema/checker implementation 必须 additive，且不得要求 private consumer details。
- Projection consumer contracts 不得暗示 v0.8 projection application readiness。

## Allowed Changes

- 创建或更新
  `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/` 下的文件。
- 创建或更新本 child package 的中文镜像。
- 创建 documentation-only public contract files：
  - `docs/contracts/external-validation-readiness-contract.md`
  - `docs/contracts/projection-consumer-contract.md`
- Review 后更新 parent v0.7 status and route surfaces：
  - `docs/iterations/v0.7/README.md`
  - `docs/iterations/v0.7/README.zh.md`
  - `docs/iterations/v0.7/v0.7-plan.md`
  - `docs/iterations/v0.7/v0.7-plan.zh.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.7/CURRENT_STATE.md`
  - `docs/iterations/v0.7/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.7/review.md`
  - `docs/iterations/v0.7/review.zh.md`

## Forbidden Changes

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、migration、
  external repository、generated result 或 `backend/worldengine/` implementation files。
- 不实现 JSON schemas、validators、command-line checkers、services、routes、stores、UI、persistence、
  migrations、fixtures 或 test code。
- 不添加 concrete validation worlds、consumer-specific examples、seed data、private transcripts、UI
  selectors、private runner imports、private fixture paths、hidden reset APIs 或 oracle internals。
- 不声明 external suite PASS、projection application readiness、generation-quality PASS、product
  readiness、runtime/API/frontend behavior、E2E、Agent smoke、autonomous 或 release readiness。

## Authorization Criteria For 0.7.2

`0.7.2` 只有在 review 确认以下条件后，才可以实现 report schema/checker support：

- `docs/contracts/external-validation-readiness-contract.md` review complete。
- status values 明确：`pass`、`fail`、`blocked`、`skipped`、`out_of_scope`。
- forbidden leaked details 可由 generic checker 测试。
- accepted `pass` reports 必须要求 redaction confirmation。
- 不需要 private fixture path、UI selector、oracle internal、seed data 或 non-redacted transcript。
- code changes 开始前，`0.7.2` child review 记录 implementation authorization。

## North Star Check

本 package 定义 public consumer contracts，而不是 application behavior，因此保持 WorldEngine generic。
External suites 和 projection applications 仍是 consumers。

## Out-of-Scope Follow-ups

- `0.7.2`：report schema and redaction checker implementation。
- `0.7.3`：readiness manifest and contract bundle。
- `0.7.4`：projection read-model contracts and any approved implementation。
- `v0.8`：first external projection application readiness。
