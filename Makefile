.DEFAULT: help
.PHONY: build.docker help clean pre-commit run setup tag
.SILENT: help run setup test

# User set
PROJECT_NAME:=mandelbrot
PYTHON=python
VENV_NAME?=.venv
PIP=pip

# Leave alone
SHELL := /bin/bash
PYTHON_VENV=${VENV_NAME}/bin/${PYTHON}
PIP_VENV=${VENV_NAME}/bin/${PIP}
BRANCH_NAME=$(shell git rev-parse --abbrev-ref HEAD | rev | cut -d'/' -f1 | rev)

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type 'make setup'"
	@echo "To spin up the project locally type 'make run'"
	@echo "To run tests 'make test'"
	@echo "To run pre-commit checks 'make pre-commit'"
	@echo "To return the repo to a fresh clone 'make clean'"
	@echo "------------------------------------"


install: pyproject.toml
	${PYTHON} -m venv ${VENV_NAME} ; \
	${PYTHON_VENV} -m pip install --upgrade pip wheel ; \
	${PIP_VENV} install .

dev_setup: pyproject.toml
	${PYTHON} -m venv ${VENV_NAME} ;\
	${VENV_NAME}/bin/pip install --upgrade pip wheel ;\
	${VENV_NAME}/bin/pip install .[dev,test] ;\
	${VENV_NAME}/bin/pre-commit install ;\
	${VENV_NAME}/bin/pre-commit autoupdate ; \

run:
	cp sample.env .env ;\
	${VENV_NAME}/bin/python bin/app.py

test:
	${VENV_NAME}/bin/python -m pytest

clean:
	sudo rm -r build/ dist/ "$(PROJECT_NAME)".egg-info/ ${VENV_NAME} ;\
	sudo find . -type f -name '*.pyc' -delete
