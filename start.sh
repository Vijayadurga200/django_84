python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn django_deploye.wsgi:application --bind 0.0.0.0:$PORT