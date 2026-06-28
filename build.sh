#!/usr/bin/env bash
# exit on error
set -o errexit

# On force l'entrée dans le dossier du projet
cd $STATIC_ROOT/../lioness_project 2>/dev/null || cd lioness_project 2>/dev/null || true

# Installation des dépendances
pip install -r requirements.txt

# On sauvegarde le chemin absolu de gunicorn pour la Start Command
echo "$(which gunicorn)" > gunicorn_path.txt

# Commandes Django
python manage.py collectstatic --no-input
python manage.py migrate
