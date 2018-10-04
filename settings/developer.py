from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '46.101.125.168', 'sp-lutsk.com', 'www.sp-lutsk.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

SITE_ID = 1
