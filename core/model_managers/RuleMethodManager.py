# -*- coding: utf-8 -*-
__author__ = 'alexz'
from core.models import RuleMethod


class CRuleMethodManager(object):
    def __init__(self, rule, method):
        self._rule = rule
        self._method = method

    def create_rule_method_if_not_exist(self):
        method_obj = self.__get_method_obj()
        if method_obj:
            return method_obj
        method_obj = RuleMethod(rule=self._rule, method=self._method)
        method_obj.save()
        pass

    def delete_rule_method_if_exist(self):
        method_obj = self.__get_method_obj()
        if method_obj:
            method_obj.delete()
        pass

    def __get_method_obj(self):
        methods_for_rule = RuleMethod.objects.filter(rule=self._rule,
                                                     method=self._method)
        if len(methods_for_rule):
            return methods_for_rule[0]
        return None