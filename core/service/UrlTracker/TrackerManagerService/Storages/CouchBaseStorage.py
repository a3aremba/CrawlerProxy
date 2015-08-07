# -*- coding: utf-8 -*-
__author__ = 'alexz'
from .BaseStorage import CBaseStorage

class CCouchBaseStorage(CBaseStorage):
    def __init__(self, *args, **kwargs):
        super(CCouchBaseStorage, self).__init__(*args, **kwargs)
        return