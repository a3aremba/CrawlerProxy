# -*- coding: utf-8 -*-
__author__ = 'alexz'


"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SERVER_TYPE = 'base'
IS_LOCAL = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xn=^e8#y*89ix48q7lr*0*zge^)lirhcf$j_%v1nof(!)hbcjt'

DATABASE_HOST = 'localhost'

USER = 'developer'
PASSWORD = 'Sy4BmcDYrzpm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../../static').replace('\\','/')

MANAGERS = ADMINS
ALLOWED_HOSTS = ['*']
CFG_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(CFG_PATH, '..'))
rootDirName = os.path.split(ROOT_PATH)[1]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'DEFAULT_STORAGE_ENGINE': 'MYISAM',
        'NAME': 'm-proxy',
        'USER': 'admin',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-UA'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'log_file_core':{
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT_PATH, '../logs/core.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'simple'
        },
    },
    'loggers': {
        'core': {
            'handlers': ['log_file_core'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

LOGGER_STATUS_CODE = [200, 300, 400, 500]
LOGGER_REDIS_HOST = ''
LOGGER_REDIS_PORT = 6379
LOGGER_REDIS_DB = 0
LOGGER_REDIS_LIST = 'corde-parel-log'
LOGGER_UDP_HOST = 'log0.bpp.it.loc'
LOGGER_UDP_PORT = 13200
LOGGER_TO_FILE = 'core'


SUIT_CONFIG = {
    'ADMIN_NAME': 'M-Proxy',
    'MENU': (

        # Rename app and set icon
        {'app': 'auth', 'label': 'Users and Groups', 'icon':'icon-lock'},
        {'app': 'core', 'label': 'M-proxy', 'icon':'icon-cog'},
    )
}

# keys for logging data to redis
TRACKER_KEY = 'Tracker_key'
LISTENER_KEY = 'Listener_key'

# allow type: REDIS | COUCHBASE
TRACKER_STORAGE_TYPE = 'REDIS'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'