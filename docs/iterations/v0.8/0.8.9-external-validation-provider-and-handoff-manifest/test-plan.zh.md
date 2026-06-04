# Test Plan

英文镜像：`test-plan.md`。

## 范围

本包是 documentation-only。未授权 runtime、API、schema、frontend、test、
fixture、migration 或 external repository implementation。

## 文档检查

运行：

```bash
git status --short --branch
git diff --check
```

检查：

- required package files exist。
- Chinese mirrors exist。
- package status 不声明 implementation complete。
- 本包不触碰 runtime、API、schema、frontend、backend test、fixture、migration 或
  external repository files。

## 实现检查

不得把 implementation tests 作为本包通过证据。Backend、frontend、E2E、Agent
smoke、autonomous、live provider 和 external validation checks 都属于未来 reviewed
implementation package 范围。

## Provider 信息检查

Provider 相关声明只能作为 planning notes，并必须在 `technical-design.md` 或最终
报告中引用公开文档。当前 provider 价格、quota 和条款可能变化，实现时必须重新
检查。

## 通过标准

本包可以进入 user review 的条件：

- docs present。
- mirrors present。
- formatting check passes。
- scope review confirms docs-only changes。
- review 记录 runtime tests 未运行及原因。
