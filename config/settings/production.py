from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PRODUCTION_POSTGRES_DB_NAME'),
        'USER': config('PRODUCTION_POSTGRES_DB_USER'),
        'PASSWORD': config('PRODUCTION_POSTGRES_DB_PASSWORD'),
        'HOST': config('PRODUCTION_POSTGRES_DB_HOST'),
        'PORT': config('PRODUCTION_POSTGRES_DB_PORT'),
    }
}
