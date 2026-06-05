# 完整产品验证缺口路由

状态：计划中的路由指南

英文镜像：`gap-routing.md`。

## 目的

本指南防止验证失败变成临时修补。完整产品验证中发现的每个 gap，都应先分类，再进入任何
实现工作。

## Failure Taxonomy

| Taxonomy | 含义 |
| --- | --- |
| `provider` | Provider configuration、live call、quota、network、model 或 provider response 失败。 |
| `world_creation` | World creation 是 generic、deterministic fallback、non-digestible、not provider-backed，或缺 required structures。 |
| `world_evolution` | ticks、parameters、rules、snapshots、diffs 或 replay 不能展示 coherent rule-driven evolution。 |
| `event_legality` | random/user-directed events 绕过 rules、直接强制非法 outcome，或缺 legality evidence。 |
| `agent_autonomy` | Agent action 缺失、只有单轮、client-scripted，或无法关联 WorldEngine public evidence。 |
| `redaction` | Evidence 泄露 secrets、private provider data、private Agent state、raw thought、hidden context、oracle internals 或 concrete external world data。 |
| `client_evidence` | Validation Client logs、API summaries、screenshots、evidence bundle、replay、diff 或 export fields 缺失/格式错误。 |
| `checker_gap` | Scenario 已文档化，但 checker/schema/fixture/result validation 还不能判断。 |
| `runtime` | 非 LLM-specific 的 core runtime、event、params、snapshot、replay 或 API behavior 失败。 |
| `frontend` | Dashboard 或 E2E behavior 失败。 |
| `docs` | 文档不一致、过度声明，或遗漏 required scope/evidence。 |
| `environment` | Local services、dependencies、credentials、ports、budget 或外部可用性阻塞验证。 |

## 路由规则

当产品行为存在，但验证资产无法判断时，路由到 testing assets：

- 缺 scenario docs。
- 缺 saved-result schema。
- 缺 checker fixtures。
- 缺 result template。
- 缺 redaction scan rule。
- 缺 command profile。

首选位置：

- `docs/testing`。
- `tools/testing`。

当 core engine capability 缺失时，路由到 WorldEngine implementation iteration：

- provider live smoke endpoint 或 command。
- provider call abstraction。
- LLM redacted evidence schema。
- LLM-backed world creation。
- world parameter 和 rule schema。
- world rule evolution engine。
- event legality engine。
- Agent persistent memory evidence。
- Agent persistent action evidence。
- runtime、event、snapshot、replay、projection 或 backend API behavior。

当 external client evidence 或 UI 缺失时，路由到 Validation Client milestone：

- operation log export。
- API summary export。
- evidence bundle field。
- replay/diff/snapshot display。
- LLM-backed lifecycle evidence display。
- Agent autonomous operation capture。
- second-Agent evidence handoff package。

当接口正确但外部执行失败时，路由到 provider/environment：

- DeepSeek key 缺失或无效。
- provider quota 用尽。
- provider rate limit。
- network failure。
- model unavailable。
- local service startup failure。
- insufficient budget。

当 secrets 或 private data 泄露时，立即路由到 redaction repair。边界修复并复核前，不继续验证。

## Iteration Decision Rule

不要因为缺验证文档或 checker 就开 WorldEngine 产品迭代。只有缺失能力属于 WorldEngine core
behavior 时，才使用产品迭代。

不要因为 WorldEngine 无法创建、演化或验证世界，就开 Validation Client milestone。客户端负责
观察和导出 evidence，不拥有 engine behavior。

除非 approved package 明确授权 repair，不要在 validation run 内修产品代码。

## Output Format

每个 gap 应记录为：

```text
ID:
Severity:
Taxonomy:
Evidence:
Blocked PASS item:
Recommended route:
Required next document or package:
Stop rule triggered: yes/no
```
