# -*- coding: utf-8 -*-
__author__ = 'alexz'
import re
from core.models import ProductRule, RuleMatch, RuleMethod
from .staticVariables import *
from core.lib.kibanaLog import CKibanaLog


class CProductRuleManager(object):
    def __init__(self):
        self._parameter_dict = {}

    def __init_params_dict(self, url_prepared, method, body):
        self._parameter_dict['body'] = body
        self._parameter_dict['method'] = method
        self._parameter_dict['schema'] = url_prepared.scheme
        self._parameter_dict['host'] = url_prepared.hostname
        self._parameter_dict['port'] = str(url_prepared.port) if url_prepared.port is not None else ''
        self._parameter_dict['path'] = url_prepared.path
        self._parameter_dict['login'] = url_prepared.login if url_prepared.username is not None else ''
        self._parameter_dict['password'] = url_prepared.password if url_prepared.password is not None else ''

    def get_confirm_rules(self, product, url_prepared, method, body):
        self.__init_params_dict(url_prepared, method, body)
        confirm_rules = []
        rules = ProductRule.objects.filter(product=product, rule_activate=True)
        for rule in rules:
            if self.__is_matches_conformity(self.get_rule_matches(rule))\
                    and self.__method_conformity(rule)\
                    and self.__rule_login_password_confirm(rule):
                confirm_rules.append(rule)
        return confirm_rules

    @staticmethod
    def get_rule_matches(rule):
        matches = RuleMatch.objects.filter(rule=rule)
        return matches

    def __is_matches_conformity(self, matches):
        result = None
        index = 0
        for field in FIELDS_LIST:
            if not matches.filter(fields=field):
                continue
            need_field = matches.filter(fields=field)[0]
            # check if first write first value to result
            if index == 0:
                result = self.__field_match(need_field.match, need_field.lex, need_field.value,
                                            self._parameter_dict.get(field))
            index += 1
            # --------------------------------------------
            # body check
            if field == 'body' and self._parameter_dict.get('method') in METHOD_WITHOUT_BODY:
                result = result and True
            # ---------------------------------------------
            result = result and self.__field_match(need_field.match, need_field.lex, need_field.value,
                                                   self._parameter_dict.get(field))
        return result

    def __method_conformity(self, rule):
        for rule_method in RuleMethod.objects.filter(rule=rule):
            if rule_method.method == 'ANY':
                return True
            if rule_method.method == self._parameter_dict.get('method'):
                return True
        return False

    def __rule_login_password_confirm(self, rule):
        if rule.url_login == self._parameter_dict.get('login', '') and \
           rule.url_password == self._parameter_dict.get('password', ''):
            return True
        return False

    @staticmethod
    def __field_match(match_type, lex_match, field_value, raw_value):
        result = False
        if match_type == 'ANY':  # IF ANY all result of field is true
            return True

        try:
            raw_value = raw_value.decode('utf-8')
        except Exception, e:
            CKibanaLog({'message': str(e),
                        'module': 'M-PROXY_DECODE_ERROR'})

        if lex_match == 'TERM':
            if field_value == raw_value:
                result = True
        elif lex_match == 'REGEXP':
            if re.search(field_value, raw_value, re.UNICODE) is not None:
                result = True
        elif lex_match == 'CONTAINS':
            if raw_value.find(field_value) != (-1):
                result = True

        if match_type == 'IS_NOT':
            result = not result

        return result
