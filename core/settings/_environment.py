# -*- coding: utf-8 -*-
__author__ = 'alexz'
from os.path import isfile, join, dirname
from ConfigParser import ConfigParser
ENVIRONMENT_INI_NAME = 'environment.ini'
PROJECT_DIR = dirname(dirname(dirname(__file__)))

def get_environment_type():
    environment_path = join(PROJECT_DIR, ENVIRONMENT_INI_NAME)
    return __get_environment_value(environment_path) if isfile(environment_path) else None

def __get_environment_value(environment_path):
    environment_file = open(environment_path)
    config = ConfigParser()
    config.readfp(environment_file)
    return config.get('Environment', 'environment_type') + '.py'
