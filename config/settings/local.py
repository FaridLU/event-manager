from decouple import config

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEVELOPMENT_LOCAL_POSTGRES_DB_NAME'),
        'USER': config('DEVELOPMENT_LOCAL_POSTGRES_DB_USER'),
        'PASSWORD': config('DEVELOPMENT_LOCAL_POSTGRES_DB_PASSWORD'),
        'HOST': config('DEVELOPMENT_LOCAL_POSTGRES_DB_HOST'),
        'PORT': config('DEVELOPMENT_LOCAL_POSTGRES_DB_PORT'),
    }
}
