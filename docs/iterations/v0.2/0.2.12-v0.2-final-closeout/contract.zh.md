# Contract

英文版本：`contract.md`

## Public Concepts

- Final closeout：在 release-candidate bundle 被接受且 blockers 被清除或明确分类后，
  以 documentation-only 方式标记 v0.2 final。
- Final review decision：human / ChatGPT approval、rejection 或 conditional
  acceptance，用于决定 final closeout 是否可以进行。
- Blocking finding：阻止 final closeout 的 unresolved P1/P2 issue。
- Accepted handoff：non-blocking finding，当前预期只适用于 P3，保留给 v0.3 或更晚 work，
  并有明确 closeout wording。
- Historical evidence：早期 package reviews 中记录的 commands 和 test results，必须与
  0.2.12 中运行的 commands 区分。

## Compatibility Constraints

- Runtime behavior 不得改变。
- Schema behavior 和 validation behavior 不得改变。
- Event storage、event pagination、archive behavior、grouping behavior 和 API
  response behavior 不得改变。
- Frontend behavior 不得改变。
- Fixture、migration 和 test implementation files 不得改变。
- `backend/worldengine/` 必须 untouched。
- 只有在 approval 存在且没有 unresolved P1/P2 findings 时，才可声明 final release
  status。
- Final closeout wording 必须区分 historical package evidence 和 current-session
  0.2.12 verification。

## Allowed Changes

- Add or update
  `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/` 下的文件。
- Review approval 后更新 `docs/releases/v0.2.md` 和 `docs/releases/v0.2.zh.md`。
- 更新 `docs/iterations/v0.2/README.md` 和 `docs/iterations/v0.2/README.zh.md`。
- 更新 `docs/iterations/v0.2/v0.2-plan.md` 和
  `docs/iterations/v0.2/v0.2-plan.zh.md`。
- 如 final review 改变 finding status、blocker classification 或 v0.3 handoff
  wording，更新 `docs/iterations/v0.2/findings.md`。
- 运行 read-only documentation checks、status consistency checks、release wording
  checks、concrete demo anchor sweeps 和 changed-file scope guards。

## Forbidden Changes

- 不修改 runtime services、schemas、API routes、app assembly、event log behavior、
  archive behavior、persistence behavior、agent behavior、frontend implementation、
  fixture files、migration files 或 test implementation files。
- 不修改 `backend/worldengine/`。
- 不实现 WorldSpec loading、RuntimeEngine-to-WorldCell migration、runtime bridge、
  generation、projection、agent loop、memory、self-continuity、resolver 或 causality
  behavior。
- 不创建 external fixture 或 validation repositories。
- 不增加 concrete external-world names、characters、locations、roles、resources、
  story rules、seed data、UI selectors、private runner state 或 application-specific
  backend logic。
- 除非 command 或 flow 在当前 session 中运行，不声明 tests、builds、runtime behavior、
  API behavior 或 frontend behavior passed。
- 除非 v0.2 final closeout approved and recorded，不标记 v0.3 ready to start。

## Acceptance Requirements

- 本包包含 README、intent、contract、technical design、test plan、plan 和 review docs
  的 English / Chinese mirrors。
- Documentation stage 中，package README 和 v0.2 milestone index 将 0.2.12 标记为
  `ready for review`。
- Final-closeout implementation 明确由 0.2.11 release-candidate approval gate。
- Final status requirements 说明 unresolved P1/P2 findings 会阻塞 closeout。
- Open P3 finding `v0.2-P3-003` 只有在 final review 接受为 non-blocking 时，才作为
  v0.3 handoff。
- Verification requirements 包含 `git diff --check`、release-status wording checks、
  status consistency checks、changed-file scope checks 和 concrete demo anchor sweep。
- 除非在当前 0.2.12 session 中运行，否则不声明 backend、frontend、API smoke、E2E、
  Agent smoke、runtime、schema execution、fixture 或 migration tests。
- Package docs 和 status docs 的 English / Chinese mirrors 保持同步。

## North Star Check

本包通过 evidence 和 boundaries close foundation milestone，保护 WorldEngine 作为通用
recursive world engine 的方向。它不增加 concrete worlds、product UI、private validation
internals 或 runtime shortcuts。

## Out-of-Scope Follow-ups

- v0.3 只能在 approved v0.2 final closeout 和 separate v0.3 package contract 后开始。
- Current-session runtime/API/frontend regression evidence 属于第一个会改变 behavior 的
  v0.3 code 或 mixed package，除非 reviewer 明确要求在 closeout 中运行。
- 任何新发现的 P1/P2 gap 必须成为 blocker 或 separately reviewed follow-up，不能成为
  unreviewed 0.2.12 implementation patch。
