# djangocms-docker-cookiecutter

## https://medium.com/@JakubBorys/docerizing-django-cms-28c3ed11ba43#.ylgod8h4a

## what's inside.
* python3
* latest Django
* pyjade

# Usage

## build
1. `docker-componse build`

## initializer database
1. `docker-compose run django python ./src/manage.py migrate`

## run
1. `docker-compose run -p 8000:8000 django python ./src/manage.py runserver 0.0.0.0:8000`
