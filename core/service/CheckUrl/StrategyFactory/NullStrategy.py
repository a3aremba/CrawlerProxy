# -*- coding: utf-8 -*-
__author__ = 'alexz'

from core.service.CheckUrl.StrategyFactory.BaseStrategy import CBaseStrategy


class CNullStrategy(CBaseStrategy):
    def response(self):
        raise Exception('Chosen strategy is not implemented.')
        pass