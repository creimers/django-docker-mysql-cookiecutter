NPM := $(shell which npm)
PYTHON := env/bin/python
PIP := env/bin/pip

all: install-common

$(PYTHON):
	virtualenv -p python3 env

$(PIP): $(PYTHON)

install-common: $(PIP)
	$(PIP) install -r source/requirements/common.txt

install-rpi: install-common
	$(PIP) install -r source/requirements/rpi.txt

install-node-packages: ./source/static/package.json
	$(NPM) install --prefix ./source/static
