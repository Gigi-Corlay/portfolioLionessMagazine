#!/usr/bin/env bash
set -o errexit

echo "📦 Upgrade pip"
pip install --upgrade pip

echo "📦 Install dependencies"
pip install -r requirements.txt

echo "📁 Django build start"

# (optionnel mais propre) vérifier qu'on est bien au bon dossier
if [ -f "manage.py" ]; then
    echo "📍 manage.py found"
else
    echo "❌ manage.py not found — check working directory"
    exit 1
fi

# IMPORTANT : migrations avant collectstatic
echo "🗄️ Running migrations"
python manage.py migrate --no-input

echo "🎨 Collect static files"
python manage.py collectstatic --no-input

# (optionnel) création admin sécurisé via variables d'env
echo "👤 Creating admin user (if env provided)"

python manage.py shell << 'EOF'
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_ADMIN_USERNAME")
email = os.environ.get("DJANGO_ADMIN_EMAIL")
password = os.environ.get("DJANGO_ADMIN_PASSWORD")

if username and email and password:
    user, created = User.objects.get_or_create(username=username, defaults={"email": email})
    user.email = email
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("✅ Admin ready")
else:
    print("⚠️ Admin env vars not set — skipping")
EOF

echo "🚀 Build finished successfully"
