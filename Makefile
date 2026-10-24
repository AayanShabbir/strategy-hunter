# Common tasks. Interpreter: .venv17 on the box (override with PY=python in CI).
PY ?= .venv17/bin/python
RUFF ?= ruff

.PHONY: help test test-sde test-engine lint status
help:
	@echo "make test        - SDE + engine test suites (no market data needed)"
	@echo "make test-sde    - tests_sde (73 tests)"
	@echo "make test-engine - engine/tests (18 tests)"
	@echo "make lint        - ruff correctness lint on src/ and tests_sde/"
	@echo "make status      - engine ledger / queue status (read-only)"

test: test-sde test-engine

test-sde:
	PYTHONPATH=. $(PY) -m pytest tests_sde

test-engine:
	cd engine && ../$(PY) -m pytest -q

lint:
	$(RUFF) check src tests_sde

status:
	./engine/hunt status
