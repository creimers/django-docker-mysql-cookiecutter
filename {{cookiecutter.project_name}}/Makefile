DOCKER := $(shell which docker-compose)
NPM := $(shell which npm)
PYTHON := env/bin/python
PIP := env/bin/pip

all: install-common

$(PYTHON):
	virtualenv -p python3 env

$(PIP): $(PYTHON)

install-common: $(PIP)
	$(PIP) install -r requirements.txt

install-node-packages: ./source/static/package.json
	#install into static dir
	$(NPM) install --prefix ./source/static
	#install for project as a whloe
	$(NPM) install

docker:
	docker-compose build
	docker-compose run django python ./source/manage.py migrate
	docker-compose run django python ./source/manage.py collectstatic --noinput
