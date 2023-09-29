#!/bin/bash

# Collect all static files
python manage.py collectstatic --no-input

# Make all migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
# python manage.py runserver 0.0.0.0:8000
nvidia-smi
# Start Server with Uvicorn to allow http and websocket connections
uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level debug --reload
