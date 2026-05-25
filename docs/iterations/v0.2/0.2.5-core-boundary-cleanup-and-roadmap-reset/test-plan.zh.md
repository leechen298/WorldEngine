# 测试计划

英文版本：`test-plan.md`

## 文档规划阶段

本 pass 只创建 0.2.5 iteration package documents。不要在本 pass 中运行 backend
tests、frontend tests、E2E tests、runtime smoke tests、schema tests 或 fixture tests。

允许的 documentation checks：

```bash
git status --short --branch
find docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset -maxdepth 1 -type f | sort
git diff --check
```

## 实现阶段命令

contract、technical design、test plan 和 plan review 并 approval 后，implementation
stage 应运行：

```bash
concrete demo anchor sweep using a temporary untracked pattern file
make check-backend
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
git diff --check
```

如果 implementation 没有创建 `test_worldspec_schema_smoke.py`，而是保留旧 test file
name，需要把 focused pytest command 替换成实际使用的 focused test path。

## 搜索验收

`rg` search 在 cleanup 前预计会找到 historical references。implementation 后：

- active docs 不得保留 concrete Demo world anchors。
- active tests 不得保留 concrete Demo world anchors。
- active fixtures 不得保留 concrete Demo world anchors。
- historical iteration documents 只有在被 0.2.5 cleanup 标记为 historical context 时，
  才可以保留旧 wording。
- 本 0.2.5 package 可以提及 old terms，用来定义 cleanup scope。

## Backend 检查

`make check-backend` 验证 backend virtual environment 存在，但不证明 backend tests
通过。

focused backend pytest command 必须证明 generic WorldSpec schema smoke test 通过。
因为 implementation 修改 backend test 和 fixture files，所以 broader backend pytest
command 也应该运行。

## Frontend 检查

除非 implementation 修改 frontend files，或 repository-level check command 明确包含
frontend verification，否则不要运行 frontend tests。本 package 禁止 frontend dashboard
changes，因此 frontend test execution 通常 out of scope。

## 不做未验证声明

除非当前 implementation session 实际运行并记录了对应 command 或 flow，否则不得声称
tests、runtime behavior、frontend behavior、E2E behavior 或 smoke flows 通过。
