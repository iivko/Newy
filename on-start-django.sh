#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

python manage.py collectstatic --no-input

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run the appropriate server
if [[ "$ENV_STATE" == "production" ]]; then
    echo "Starting Gunicorn in production mode..."
    exec gunicorn bloger.wsgi:application --workers "${GUNICORN_WORKERS:-3}" --forwarded-allow-ips="*"
else
    echo "Starting Django development server..."
    exec python manage.py runserver 0.0.0.0:8000
fi
