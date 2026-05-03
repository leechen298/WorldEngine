SHELL := /bin/bash

.PHONY: help setup setup-backend setup-frontend dev dev-backend dev-frontend check-backend check-frontend

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
