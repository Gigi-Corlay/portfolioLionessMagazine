#!/usr/bin/env bash
# exit on error
set -o errexit

# Activation de l'environnement global de Render
if [ -f "../.venv/bin/activate" ]; then
    source ../.venv/bin/activate
fi

# Installation des dépendances
pip install --upgrade pip
pip install -r requirements.txt

# On entre dans le dossier du projet pour les commandes Django
cd $STATIC_ROOT/../lioness_project 2>/dev/null || cd lioness_project 2>/dev/null || true

# Commandes Django standard
python manage.py collectstatic --no-input
python manage.py migrate

# CRÉATION AUTOMATIQUE DU COMPTE ADMIN (ajustez le pseudo et l'email si besoin)
DJANGO_SUPERUSER_PASSWORD="Le Magazine des Reines 2026" \
python manage.py createsuperuser \
    --username "Admin: LIONESS" \
    --email "lioness.lemagdesreines@gmail.com" \
    --noinput || true
