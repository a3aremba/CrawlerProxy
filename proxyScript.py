__author__ = 'alexz'

from libcproxy.script import ScriptContext, concurrent
from libcproxy.protocol.http import HTTPFlow, HTTPRequest, HTTPResponse
from libcproxy.protocol.tcp import TCPHandler
from libcproxy.protocol import KILL
import os, sys, platform


args = sys.argv
if (platform.node() == 'VM-MYPAY-POLY01'):
    sys.path.append('/home/docker/code/app/') # add this folder to system path
else:
    sys.path.append(os.getcwd()) # add this folder to system path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # turn on django settings


from netlib.odict import ODictCaseless
from core.service.CheckUrl.CheckUrlService import CCheckUrlService
from debug import pycharmDebug

pycharmDebug()
"""
    This is a script stub, with definitions for all events.
"""
def start(context, argv):
    HTTPRequest._headers_to_strip_off.remove("Connection")
    HTTPRequest._headers_to_strip_off.remove("Upgrade")
    """
        Called once on script startup, before any other events.
    """

def clientconnect(context, conn_handler):
    """
        Called when a client initiates a connection to the proxy. Note that a
        connection can correspond to multiple HTTP requests
    """
    HTTPRequest._headers_to_strip_off.append("Connection")
    HTTPRequest._headers_to_strip_off.append("Upgrade")
    context.log("clientconnect")

def serverconnect(context, conn_handler):
    """
        Called when the proxy initiates a connection to the target server. Note that a
        connection can correspond to multiple HTTP requests
    """
    context.log("serverconnect")

@concurrent
def request(context, flow):
    """
        Called when a client request has been received.
    """

    checkService = CCheckUrlService()
    response = checkService.check(flow.request.method, flow.request.url,
                                  flow.request.content, flow.request.headers)

    if response:
        resp = HTTPResponse(
            [1, 1], response.http_code, response.msg,
            ODictCaseless(response.headers),
            response.content)
        flow.reply(resp)
    context.log("request")

def responseheaders(context, flow):
    """
        Called when the response headers for a server response have been received,
        but the response body has not been processed yet. Can be used to tell mitcproxy
        to stream the response.
    """
    flow.response.headers['Mitm-Proxy'] = ["enabled"]
    flow.response.headers['Department'] = ["it-isto"]
    context.log("responseheaders")

@concurrent
def response(context, flow):
    """
       Called when a server response has been received.
       :type context: ScriptContext
       :type flow: HTTPFlow
    """
    value = flow.response.headers.get_first("Connection", None)
    if value and value.upper() == "UPGRADE":
        # We need to send the response manually now...
        flow.client_conn.send(flow.response.assemble())
        # ...and then delegate to tcp passthrough.
        TCPHandler(flow.live.c, log=False).handle_messages()
        flow.reply(KILL)
    context.log("response")

def error(context, flow):
    """
        Called when a flow error has occured, e.g. invalid server responses, or
        interrupted connections. This is distinct from a valid server HTTP error
        response, which is simply a response with an HTTP error code.
    """
    context.log("error")

def clientdisconnect(context, conn_handler):
    """
        Called when a client disconnects from the proxy.
    """
    context.log("clientdisconnect")

def done(context):
    """
        Called once on script shutdown, after any other events.
    """
    context.log("done")