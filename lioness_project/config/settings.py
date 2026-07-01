import os
import mimetypes
from pathlib import Path

import dj_database_url
from django.utils.translation import gettext_lazy as _

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)

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

# False automatiquement sur Render
DEBUG = "RENDER" not in os.environ

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com",
]

# =====================================================
# APPLICATIONS
# =====================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Packages
    "imagekit",
    "ckeditor",

    # Applications
    "core",
    "accounts",
    "dashboard",
    "blog_magazine",
    "magazine",
    "donations",
]

# =====================================================
# MIDDLEWARE
# =====================================================

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
                "django.template.context_processors.media",
                "config.settings.global_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# =====================================================
# DATABASE
# =====================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if os.environ.get("DATABASE_URL"):
    DATABASES["default"] = dj_database_url.config(
        conn_max_age=600,
        ssl_require=True,
    )

# =====================================================
# PASSWORDS
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
# LOGIN
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

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

WHITENOISE_USE_FINDERS = True

# =====================================================
# MEDIA
# =====================================================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =====================================================
# IMAGEKIT
# =====================================================

IMAGEKIT_URL = os.environ.get(
    "IMAGEKIT_URL",
    ""
)

# =====================================================
# EMAIL
# =====================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =====================================================
# SECURITY (Render)
# =====================================================

CSRF_USE_SESSIONS = False

if DEBUG:

    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

else:

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_SSL_REDIRECT = True

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )

# =====================================================
# CONTEXT PROCESSOR
# =====================================================

def global_settings(request):
    return {
        "IMAGEKIT_URL": IMAGEKIT_URL,
        "DEBUG": DEBUG,
    }
