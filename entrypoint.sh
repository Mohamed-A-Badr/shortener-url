#!/bin/ash

echo "Apply migrations to database"
python manage.py makemigrations
python manage.py migrate

exec "$@"