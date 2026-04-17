.PHONY: install run ingest test lint format eval

install:
	pip install -U pip
	pip install -e ".[dev]"

run:
	uvicorn app.main:app --reload

ingest:
	python scripts/ingest.py

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

eval:
	python evals/run_eval.py
