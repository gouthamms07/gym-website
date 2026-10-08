#!/bin/sh
set -eu

cd /app/app
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec "$@"
