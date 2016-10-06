from . import _helper
import os

# Load configuration defaults
from .defaults import *

# Override default settings
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

LOGGING['handlers']['compass_file']['formatter'] = 'compact'

_DB_DIR = os.path.join(_helper.SITECONFIG_DIR, 'db/')
try:
    os.mkdir(_DB_DIR)
except OSError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(_DB_DIR, 'dev.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

AUTH_PASSWORD_VALIDATORS = []

MEDIA_ROOT = os.path.join(_helper.SITECONFIG_DIR, 'media/')
STATIC_ROOT = ''
