# -*- coding: utf-8 -*-
from core.lib.MainLogger import CMainLogger

'''
Created on Jan 23, 2014

@author: alexz
'''
class CKibanaLog(object):
    def __init__(self, logDict):
        self.MainLogger = CMainLogger()
        self.MainLogger.logging(logDict)
    
    @property
    def uniq_id(self):
        return self.MainLogger.uniq_id
        
