# Contract

英文源文件：`contract.md`。

状态：文档已起草 / 等待评审

## 公开概念

- **Immediate worldview fidelity**：公开 scorecard evidence，用于检查 generated public world model、creation summary 和 rule summary 是否覆盖关键 public premise indicators。
- **Bounded-run worldview fidelity**：公开 scorecard evidence，用于检查 bounded runtime/event/diff evidence 是否存在 premise coverage 缺失、contradictions、redaction failures 或 evidence gaps。
- **v0.11 closeout result**：关于 rule-bound world evolution 的有边界声明，不是 Agent autonomy、provider quality、external validation 或 complete MVP readiness。

## 允许修改

评审通过后，本包可以修改：

- `backend/app/core/worldview_fidelity.py` 和 `backend/app/schemas/world_generation.py`，用于 additive public fidelity helpers/schema refinements。
- 聚焦 fidelity tests 和 v0.11 regression tests。
- v0.11 package docs、parent status/review/plan docs 和 handoff docs。
- 如需诚实分类 closeout，可修改 manifest / review text。

## 禁止修改

本包不得：

- 在 public evidence 中使用 raw prompt、raw provider response、provider trace、hidden context、private evaluator data、secret 或 Agent private memory。
- 没有当前 session scorecard/test evidence 时，从 subjective review 声明 PASS。
- 实现 provider live calls 或外部 Validation Client behavior。
- 实现 Agent autonomy、pseudo-self、sleep consolidation 或 long-term memory。
- 修改 frontend、persistence、migrations、具体 demo fixtures 或 `backend/worldengine/`。
- 新增 rule/direction/event-generation feature scope，除非明确记录为 blocker repair。

## 兼容性要求

- 现有 world generation、provider preflight、session、rules、directions、event/diff、manifest 和 public evidence tests 必须保持兼容。
- Fidelity artifacts 必须公开且脱敏安全。
- v0.11 closeout 必须区分 passed、blocked、failed、not-run 和 out-of-scope claims。
- External Validation Client 和 provider live claims 仍未授权，除非后续 package 明确授权。

## 范围外后续

- v0.12 负责 Agent continuity、外部自动化验证、最终 MVP validation 和任何 Validation Client automation。
