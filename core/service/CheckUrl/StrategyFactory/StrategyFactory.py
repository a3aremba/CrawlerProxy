# -*- coding: utf-8 -*-
__author__ = 'alexz'

from core.service.CheckUrl.StrategyFactory.ImitateStrategy import CImitateStrategy
from core.service.CheckUrl.StrategyFactory.PassStrategy import CPassStrategy
from core.service.CheckUrl.StrategyFactory.NullStrategy import CNullStrategy


class CStrategyFactory(object):
    def factory(rule):
        if rule.strategy == "PASS":
            return CPassStrategy(rule)
        elif rule.strategy == "IMITATE":
            return CImitateStrategy(rule)
        else:
            return CNullStrategy(rule)
    factory = staticmethod(factory)
