# 完整产品验证规范

状态：计划中的验证规范

英文镜像：`validation-spec.md`。

## 验证权威

完整产品验证只能从可复核 evidence 声明 PASS：

- 当前会话命令输出。
- deterministic checker output。
- scorecard checker output。
- saved-result checker output。
- 第二 Agent 只读复核，且无 blocking P1 或 P2 issue。
- 明确记录当前会话 evidence 的 durable result files。

以下内容不是 PASS 来源：

- plans。
- 只有 UI smoke。
- 人工印象。
- 只有 provider readiness。
- 只有 API key 存在。
- 把 deterministic mock behavior 当成真实行为。
- 没有 checker evidence 的 Agent 自我报告。
- result directory 未被 documented checker 检查。

## 角色

| 角色 | 职责 | PASS 权限 |
| --- | --- | --- |
| Main validation agent | 运行命令、操作流程、协调 evidence、写 result summary。 | 没有 checker 或 command evidence 时不能自我声明 PASS。 |
| First operating Agent | 以 human observer/director perspective 操作 UI 或 client flows。 | 只提供 supporting evidence。 |
| Second review Agent | 对 evidence 做只读复核，并报告 P1/P2/P3 findings。 | 存在 P1/P2 时可以阻断 PASS。 |
| Deterministic checker | 验证固定 schemas、fixtures、operation logs、result directories 和 redaction rules。 | 对覆盖字段具有权威性。 |
| Scorecard checker | 验证多步骤 autonomous 或 LLM-backed lifecycle evidence。 | 对声明的 score items 具有权威性。 |
| Human reviewer | 审核 claims 并批准下一步工作。 | 可以接受或拒绝流程，但不能替代缺失 evidence。 |

## Verdict Values

| Verdict | 含义 |
| --- | --- |
| `clean_pass` | 所有 in-scope required checks 都通过，没有 blocking P1/P2，且没有缺 required evidence。 |
| `partial_pass` | 有意义的 in-scope checks 通过，但至少一个 required check 缺失、跳过、阻塞或失败。 |
| `failed` | 核心 required behavior 被 evidence 反证。 |
| `blocked` | 因外部依赖、环境、凭据或 required artifact 不可用，验证无法继续。 |
| `not_run` | 该验证层已计划但未执行。 |

对明确不在当前范围的单项能力使用 `out_of_scope`。不要对未来路线图范围使用 `pass`。

## 必须列出的层级状态

每次完整验证结果必须包含以下层级状态：

- L0 documentation and scope audit。
- L1 schemas and contracts。
- L2 backend unit and API compatibility。
- L3 generation and import。
- L4 runtime lifecycle。
- L5 Agent loop and memory。
- L6 frontend and E2E。
- L7 Agent smoke。
- L8 autonomous saved-result validation。
- L9 LLM-backed lifecycle validation。
- L10 external client evidence review。
- L11 final verdict audit。

如果某层还不能执行，标记为 `blocked`、`not_run` 或 `out_of_scope` 并说明原因。
不能省略该层。

## 硬边界

- WorldEngine core 必须保持 generic，不得存储 concrete validation worlds、characters、
  maps、locations、story rules 或 external oracle internals。
- 外部客户端只能消费 public APIs、schemas、CLI contracts、exported contracts 和
  redacted reports。
- Validation Client 不得拥有 LLM generation、provider keys、provider calls 或权威
  evaluation。
- 用户方向可以影响 external events 和 world environment，但不得直接修改 Agent private
  state 或写入非法最终结果。
- Agent autonomy evidence 必须来自 WorldEngine public evidence，而不是 client scripts。
- Schema changes 必须 additive，除非 active iteration contract 允许 breaking changes。
- Code、checker、fixture、API、frontend 和 provider implementation changes 仍需要对应
  iteration 或 milestone gate。

## Redaction Boundaries

evidence 包含以下内容时立即 FAIL：

- API keys。
- authorization headers。
- raw prompts。
- raw provider requests。
- raw provider responses。
- raw provider traces。
- private Agent memory。
- private Agent goals。
- raw thought。
- raw chain-of-thought。
- hidden context。
- private evaluator data。
- private validation oracle logic。
- 存入 WorldEngine core 的 concrete external validation world seed data。

允许的 evidence 必须 public 且 bounded：

- public IDs 和 public labels。
- public world state summaries。
- public rule summaries。
- public memory summaries。
- public intent summaries。
- public thought 或 reflection summaries。
- event ids、snapshot ids、diff ids、replay references。
- redacted provider class、model label、success/failure、latency 和 approximate token
  bucket。

## 完整产品 PASS 规则

完整产品验证只有在以下条件全部满足时，才能标记为 `clean_pass`：

- `coverage-map.md` 中每个 CPV row 都出现在 result matrix。
- 每个 in-scope CPV row 都是 `pass`。
- 每个 required command 或 checker 都有当前会话 evidence。
- 每个 required artifact 都存在。
- redaction scan clean。
- 要求第二 Agent 复核时，没有 blocking P1/P2。
- skipped 或 future-scope items 被明确标记，并且不与声明范围冲突。

如果 LLM-backed lifecycle 在范围内，但没有运行 DeepSeek live call，则完整产品验证不能声明
LLM-backed lifecycle PASS。
