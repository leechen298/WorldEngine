# Review

英文原文：`review.md`。

Status：implementation complete / focused verification passed / evaluator PASS

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
external_validation_authorized: no

## 变更文件

Documentation draft：

```text
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.zh.md
```

Implementation files：

```text
backend/app/schemas/world_direction.py
backend/app/api/routes/world.py
backend/app/tests/test_world_direction_boundary.py
```

## 已运行命令

Documentation checks：

```text
git diff --check
```

结果：exit 0，无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

结果：exit 0；`files 14`；`missing []`。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary"); combined="\n".join(path.read_text() for path in root.glob("*.md")); required=["implementation_authorized: no","provider_live_call_authorized: no","generated_result_creation_authorized: no","external_validation_authorized: no","WorldDirectionRequest","WorldDirectionQueueItem","direct_final_fact","agent_private_state_mutation","rule_bypass","/worlds/{world_id}/director-guidance","0.9.7-rule-linked-evolution-and-event-legality"]; missing=[term for term in required if term not in combined]; print("missing", missing); raise SystemExit(1 if missing else 0)'
```

结果：exit 0；`missing []`。

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|Status(:|：).*implementation complete|Status(:|：).*ready for implementation" docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary
```

结果：documentation gate approval 前 exit 1，无输出。Initial draft 当时没有记录 implementation
authorization 或 live/external authorization。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

结果：exit 0；`missing []`；`bad []`。

Evaluator PASS 后，已仅为本包记录 `implementation_authorized: yes`。Provider live-call、
generated-result 和 external validation authorization 仍为 `no`。

Focused implementation test：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Initial RED result：exit 2，符合预期，原因是缺少 `app.schemas.world_direction`。

GREEN result after implementation：exit 0；`6 passed in 0.30s`。

Related public surface regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

结果：exit 0；`40 passed in 0.65s`。

Backend regression：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

结果：exit 0；`303 passed in 2.87s`。

Implementation review repair RED：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

添加 evaluator-gap tests 后结果：exit 1；`4 failed, 11 passed in 0.52s`。失败覆盖了
`public_context` keys 和 `branch_id` 的 private marker 泄漏、不可达的
`future_evaluation_hint`，以及 public rule constraints 的分类优先级。

Implementation review repair focused GREEN：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

结果：exit 0；`15 passed in 0.43s`。

Implementation review repair related public surface regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

结果：exit 0；`49 passed in 0.80s`。

Implementation review repair backend regression：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

结果：exit 0；`312 passed in 2.99s`。

Implementation re-review repair RED：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

添加 documented-private-evidence tests 后结果：exit 1；`3 failed, 17 passed in 0.54s`。
失败覆盖了 `branch_id`、`public_context` keys 和 `instruction_text` 中的文档 anti-leak terms：
`raw prompt`、`raw provider response`、`private evaluator data`。

Implementation re-review repair focused GREEN：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

结果：exit 0；`20 passed in 0.52s`。

Implementation re-review repair related public surface regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

结果：exit 0；`54 passed in 0.88s`。

Implementation re-review repair backend regression：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

结果：exit 0；`317 passed in 3.09s`。

```text
git diff --check
```

second repair 后结果：exit 0，无输出。

## 测试结果

Focused、related public surface 和 backend regression tests 在 implementation review repairs
后已按上文记录通过。Provider、checker、external validation、generated-result、E2E、
autonomous、frontend 和 Validation Client tests 未运行，因为本包不授权这些工作。

## 兼容性审查

Implementation 添加 additive public `/worlds/{world_id}/direction` surface，并在 focused 和
related regression tests 下保持既有 benign `/worlds/{world_id}/director-guidance` behavior、
public handoff behavior、event listing、runtime controls、rule-parameter schemas 和 fidelity
helpers。

## 范围审查

Implementation 保持在 active-backend public direction schema、world-route API behavior 和
focused backend tests 范围内。它没有添加 live provider calls、generated-result creation、
checker execution、external validation、Validation Client code、frontend UI、durable
scheduling、event legality/final adjudication、Agent continuity 或 `backend/worldengine/`
changes。

## Subagent Findings

Read-only documentation/contract evaluator：

```text
agent: 019e98f6-7cf2-7b12-842e-1cd4991c608b
scope: 0.9.6 docs/contract/design/test-plan/mirror review only
status: PASS
```

Verdict：PASS，没有 P0/P1/P2/P3 findings。

Evaluator 确认：

- required mixed-package docs 和 Chinese mirrors exist。
- package status 和 authorizations 在 review 前保持关闭。
- contract 与 parent v0.9 route 和 `v0.9-plan.md` coherent。
- local review updates 后，implementation scope 足够具体，可以 authorize。
- package 保留 queued world-level guidance 与 out-of-scope event legality/direct
  mutation 的边界。

Initial implementation-scope evaluator：

```text
agent: 019e9900-d096-7cc1-b1e3-05ad9b54b588
scope: 0.9.6 implementation review only
status: FAIL
```

Verdict：FAIL，有一个 P1 和一个 P2。

- P1：用户可控的 `public_context` keys 和 `branch_id` 可能通过 public responses 或 event
  payloads 泄漏 private markers，因为 classification 当时只检查 `instruction_text`。
- P2：evaluator-gap tests 不足，并且 deterministic classification 中
  `future_evaluation_hint` 不可达。

Local repair 已增加覆盖 `instruction_text`、`branch_id` 和 `public_context` keys 的
private-marker redaction tests；覆盖所有 allowed categories 可达性、rule bypass、Agent goal
mutation、timing、以及既有 director-guidance compatibility。Implementation 现在会跨所有
public request fields 分类，在需要 redaction 时不回显事件字段，并暴露缺失的
future-evaluation category。

First implementation-scope re-review：

```text
agent: 019e9900-d096-7cc1-b1e3-05ad9b54b588
scope: 0.9.6 implementation re-review only
status: FAIL
```

Verdict：FAIL，有一个 P1 和一个 P3。

- P1：private marker vocabulary 漏掉了文档中的 anti-leak terms：`raw prompt`、
  `raw provider response`、`private evaluator data`。
- P3：focused tests 尚未断言 `inventory_injection` 和 `relationship_override` forbidden
  categories。

Local second repair 已增加测试，覆盖 `branch_id`、`public_context` keys 和 `instruction_text`
中的 documented anti-leak terms；补齐剩余 forbidden categories；并将文档 raw/private
evidence terms 的空格和下划线形式加入 marker vocabulary。

Second implementation-scope re-review：

```text
agent: 019e9900-d096-7cc1-b1e3-05ad9b54b588
scope: 0.9.6 implementation second re-review only
status: PASS
```

Verdict：PASS，无 P0/P1/P2/P3 findings。

Evaluator 确认 marker vocabulary 覆盖 documented anti-leak terms，classification 检查
`instruction_text`、`branch_id` 和 `public_context` keys，需要 redaction 时 public/event
echo 会置空，focused tests 覆盖 documented anti-leak terms 以及剩余 forbidden categories，
且 `future_evaluation_hint` 仍可达。

## 未解决 P1/P2/P3

- 无。

## 最终评估

Documentation gate complete。Implementation 已完成 reviewed `0.9.6` scope。Focused、related
public-surface、backend regression 和 `git diff --check` verification 已通过，
implementation-scope evaluator re-review 已通过，且无 P0/P1/P2/P3 findings。

Provider live calls、generated-result creation、checker execution、external validation、
Validation Client changes、frontend UI、event legality、Agent continuity、durable scheduling
和 `backend/worldengine/` changes 仍未授权。
