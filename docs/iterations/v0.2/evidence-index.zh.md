# v0.2 Evidence Index

状态：0.2.9 audit evidence

本文档把 v0.2 的 active claims 映射到 evidence。它区分
`implemented`、`documented`、`tested`、`reviewed`、`planned`、
`not implemented`、`historical artifact` 和 `finding`，避免后续
compatibility 与 release 工作把计划项误当成已实现能力。

## Evidence Status Key

- `implemented`：仓库中已有代码或文档交付物。
- `documented`：已有 contract、boundary、roadmap 或 implementation map。
- `tested`：package review 中记录了当前会话的命令证据。
- `reviewed`：package review 或 documentation review 记录了 approval。
- `planned`：列为 future 或 later-package work。
- `not implemented`：明确不属于当前实现范围。
- `historical artifact`：仅作为历史记录保留。
- `finding`：记录在 `findings.md` 中的未解决或已关闭事项。

## Active Claim Map

| Claim | Source | Evidence | Verification source | Status | Notes |
|---|---|---|---|---|---|
| v0.2 是 Recursive World Foundation milestone，不是 final release。 | `docs/iterations/v0.2/README.md`、`docs/iterations/v0.2/v0.2-plan.md`、`docs/roadmap.md` | v0.2 plan 和 roadmap 保持 `planned / in progress`。 | 0.2.6 review 记录了剩余 package sequence 的 documentation checks。 | documented / reviewed | 0.2.11 和 0.2.12 仍是未来的 release-candidate 与 final-closeout packages。 |
| WorldEngine 保持通用 recursive world engine，不变成 demo-specific backend。 | `docs/project-north-star.md`、`docs/product-model.md`、`docs/scope-boundaries.md` | 0.2.5 清理 active concrete external-world anchors，并增加 external consumer boundaries。 | 0.2.5 review 记录 targeted active-docs/tests/fixtures grep，没有 active concrete demo anchors。 | documented / reviewed / tested | Historical package text 与 active direction 分开归类。 |
| `backend/app/` 是 active backend path。 | `AGENTS.md`、`docs/current-implementation.md`、`docs/backend-implementation.md` | Current implementation docs 描述 active FastAPI assembly 和 routes。 | 0.2.5、0.2.7、0.2.8 reviews 记录没有 runtime path changes。 | documented / reviewed | 0.2.10 将执行 detailed compatibility review。 |
| `backend/worldengine/` 是 legacy。 | `AGENTS.md`、`docs/current-implementation.md`、`docs/backend-implementation.md` | Current implementation docs 说明 legacy path 没有接入 active app。 | 0.2.7 和 0.2.8 reviews 记录没有 `backend/worldengine/` changes。 | documented / reviewed | Detailed legacy boundary documentation 计划在 0.2.10 完成。 |
| `EntityRef` 作为 domain-neutral schema reference 存在。 | `docs/contracts/entity-ref-contract.md`、`backend/app/schemas/entity.py` | 0.2.2 增加 schema；0.2.7 增加 contract document。 | 0.2.2 review：focused schema test `15 passed`；backend tests `78 passed`。0.2.7 review：focused schema tests `19 passed`；`make check-backend` passed。 | implemented / documented / tested / reviewed | 未实现 resolver、loader、registry、memory、projection 或 external fixture semantics。 |
| `WorldCell` 作为 recursive schema object 存在。 | `docs/contracts/worldcell-contract.md`、`backend/app/schemas/world_cell.py` | 0.2.2 增加 schema；0.2.7 记录 recursive child semantics。 | 0.2.2 和 0.2.7 reviews 记录 focused schema tests 和 backend checks 通过。 | implemented / documented / tested / reviewed | Runtime loading、tick behavior、generation 和 projection 仍不在范围内。 |
| `WorldSpec` 作为 versioned recursive schema wrapper 存在。 | `docs/contracts/worldspec-contract.md`、`backend/app/schemas/world_cell.py` | 0.2.2 增加 schema；0.2.7 记录 versioning 和 round-trip expectations。 | 0.2.7 review 记录 schema smoke 与 world-cell tests `19 passed`，且 `make check-backend` passed。 | implemented / documented / tested / reviewed | v0.2 中它不是 loader interface。 |
| Generic WorldSpec schema smoke coverage 替代了 concrete fixture tests。 | `backend/app/tests/test_worldspec_schema_smoke.py`、0.2.5 review | 0.2.5 删除 concrete fixture data/test，并增加 domain-neutral in-memory schema smoke tests。 | 0.2.5 review：smoke test `4 passed`；backend app tests `91 passed`。 | implemented / tested / reviewed | Active fixtures 不保存 concrete external-world seed data。 |
| `EventRef` 和可选 `Event.refs` 作为 additive event reference structure 存在。 | `docs/contracts/event-ref-contract.md`、`backend/app/schemas/event.py` | 0.2.3 增加 event-local refs；0.2.8 增加 contract 和 free-form metadata coverage。 | 0.2.3 review：focused event tests `9 passed`；backend tests `87 passed`。0.2.8 review：focused event tests `10 passed`；`make check-backend` passed。 | implemented / documented / tested / reviewed | 未实现 resolver、causality engine、runtime binding、memory link 或 projection behavior。 |
| 既有 event payload 与 API behavior 保持兼容。 | 0.2.3 和 0.2.8 reviews | Reviews 说明 `Event.refs` 仍可选，payload/runtime/API/frontend behavior 未改变。 | 两次 implementation reviews 都记录 focused event compatibility tests 通过。 | tested / reviewed | 这是 schema-local compatibility evidence，不是 runtime causality claim。 |
| External fixture 和 validation worlds 是 consumers，不是 core fixtures。 | `docs/external-fixture-boundary.md`、`docs/validation-report-template.md`、`docs/scope-boundaries.md` | 0.2.5 增加 boundary 与 redacted validation report docs。 | 0.2.5 review 记录 concrete fixture deletion 和 active anchor sweep。 | documented / reviewed / tested | v0.2 不创建 external repositories。 |
| v0.2 foundation work 保持 v0.1 runtime scaffold behavior。 | `docs/current-implementation.md`、`docs/backend-implementation.md`、completed package reviews | Code packages 0.2.2、0.2.3、0.2.5、0.2.7、0.2.8 记录 compatibility reviews。 | 0.2.2、0.2.3、0.2.5 backend regression 通过；0.2.7 和 0.2.8 因没有 schema/runtime code changes，仅运行 focused checks。 | documented / tested / reviewed | 0.2.10 负责 explicit legacy compatibility review。 |
| Iteration workflow 要求 implementation 前先完成 documentation gates。 | `docs/iterations/README.md`、`docs/iterations/v0.2/development-workflow.md` | 0.2.1 建立 iteration standards；0.2.6 增加 workflow docs 和 final review bundle template。 | 0.2.6 review 记录 detailed plan acceptance checks 和 bilingual mirror checks。 | documented / reviewed | 0.2.9 按该 gate 执行 documentation-only audit implementation。 |
| 0.2.4 concrete fixture package 已被取代，仅为 historical artifact。 | `docs/iterations/v0.2/README.md`、0.2.5 review | v0.2 index 将 0.2.4 标记为 `historical artifact`；0.2.5 review 记录 cleanup。 | 0.2.5 review 记录 concrete fixture data 删除和 replacement tests。 | historical artifact / reviewed | Historical evidence 不得驱动未来 engine abstractions。 |
| WorldSpec loader 和 RuntimeEngine bridge 在 v0.2 未实现。 | `docs/scope-boundaries.md`、`docs/roadmap.md`、`docs/iterations/v0.2/v0.2-plan.md` | v0.2 non-goals 和 v0.3 roadmap handoff 定义 future scope。 | Completed package reviews 反复记录没有 loader 或 runtime bridge changes。 | planned / not implemented / reviewed | v0.3 只能通过后续 reviewed package 处理。 |
| Agent loop、memory、self-continuity、generation、projection API、product UI 和 external repositories 属于 future scope。 | `docs/project-north-star.md`、`docs/scope-boundaries.md`、`docs/roadmap.md`、`docs/iterations/v0.2/v0.2-plan.md` | Roadmap 将这些内容放在后续 milestones。 | 0.2.5、0.2.7、0.2.8 scope reviews 记录没有此类 implementation。 | planned / not implemented / reviewed | North Star direction 已存在，但 runtime implementation 不属于 v0.2。 |
| 0.2.7 和 0.2.8 status drift 由本次 audit 解决。 | `docs/iterations/v0.2/findings.md`、`docs/iterations/v0.2/v0.2-plan.md`、`docs/iterations/v0.2/v0.2-plan.zh.md` | 0.2.9 更新 detailed plan status fields，使其与 milestone index 一致。 | 0.2.9 verification 记录 English 与 Chinese mirrors 的 status grep。 | finding / reviewed | Findings 以 status-synchronization evidence 关闭。 |

## Evidence Limits

- 本 index 不为 runtime behavior 增加超过已完成 package reviews 的实现证据。
- 0.2.9 不重新运行 backend/frontend tests，因为本 package 是
  documentation-only，且禁止 runtime、schema、API、frontend、fixture、
  migration 和 test implementation changes。
- 0.2.10 仍是 detailed legacy/runtime compatibility boundary review 的
  handoff package。
