# 0.9.2 LLM Worldview Ingestion And Generation Contract

英文镜像：`README.md`。

Status：ready for implementation
Type：mixed implementation package
implementation_authorized：yes
evidence_execution_authorized：yes, limited to non-live focused tests in `test-plan.md`
provider_live_call_authorized：no
external_validation_authorized：no

## 目标

定义 reviewed contract：把用户提供的 basic worldview premise，通过 WorldEngine-owned
LLM-backed generation，转成 public、system-digestible、premise-specific generated
world model。

本包准备 v0.9 第一条 LLM-backed world creation surface。Implementation 只有在 review
授权后才能开始。既有 deterministic world creation 必须继续 available 且 clearly labeled；
不得把 deterministic fallback 或 mock-only evidence 声明成 LLM-backed PASS。

## 范围

documentation/contract review 之后允许：

- 添加 worldview input schema 和 validation semantics。
- 在 active `backend/app/` backend 中添加 LLM-backed world generation request path。
- 添加 public generated world model schemas 和 `world_creation_summary` style public
  artifact contract。
- 添加 generation provenance summary fields，证明 response 是 WorldEngine-owned、
  provider-classified、redacted，并且是 provider-backed、not configured 或 blocked。
- 添加 validation metadata，覆盖 premise specificity、system digestibility、runtime
  readiness、deterministic fallback labeling 和 redaction。
- 添加明确的 fallback-vs-LLM classification fields，例如 `creation_mode`、`llm_backed`、
  `provider_backed` 和 `deterministic_generic_fallback_detected`。
- 添加 focused backend tests，覆盖 schema validation、API behavior、fallback
  classification、provider-blocked behavior、redaction 和 existing deterministic
  `POST /worlds` compatibility。
- 仅在本包需要验证 public `world_creation_summary` artifact 时，添加 checker support 或
  fixture contract updates。
- code work 后更新本包 `review.md`。

禁止：

- 不暴露、持久化、记录或导出 raw prompts、raw provider requests、raw provider
  responses、provider traces、secrets、authorization headers、private evaluator data、
  hidden context、raw thought、chain-of-thought、private Agent memory 或 private goals。
- 不让 Validation Client 生成、改写、存储 provider keys，或 evaluate generated world content。
- 不在本仓库存储 concrete demo-world fixtures、external validation seed data、maps、
  characters、resources、story rules、oracle internals 或 application-specific backend behavior。
- 不把 existing deterministic generic world creation 声明成 LLM-backed success。
- 不把 `/provider/live-smoke` safe mock behavior 当成 provider-backed world generation proof。
- 不实现 world rule evolution、event legality、bounded runtime control、Agent continuity、
  narrative projection、diagnostic dialogue、full LLM-backed checker、Validation Client
  evidence export 或 lifecycle PASS。
- 不修改 `backend/worldengine/`。

## Deliverables

- Full package document set 和 Chinese mirrors。
- code changes 之前的 reviewed implementation authorization。
- Public worldview ingestion request contract。
- LLM-backed generation request/response contract。
- Public generated world model summary 和 validation metadata contract。
- Redaction 和 deterministic fallback classification rules。
- Focused test plan 和 implementation plan。
- Documentation/contract evaluator evidence。

## Status Checklist

- [x] Package documents drafted。
- [x] Chinese mirrors drafted。
- [x] Documentation/contract evaluator complete。
- [x] Implementation authorized。
- [ ] Implementation complete。
- [ ] Focused verification complete。
- [ ] Review evidence updated。
- [ ] Handoff to `0.9.3` recorded。

## Final Assessment State

当前值：`ready for implementation`。

Implementation 仅在 reviewed non-live `0.9.2` scope 内授权。Live provider calls 继续关闭，
除非本包被明确更新并重新 review 以授权 bounded live execution。
