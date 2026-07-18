# Contract

英文源文件：`contract.md`。

## Public Concepts

- `public working memory`：从 public observation/action/rest evidence 派生的 short-term
  redaction-safe summary。
- `public episodic memory`：锚定 event/runtime refs 的 redaction-safe public Agent
  experience summary。
- `rest consolidation`：WorldEngine-owned step，记录 public rest 和 consolidation
  evidence，但不声明 private cognition。
- `memory evidence ref`：指向 events、runtime ticks、session Agent steps 或 consolidation
  records 的 public reference。

## Allowed Changes

- 在 `backend/app/schemas/` 新增 public memory response schemas。
- 如需 helper methods，只以 additive 方式扩展 in-memory Agent memory store。
- 在现有 session route 边界内新增 session Agent memory read/consolidation APIs。
- 扩展 `0.12.1` session Agent rest path，写入 public memory 和 consolidation evidence。
- 更新 manifest/public handoff discovery。
- 新增 focused backend tests。
- 更新 package 和 parent review evidence。

## Forbidden Changes

- memory records、events、API responses、tests 或 review evidence 中不得包含 raw private
  memory、raw thought、chain-of-thought、private goals、hidden context、secrets、raw
  prompts、raw provider responses 或 provider traces。
- 不做 automatic per-tick personality、skill、relationship、injury、death、inventory 或
  long-term memory mutation。
- 不把 diagnostic conversation 插入 memory。
- 不实现或执行 external Validation Client。
- 不执行 provider live call。
- 不做 frontend、persistence/migration、checker automation、narrative/diagnostic 或
  complete MVP closeout work。
- 不在 `backend/worldengine/` 下实现。

## Required Behavior

- Session Agent memory read 返回 public working 和 episodic summaries。
- 非 rest Agent step 可以记录 bounded public working memory。
- Rest Agent step 记录 public rest/consolidation evidence 和 episodic public summary。
- Memory records 包含指向 public events/runtime/session Agent steps 的 evidence refs。
- 重复 normal ticks 不自动修改 personality、skills 或 long-term memory。
- memory-facing requests 中的 private markers 会被 reject，或不会出现在 public evidence 中。

## Compatibility Requirements

- Existing memory substrate tests 继续通过。
- Existing session Agent runtime loop tests 继续通过。
- Manifest additions 是 additive。
- Existing request-driven Agent loop memory context 保持兼容。

## Exit Criteria

- Documentation evaluator 记录无 P1/P2 findings。
- 代码变更前记录 `implementation_authorized: yes`。
- Focused tests 证明 memory summary creation、rest consolidation、redaction、no per-tick
  personality/skill mutation、evidence refs 和 compatibility。
- Closeout 前 implementation-scope evaluator 无 blocking P1/P2。
