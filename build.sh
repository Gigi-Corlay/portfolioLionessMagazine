#!/usr/bin/env bash
# exit on error
set -o errexit

echo "--- Étape 1 : Vérification et navigation dans le dossier projet ---"
if [ -d "lioness_project" ]; then
    echo "Navigation vers lioness_project..."
    cd lioness_project
fi

echo "--- Étape 2 : Mise à jour de pip et installation des dépendances ---"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "--- Étape 3 : Collecte des fichiers statiques ---"
# Le flag --clear nettoie l'ancien cache pour forcer la copie de CKEditor
python manage.py collectstatic --noinput --clear

echo "--- Étape 4 : Application des migrations de la base de données ---"
python manage.py migrate --noinput

echo "--- Étape 5 : Création du Superuser de secours ---"
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin_lionne"

if not User.objects.filter(username=username).exists():
    print("Création du superutilisateur...")
    User.objects.create_superuser(
        username=username,
        email="adminlionne@lioness.com",
        password=os.environ.get("DJANGO_SUPERUSER_PASSWORD", "DefaultPassword123!")
    )
else:
    print("Le superutilisateur existe déjà.")
EOF

echo "--- Build terminé avec succès ! 🎉 ---"
