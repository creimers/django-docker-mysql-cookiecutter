FROM python:3.6

ADD . /project
WORKDIR /project

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /project/bin/uwsgi.sh

{% if cookiecutter.celery != 'y' %}

RUN rm -f /project/config/celery_config.py

{% endif %}
