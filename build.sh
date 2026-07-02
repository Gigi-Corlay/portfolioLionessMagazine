#!/usr/bin/env bash
set -o errexit

cd lioness_project

echo "Upgrade pip"
pip install --upgrade pip

echo "Install dependencies"
pip install -r requirements.txt

# CORRECTION ICI : On génère la migration manquante AVANT d'exécuter les migrations
echo "Generating missing migrations for blog_magazine"
python manage.py makemigrations blog_magazine

echo "Running migrations"
python manage.py migrate --noinput

echo "Creating superuser if not exists"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin_lionne').exists() or User.objects.create_superuser('admin_lionne', 'adminlionne@lioness.com', 'LionessSecurePass2026!!')"

echo "Collect static files"
python manage.py collectstatic --noinput --clear

echo "Build finished successfully"
