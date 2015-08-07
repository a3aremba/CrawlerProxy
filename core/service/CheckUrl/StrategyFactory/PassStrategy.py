# -*- coding: utf-8 -*-
__author__ = 'alexz'

from core.service.CheckUrl.StrategyFactory.BaseStrategy import CBaseStrategy


class CPassStrategy(CBaseStrategy):
    def response(self):
        return None
