DC := $(shell which docker-compose)

{% if cookiecutter.zappa == 'y' %}
PYTHON := env/bin/python
PIP := env/bin/pip

$(PYTHON):
	-rm -rf env
	virtualenv -p python2.7 env

$(PIP): $(PYTHON)
{% endif %}

{% if cookiecutter.zappa == 'y' %}

all: install zappa

{% else %}

all: install

{% endif %}

install: $(DC)
	docker-compose build

{% if cookiecutter.zappa == 'y' %}

zappa: $(PIP)
	$(PIP) install -r requirements.txt

{% endif %}
