"""
Django settings for naxos project.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import os
from .util import root, BASE_DIR
from .secretKeyGen import SECRET_KEY  # Secret key from generator module


DEBUG = eval(os.environ.get("DEBUG_MODE", "False"))

# Configuring directories
MEDIA_ROOT = root("media")
STATICFILES_DIRS = (root("static"),)

# Security
RAW_HOSTS = (os.environ.get("HOSTNAME"), "localhost")
ALLOWED_HOSTS = tuple(filter(lambda x: x != None, RAW_HOSTS))
SECRET_KEY = SECRET_KEY
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True

# HTTPS
SESSION_COOKIE_SECURE = False  # True for full HTTPS
CSRF_COOKIE_SECURE = False     # True for full HTTPS

# App conf
ADMINS = ((os.environ.get("ADMIN_NAME"), os.environ.get("ADMIN_EMAIL")),)
INSTALLED_APPS = (
    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # Third-party Apps
    "crispy_forms",

    # Project Apps
    "forum",
    "user",
    "pm",
    "blog",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.security.SecurityMiddleware",
)

ROOT_URLCONF = "naxos.urls"

WSGI_APPLICATION = "naxos.wsgi.application"

LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

AUTH_USER_MODEL = "user.ForumUser"

LOGIN_URL = "user:login"
LOGIN_REDIRECT_URL = "forum:top"

CRISPY_TEMPLATE_PACK = "bootstrap3"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            root("templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": DEBUG,
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

CONN_MAX_AGE = None

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
        "LOCATION": os.environ.get("CACHE_LOCATION"),
    }
}

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "colored_verbose": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(levelname)-8s%(red)s%(module)-30s%(reset)s %(blue)s%(message)s"
        },
    },
    "handlers": {
        'colored_console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'colored_verbose'
        }
    },
    'loggers': {
        '': {
            'level': LOG_LEVEL,
            'handlers': ['colored_console'],
        },
        'gunicorn.access': {
            'handlers': ['colored_console']
        },
        'gunicorn.error': {
            'handlers': ['colored_console']
        }
    }
}

# Email
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL")  # email address to use
EMAIL_HOST_USER = os.environ.get("SERVER_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = os.environ.get("EMAIL_SERVER_PREFIX", "")
