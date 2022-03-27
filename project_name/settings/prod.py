from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]


ADMINS = []

ALLOWED_HOSTS = [
    "localhost",
]

# Redirect all HTTP request do HTTPS
# See https://docs.djangoproject.com/en/3.1/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                + "pathname=%(pathname)s lineno=%(lineno)s "
                + "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "testlogger": {
            "handlers": ["console"],
            "level": "INFO",
        }
    },
}
