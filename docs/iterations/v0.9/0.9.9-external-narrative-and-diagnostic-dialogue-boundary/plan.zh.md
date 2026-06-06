# Plan

英文原文：`plan.md`。

Status：reviewed / ready for implementation

## Documentation Stage

1. 读取 parent v0.9 state、`v0.9-plan.md`、0.9.8 closeout、north-star、product model、
   scope boundaries、roadmap 和 iteration rules。
2. 为 `0.9.9` 创建完整 mixed-package document set。
3. 保持 implementation authorization 关闭：`implementation_authorized: no`。
4. 运行 `test-plan.md` 中的 documentation checks。
5. 请求 documentation/contract/design/test-plan evaluator。
6. 如果无 P0/P1/blocking P2 findings，更新 review evidence 并记录 positive implementation
   authorization；否则修复 docs 并重新 review。

## Implementation Stage After Review Only

只有本 package review 记录 positive implementation authorization 后才可开始 implementation。

Planned implementation order：

1. 添加面向 narrative projection、diagnostic dialogue、boundary decisions、provenance、
   redaction status 和 mutation flags 的 additive public schemas。
2. 添加 deterministic helper，reject private markers 和 default-canonical mutation attempts。
3. 如果 implementation 选择 API inspection，添加 optional additive route/manifest exposure。
4. 添加 `test-plan.md` 中的 focused tests。
5. 运行 focused、related 和 backend regression commands。
6. 请求 implementation-scope evaluator。
7. Implementation closeout 后更新 `review.md` 和 parent route/status docs。

## Stop Conditions

如果 implementation 需要以下内容，停止：

- live provider calls。
- generated-result creation。
- checker fixture 或 checker execution changes。
- external validation。
- frontend UI 或 Validation Client code。
- player-in-world chat。
- narrative game content。
- diagnostic-to-Agent-memory bridge。
- `backend/worldengine/` changes。
