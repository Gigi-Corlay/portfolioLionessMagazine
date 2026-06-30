#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. On met à jour pip et on installe les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# 2. On se déplace dans le dossier du projet Django si nécessaire
cd $STATIC_ROOT/../lioness_project 2>/dev/null || cd lioness_project 2>/dev/null || true

# 3. Chemin vers le bon exécutable Python
PYTHON_BIN="/opt/render/project/src/.venv/bin/python"

# 4. Commandes Django standard
$PYTHON_BIN manage.py collectstatic --no-input
$PYTHON_BIN manage.py migrate

# --- AJOUT ICI POUR L'IMPORTATION GRATUITE DES ARTICLES ---
# if [ -f "data.json" ]; then
#     echo "Importation des articles en cours..."
#     $PYTHON_BIN manage.py loaddata data.json
# fi
# -----------------------------------------------------------

# 5. Création/Mise à jour de l'administrateur
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
"
