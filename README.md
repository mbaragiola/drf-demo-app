# Django REST Framework demo app

## Basic instructions

### Getting and building the project:

    $ git clone git@mbaragiola:drf-demo-app.git
    $ cd drf_demo_app
    $ docker-compose -f local.yml build

### Running tests

    $ docker-compose -f local.yml run django pytest

## Disclaimer


- The backbone of the project was built using [django-cookiecutter](https://github.com/pydanny/cookiecutter-django).
- Documentation is done by Swagger.
- Validation is almost null, this could be improved in the serializers.
