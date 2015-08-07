# -*- coding: utf-8 -*-
__author__ = 'alexz'
from core.models import RuleMatch
from .staticVariables import *


class CRuleMatchManager(object):
    def __init__(self, product_rule_entity, form):
        self._product_rule_entity = product_rule_entity
        self._form = form

    def create_matchs(self):
        for field in FIELDS_LIST:
            self.__create_match_for_field(field)
        return

    def fill_form_by_value(self):
        for field in FIELDS_LIST:
            self.__fill_form_field(field)

        return self._form

    def create_match_rule_from_tracker(self, field,  value_data='', match_data='IS', lex_data='TERM'):
        rule_match_obj, created = RuleMatch.objects.get_or_create(rule=self._product_rule_entity, fields=field)
        rule_match_obj.match = match_data
        rule_match_obj.lex = lex_data
        rule_match_obj.value = '' if value_data is None else value_data
        rule_match_obj.save()

    def __create_match_for_field(self, field_name):
        try:
            match, lex, value = self.get_form_value(field_name)
        except Exception, e:
            return

        rule_match_obj, created = RuleMatch.objects.get_or_create(rule=self._product_rule_entity,
                                                                  fields=field_name)
        rule_match_obj.match = match
        rule_match_obj.lex = lex
        rule_match_obj.value = value
        rule_match_obj.save()
        return True

    def __fill_form_field(self, field):
        rule_match_obj = self.__get_rule_match(field)
        if not rule_match_obj:
            return None
        match, lex, value = self.__get_field_names(field)
        self._form.fields[match].initial = rule_match_obj.match
        self._form.fields[lex].initial = rule_match_obj.lex
        self._form.fields[value].initial = rule_match_obj.value

    def __get_rule_match(self, field):
        rule_match_query = RuleMatch.objects.filter(rule=self._product_rule_entity, fields=field)
        if len(rule_match_query):
            return rule_match_query[0]
        return None

    def get_form_value(self, field):
        match, lex, value = self.__get_field_names(field)
        return self._form[match].value(), self._form[lex].value(), self._form[value].value()

    def __get_field_names(self, field):
        return field+MATCH_NAME, field+LEX_NAME, field+VALUE_NAME