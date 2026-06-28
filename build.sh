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

# CRÉATION OU MISE À JOUR FORCÉE DE L'ADMINISTRATEUR via Python
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin_lioness'
email = 'lioness.lemagdesreines@gmail.com'
password = 'LionessSecurePass2026!!'

user, created = User.objects.get_or_create(username=username, defaults={'email': email})
user.set_password(password)
user.is_staff = True
user.is_superuser = True
user.save()
if created:
    print('Superuser cree avec succes !')
else:
    print('Mot de passe du superuser mis a jour !')
"

