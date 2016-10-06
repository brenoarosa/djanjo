"""
WSGI config for compass project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siteconfig.settings")

def _setup_application(environ, start_response):

    if 'DJANGO_DEPLOY_ENV' not in os.environ:
        deploy_env = environ.get('DJANGO_DEPLOY_ENV', 'dev')
        os.environ['DJANGO_DEPLOY_ENV'] = deploy_env

    application = get_wsgi_application()
    return application(environ, start_response)

application = _setup_application
