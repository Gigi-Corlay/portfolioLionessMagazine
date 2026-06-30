#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. On met à jour pip et on installe les dépendances à la racine
pip install --upgrade pip
pip install -r requirements.txt

# 2. On se déplace dans le dossier du projet Django si nécessaire
cd $STATIC_ROOT/../lioness_project 2>/dev/null || cd lioness_project 2>/dev/null || true

# 3. ÉTAPE CRUCIALE : On force l'utilisation du Python de l'environnement virtuel de Render
# Au lieu de taper "python", on utilise le chemin direct vers le python du .venv
PYTHON_BIN="/opt/render/project/src/.venv/bin/python"

# 4. Commandes Django standard sécurisées
$PYTHON_BIN manage.py collectstatic --no-input
$PYTHON_BIN manage.py migrate

# 5. CRÉATION OU MISE À JOUR FORCÉE DE L'ADMINISTRATEUR via le bon exécutable Python
$PYTHON_BIN -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin_lionne'
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
