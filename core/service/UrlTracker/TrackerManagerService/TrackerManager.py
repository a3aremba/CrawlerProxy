# -*- coding: utf-8 -*-
__author__ = 'alexz'

from urlparse import urlparse
from .Storages.RedisStorage import CRedisStorage
from .Storages.CouchBaseStorage import CCouchBaseStorage
from .decorators import check_status
from core.settings import TRACKER_STORAGE_TYPE
from core.models import Product, ProductRule, RuleMethod
from core.model_managers.RuleMatchManager import CRuleMatchManager
from core.forms import ProductRuleForm
from core.utils import merge_dict


class CTrackerManagerService(object):
    def __init__(self, product_id):
        self.__product_id = product_id
        self._product_entity = None
        self._tracker = None
        self._status = True
        self._message = True
        self.__init_tracker()

    def get_message(self):
        return_dict = {'status': self._status,
                       'message': self._message}
        if self._tracker and \
           not self._tracker.get_status_message().get('status'):
            return_dict.update(self._tracker.get_status_message())
        return return_dict

    def __init_tracker(self):
        if self.__get_model_entity():
            self.__set_tracker()

    @check_status
    def start_tracker(self):
        self._tracker.start_tracker()
        return self._tracker.get_status_message()

    @check_status
    def stop_tracker(self):
        self._tracker.stop_tracker()
        return self._tracker.get_status_message()

    @check_status
    def clear_buffer(self):
        self._tracker.delete_tracker()
        return self._tracker.get_status_message()

    @check_status
    def get_collect(self):
        text_response = ''
        for index, save_request in enumerate(self._tracker.get_collect_value().get('tracked_value')):
            text_response += str(index+1) + '. ' + str(save_request.get('time')) + ' | ' \
                             + str(save_request.get('url')) + ' | ' + str(save_request.get('method')) + ' | ' \
                             + str(save_request.get('strategy')) + ' ('+str(save_request.get('rule_name'))+')' + '\n'

        return merge_dict(self.get_message(), {'text_response': text_response})

    @check_status
    def make_rule(self):
        tracked_value = self._tracker.get_collect_value().get('tracked_value')
        if not tracked_value:
            self._status = False
            self._message = u'Новые правила отсутствуют'
            return self.get_message()

        new_rules = []
        tracked_value = self.__delete_duplicate_from_list(tracked_value)
        for save_request in tracked_value:
            if save_request.get('make_rule'):
                rule = self.__make_product_rule(save_request)
                if rule:
                    new_rules.append(rule)
        return merge_dict(self.get_message(), {'created_rules': new_rules})

    def write(self, method, url, body, rule=None):
        self._tracker.write(method, url, body, rule)
        return self.get_message()

    def __make_product_rule(self, save_request):
        url_prepared = urlparse(save_request.get('url').replace('None', '/'))
        product_rule = ProductRule()
        product_rule.url_login = url_prepared.username if url_prepared.username is not None else ''
        product_rule.url_password = url_prepared.password if url_prepared.password is not None else ''
        product_rule.rule_activate = True
        product_rule.name = u'Новое правило для ' + str(save_request.get('url')) + ' - '\
                            + str(save_request.get('method'))
        product_rule.product = self._product_entity

        product_rule.strategy = 'PASS'
        product_rule.weight = 1
        product_rule.time_out_time = 0.1
        try:
            product_rule.save()
        except Exception, e:
            return None

        # create method

        rule_method = RuleMethod()
        rule_method.rule = product_rule
        rule_method.method = save_request.get('method')
        rule_method.save()

        # create matchs
        product_rule_form = ProductRuleForm(product_rule)
        rule_match_manager = CRuleMatchManager(product_rule, product_rule_form)

        # host method create
        rule_match_manager.create_match_rule_from_tracker('host', url_prepared.hostname)
        rule_match_manager.create_match_rule_from_tracker('schema', url_prepared.scheme)
        rule_match_manager.create_match_rule_from_tracker('port', url_prepared.port,
                                                          'ANY' if not url_prepared.port else 'IS')
        rule_match_manager.create_match_rule_from_tracker('path', url_prepared.path)
        rule_match_manager.create_match_rule_from_tracker('body', save_request.get('body'))

        return product_rule

    @staticmethod
    def __delete_duplicate_from_list(list_duplicat):
        seen = set()
        new_list = []
        for dictionary in list_duplicat:
            del dictionary['time']  # delete time, because time is different
            t = tuple(dictionary.items())
            if t not in seen:
                seen.add(t)
                new_list.append(dictionary)
        return new_list

    def __get_model_entity(self):
        if isinstance(self.__product_id, Product):
            self._product_entity = self.__product_id
            return self._status
        try:
            self._product_entity = Product.objects.get(id=self.__product_id)
        except Exception, e:
            self._status = False
            self._message = 'Get rule error: '+str(e)
        return self._status

    def __set_tracker(self, tracker_store_type=TRACKER_STORAGE_TYPE):
        try:
            self._tracker = {
                'REDIS': CRedisStorage(self._product_entity.unique_header),
                'COUCHBASE': CCouchBaseStorage(self._product_entity.unique_header)
            }.get(tracker_store_type, CRedisStorage(self._product_entity.unique_header))
        except Exception, e:
            self._status = False
            self._message = 'Get error in set tracker: '+str(e)
