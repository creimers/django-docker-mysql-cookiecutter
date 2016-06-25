# djangocms-docker-cookiecutter

## https://medium.com/@JakubBorys/docerizing-django-cms-28c3ed11ba43#.ylgod8h4a

## what's inside.
* python3
* Django 1.9.5
* pyjade

# Usage

## build
1. `docker-componse build`

## initializer database
1. `docker-compose run django python ./manage.py migrate`

## run
1. `docker-compose run -p 8000:8000 django python ./manage.py runserver 0.0.0.0:8000`
