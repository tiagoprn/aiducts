.PHONY: help
SHELL := /bin/bash
PROJECT_NAME = aiducts
PYTHON_VERSION=3.13

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Clean python bytecodes, optimized files, logs, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -fr .pytest_cache/
	@rm -f coverage.xml
	@rm -f *.log
	@find . -name "celerybeat-schedule*" | xargs rm -rf

init-env:  ## create a .env file with the environment variables.
	@cp etc/env.sample .env
	@echo '.env file initialized at the project root. Customize it as you may.'
	@echo '0.1' > VERSION
	@echo 'Created file containing the app version.'

dev-setup-uv:  ## setup the development environment using uv
	@read -p "Make sure you have the uv python package manager installed. Press Enter to continue..." dummy
	@echo 'Updating uv...'
	@uv self update
	@echo "Installing python $$PYTHON_VERSION on uv..."
	@uv python install $(PYTHON_VERSION)
	@echo "Creating a python venv on the project folder..."
	@uv venv --python $(PYTHON_VERSION)
	@echo "Python venv created using uv under '.venv' on the project root."
	@echo "Activate the venv now to install the project requirements."

dev-setup-ruff:  ## install ruff globally (using uv)
	@echo 'This will install ruff (linter and formatter) globally.'
	@uv tool install ruff@latest

requirements:  ## Install pip requirements using uv
	@read -p "This uses the uv python package manager. It will override your requirements.txt from requirements.in." dummy
	@read -p "Make sure you have manually activated the virtualenv with the 'source' command before continuing!" dummy
	@uv pip compile requirements.in --output-file requirements.txt
	@uv pip install -r requirements.txt

style-autofix:	## Run ruff to format your code
	@echo 'running ruff...'
	@ruff format

style:  ## Run ruff to check code style
	@echo 'running ruff format check...'
	@ruff format --check

lint:  ## Run the ruff linter to enforce our coding practices
	@printf '\n --- \n >>> Running linter...<<<\n'
	@ruff check
	@printf '\n FINISHED! \n --- \n'

lint-autofix:  ## Run the ruff linter to enforce our coding practices, and autofix errors that are fixable
	@printf '\n --- \n >>> Running linter...<<<\n'
	@ruff check --fix
	@printf '\n FINISHED! \n --- \n'

test: clean migrate  ## Run the test suite
	@cd $(PROJECT_NAME) && py.test -s -vvv

coverage: clean migrate  ## Run the test coverage report
	@py.test --cov-config .coveragerc --cov $(PROJECT_NAME) $(PROJECT_NAME) --cov-report term-missing
