# -*- coding: utf-8 -*-
'''
Created on Jun 5, 2014

@author: alexz
'''
import redis
import datetime
import json
import logging
import traceback
import types
import uuid

from socket import *
from core.extras.SystemInfo import CSystemInfo # this must be declared
from core.settings import LOGGER_STATUS_CODE, LOGGER_REDIS_HOST, LOGGER_REDIS_PORT,\
LOGGER_REDIS_DB, LOGGER_REDIS_LIST, LOGGER_UDP_HOST, LOGGER_UDP_PORT, LOGGER_TO_FILE, rootDirName

logger = logging.getLogger(LOGGER_TO_FILE)
class CMainLogger(object):

    def __init__(self): 
        self._loggingData = None
        self._notificationType = 'INFO'
        self._loggerTrace = None
        self._uniq_id = str(uuid.uuid1())
        
    @property
    def uniq_id(self):
        return self._uniq_id
        
    def logging(self, loggingData):
        if not self.is_logging(loggingData):
            return False
        
        self.__initialize_logger_data(loggingData)
        result = False
        if self.__logging_in_redis():
            result = True
        elif self.__logging_in_udp():
        # if self.__logging_in_udp():
            result = True
        else:
            try:
                self.__logging_in_file()
                result = True
            except Exception, e:
                result = False
                print str(e)
        
        return result
       
    def is_logging(self, loggingData):
        if not isinstance(loggingData, dict):
            return True
        
        statusCode = loggingData.get('statusCode', None)
        if statusCode is not None:
            if self.__get_statuscode_type(int(statusCode)) in LOGGER_STATUS_CODE:
                return True
            else: 
                return False
        else:
            return True   
        
    def __initialize_logger_data(self, loggingData):
        self._loggingData = self.__get_dict(loggingData)
        self._loggingData['host'] = CSystemInfo().getIP()
        self._loggingData['time'] = str(datetime.datetime.now())
        self._loggingData['projectName'] = rootDirName
        self._loggingData['uniq_id'] = self._uniq_id
        if traceback.format_exc() != 'None\n':
            self._loggingData['tracebackException'] = traceback.format_exc()
            self._loggingData['AlertType'] = 'CLIENT_ERROR'
    
    def __logging_in_redis(self):
        result = False
        try:
            redisLogServer = redis.Redis(host=LOGGER_REDIS_HOST,
                                         port=LOGGER_REDIS_PORT,
                                         db=LOGGER_REDIS_DB)
            redisLogServer.rpush(LOGGER_REDIS_LIST, json.dumps(self._loggingData))
            result = True
        except Exception, e:
            self._loggingData['redisLogError'] = str(e)
            pass

        return result
    
    def __logging_in_udp(self):
        result = False
        try:
            s = socket(AF_INET,SOCK_DGRAM)
            host = LOGGER_UDP_HOST
            port = LOGGER_UDP_PORT
            addr = (host,port)
            s.sendto(json.dumps(self._loggingData), addr)
            s.close()
            result = True
        except Exception, e:
            self._loggingData['udpLogError'] = str(e)
            pass
        
        return result
    
    def __logging_in_file(self):
        logger.info(self._loggingData)
        return True
    
    def __get_dict(self, loggingData):
        if isinstance(loggingData, dict):
            loggingData['AlertType'] = self._notificationType
            return loggingData
        elif isinstance(loggingData, basestring):
            loggingData = str(loggingData.encode('utf-8'))
        else :
            try:
                loggingData = str(loggingData)
            except Exception, e:
                loggingData = 'Unable lead to string: '+ str(e)
        
        return {'message': loggingData,
                'AlertType': self._notificationType
                }
        
    def __get_statuscode_type(self, statusCode):
        returnStatusCode = 0
        if statusCode >= 200 and statusCode < 300:
            returnStatusCode = 200
            self._notificationType = 'INFO'
        elif statusCode >= 300 and statusCode < 400 :
            returnStatusCode = 300
            self._notificationType = 'ALERT'
        elif statusCode >= 400 and statusCode < 500 :
            returnStatusCode = 400
            self._notificationType = 'CLIENT_ERROR'
        elif statusCode >= 500 and statusCode < 600 :
            returnStatusCode = 500
            self._notificationType = 'SERVER_ERROR'
            
        return returnStatusCode
        