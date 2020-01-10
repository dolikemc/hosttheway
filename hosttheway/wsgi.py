"""
WSGI config for hosttheway project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('USERPROFILE').startswith('C:'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hosttheway.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hosttheway.settings.production")

application = get_wsgi_application()
