SHELL := /bin/bash

.PHONY: help setup setup-backend setup-frontend dev dev-backend dev-frontend check-backend check-frontend test-e2e validate-agent-smoke-result validate-agent-smoke-fixtures validate-agent-autonomous-result validate-agent-autonomous-fixtures validate-codex-skills sync-codex-skills

BACKEND_DIR := backend
FRONTEND_DIR := frontend
BACKEND_VENV := $(BACKEND_DIR)/.venv
BACKEND_PYTHON := $(BACKEND_VENV)/bin/python
BACKEND_PIP := $(BACKEND_VENV)/bin/pip

help:
	@echo "Available commands:"
	@echo "  make setup          Install backend and frontend dependencies"
	@echo "  make dev            Start backend and frontend together"
	@echo "  make dev-backend    Start only the FastAPI backend"
	@echo "  make dev-frontend   Start only the Vite frontend"
	@echo "  make test-e2e       Run browser E2E tests"
	@echo "  make validate-agent-smoke-result RESULT_DIR=<dir>"
	@echo "  make validate-agent-smoke-fixtures"
	@echo "  make validate-agent-autonomous-result RESULT_DIR=<dir>"
	@echo "  make validate-agent-autonomous-fixtures"
	@echo "  make validate-codex-skills"

setup: setup-backend setup-frontend

setup-backend:
	@test -d "$(BACKEND_VENV)" || python3 -m venv "$(BACKEND_VENV)"
	@"$(BACKEND_PIP)" install -r "$(BACKEND_DIR)/requirements.txt"

setup-frontend:
	@cd "$(FRONTEND_DIR)" && pnpm install

dev: check-backend check-frontend
	@trap 'kill 0' INT TERM EXIT; \
	$(MAKE) dev-backend & \
	$(MAKE) dev-frontend & \
	wait

check-backend:
	@test -x "$(BACKEND_PYTHON)" || (echo "Missing $(BACKEND_PYTHON). Run 'make setup' first." && exit 1)

check-frontend:
	@test -d "$(FRONTEND_DIR)/node_modules" || (echo "Missing frontend/node_modules. Run 'make setup' first." && exit 1)

dev-backend:
	@$(MAKE) check-backend
	@cd "$(BACKEND_DIR)" && .venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend:
	@$(MAKE) check-frontend
	@cd "$(FRONTEND_DIR)" && pnpm dev

test-e2e: check-backend check-frontend
	@cd "$(FRONTEND_DIR)" && pnpm exec playwright test

validate-agent-smoke-result: check-backend
	@test -n "$(RESULT_DIR)" || (echo "Missing RESULT_DIR. Usage: make validate-agent-smoke-result RESULT_DIR=<dir>" && exit 2)
	@$(BACKEND_PYTHON) tools/testing/validate_agent_smoke_result.py "$(RESULT_DIR)"

validate-agent-smoke-fixtures: check-backend
	@$(BACKEND_PYTHON) tools/testing/validate_agent_smoke_result.py tools/testing/fixtures/agent-smoke/valid-basic-runtime
	@$(BACKEND_PYTHON) tools/testing/validate_agent_smoke_result.py tools/testing/fixtures/agent-smoke/valid-params-flow
	@$(BACKEND_PYTHON) tools/testing/validate_agent_smoke_result.py tools/testing/fixtures/agent-smoke/valid-invalid-param
	@$(BACKEND_PYTHON) tools/testing/validate_agent_smoke_result.py tools/testing/fixtures/agent-smoke/valid-agent-autotune
	@if $(BACKEND_PYTHON) tools/testing/validate_agent_smoke_result.py tools/testing/fixtures/agent-smoke/invalid-agent-verdict >/tmp/worldengine-invalid-agent-smoke.out 2>&1; then \
		cat /tmp/worldengine-invalid-agent-smoke.out; \
		echo "Expected invalid-agent-verdict fixture to fail, but it passed."; \
		exit 1; \
	else \
		cat /tmp/worldengine-invalid-agent-smoke.out; \
		echo "invalid-agent-verdict fixture failed as expected."; \
	fi
	@$(BACKEND_PYTHON) -m pytest tools/testing/test_validate_agent_smoke_result.py -q

validate-agent-autonomous-result: check-backend
	@test -n "$(RESULT_DIR)" || (echo "Missing RESULT_DIR. Usage: make validate-agent-autonomous-result RESULT_DIR=<dir>" && exit 2)
	@$(BACKEND_PYTHON) tools/testing/validate_agent_autonomous_result.py "$(RESULT_DIR)"

validate-agent-autonomous-fixtures: check-backend
	@$(BACKEND_PYTHON) tools/testing/validate_agent_autonomous_result.py tools/testing/fixtures/agent-autonomous/valid-dashboard-basic-runtime
	@$(BACKEND_PYTHON) tools/testing/validate_agent_autonomous_result.py tools/testing/fixtures/agent-autonomous/valid-worldengine-full-lifecycle
	@for fixture in invalid-agent-verdict invalid-direct-api-operation invalid-cli-nonzero-exit invalid-unverified-p1 invalid-failed-score-item invalid-missing-artifact; do \
		if $(BACKEND_PYTHON) tools/testing/validate_agent_autonomous_result.py tools/testing/fixtures/agent-autonomous/$$fixture >/tmp/worldengine-invalid-agent-autonomous.out 2>&1; then \
			cat /tmp/worldengine-invalid-agent-autonomous.out; \
			echo "Expected $$fixture fixture to fail, but it passed."; \
			exit 1; \
		else \
			cat /tmp/worldengine-invalid-agent-autonomous.out; \
			echo "$$fixture fixture failed as expected."; \
		fi; \
	done
	@$(BACKEND_PYTHON) -m pytest tools/testing/test_validate_agent_autonomous_result.py -q

validate-codex-skills:
	@python3 tools/testing/sync_codex_skills.py --dry-run

sync-codex-skills:
	@echo "personal sync disabled; use validate-codex-skills" >&2
	@exit 2
