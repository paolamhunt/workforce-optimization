VENV := .venv
PY := PYTHONPATH=src $(VENV)/bin/python

.PHONY: venv install test lint solve

venv:
	python3 -m venv $(VENV)

install: venv
	$(PY) -m pip install -U pip
	$(PY) -m pip install -e ".[dev]"

test:
	$(PY) -m pytest -q

lint:
	$(PY) -m ruff check .

solve:
	$(PY) scripts/solve_toy.py