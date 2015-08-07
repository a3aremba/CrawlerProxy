# -*- coding: utf-8 -*-

import socket
import commands
import platform

class CSystemInfo:
    def __init__(self):
        self.__setIP()
    
    def __setIP(self):
        self.__SERVER_ADDR = socket.gethostbyname(socket.gethostname())
        
        if platform.system() == 'Linux':
            SERVER_ADDRESSES = commands.getoutput("/sbin/ifconfig | grep -i \"inet\" | grep -iv \"inet6\" | " +
                                                  "awk {'print $2'} | sed -ne 's/addr\:/ /p'")
            for SERVER_ADDR in SERVER_ADDRESSES.split(' '):
                if SERVER_ADDR.strip() != '' and SERVER_ADDR.strip() != '127.0.0.1':
                    self.__SERVER_ADDR = SERVER_ADDR.strip()
    
    def getIP(self):
        return self.__SERVER_ADDR
