__author__ = 'alexz'

from os.path import dirname, join, isfile
from _environment import get_environment_type

_base = join(dirname(__file__), '_base.py')
_local = join(dirname(__file__), '_local.py')
execfile(_base) # load base

try:
    environment = get_environment_type()
    if environment:
        execfile(join(dirname(__file__),  environment)) # load environment file
except Exception, e:
    raise BaseException('Can\'t load environment \''+ get_environment_type() + '\' error: '+str(e))

if isfile(_local):
    execfile(_local) # load local if create