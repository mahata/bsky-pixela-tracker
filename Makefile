pre-commit:
	ruff check
	ruff format . --check --diff
	python -m unittest
