__author__ = 'alexz'
import os, json
from core.settings import BASE_DIR

def pycharmDebug():
    debugSettings = BASE_DIR + '/debug.json'
    if (os.path.isfile(debugSettings)):
        debugAttrs = json.loads(file(debugSettings, 'r').read())
        if (debugAttrs.get('enabled')):
            import pydevd
            print debugAttrs
            pydevd.settrace(debugAttrs.get('host'), port=debugAttrs.get('port'), stdoutToServer=True, stderrToServer=True)
            return True

    # Otherwise:
    return False
