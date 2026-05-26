# 0.2.9 Generic Schema Evidence and Boundary Audit

状态：`ready for review`

类型：`documentation-only`

英文版本：`README.md`

## 目标

为 v0.2 schema、event、external boundary、legacy boundary 和 status claims
建立可 review 的 documentation-only audit contract，使其在 compatibility review
和 release-candidate 工作前都能映射到 evidence。

## 范围

本 package 在 documentation review 通过后，会创建 evidence 与 boundary audit
documentation。它可以检查 existing contracts、package reviews、current
implementation docs、boundary docs 和 repository paths，但不得修改 runtime、
schema、API、frontend、fixture、migration 或 test implementation files。

Missing evidence 必须记录为 findings 或 next-package input，不得通过未经 review
的 implementation work 修复。

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
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation-stage evidence complete
- [ ] Audit documents complete
- [ ] Review complete

## Review 通过后的计划交付

- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/evidence-index.zh.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/boundary-audit.zh.md`
- 对 `docs/iterations/v0.2/findings.md` 的更新，用于记录 missing evidence、
  boundary gaps 或 status drift。
- 本 package `review.md` 和 `review.zh.md` 中的 implementation evidence。

## 假设

- `docs/iterations/v0.2/README.md` 是 milestone index。
- 除非 later reviewed contract 明确升级 scope，0.2.9 保持
  documentation-only。
- Existing v0.2 package reviews 是 command 和 test evidence 的 primary source。
- `docs/iterations/v0.2/findings.md` 中记录的 deferred 0.2.7 / v0.2 plan
  status mismatch 属于本 audit scope。

## 未决风险

- 部分 active v0.2 claims 可能只有 documentation，没有 current-session test
  evidence；这些必须准确标记。
- Completed package review files 可能在同一文件中同时包含 historical
  documentation-stage evidence 和后续 implementation evidence；audit 必须引用
  相关 section。
- Anchor sweeps 可能因 historical review text 产生 false positives；audit
  必须区分 active boundary violations 和 historical evidence。
