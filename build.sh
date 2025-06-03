#!/usr/bin/env bash
# exit on error
set -o errexit

# Change to the project directory
cd random_number_generator

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate 