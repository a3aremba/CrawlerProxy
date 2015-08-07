# -*- coding: utf-8 -*-
__author__ = 'alexz'

from core.service.CheckUrl.StrategyFactory.BaseStrategy import CBaseStrategy
from core.service.CheckUrl.ResponseContent import CRescponseContent
from time import sleep

class CImitateStrategy(CBaseStrategy):
    def response(self):
        self._make_time_out()
        response = CRescponseContent()
        response.set_http_code(self._rule.imitate_status)
        response.set_content(self._rule.imitate_body.encode('utf-8')) # encode utf-8 use for https connection that OpenSSL don't support unicode
        response.set_headers(self._make_headers(self._rule.imitate_headers))
        return response

    def _make_headers(self, headers):
        return_list = []
        try:
            headers = headers.decode('string_escape').replace('\t', '')
            header_list = headers.split('\r\n')
            for header in header_list:
                current_header = header.split(':')
                if len(current_header) != 2:
                    break
                return_list.append(current_header)
            return return_list
        except Exception, e:
            pass
        return return_list

    def _make_time_out(self):
        if self._rule.time_out_time:
            sleep(self._rule.time_out_time)
        return True




