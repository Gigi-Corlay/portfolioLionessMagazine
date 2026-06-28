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

# ON FORCE LE SCRIPT À ENTRER DANS LE DOSSIER DU PROJET AVANT LES COMMANDES DJANGO
cd $STATIC_ROOT/../lioness_project 2>/dev/null || cd lioness_project 2>/dev/null || true

# Commandes Django standard
python manage.py collectstatic --no-input
python manage.py migrate
