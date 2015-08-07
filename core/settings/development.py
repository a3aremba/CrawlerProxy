# -*- coding: utf-8 -*-
__author__ = 'alexz'

SERVER_TYPE = 'development'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'DEFAULT_STORAGE_ENGINE': 'MYISAM',
        'NAME': 'm_proxy',
        'USER': 'developer',
        'PASSWORD': 'Sy4BmcDYrzpm',
        'HOST': '10.1.96.130',
        'PORT': '3306',
    }
}