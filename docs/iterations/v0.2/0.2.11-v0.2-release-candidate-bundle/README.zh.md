# 0.2.11 v0.2 Release Candidate Bundle

状态：`review complete`

类型：`documentation-only`

英文版本：`README.md`

## 目标

准备一个可 review 的 documentation-only package，用于在 0.2.10 之后组装
v0.2 release-candidate evidence bundle，但不声明 v0.2 final release。

## 范围

本包后续会创建 release-candidate bundle，用来汇总已完成的 v0.2 package
evidence、compatibility boundaries、known limitations、unresolved findings，
以及给 human / ChatGPT review 的 final-review input。

bundle 只能反映 completed package reviews 和 v0.2 audit documents 中已经存在的
evidence。它不能通过修改 runtime、schema、API、frontend、fixture、migration 或
test implementation files 来填补 evidence gaps。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 状态清单

- [x] Docs drafted
- [x] Contract drafted
- [x] Technical design drafted
- [x] Test plan drafted
- [x] Documentation-stage evidence complete
- [x] Release-candidate bundle complete
- [x] Human / ChatGPT review complete
- [x] Review complete

## Review 后计划交付

- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`
- `docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md`
- `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md`
- `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md`
- 更新 `docs/releases/v0.2.md`
- 更新 `docs/releases/v0.2.zh.md`
- 如果 release-candidate review 发现 evidence gaps、P1/P2 blockers 或 v0.3
  handoff risks，则更新 `docs/iterations/v0.2/findings.md`。
- 在 `review.md` 和 `review.zh.md` 记录本包 implementation evidence。

## 假设

- 0.2.1 到 0.2.10 在本包 implementation 前均保持 `review complete`。
- 0.2.11 是 release-candidate package，不是 final closeout。
- `docs/iterations/v0.2/README.md` 是 milestone index。
- Release-candidate claims 必须可追溯到已有 reviews、audits、contracts 或
  release docs。
- 当前 open P3 findings 如果不阻塞 release-candidate review，可继续作为 v0.3
  handoff items。

## 开放风险

- 组装 bundle 时可能发现 P1/P2 evidence gap。若出现，必须显式记录，并且在
  resolved 或 explicitly accepted 前不得进入 final closeout。
- 既有 package reviews 中的测试来自 earlier sessions，不是当前 0.2.11 的 runtime
  re-execution。bundle 必须区分 historical package evidence 和 0.2.11
  当前运行的 commands。
- Release wording 可能误导为 final status。本包必须明确所有 release-candidate
  docs 都不是 final；v0.2 只有到 0.2.12 才能 final。
