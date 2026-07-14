#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Verification du dossier..."
if [ -d "lioness_project" ]; then
    echo "Navigation vers lioness_project..."
    cd lioness_project
fi

echo "Upgrade pip"
python -m pip install --upgrade pip

echo "Install dependencies"
pip install -r requirements.txt

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
        password=os.environ.get("DJANGO_SUPERUSER_PASSWORD", "DefaultPassword123!")
    )
EOF

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Build finished successfully"
