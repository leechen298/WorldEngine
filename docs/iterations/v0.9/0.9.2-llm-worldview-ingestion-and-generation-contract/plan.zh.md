# Plan

英文镜像：`plan.md`。

## Ordered Steps

1. 读取 v0.9 parent docs、v0.6 generation contracts、v0.8 public world creation handoff、
   `0.9.1` provider smoke/redaction docs，以及 LLM-backed world creation scenario。
2. 创建完整 `0.9.2` package document set 和 Chinese mirrors。
3. 运行 `test-plan.md` 中的 documentation checks。
4. 发送给 read-only documentation/contract evaluator。
5. 修复或记录 evaluator findings。
6. 如果没有 P0/P1/blocking P2，更新 `review.md` 为 `implementation_authorized: yes`；
   否则在 code changes 前停止。
7. 只实现 reviewed active-backend worldview generation contract。
8. 添加 public schemas、route wiring、generation helper 和 focused backend tests。
9. 保持 existing deterministic `POST /worlds`、provider smoke、manifest 和 validation error
   sanitization behavior。
10. 运行 focused backend tests，以及本包修改的 checker tests。
11. 如果 implementation 触碰 shared backend surfaces，运行 backend regression。
12. 更新 `review.md`，记录 commands、results、compatibility review、scope review、
    unresolved findings、final assessment 和 handoff to `0.9.3`。

## Phase Boundaries

Documentation phase：

- 创建并 review package documents。
- authorization 前不得修改 runtime、API、schema、backend test、checker、fixture、provider、
  generated result、external repository、Validation Client 或 `backend/worldengine/` files。

Implementation phase：

- 只有本包 review 记录 `implementation_authorized: yes` 后才可开始。
- 必须停留在 allowed active-backend 和 focused checker/test scope。
- 不得把 deterministic fallback 重新解释成 LLM-backed success。

Evidence execution phase：

- Live provider calls 默认关闭。
- 没有 provider authorization 时，只记录 not-configured、fallback 或 blocked behavior，不记录
  provider-backed PASS。
- Generated public evidence 必须 redacted and structured。
- Safe mock behavior 可支持 deterministic tests，但必须标为 non-live，不能算 provider-backed
  generation PASS。

## Files

Documentation phase 创建：

```text
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/README.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/README.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/intent.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/intent.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/contract.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/contract.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/technical-design.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/technical-design.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/test-plan.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/test-plan.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/plan.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/plan.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/review.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/review.zh.md
```

Implementation authorization 后允许：

```text
backend/app/agent/
backend/app/api/routes/
backend/app/api/app_factory.py
backend/app/schemas/
backend/app/tests/
tools/testing/validate_agent_autonomous_result.py
```

Do not touch：

```text
backend/worldengine/
frontend/
external repositories
Validation Client repository
generated result directories
concrete validation fixtures
migrations
```

## Verification

Documentation phase：

- required child docs and mirrors。
- required term coverage。
- markdown whitespace/final newline check。
- `git diff --check`。
- subagent/evaluator review。

Implementation phase after authorization：

- focused backend API/schema/redaction tests。
- existing public handoff tests。
- shared backend surfaces changed 时 backend regression。
- checker support changed 时 checker validation。

## Stop Conditions

Stop if：

- package docs 与 v0.9 parent scope 冲突。
- evaluator reports unresolved P0/P1/blocking P2。
- implementation requires Validation Client changes。
- implementation requires `backend/worldengine/` changes。
- generated output cannot be structured without concrete demo content。
- premise specificity can only be proven by exposing raw prompt or raw provider response。
- deterministic fallback would be presented as LLM-backed PASS。
- safe mock 或 provider readiness would be presented as provider-backed world generation evidence。
- tests cannot prove redaction、fallback classification 和 compatibility。

## Review Update Step

closeout 前，`review.md` 必须记录：

- changed files。
- commands run。
- documentation/contract evaluator evidence。
- test results 或 docs-only no-test rationale。
- provider live-call status。
- compatibility review。
- scope review。
- unresolved P1/P2/P3 findings。
- final assessment and handoff。
