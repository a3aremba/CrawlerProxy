# -*- coding: utf-8 -*-
__author__ = 'alexz'

from libcproxy import controller
from threading import Thread

class CProxyServer(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)
        self.stickyhosts = {}

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, flow):
        hid = (flow.request.host, flow.request.port)
        if flow.request.headers["cookie"]:
            self.stickyhosts[hid] = flow.request.headers["cookie"]
        elif hid in self.stickyhosts:
            flow.request.headers["cookie"] = self.stickyhosts[hid]
        flow.reply()

    def handle_response(self, flow):
        hid = (flow.request.host, flow.request.port)
        if flow.response.headers["set-cookie"]:
            self.stickyhosts[hid] = flow.response.headers["set-cookie"]
        flow.reply()


class CProxyServerThreading(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self._proxy_server = CProxyServer(server)

    def get_proxy_server_instance(self):
        return self._proxy_server

    def run(self):
        self._proxy_server.run()
