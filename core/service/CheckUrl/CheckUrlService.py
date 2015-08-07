# -*- coding: utf-8 -*-
__author__ = 'alexz'

import re
from urlparse import urlparse
from core.models import Product
from core.model_managers.ProductRuleManager import CProductRuleManager
from core.service.CheckUrl.StrategyFactory.StrategyFactory import CStrategyFactory
from core.service.UrlTracker.TrackerManagerService.TrackerManager import CTrackerManagerService
from core.lib.kibanaLog import CKibanaLog


class CCheckUrlService(object):
    def __init__(self):
        self._uniq_header = None
        pass

    def check(self, method, url, body, headers):
        CKibanaLog({'module': 'CHECK_RULE',
                    'method': method,
                    'url': url,
                    'body': body})
        response = None
        rule = None
        product = self._product_conformity(headers)
        confirm_rules = self._find_need_rules(method, url, body, product)
        if confirm_rules:
            rule = self._get_rule_with_biggest_weight(confirm_rules)
            CKibanaLog({'module': 'RULE_IS',
                        'rule': str(rule)})
            try:
                response = self._make_response_content(rule)
            except Exception, e:
                CKibanaLog({'exception': str(e),
                            'module': 'ERROR_MAKE_RESPONSE'})
        else:
            CKibanaLog({'module': 'WITHOUT_RULE',
                        'message': 'rule is None'})

        try:
            tracker_manager = CTrackerManagerService(product)
            tracker_manager.write(method, url, body, rule)
        except:
            pass
        return response

    def _product_conformity(self, raw_headers):
        uniq_header = raw_headers.get('cproxy-ProductId', None)
        if not uniq_header:
            return None
        self._uniq_header = uniq_header[0]
        product = Product.objects.filter(unique_header=uniq_header[0])
        if len(product) == 0:
            return None
        return product[0]

    @staticmethod
    def _find_need_rules(method, url, body, product):
        if not product:
            return None
        url_prepared = urlparse(url.replace('None', '/'))  # This is HACK some url content 'None'
                                                           # instead of path e.g. 'http://www.google.com.ua:443None'
        confirm_rules = CProductRuleManager().get_confirm_rules(product, url_prepared, method, body)
        return confirm_rules

    @staticmethod
    def _rule_match(match_type, lex_match, field_value, raw_value):
        result = False
        if match_type == 'ANY':  # IF ANY all result of field is true
            return True

        if lex_match == 'TERM':
            if field_value == raw_value:
                result = True
        elif lex_match == 'REGEXP':
            if re.search(field_value, raw_value) is not None:
                result = True
        elif lex_match == 'CONTAINS':
            if raw_value.find(field_value) != (-1):
                result = True

        if match_type == 'IS_NOT':
            result = not result

        return result

    @staticmethod
    def _make_response_content(rule):
            strategy = CStrategyFactory().factory(rule)
            return strategy.response()

    @staticmethod
    def _get_rule_with_biggest_weight(confirm_rules):
        return max(confirm_rules, key = lambda c: c.weight)