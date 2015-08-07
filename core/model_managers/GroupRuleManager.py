# -*- coding: utf-8 -*-
__author__ = 'alexz'
from core.models import ProductRuleGroups, ProductRule
from django.contrib.admin.templatetags.admin_list import results, ResultList
from django.utils.safestring import mark_safe


class CGroupRuleManager(object):
    def make_grouping_result_list(self, cl):
        grouping_rule_dict = self.__make_groups_rule_dict(cl.result_list)
        result_list = self.__convert_to_response_lists(grouping_rule_dict, cl)
        return result_list

    @staticmethod
    def toogle_rule_by_group_id(id, toggle):
        ident = int(id) if id != 'none' else None
        group = None
        if ident:
            group = ProductRuleGroups.objects.filter(id=ident)[0]
        rules = ProductRule.objects.filter(group=group)
        values = []
        for rule in rules:
            rule.rule_activate = toggle
            rule.save()
            value = {'id': rule.id,
                     'value': toggle,
                     'type': 'rule'}
            values.append(value)

        return {'status': False,
                'message': 'error',
                'values': values}

    @staticmethod
    def __make_groups_rule_dict(query_list):
        groups_dict = {}
        for rule in query_list:
            if rule.group not in groups_dict.keys():
                groups_dict[rule.group] = [rule]
            else:
                groups_dict[rule.group].append(rule)
        return groups_dict

    def __convert_to_response_lists(self, grouping_rule_dict, cl):
        table_list = []
        for group in grouping_rule_dict.keys():
            cl.result_list = grouping_rule_dict[group]
            list_of_rules = list(results(cl))
            table_list.append(ResultList(None, self.__get_table_string_list(group, list_of_rules, cl)))
            table_list += list_of_rules
        return table_list


    def __get_table_string_list(self, group, list_of_rules, cl):
        def get_group_name(group, list_of_rules):
            name = u"Без группы" if not group else unicode(group)
            return name + ' ('+str(len(list_of_rules))+') '

        def get_colspan_value(list_of_rules):
            return str(len(list_of_rules[0])-1)

        def checked(cl):
            flag = True
            for rule in cl.result_list:
                if not rule.rule_activate:
                    flag = False
                    break

            return flag

        group_id = str(group.id) if group else 'none'
        data_group_name = 'group_' + group_id

        row_string = '<td colspan=' + get_colspan_value(list_of_rules) \
                     + ' class="group_checked ' \
                     + data_group_name \
                     + '">' + get_group_name(group, list_of_rules) + '</td>' \
                     + '<td> ' + self.get_image_attribute(group, checked(cl)) + ' </td>'

        return [row_string]

    @staticmethod
    def get_image_attribute(obj, checked=False):
        def make_attributes(obj):
            obj_type = 'rule' if isinstance(obj, ProductRule) else 'group'
            data_id = str(obj.id) if obj else 'none'
            id_attribute = obj_type + '_' + data_id
            attributes = 'class="toggle_activate" '
            attributes += 'data-type="' + obj_type + '" ' + 'data-id="' + data_id + '" '
            attributes += "id=" + id_attribute
            return attributes

        def get_icon(value=False):
            return {True: '/static/admin/img/icon-yes.gif',
                    False: '/static/admin/img/icon-no.gif'}.get(value)

        string = '<img alt="' + str(checked) + '" ' + make_attributes(obj) + ' src="' + get_icon(checked) + '">'

        return mark_safe(string)

    def toggle_group(self, group_id, toggle):
        ident = int(group_id) if group_id != 'none' else None
        group = None
        values = []
        if ident:
            group = ProductRuleGroups.objects.filter(id=ident)[0]
            values.append({'id': group.id,
                           'value': toggle,
                           'type': 'group'})
        else:
            values.append({'id': 'none',
                           'value': toggle,
                           'type': 'group'})
        rules = ProductRule.objects.filter(group=group)
        for rule in rules:
            rule.rule_activate = toggle
            rule.save()
            values.append({'id': rule.id,
                           'value': toggle,
                           'type': 'rule'})

        return {'status': True,
                'message': '',
                'values': values}

    def toggle_rule_by_id(self, rule_id, toggle):
        values = []
        try:
            rule = ProductRule.objects.get(id=int(rule_id))
        except Exception, e:
            return {'status': False,
                    'message': str(e),
                    'values': values}
        try:
            rule.rule_activate = toggle
            rule.save()
            values.append({'id': rule.id,
                           'value': toggle,
                           'type': 'rule'})

            if not toggle:
                values.append({'id': rule.group.id if rule.group else 'none',
                               'value': toggle,
                               'type': 'group'})

            if toggle:
                rules_of_currenct_group = ProductRule.objects.filter(group=rule.group)
                group_flag = True
                for rule_in_current_group in rules_of_currenct_group:
                    if not rule_in_current_group.rule_activate:
                        group_flag = False

                values.append({'id': rule.group.id if rule.group else 'none',
                               'value': group_flag,
                               'type': 'group'})

        except Exception, e:
            return {'status': False,
                    'message': str(e),
                    'values': values}

        return {'status': True,
                'message': '',
                'values': values}
