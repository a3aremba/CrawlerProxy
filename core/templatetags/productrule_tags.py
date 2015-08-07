# -*- coding: utf-8 -*-
__author__ = 'alexz'
from django import template
from django.contrib.admin.templatetags.admin_list import result_list as admin_list_result_list
from django.contrib.admin.templatetags.admin_modify import submit_row as admin_submit_row
from core.model_managers.GroupRuleManager import CGroupRuleManager


def result_list(cl):
    mycl = {}
    group_rule_manager = CGroupRuleManager()
    mycl.update(admin_list_result_list(cl))
    # comment next string, if you want to see normal view of productrule_list
    mycl['results'] = group_rule_manager.make_grouping_result_list(cl)
    return mycl

def submit_row(context):
    my_context = {}
    my_context.update(admin_submit_row(context))
    my_context['button_save_as'] = {
        'active': True,
        'attributes': {'class': 'btn btn-high',
                       'data_toggle': 'modal',
                       'data_target': '#exampleModal'}}
    return my_context

register = template.Library()
result_list = register.inclusion_tag("admin/core/productrule/change_list_results.html")(result_list)
submit_row = register.inclusion_tag("admin/core/productrule/submit_line.html", takes_context=True)(submit_row)