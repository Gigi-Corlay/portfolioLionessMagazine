#!/usr/bin/env bash

# exit on error
set -o errexit

# On force le script à entrer dans le bon dossier s'il n'y est pas déjà
cd $STATIC_ROOT/../lioness_project 2>/dev/null || cd lioness_project 2>/dev/null || true

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
