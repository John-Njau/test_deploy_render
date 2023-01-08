#!/usr/bin/env bash
# exit on error

set -o errexit

poetry install

python manage.py migrate collectstatic --no-input
python manage.py migrate