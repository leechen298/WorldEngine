# 0.11.1 Provider And Worldview Generation Preflight

英文版本：`README.md`。

状态：`implementation complete / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

新增一个 redaction-safe preflight surface，让 public clients 在 v0.11 rule-bound
evolution 依赖 provider/worldview generation 前，能知道当前是 provider-backed、
safe mock、deterministic fallback，还是 blocked。

本包不执行 live provider calls。它只基于 WorldEngine 已有 provider/worldview helpers
诚实分类 readiness 和 generation mode，并暴露 client-readable evidence。

## 范围

评审后允许：

- 新增 additive provider/worldview preflight schema 和 API。
- 为 preflight surface 更新 manifest discovery。
- 生成 redaction-safe provider 和 worldview mode summaries。
- 增加 focused backend tests，覆盖 configured、not configured、mock、fallback 和
  redaction behavior。
- 记录文档证据并同步 parent route。

禁止：

- 不运行 live provider calls，不声明 provider quality PASS。
- 不暴露 raw prompts、raw provider responses、provider traces、secrets、private memory、
  raw thought、hidden context 或 private evaluator data。
- 不实现 Validation Client，也不声明 external Validation Client PASS。
- 不实现 world rules、direction queue、event generation、diff application 或 fidelity scoring。
- 不做 durable persistence/migrations。
- 不修改 `backend/worldengine/`。

## Expected Deliverables

- Public provider/worldview preflight API。
- 与 provider readiness 和 generation mode 绑定的 public preflight status taxonomy。
- Manifest 中的 preflight surface entry。
- Focused tests 证明 not-configured、safe-mock、configured-without-live-call blocked、
  deterministic fallback 和 redaction behavior。

## 状态检查清单

- [x] Package documents drafted。
- [x] Documentation / contract evaluator complete。
- [x] implementation_authorized: yes。
- [x] Implementation complete。
- [x] Verification complete。
- [x] Evaluator closeout complete。
