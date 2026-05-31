# 0.6.2 模板目录与确定性生成核心

Status: review complete
Type: mixed
implementation_authorized: yes

## 目标

定义并在 review authorization 之后只实现 v0.6 的 generic template catalog 和
deterministic template-to-`WorldSpec` generator core。

只有当本 package 的 contract、technical design、test plan 和 execution plan 通过
documentation/contract review，并且 `review.md` 记录 `implementation_authorized:
yes` 后，implementation phase 才能开始。

## 范围

文档阶段：

- 创建本 package 和中文镜像。
- 定义 implementation phase 可以触碰的准确 backend schema/service/test 文件。
- 定义 deterministic generation semantics 和 diagnostics。
- 定义 verification commands 和 compatibility gates。

实现阶段，仅在授权后：

- 创建 `backend/app/schemas/world_generation.py`。
- 创建 `backend/app/core/world_generation.py`。
- 在 `backend/app/tests/` 下创建 focused backend tests：
  - `test_world_generation_schema.py`
  - `test_template_catalog.py`
  - `test_deterministic_world_generation.py`

禁止：

- 不添加 public API routes、API envelope changes、frontend code、persistence、
  migrations、archive/params changes、Agent loop 或 memory changes、runtime
  tick/event behavior changes、live AI-provider behavior、external validation
  readiness、projection readiness、generated seed files 或 `backend/worldengine/`
  runtime features。
- 不添加 concrete demo-world names、maps、characters、locations、resources、story
  rules、private validation oracle details 或 application-specific backend
  behavior。

## 交付物

- 完整 package docs 和中文镜像。
- 已评审 implementation authorization criteria。
- 授权后的 generic generation schema 和 deterministic generator core。
- 实现后的 focused tests 以及相邻 schema/loader/runtime-context compatibility
  evidence。

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

## 当前评估

Documentation/contract review、implementation、code review 和 validation evidence
均已完成，evaluator PASS，且无 P1/P2/P3。本 package 将已评审的 deterministic
template generator core hand off 给
`0.6.3-structured-generation-plan-compiler`。
