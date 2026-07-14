import os
from pathlib import Path

import dj_database_url
import cloudinary
from django.utils.translation import gettext_lazy as _

# ======================================================
# APPLICATIONS
# ======================================================

INSTALLED_APPS = [
    # 1. EN PREMIER : Cloudinary Storage
    "cloudinary_storage",
    "cloudinary",

    # 2. EN DEUXIÈME : Les applications par défaut de Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",  # Cloudinary_storage DOIT être avant celle-ci

    # 3. Le reste de tes packages
    "django_ckeditor_5",

    # 4. Tes applications locales
    "core",
    "accounts",
    "dashboard",
    "blog_magazine",
    "magazine",
    "donations",
]

# ======================================================
# BASE
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================================
# SECURITY
# ======================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-change-me"
)

DEBUG = os.getenv("RENDER") is None

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,.onrender.com"
).split(",")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    CSRF_TRUSTED_ORIGINS = [
        "https://portfoliolionessmagazine.onrender.com",
    ]

# ======================================================
# MIDDLEWARE
# ======================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "config.urls"

# ======================================================
# TEMPLATES
# ======================================================

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

WSGI_APPLICATION = "config.wsgi.application"

# ======================================================
# DATABASE
# ======================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:

    DATABASES = {

        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )

    }

else:

    DATABASES = {

        "default": {

            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",

        }

    }

# ======================================================
# PASSWORDS
# ======================================================

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

# ======================================================
# INTERNATIONALISATION
# ======================================================

LANGUAGE_CODE = "en"

LANGUAGES = [

    ("fr", _("Français")),
    ("en", _("English")),

]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# ======================================================
# STATIC
# ======================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# On garde ce dossier s'il contient tes designs personnalisés locaux
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder", # <--- Indispensable pour CKEditor 5 !
]

# WhiteNoise & Stockage des fichiers
STORAGES = {
    "staticfiles": {
        # WhiteNoise s'occupera de distribuer tes fichiers statiques en production
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage" if os.getenv("RENDER") else "django.core.files.storage.FileSystemStorage",
    },
}

# ======================================================
# MEDIA
# ======================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# ======================================================
# CLOUDINARY
# ======================================================

# On remplace tout l'ancien code par cette configuration simple :
CLOUDINARY_STORAGE = {
    'URL': os.getenv('CLOUDINARY_URL')
}

# ======================================================
# CKEDITOR
# ======================================================

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "link",
            "blockQuote",
            "imageUpload",
            "|",
            "undo",
            "redo",
        ],
        "heading": {
            "options": [
                {"model": "paragraph", "title": "Paragraph", "class": "ck-heading_paragraph"},
                {"model": "heading1", "view": "h1", "title": "Heading 1", "class": "ck-heading_heading1"},
                {"model": "heading2", "view": "h2", "title": "Heading 2", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "Heading 3", "class": "ck-heading_heading3"},
            ]
        },
    },
}

# ======================================================
# LOGIN
# ======================================================

LOGIN_URL = "accounts:login"

LOGIN_REDIRECT_URL = "/dashboard/"

LOGOUT_REDIRECT_URL = "/"

# ======================================================
# EMAIL
# ======================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ======================================================
# DEFAULT FIELD
# ======================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "ERROR",
    },
}
