# IDS706_alejandroparedeslatorre_multipleversions
[![CI](https://github.com/nogibjj/IDS706_alejandroparedeslatorre_assignment4_matrixversionbuild/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/IDS706_alejandroparedeslatorre_assignment4_matrixversionbuild/actions/workflows/CI.yml)

Assignment 4

!(matrix_run)[matrix_run.JPG]

## Purpose of project
The purpose of this project is to test multiple python versions and environments in Github Actions. 

I use `setup-python` action in conjuction with `matrix strategy` to run multiple jobs with different configurations. 

`main.py` is going to return the versionn of the python version.

## Preparation
1. open codespaces 
2. wait for container to be built and virtual environment to be activated with requirements.txt installed 
3. make changes to any parts of the code `main.py` or `test_main.py`
4. push to see code testing in different operating systems and different python environments 

According to the requirement it gets added

* `Makefile`

* `Dockerfile`

* `requirements.txt`

* `githubactions` with a matrix of python versions 

* `.devcontainer` for Githubcodespace 

## Preparation
1. open codespaces 
2. load repo to code spaces
2. Wait for the installation of all the requirements in requirements.txt

## Check format and test errors
1. Format code `make format`
2. Lint code `make lint`
3. Test code `make test`
