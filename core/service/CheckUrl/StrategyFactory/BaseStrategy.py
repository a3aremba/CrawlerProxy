# -*- coding: utf-8 -*-
__author__ = 'alexz'


class CBaseStrategy(object):
    def __init__(self, rule):
        self._rule = rule

    def response(self):
       raise NotImplementedError

