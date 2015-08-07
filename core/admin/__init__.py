# -*- coding: utf-8 -*-
__author__ = 'alexz'
from django.contrib import admin
from core.models import Department, Product, ProductRule, ProductRuleGroups, RuleMethod, RuleMatch
from core.forms import ProductRuleForm, METHODS
from core.model_managers.RuleMethodManager import CRuleMethodManager
from core.model_managers.RuleMatchManager import CRuleMatchManager
from core.model_managers.GroupRuleManager import CGroupRuleManager
from .urls import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'created')
    list_display_links = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'created')
    list_display_links = ('id', 'name')
    readonly_fields = ('unique_header',)

    def get_urls(self):
        return add_product_admin_url() + super(ProductAdmin, self).get_urls()


class ProductRuleAdmin(admin.ModelAdmin):
    form = ProductRuleForm
    fieldsets = (
        (u'Правило', {
            'fields': (('name', 'weight', 'rule_activate'), 'product', 'url_login', 'url_password', 'group')
        }),
        (u'Схема, правило соответствия', {
            'fields': (('schema_match_type', 'schema_lex_type', 'schema_value'),)
        }),
        (u'Хост, правило соответствия', {
            'fields': (('host_match_type', 'host_lex_type', 'host_value'),)
        }),
        (u'Порт, правило соответствия', {
            'fields': (('port_match_type', 'port_lex_type', 'port_value',),)
        }),
        (u'Путь, правило соответствия', {
            'fields': (('path_match_type', 'path_lex_type', 'path_value'),)
        }),
        (u'Метод', {
            'fields': ('request_ANY', ('request_GET', 'request_DELETE', 'request_TRACE'), ('request_POST',
            'request_HEAD', 'request_PATCH'), ('request_PUT', 'request_CONNECT', 'request_OPTIONS'))
        }),
        (u'Тело запроса, правило соответствия', {
            'fields': (('body_match_type', 'body_lex_type'), 'body_value')
        }),
        (u'Стратегия Имитации', {
            'fields': ('strategy', 'imitate_status', 'imitate_headers', 'imitate_body', 'time_out_time', 'created',
                       'modified')
        }),
    )
    save_as = True
    list_display = ('id', 'name', 'product', 'group', 'show_rule_activate')
    list_display_links = ('id', 'name')
    list_filter = ('product',)
    search_fields = ('name', )
    readonly_fields = ('created', 'modified')
    actions = ['duplicate_event']

    def duplicate_event(self, request, queryset):
        for object in queryset:
            # get methods
            methods = RuleMethod.objects.filter(rule=object)
            matchs = RuleMatch.objects.filter(rule=object)
            object.id = None
            object.name += "_copy"
            object.save()
            # copy methods when duplicate
            for method in methods:
                method.id = None
                method.rule = object
                method.save()
            # copy matchs when duplicate
            for match in matchs:
                match.id = None
                match.rule = object
                match.save()

    duplicate_event.short_description = u"Дублировать запись"

    def show_rule_activate(self, obj):
        group_manager = CGroupRuleManager()
        return group_manager.get_image_attribute(obj, obj.rule_activate)
    show_rule_activate.short_description = u'активировать правило'

    # define change_list for grouping comment this string if you want to see normal view of productrule_list
    change_list_template = 'admin/core/productrule/product_rule_change_list.html'

    # url for activate deactivate rule
    def get_urls(self):
        return add_product_rule_admin_url() + super(ProductRuleAdmin, self).get_urls()

    def save_model(self, request, obj, form, change):
        super(ProductRuleAdmin, self).save_model(request, obj, form, change)
        if not obj.id:
            return
        for method in METHODS:
            rule_manager = CRuleMethodManager(obj, method)
            if form.cleaned_data.get('request_'+method) is True:
                rule_manager.create_rule_method_if_not_exist()
            else:
                rule_manager.delete_rule_method_if_exist()

        match_manager = CRuleMatchManager(obj, form)
        match_manager.create_matchs()

    class Media:

        js = (
            '/static/core/js/jquery-1.11.1.min.js',
            '/static/core/js/custom.js',
        )
        css = {
            'all': ('/static/core/css/custom_admin.css',)
        }


class RuleMethodAdmin(admin.ModelAdmin):  # not show at admin part
    list_display = ('id', 'rule', 'method')


class RuleMatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'rule')


class ProductRuleGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRule, ProductRuleAdmin)
admin.site.register(ProductRuleGroups, ProductRuleGroupsAdmin)
# admin.site.register(RuleMatch, RuleMatchAdmin)
