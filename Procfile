release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn --pythonpath . config.wsgi