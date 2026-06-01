# 技术设计

状态：review complete

## 结构

本修复包含两个代码层变更和一个证据层同步。

| 区域 | 设计 |
| --- | --- |
| Failed generation fallback | 在 template 和 plan generation 中，fallback digest payload 使用 `_json_compatible_or_none(request.seed_material)` 保留有效 `seed_material`，不再一律丢弃 seed。 |
| Preview API coverage | 增加 FastAPI TestClient 测试，提交带 sensitive redacted provenance metadata 的 imported-plan preview request，并断言 public response 失败且已脱敏。 |
| Evidence reconciliation | 增加本 package，并在验证后更新 parent review、implementation summaries 和 durable reliability result。 |

## 影响文件

代码/测试文件：

- `backend/app/core/world_generation.py`
- `backend/app/tests/test_deterministic_world_generation.py`
- `backend/app/tests/test_structured_generation_plan_compiler.py`
- `backend/app/tests/test_generation_preview_api.py`

现有 frontend/E2E repair files 只因为当前 post-closeout dirty set 已包含已评审的
dashboard diagnostics repair 而处于本包范围内：

- `frontend/src/components/GenerationPanel.vue`
- `frontend/src/components/GenerationPanel.test.ts`
- `frontend/e2e/dashboard-generation.spec.ts`

文档/证据文件见 `contract.md`。

## 数据流

1. Validation 为非 JSON metadata 或 constraints 收集 diagnostics。
2. Digest creation 先尝试完整 canonical payload。
3. 如果完整 payload 不可 canonical，fallback digest 保留稳定 ids、versions、可 canonical 的
   request constraints，以及可 canonical 的 seed material。
4. 如果 seed material 本身不可 canonical，保留现有 `unsupported_seed_material` diagnostic，并将
   fallback seed material 设为 `None`。

## 兼容性策略

修复只改变 fallback digest 场景中的 failed-result metadata。Passed generation 行为和 public
schema 形状保持不变。

## 防漂移规则

- 修复 diagnostics 时不新增 generation behavior。
- 不用 `0.6.10` 授权 implementation edits。
- 保持 reliability result 与 package review evidence 一致。
