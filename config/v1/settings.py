from pathlib import Path
import dj_database_url
from hrm_backend.config.v1.database_config import postgres_config

BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "hrm_backend",
]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": postgres_config.POSTGRES_DB_NAME,
#         "USER": postgres_config.POSTGRES_USERNAME,
#         "PASSWORD": postgres_config.POSTGRES_PASSWORD,
#         "HOST": postgres_config.POSTGRES_HOST,
#         "PORT": postgres_config.POSTGRES_PORT,
#     }
# }

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

SECRET_KEY = "anything-random"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
