# -*- coding: utf-8 -*-
__author__ = 'alexz'

from django.forms import ModelForm, Select, TextInput, BooleanField, CheckboxInput, ValidationError, CharField, Textarea
from core.models import RuleMethod, ProductRule, RuleMatch
from core.model_managers.RuleMatchManager import CRuleMatchManager

METHODS = ['ANY', 'GET', 'POST', 'PUT', 'DELETE', 'HEAD',
           'PATCH', 'TRACE', 'CONNECT', 'OPTIONS']

select_match_widget = Select(attrs={'class': 'select-mini'}, choices=RuleMatch.matchType)
select_lex_widget = Select(attrs={'class': 'select-mini'}, choices=RuleMatch.lexMatch)


class ProductRuleForm(ModelForm):
    request_ANY = BooleanField(label="ANY:", required=False)
    request_GET = BooleanField(label="GET:", required=False,
                               widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_POST = BooleanField(label="POST:", required=False,
                                widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_PUT = BooleanField(label="PUT:", required=False,
                               widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_DELETE = BooleanField(label="DELETE:", required=False,
                                  widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_HEAD = BooleanField(label="HEAD:", required=False,
                                widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_PATCH = BooleanField(label="PATCH:", required=False,
                                 widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_TRACE = BooleanField(label="TRACE:", required=False,
                                 widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_CONNECT = BooleanField(label="CONNECT:", required=False,
                                   widget=CheckboxInput(attrs={'class': 'request-data'}))
    request_OPTIONS = BooleanField(label="OPTIONS:", required=False,
                                   widget=CheckboxInput(attrs={'class': 'request-data'}))

    host_match_type = CharField(label=u'Хост', required=True, widget=select_match_widget)
    host_lex_type = CharField(label='', required=True, widget=select_lex_widget)
    host_value = CharField(label='', required=False)
    schema_match_type = CharField(label=u'Схема', required=True, widget=select_match_widget)
    schema_lex_type = CharField(label='', required=True, widget=select_lex_widget)
    schema_value = CharField(label='', required=False)
    path_match_type = CharField(label=u'Путь', required=True, widget=select_match_widget)
    path_lex_type = CharField(label='', required=True, widget=select_lex_widget)
    path_value = CharField(label='', required=False)
    port_match_type = CharField(label=u'Порт', required=True, widget=select_match_widget)
    port_lex_type = CharField(label='', required=True, widget=select_lex_widget)
    port_value = CharField(label='', required=False)
    body_match_type = CharField(label=u'Контент запроса', required=True, widget=select_match_widget)
    body_lex_type = CharField(label='', required=True, widget=select_lex_widget)
    body_value = CharField(label='', required=False, widget=Textarea(attrs={'class': 'vLargeTextField'}))

    def __init__(self, *args, **kwargs):
        super(ProductRuleForm, self).__init__(*args, **kwargs)
        self.__set_method_rule()
        self.__set_match_field()

    def __set_method_rule(self):
        methods_for_rule = RuleMethod.objects.filter(rule=self.instance)
        for method in methods_for_rule:
            self.fields['request_'+method.method].initial = True

    def __set_match_field(self):
        match_manager = CRuleMatchManager(self.instance, self)
        match_manager.fill_form_by_value()

    def clean(self):
        cleaned_data = super(ProductRuleForm, self).clean()
        method_flag = False
        for method in METHODS:
            if cleaned_data.get('request_'+method):
                method_flag = True
                break

        if not method_flag:
            raise ValidationError("One of method must be chosen")

        return cleaned_data

    class Meta:
        model = ProductRule
        widgets = {
            'host_match_type': Select(attrs={'class': 'select-mini'}),
            'host_lex_type': Select(attrs={'class': 'select-mini'}),
            'path_match_type': Select(attrs={'class': 'select-mini'}),
            'path_lex_type': Select(attrs={'class': 'select-mini'}),
            'body_match_type': Select(attrs={'class': 'select-mini'}),
            'body_lex_type': Select(attrs={'class': 'select-mini'}),
            'port_match_type': Select(attrs={'class': 'select-mini'}),
            'port_lex_type': Select(attrs={'class': 'select-mini'}),
            'weight': TextInput(attrs={'class': 'select-mini'})
        }