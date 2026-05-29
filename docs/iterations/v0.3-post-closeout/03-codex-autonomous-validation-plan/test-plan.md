# Test Plan

Status: planned / not executed

This is the command and evidence plan for the future independent reviewer. No
commands are run by this package.

## Future Commands

Repository state:

```bash
git status --short --branch
git rev-parse HEAD
git diff --check
```

Focused loader validation:

```bash
cd backend
.venv/bin/python -m pytest app/tests/test_worldspec_loader.py
```

Focused bridge validation:

```bash
cd backend
.venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
```

Event compatibility validation:

```bash
cd backend
.venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py
```

Optional broader backend validation:

```bash
cd backend
.venv/bin/python -m pytest app/tests
```

## Expected Reviewer Checks

- Compare v0.3 release claims with docs and code.
- Check that `load_worldspec` is generic and schema-backed.
- Check that runtime context bridge output is bounded and inert.
- Check that `RuntimeEngine` context storage does not change step output.
- Check that Event.refs empty responses preserve legacy API shape.
- Check that non-empty refs still serialize.
- Check that no concrete demo-world content appears in the validation package.
- Check that unrun validation is not claimed as evidence.

## Commands Not Run And Why

No commands are run in this package because it is planning-only.

## Blocker Recording Rule

If the future reviewer cannot run a command, the review must record the exact
command, working directory, failure string, and whether the final
recommendation is `blocked` or `failed`.

## No Unverified Claims Rule

The reviewer must not report a check as successful without current-session
command evidence or an explicit accepted historical-evidence rationale.
