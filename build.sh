#!/usr/bin/env bash
# exit on error
set -o errexit

# On remonte d'un niveau pour activer l'environnement virtuel global de Render
if [ -f "../.venv/bin/activate" ]; then
    source ../.venv/bin/activate
fi

# On s'assure d'installer les paquets au bon endroit
pip install --upgrade pip
pip install -r requirements.txt

# Commandes Django standard
python manage.py collectstatic --no-input
python manage.py migrate
