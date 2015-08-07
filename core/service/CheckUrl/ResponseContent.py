# -*- coding: utf-8 -*-
__author__ = 'alexz'


class CRescponseContent():
    def __init__(self):
        self._http_code = 200
        self._content = ''
        self._msg = ''
        self._headers = []

    @property
    def http_code(self):
        return self._http_code

    @property
    def content(self):
        return self._content

    @property
    def msg(self):
        return self._msg

    @property
    def headers(self):
        return self._headers

    def set_http_code(self, code):
        self._http_code = code
        return self

    def set_content(self, content):
        self._content = content
        return self

    def set_msg(self, msg):
        self._msg = msg
        return self

    def set_headers(self, headers):
        self._headers = headers
        return self
