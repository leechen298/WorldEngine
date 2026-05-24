# Agent Smoke Transcript: dashboard-invalid-param

## Scenario

`dashboard-invalid-param`

## Actions

1. Ran the approved evidence helper baseline command before dashboard UI actions.
2. Opened the WorldEngine dashboard at `http://127.0.0.1:5173/`.
3. Filled `system.secret` in the params path input.
4. Filled `blocked` in the params value input.
5. Clicked `Apply`.
6. Observed the dashboard validation error through `world-params-error`: Param validation failed; system.secret: Reserved params cannot be modified.
7. Captured `screenshots/dashboard-invalid-param.png`.

## Notes

No direct API operation was recorded as an Agent operation. Backend API reads used to produce `api-baseline.json` and `api-summary.json` are performed by approved helper commands.
