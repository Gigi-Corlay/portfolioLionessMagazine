import os
from pathlib import Path
import dj_database_url

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================================
# SECURITY
# =====================================================

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = not os.environ.get("RENDER")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com",
    "portfoliolionessmagazine.onrender.com",
]

# =====================================================
# APPS
# =====================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "cloudinary",
    "cloudinary_storage",
    "ckeditor",

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
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
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
    DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# =====================================================
# STATIC + STORAGE
# =====================================================

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# =====================================================
# SECURITY HEADERS
# =====================================================

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
else:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

# =====================================================
# I18N
# =====================================================

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("fr", _("Français")),
    ("en", _("English")),
]

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]

# =====================================================
# LOGIN
# =====================================================

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

# =====================================================
# EMAIL
# =====================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
