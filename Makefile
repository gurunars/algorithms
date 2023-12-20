docs: .utils
	poetry run sphinx-build algorithms build
	touch build/.nojekyll

check: lint test

open:
	open build/index.html

test:
	poetry run pytest algorithms --doctest-modules

fmt:
	poetry run black algorithms

lint:
	poetry run pyright
	poetry run black --check algorithms

.utils:
	mkdir .utils
	wget https://github.com/plantuml/plantuml/releases/download/v1.2023.13/plantuml-mit-1.2023.13.jar -O .utils/plantuml.jar

.PHONY: lint test fmt docs check open