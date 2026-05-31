# 测试计划

状态：review complete

## 文档检查

从仓库根目录运行：

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed=('docs/iterations/v0.5/',); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
python3 -c "from pathlib import Path; forbidden=('backend/app/','backend/worldengine/','frontend/','migrations/','fixtures/','test-results/'); bad=[p for p in Path('.').glob('**/*agent_memory*') if any(str(p).startswith(prefix) for prefix in forbidden)]; print('forbidden_agent_memory_paths=' + str(len(bad))); [print(str(p)) for p in bad]; raise SystemExit(1 if bad else 0)"
```

预期结果：

- `git diff --check` 退出码为 0。
- package docs and mirrors check 输出 `missing=0`。
- changed-file scope guard 输出 `out_of_scope=0`。
- forbidden implementation path sentinel 输出 `forbidden_agent_memory_paths=0`。

## Evaluator 检查

必须运行一个只读 documentation/contract evaluator，检查：

- 全部英文 package docs。
- 中文 mirror presence 和 status equivalence。
- concept/scope 与 v0.5 parent docs 的一致性。
- `0.5.2` authorization criteria。
- 没有 runtime、schema、API、frontend、test、fixture、migration 或
  `backend/worldengine/` changes。

Evaluator 必须报告没有 P1、没有 blocking P2，才能 closeout。

## 回归测试

本包是 documentation-only，且不修改 implementation surfaces。因此不要求运行 backend、frontend、
API、E2E、runtime、Agent smoke、autonomous validation、build、fixture、migration 或
external validation commands。

## 接受标准

- 全部 package docs 和 mirrors 存在。
- Contract 定义六个 v0.5 public concepts。
- `0.5.2` authorization criteria 明确。
- Review 记录 exact documentation commands 和 evaluator findings。
- 没有 implementation files 被修改。
- 没有 unresolved P1/P2。

## 阻塞记录规则

如果任何检查失败，在 `review.md` 记录 exact failure，只在 documentation scope 内修复，
并在声称 closeout 前重新运行失败命令。

如果 required evaluator 不可用，记录 `BLOCKED` 或 `NEEDS_USER_INPUT`，不要关闭本包。

## 未运行项

以下检查有意不运行：

- backend tests
- frontend tests
- E2E tests
- runtime/API smoke tests
- Agent smoke checks
- autonomous validation checks
- builds
- fixture validation
- migrations
- external validation runners

原因：本包是 documentation-only，不修改 implementation、runtime、API、frontend、fixture、
migration 或 validation-runner surfaces。
