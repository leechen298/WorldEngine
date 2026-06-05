# 完整产品验证结果模板

状态：模板

英文镜像：`result-template.md`。

用于：

```text
docs/testing/results/YYYY-MM-DD-complete-product-validation.zh.md
```

## Header

```markdown
# 完整产品验证结果

Status: clean_pass | partial_pass | failed | blocked
Mode: documentation audit | command validation | autonomous validation | LLM-backed lifecycle | mixed
Date: YYYY-MM-DD
Branch:
Commit:
Result directory:
英文镜像：`YYYY-MM-DD-complete-product-validation.md`
```

## Scope

```markdown
## Scope

In scope:

- ...

Out of scope:

- ...

本结果不声明：

- ...
```

## Current Baseline

记录本次运行依赖的当前状态：

- active version 或 package state。
- 相关 prior durable result files。
- LLM-backed lifecycle 是否在范围内。
- Validation Client 是否在范围内。

## Command Matrix

| Layer | Command or checker | Working directory | Result | PASS authority | Artifact |
| --- | --- | --- | --- | --- | --- |
| L0 | ... | ... | ... | yes/no | ... |

## Coverage Matrix

| CPV ID | Capability | Scope status | Validation status | Evidence | Findings |
| --- | --- | --- | --- | --- | --- |
| CPV-01 | Governance and scope boundary | in_scope | pass/fail/blocked/skipped/out_of_scope | ... | ... |

`coverage-map.md` 中每个 CPV row 都必须出现。

## Scenario Results

| Scenario | Status | PASS/FAIL source | Artifact | Notes |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

## Artifact Summary

列出 required artifacts 及其是否存在：

- `result.json`:
- `coverage-matrix.json`:
- `command-matrix.md`:
- `operation-log.jsonl`:
- `api-summary.json`:
- `redaction-scan.json`:
- `second-agent-review.md`:

## Redaction Review

```markdown
Redaction verdict: pass | fail | not_run

Forbidden content scan:

- API keys:
- authorization headers:
- raw prompts:
- raw provider responses:
- private Agent memory/goals/thought:
- hidden context:
- private evaluator/oracle data:
- concrete external validation world seed data:
```

## Second-Agent Review

```markdown
Second-Agent review: pass | failed | not_run
Reviewer:
Blocking P1/P2: yes | no
Report:
```

## Failures And Findings

| ID | Severity | Taxonomy | Evidence | Required follow-up |
| --- | --- | --- | --- | --- |
| ... | P1/P2/P3 | provider/world_creation/world_evolution/event_legality/agent_autonomy/redaction/client_evidence/checker_gap/runtime/frontend/docs/environment | ... | ... |

## Verdict

```markdown
Verdict: clean_pass | partial_pass | failed | blocked

Reason:

Evidence source:

Unresolved blockers:
```

## Handoff

使用 `gap-routing.md` 路由后续：

- testing assets:
- WorldEngine iteration:
- Validation Client milestone:
- provider/environment:
- redaction repair:
