#!/usr/bin/env bash
set -o errexit

cd lioness_project

echo "Upgrade pip"
python -m pip install --upgrade pip

echo "Install dependencies"
pip install -r requirements.txt

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Create superuser if it does not exist"
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin_lionne").exists():
    User.objects.create_superuser(
        "admin_lionne",
        "adminlionne@lioness.com",
        "LionessSecurePass2026!!"
    )
EOF

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Build finished successfully"