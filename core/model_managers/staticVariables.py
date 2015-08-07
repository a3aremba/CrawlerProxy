# -*- coding: utf-8 -*-
__author__ = 'alexz'

FIELDS_LIST = ['host', 'port', 'schema', 'path', 'body']
LEX_TYPES_LIST = ['TERM', 'REGEXP', 'CONTAINS']
MATCH_TYPES_LIST = ['ANY', 'IS', 'IS_NOT']

METHOD_WITHOUT_BODY = ['GET', 'HEAD', 'DELETE', 'PATCH']

MATCH_NAME = '_match_type'
LEX_NAME = '_lex_type'
VALUE_NAME = '_value'