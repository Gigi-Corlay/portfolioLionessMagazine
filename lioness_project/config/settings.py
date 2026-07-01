import os
import dj_database_url
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# =====================================================
# BASE DIRECTORY
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================================
# SECURITY
# =====================================================

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-me-in-production"
)

# Reste True en local, mais passe automatiquement à False sur Render
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "portfoliolionessmagazine.onrender.com",
]

# =====================================================
# APPLICATIONS
# =====================================================

INSTALLED_APPS = [
    # Applications requises pour le stockage Cloudinary (DOIVENT ÊTRE EN HAUT)
    'cloudinary_storage',
    
    # Les applications indispensables de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Les applications tierces
    'cloudinary',
    'ckeditor',

    # Vos applications locales
    'core',
    'accounts',
    'dashboard',
    'blog_magazine',
    'magazine',
    'donations',
]

# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =====================================================
# URLS
# =====================================================

ROOT_URLCONF = "config.urls"

# =====================================================
# TEMPLATES
# =====================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# =====================================================
# WSGI
# =====================================================

WSGI_APPLICATION = "config.wsgi.application"

# =====================================================
# DATABASE
# =====================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Si l'environnement Render fournit une base de données PostgreSQL, Django l'utilise automatiquement
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# =====================================================
# PASSWORD VALIDATION
# =====================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# =====================================================
# INTERNATIONALIZATION
# =====================================================

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("fr", _("Français")),
    ("en", _("English")),
]

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

LANGUAGE_COOKIE_NAME = "lioness_language"

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# =====================================================
# AUTHENTICATION
# =====================================================

LOGIN_URL = "accounts:login"

LOGIN_REDIRECT_URL = "/dashboard/"

LOGOUT_REDIRECT_URL = "/"

# =====================================================
# STATIC FILES
# =====================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = BASE_DIR / "staticfiles"

# =====================================================
# MEDIA FILES
# =====================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# =====================================================
# EMAIL
# =====================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# =====================================================
# DEFAULT PRIMARY KEY
# =====================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =====================================================
# SECURITY (DEV ONLY)
# =====================================================

CSRF_USE_SESSIONS = False

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# =====================================================
# CKEDITOR CONFIG
# =====================================================

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'width': '100%',
        'height': '400',
    }
}

# =====================================================
# PRODUCTION STORAGE (CLOUDINARY)
# =====================================================

if not DEBUG:
    # Django-cloudinary-storage détecte automatiquement la variable 'CLOUDINARY_URL' de Render !
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.backends.MediaCloudinaryStorage'

# =====================================================
# STATIC FILES
# =====================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Ce stockage va gérer vos fichiers CSS/JS sans planter s'il manque le favicon.ico
STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'

STATIC_ROOT = BASE_DIR / "staticfiles"
