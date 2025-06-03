#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r random_number_generator/requirements.txt

# Change to the project directory
cd random_number_generator

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate 