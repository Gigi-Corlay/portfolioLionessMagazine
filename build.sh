#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Si ton requirements.txt est à la racine, on l'installe AVANT de changer de dossier
echo "Upgrade pip"
python -m pip install --upgrade pip

echo "Install dependencies"
# On va chercher le requirements.txt qui est au même niveau que build.sh
pip install -r requirements.txt

# 2. Maintenant on entre dans le dossier du projet Django
cd lioness_project

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Create superuser if it does not exist"
# Note : N'oublie pas de créer la variable DJANGO_SUPERUSER_PASSWORD 
# dans l'onglet "Environment" sur ton dashboard Render !
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin_lionne"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email="adminlionne@lioness.com",
        password=os.environ.get("DJANGO_SUPERUSER_PASSWORD", "DefaultPassword123!")
    )
EOF

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Build finished successfully"
