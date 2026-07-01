#!/usr/bin/env bash
set -o errexit

cd lioness_project

echo "Upgrade pip"
pip install --upgrade pip

echo "Install dependencies"
pip install -r requirements.txt

echo "Running migrations"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput --clear

echo "Build finished successfully"
