# -*- coding: utf-8 -*-
__author__ = 'alexz'

from libcproxy import controller, proxy
from libcproxy.proxy.server import ProxyServer
from .ProxyServer import CProxyServer, CProxyServerThreading
from core.utils import singleton

START_PORT_VALUE = 8990
END_PORT_VALUE = 8999

@singleton
class CProxyManagerService(object):
    def __init__(self):
        self._ports = range(START_PORT_VALUE, END_PORT_VALUE)
        self._server_dict = {}

    def create_new_proxy_server(self):
        status = True
        message = ''
        port = None
        try:
            port, server_config = self.__configure_server()
            server_thread = CProxyServerThreading(server_config)
            m_instance = server_thread.get_proxy_server_instance()
            server_thread.start()
            print "thread pid is: %s" % server_thread.ident
            print "server started on %s port" % port
            self._server_dict.update({port: m_instance})
        except Exception, e:
            status = False
            message = 'Creating proxy server error '+str(e)

        return {'status': status,
                'message': message,
                'port': port}

    def stop_proxy_server(self, port):
        result = {'status': True,
                  'message': ''}
        try:
            proxy_server_instance = self._server_dict.get(port, None)
            proxy_server_instance.shutdown()
            del self._server_dict[port]
        except Exception, e:
            result['status'] = False
            result['message'] = str(e)
        return result

    def show_server_dict(self):
        return self._server_dict

    def __configure_server(self):
        port = self.__get_free_port()
        if not port:
            raise Exception('All port are already busy ! please, try again later')
        config = proxy.ProxyConfig(port=port)  # it's possible to add any other config
        return port, ProxyServer(config)

    def __get_free_port(self):
        for port in range(START_PORT_VALUE, END_PORT_VALUE):
            if self._server_dict.get(port, None) is None:
                return port
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Destroy all elements
        print 'is destructor'
        for instance_dict in enumerate(self._server_dict):
            print instance_dict
