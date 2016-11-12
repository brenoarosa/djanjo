"""
Django settings.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from . import _helper

DEBUG = True

# Creates log directory if not available
try:
    os.mkdir(_helper.LOG_DIR)
except OSError:
    pass


ADMINS = (
    ('Admin', 'root@localhost'),
)


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

ROOT_URLCONF = 'siteconfig.urls'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'compressor',
    'django_extensions',
    'compass',
    'sekizai',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # let user browser select the language by session, cookie or accept-language header defaulting to LANGUAGE_CODE
    # https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(_helper.SITECONFIG_DIR, 'templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.tz",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "sekizai.context_processors.sekizai",
            ],
            'debug': DEBUG,
        },
    },
]

ALLOWED_HOSTS = ['localhost']

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SECRET_KEY = _helper.get_secret_key()


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

WSGI_APPLICATION = 'siteconfig.wsgi.application'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# COMPRESS_ENABLED = False

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#########################
# Log                   #
#########################

LOGGING = {
    'version': 1,  # inserting logfile on this version
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(process)d.%(thread)d] %(levelname)-8s '
                      '%(name)s %(funcName)s(%(lineno)d): %(message)s'
        },
        'compact': {
            'format': '%(asctime)s %(levelname)-8s '
                      '%(name)s %(funcName)s(%(lineno)d): %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'level': 'ERROR',
        },
        'database_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(_helper.LOG_DIR, 'database.log'),
            'formatter': 'verbose',
        },
        'compass_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(_helper.LOG_DIR, 'compass.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['database_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['compass_file'],
            'level': 'DEBUG',
        },
        'compass': {
            'handlers': ['compass_file'],
            'level': 'DEBUG',
        },
    },
}

#########################
# Plugins               #
#########################
