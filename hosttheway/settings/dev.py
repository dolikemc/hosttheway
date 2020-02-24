from pathlib import PurePath, WindowsPath
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n1*jg+9_*rz&x8l(*ih)0n))x+li!55c&5#b4k&e#+yi8_$0o%'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if os.name in ('nt'):
    GDAL_LIBRARY_PATH = r'C:\Users\buchetmc\PycharmProjects\GIT\hosttheway\venv4\Lib\site-packages\osgeo\gdal300.dll'
else:
    GDAL_LIBRARY_PATH = ''

try:
    from .local import *
except ImportError:
    pass
