# 0.6.3 结构化生成计划编译器

Status: review complete
Type: mixed
implementation_authorized: yes

## 目标

定义并且仅在 review authorization 之后实现 structured generation plan compiler，把已验证的
plan data 通过 `0.6.1` 已评审的 generic generation semantics 和 `0.6.2` 的
deterministic generator evidence 转换为 valid `WorldSpec` output。

本 package 必须保持 plan compilation provider-independent。Structured plan 后续可能由
AI system 产生，但本 package 把所有 plan 都当作 untrusted data，不执行 free-form prompt
text，也不调用 external providers。

## 范围

文档阶段：

- 创建本 package 和中文镜像。
- 定义 plan schema、compiler semantics、deterministic diagnostics 和 metadata
  requirements。
- 定义 authorization 后可以触碰的准确 backend files。
- 定义 verification commands 和 compatibility gates。

实现阶段，仅在授权后：

- 扩展 `backend/app/schemas/world_generation.py`，添加 additive structured plan
  schema 和 metadata fields。
- 扩展 `backend/app/core/world_generation.py`，添加 plan validation 和 compiler
  functions。
- 添加 focused backend tests，覆盖 structured plan schema 和 compiler behavior。
- 只在保护兼容性需要时更新现有 generation tests。

禁止：

- 不添加 public API routes、frontend、persistence、migrations、fixtures、generated
  seed files、external validation readiness、projection readiness、Agent/memory
  changes、runtime tick/event changes 或 `backend/worldengine/` runtime features。
- 不把 free-form prompt text 当成可执行 generation behavior。
- 不调用 external AI providers，也不读取 credentials/secrets。
- 不添加 concrete world names、maps、characters、locations、resources、story
  rules、private validation oracle details 或 application-specific backend behavior。

## 交付物

- 完整 package docs 和中文镜像。
- 已评审 implementation authorization criteria。
- 授权后的 structured plan schema 和 deterministic compiler。
- 实现后的 focused tests，以及相邻 template-generator / loader /
  runtime-context compatibility evidence。

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
均已完成，evaluator PASS，且无 P1/P2/P3。本 package 将已评审的 structured plan compiler
evidence hand off 给
`0.6.4-ai-assisted-generation-boundary-and-plan-import`。
