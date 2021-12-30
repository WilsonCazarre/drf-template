import os
import django.core.exceptions

from dotenv import load_dotenv

load_dotenv()

try:
    env = os.environ["DJANGO_ENVIRONMENT"]
except KeyError:
    raise django.core.exceptions.ImproperlyConfigured(
        'DJANGO_ENVIRONMENT variable must be set to either "dev" or "prod" '
        "in the current environment"
    )

if env == "dev":
    from .dev import *
elif env == 'prod':
    from .prod import *
