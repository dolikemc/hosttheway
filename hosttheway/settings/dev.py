from pathlib import PurePath, WindowsPath
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n1*jg+9_*rz&x8l(*ih)0n))x+li!55c&5#b4k&e#+yi8_$0o%'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# you need to download the whl package from https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
# and install it via pip install GDAL-3.0.4-cp37-cp37m-win.whl
if os.name in ('nt'):
    GDAL_LIBRARY_PATH = r'C:\Users\buchetmc\PycharmProjects\GIT\hosttheway\venv4\Lib\site-packages\osgeo\gdal300.dll'
    #SPATIALITE_LIBRARY_PATH = r'mod_spatialite'
else:
    GDAL_LIBRARY_PATH = ''

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
