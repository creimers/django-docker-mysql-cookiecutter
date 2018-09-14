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

runserver: $(DC)
	docker-compose run -p {{cookiecutter.port}}:{{cookiecutter.port}} django python ./manage.py runserver 0.0.0.0:{{cookiecutter.port}}

superuser: $(DC)
	docker-compose run django python ./manage.py createsuperuser

test: $(DC)
	docker-compose run django py.test

shell:
	 docker-compose run django python ./manage.py shell

backup:
	docker-compose exec db pg_dump -U postgres -d postgres -f ./db_backups/`date +%Y-%m-%d_%H:%M:%S`.sql
