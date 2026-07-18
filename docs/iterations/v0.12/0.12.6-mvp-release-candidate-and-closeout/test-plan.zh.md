# Test Plan

英文原文：`test-plan.md`。

## 文档门禁

```bash
git diff --check
python3 required-file completeness check
rg status consistency checks
rg authorization scans
```

预期结果：

- `git diff --check` exit `0` 且无输出。
- required files 存在且非空。
- 没有打开 active implementation/provider/external-validation authorization。
- final closeout classification 是 PARTIAL，不是 PASS。
- 不声明 complete MVP PASS。

## 未运行命令

- Provider live calls：未授权。
- External Validation Client automation：本仓库不可用，且已被 `0.12.5` BLOCKED。
- Frontend/E2E：不属于 closeout。
- Code tests：closeout 只改文档，不需要。

## Blocker Rule

Missing current v0.12 external Validation Client export 仍是 complete MVP PASS 的 blocker，final closeout 必须明确保留。
