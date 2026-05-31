# 契约

状态：planned / ready for review

## 公共概念

- `v0.6 World Generation v1`：generic、inspectable `WorldSpec` data generation 的版本边界。
- `WorldGenerationRequest`：未来 request boundary，可携带 generic template id、
  structured generation plan、constraints 和 provenance。
- `WorldTemplate`：generic、reusable generation shape，不得编码 concrete demo-world
  content。
- `GenerationPlan`：可以被验证并编译为 `WorldSpec` 的 structured input。
- `AI-assisted generation`：provider-independent import of structured plans，这些 plan
  可能由 AI system 产生；本 package 不暗示 live provider calls。
- `GenerationMetadata`：inspectable provenance、diagnostics、template/plan lineage、
  validation status 和 regeneration lineage。
- `GenerationPreview`：在 runtime use 前可评审的 bounded generated output summary。
- `RegenerationRequest`：未来 request，用 explicit lineage 和 constraints 修订 prior
  generation request 或 output。

## 能力拆分

| Capability | This package | First implementation candidate |
| --- | --- | --- |
| Generation boundary | 定义 campaign 和 scope | 不写代码 |
| Generation contracts | 只规划 | `0.6.1` docs |
| Template generator | 只规划 | `0.6.2` |
| Structured plan compiler | 只规划 | `0.6.3` |
| AI-assisted plan import | 只规划 | `0.6.4` |
| Metadata and preview API | 只规划 | `0.6.5` |
| Regeneration/readiness | 只规划 | `0.6.6` |
| Dashboard preview | 只规划 | `0.6.7` |

## 兼容性要求

- Existing v0.5 memory/loop schemas 和 APIs 在 `0.6.0` 中保持不变。
- Existing v0.3 `WorldSpec` loader 和 runtime-context bridge 保持不变。
- `WorldSpec`、`WorldCell`、`EntityRef`、`load_worldspec`、
  `build_runtime_context` 和 `RuntimeEngine` tick/time behavior 是
  compatibility-sensitive。
- Existing API envelope/error shape、event routes、params behavior、archive behavior
  和 optional event reference behavior 保持不变。
- Future schema changes 必须是 additive，除非后续已评审 child 明确允许 breaking change。
- v0.5 command evidence 只是 handoff evidence，不是 current v0.6 pass evidence。

## 允许修改

- 创建 `docs/iterations/v0.6/**` documentation。
- 创建 parent campaign files、child package files、中文镜像、review evidence 和 package
  sequencing。
- 命名 planned future implementation paths，但不创建它们：
  - `backend/app/schemas/world_generation.py`
  - `backend/app/world/generation.py` 或等价的已批准路径
  - `backend/app/api/routes/world_generation.py`
  - `backend/app/tests/test_world_generation_*.py`
  - `frontend/src/components/GenerationPanel.vue`
- 记录 evaluator status 和 review findings。

## 禁止修改

- 不得修改 runtime、schema、API、frontend、backend test、fixture、migration、generated
  result、external repository 或 `backend/worldengine/` implementation files。
- 不得在本 package 中创建 planned future implementation paths。
- 不得添加 generation store behavior、public generation APIs、preview UI、regeneration
  behavior、runtime-readiness behavior、durable persistence、migrations 或 tests。
- 不得添加 concrete world names、maps、characters、locations、resources、story rules、
  seed data、UI-specific app behavior、private validation oracle details、external
  validation readiness、projection app readiness、live AI-provider calls 或
  application-specific backend logic。

## North Star 检查

本 package 通过把 world generation 准备为 generic engine capability 来对齐 north star。
它让 application surfaces 继续作为 consumers，不存储 concrete world content，也不把
recursive world architecture 替换为 product-specific state。

## 范围外后续工作

- `0.6.1`：public generation contracts 和 template semantics。
- `0.6.2`：deterministic template generator core。
- `0.6.3`：structured generation plan compiler。
- `0.6.4`：AI-assisted structured plan import boundary。
- `0.6.5`：generation validation、metadata 和 preview API。
- `0.6.6`：regeneration 和 runtime-readiness integration。
- `0.6.7`：dashboard generation preview 和 E2E smoke。
- v0.7 external validation readiness 和 v0.8 projection application readiness。
