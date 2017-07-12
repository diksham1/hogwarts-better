"""
WSGI config for hogwarts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hogwarts.settings")

application = DjangoWhiteNoise(get_wsgi_application())

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


