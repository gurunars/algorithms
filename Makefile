export POETRY_VIRTUALENVS_IN_PROJECT=true

.PHONY: lint test fmt check open clean reinstall
.EXPORT_ALL_VARIABLES: lint test fmt check open clean reinstall $(MAKECMDGOALS)

build: .utils .venv
	poetry run sphinx-build algorithms build

.venv:
	poetry install

reinstall:
	rm -rf .venv
	poetry install

check: lint test

open: build
	open build/index.html

test:  
	poetry run pytest algorithms --doctest-modules

fmt:
	poetry run black algorithms

lint:
	poetry run pyright
	poetry run black --check algorithms

clean:
	rm -rf build

.utils:
	mkdir .utils
	wget https://github.com/plantuml/plantuml/releases/download/v1.2023.13/plantuml-mit-1.2023.13.jar -O .utils/plantuml.jar
