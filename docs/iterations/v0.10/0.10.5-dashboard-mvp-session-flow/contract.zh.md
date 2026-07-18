# Contract

英文版本：`contract.md`。

## UI Contract

Dashboard 必须暴露 visible MVP session flow：

- worldview premise input。
- create-session action，背后调用 `POST /sessions/from-worldview`。
- current session id、world id、status、generation mode/status 和 runtime ref。
- bounded run action，背后调用 `POST /sessions/{session_id}/run`。
- pause 和 resume actions，背后调用 session-scoped controls。
- snapshot evidence list，背后调用 `GET /sessions/{session_id}/snapshots`。
- timeline refresh，复用现有 public event-step APIs。

## API Client Contract

Frontend API methods 只使用 public backend routes。Request/response types 必须建模 public
session fields，并避免 raw/private provider data。

## Evidence Contract

Tests 必须证明：

- dashboard renders the session shell。
- create-from-worldview 调用 public API 并展示 returned session data。
- bounded run 调用 session run API，并刷新 runtime/timeline/snapshot state。
- pause/resume controls 调用 session-scoped APIs。
- backend 和 dev server 可用时，E2E smoke 能驱动 create/run/inspect。

## Compatibility Contract

现有 dashboard panels 应保持可用，或被整合进 session shell。Existing runtime step behavior 不得
被破坏，除非在 tests 和 UI 中明确由 session run controls 替代。

## Forbidden Claims

Dashboard 不得声明 live provider quality、external Validation Client PASS、Agent autonomy、
product release readiness 或 durable persistence。
