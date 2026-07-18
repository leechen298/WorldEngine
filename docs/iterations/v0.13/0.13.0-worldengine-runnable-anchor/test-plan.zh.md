# 测试计划

英文源文件：`test-plan.md`。

## 文档 Gate

实现授权前运行：

```bash
git diff --check
python3 -c "from pathlib import Path; p=Path('docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor'); required=['README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md']; print({'missing':[n for n in required if not (p/n).exists()],'empty':[n for n in required if (p/n).exists() and not (p/n).read_text().strip()]})"
rg -n "implementation_authorized: yes|external_repository_changes_authorized: yes|evidence_execution_authorized: yes" docs/iterations/v0.13
rg -n "Godot.*(node|scene tree|collision|frame)|concrete.*world|raw thought|private memory" docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor
```

预期结果：没有 whitespace error；没有 missing/empty package file；没有 active authorization
设为 `yes`；没有把具体外部内容或 engine-specific runtime 语义移入 WorldEngine 的 contract
表述。

## 规划 Backend 聚焦测试

实现授权后新增并运行：

```bash
cd backend
.venv/bin/python -m pytest \
  app/tests/test_engine_v1_generation.py \
  app/tests/test_engine_v1_session.py \
  app/tests/test_engine_v1_agent.py \
  app/tests/test_engine_v1_interventions.py \
  app/tests/test_engine_v1_protocol.py -q
```

必须断言：

- `AC-01`：相同规范化 brief 和 seed 得到相同 ready package hash；允许输入改变后 hash 和
  对应 public field 改变。
- `AC-02`：Session source hash 等于 generated package hash；initial snapshot、canonical
  state 和 projection 的 revision/state hash 一致。
- `AC-03`：`step N` 精确推进 N 个 tick，并保持 time、sequence 和 revision 单调。
- `AC-04`：一个 Agent 产生 perception -> decision -> action request -> rule judgment ->
  result -> event -> diff -> experience evidence。
- `AC-05`：后续 Agent decision 引用先前 public experience，并产生机器可观察的变化。
- `AC-06`：在明确 window 中接受一条 bounded direction，且只通过后续 rule-linked event 和
  非空 diff 应用。
- `AC-07`：在同一 window 中提交的 direct-final-fact direction 返回稳定 rejection reason、
  rejected event、无 diff，目标状态不变。
- `AC-08`：重复 request ID 幂等；stale revision 冲突且不修改状态。
- `AC-09`：当前 state hash 可以从最小运行拥有的 snapshot/diff chain 重建。
- `AC-10`：只使用 base URL 和 capability manifest 的黑盒测试客户端完成生成、boot、step、
  Agent 检查、两种 direction、event polling 和 evidence export。

## 规划 Frontend 验证

```bash
cd frontend
pnpm test
pnpm build
pnpm test:e2e --grep "minimum runnable anchor"
```

必须覆盖：

- 管理控制台生成 package 并显示 readiness/hash。
- 通过 API boot 和 step 同一个 Session。
- 显示 public projection 的 session ID、tick、revision 和 state hash。
- 显示 Agent causal chain 和 prior-experience ref。
- 通过明确 window 提交 accepted/rejected directions。
- 显示 events/diffs/snapshots 并请求 evidence export。
- 不 import backend code，也不直接写 storage。

## 规划回归验证

完成 focused verification 和 implementation-scope review 后运行：

```bash
cd backend
.venv/bin/python -m pytest -q
cd ../frontend
pnpm test
pnpm build
```

只有 focused backend/frontend tests 通过且 code-review evaluator 无 P1/P2 后，才运行更广的
E2E。

## 黑盒 API Smoke

实现计划必须增加一条命令或测试：从干净进程启动 WorldEngine，只通过 HTTP 和 manifest
discovery 驱动完整 WorldEngine 侧流程，输出 correlation IDs 和 WorldEngine-side classification，
但不得声明完整 v0.13 PASS。

## Blocker 与结果规则

- `PASS`：断言已执行，当前证据证明符合预期。
- `FAIL`：断言已执行，但行为或证据不符。
- `BLOCKED`：必需 dependency/environment 不可用，导致命令无法执行。
- `NOT_RUN`：当前阶段有意未执行。
- 缺失证据永远不能 PASS；路径已经执行时应为 FAIL。
- 在 `review.md` 中记录 exact commands、exit codes、counts 和 artifact paths。

## Documentation Stage 不运行

- Backend/frontend/runtime tests：实现尚未授权。
- Provider live calls：必过路径禁止依赖。
- Godot 与 external checker：属于 `0.13.1` 和 `0.13.2`。
- Complete MVP validation：需要外部当前运行证据。
