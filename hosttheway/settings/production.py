from .base import *

DEBUG = False
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o=%z6r!m0u792slh3_cxt-ut6mf((^33n0*4-4%n5p55hfos2#'

SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['hosttheway.buchetmann.org']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/var/www/ssd1470/priv/hosttheway/db.conf',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

STATIC_ROOT = '/var/www/ssd1470/htdocs/hosttheway/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/var/www/ssd1470/htdocs/hosttheway/media/'
MEDIA_URL = '/media/'

try:
    from .local import *
except ImportError:
    pass
