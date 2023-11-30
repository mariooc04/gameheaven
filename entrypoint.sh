#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

python manage.py shell < script.py

gunicorn sisinf.wsgi:application --bind 0.0.0.0:8000 --forwarded-allow-ips="*"
```