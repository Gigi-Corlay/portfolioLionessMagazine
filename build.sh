#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Upgrade pip"
python -m pip install --upgrade pip

echo "Install dependencies"

pip install -r lioness_project/requirements.txt


cd lioness_project

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Create superuser if it does not exist"
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin_lionne"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email="adminlionne@lioness.com",
        password=os.environ["DJANGO_SUPERUSER_PASSWORD"]
    )
EOF

Et définir DJANGO_SUPERUSER_PASSWORD dans les variables d'environnement de ton dashboard Render (pas dans le code).

Essaie python manage.py createsuperuser en local et dis-moi si ça débloque la connexion à /admin/.

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Build finished successfully"
