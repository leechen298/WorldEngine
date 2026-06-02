# Intent

## Objective

创建一个 review-gated audit package，用来判断 reviewed v0.8 evidence 是否足够一致，可以进入
release-candidate bundle 准备。

## Why This Exists

v0.8 已有 documentation contracts、一个 implementation-bearing readiness slice，以及一个
core-side smoke evidence package。在 release-candidate packaging 前，campaign 需要一个独立的
documentation-only audit，验证 evidence references、status surfaces、compatibility
boundaries 和 non-claim language。

## In Scope

- Audit `0.8.0` 到 `0.8.5` review evidence。
- 确认 required evidence references resolve。
- 分类 unresolved P1/P2/P3 findings。
- 确认 skipped、blocked 和 out-of-scope checks 没有被转换为 PASS。
- 确认 v0.7 handoff evidence 没有被提升为 current v0.8 PASS。
- 推荐 release-candidate packaging 是否可以启动。

## Out Of Scope

- Runtime、schema、API、frontend、backend test、checker、fixture、migration 或
  generated-result changes。
- 新 code repairs 或 implementation work。
- External validator 或 external app execution。
- Product readiness、external validation PASS、frontend/E2E PASS、Agent smoke PASS、
  autonomous PASS、generation-quality PASS 或 final v0.8 readiness。

## Success Criteria

只有当 audit report 记录没有 unresolved P1 或 blocking P2 会阻塞 release-candidate packaging，
或用 evidence 明确 block handoff 时，本 package 才可 close。
