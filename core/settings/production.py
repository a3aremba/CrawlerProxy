# -*- coding: utf-8 -*-
__author__ = 'alexz'

SERVER_TYPE = 'production'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'DEFAULT_STORAGE_ENGINE': 'MYISAM',
        'NAME': 'm-proxy',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}