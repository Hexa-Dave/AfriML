import os
import os.path
from .settings import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]



#CORS_ALLOWED_ORIGINS = [
 #   "https://afrimlfront.z1.web.core.windows.net",
#]


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    }
}


# Static files settings for production
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "Backend/staticfiles")  # Ensure static files are collected here for production

# If you have custom static files in development, this is where they are located
STATICFILES_DIRS = [os.path.join(BASE_DIR, "Backend/static")]



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNECTION_STR = {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNECTION_STR['dbname'],
        "HOST": CONNECTION_STR['host'],
        "USER": CONNECTION_STR['user'],
        "PASSWORD": CONNECTION_STR['password'],
    }
}
