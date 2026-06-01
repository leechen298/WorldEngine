# 合同

状态：review complete

implementation_authorized: yes

## 公共概念

本包不新增公共概念。它修复现有 v0.6 generation reliability 和 evidence consistency：

- 即使无关的非 JSON metadata 或 constraints 让完整 request payload 无法 canonical，
  failed generation ids 与 seed digests 也必须保留有效 seed material。
- 当 redacted provenance 仍包含 sensitive metadata keys 时，imported-plan preview 必须通过
  public preview API 失败。
- clean-pass evidence 需要已评审的 package-specific scope guard，而不是
  documentation-only 的 `0.6.10` contract。

## 允许修改

- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/**`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_deterministic_world_generation.py`
- `backend/app/tests/test_structured_generation_plan_compiler.py`
- `backend/app/tests/test_generation_preview_api.py`
- `backend/app/tests/test_plan_import_boundary.py`
- `frontend/src/components/GenerationPanel.vue`
- `frontend/src/components/GenerationPanel.test.ts`
- `frontend/e2e/dashboard-generation.spec.ts`
- `docs/backend-implementation.md`
- `docs/backend-implementation.zh.md`
- `docs/current-implementation.md`
- `docs/current-implementation.zh.md`
- `docs/frontend-implementation.md`
- `docs/frontend-implementation.zh.md`
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`
- `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`

## 禁止修改

- `backend/worldengine/**`
- `backend/app/alembic/**`
- `backend/migrations/**`
- `test-results/**`
- 外部仓库。
- 新 public routes、新 schemas、migrations、persistence、live provider integration、
  concrete world content、private validation oracle details、projection application code，
  或 v0.7/v0.8 范围。
- root README 或 roadmap status sync，除非后续 review 明确要求。

## 兼容性要求

- 现有 v0.6 template、plan、import、preview、regeneration、runtime-readiness、
  dashboard 和 E2E 行为保持 additive 和 backward compatible。
- 只有之前因 fallback path 折叠的 failed requests，其 failed generation id/digest 值可以变化。
- 不得声明 live Agent smoke、full autonomous runner、external validation readiness、
  projection readiness、live provider behavior、generation quality 或 product readiness 已通过。

## 范围外后续

- v0.7 负责 external validation readiness。
- v0.8 负责 external projection application readiness。
- 未来 generation-quality evaluation 需要独立已评审 package。
