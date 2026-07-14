import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialisation de l'application
application = get_wsgi_application()

# Enveloppement avec WhiteNoise pour servir les fichiers statiques
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), '../staticfiles'))
