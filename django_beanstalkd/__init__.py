"""
Django Beanstalk Interface
"""
from __future__ import absolute_import
from builtins import str
from builtins import object
from django.conf import settings
import greenstalk

from .decorators import beanstalk_job

def connect_beanstalkd():
    """Connect to beanstalkd server(s) from settings file"""

    server = getattr(settings, 'BEANSTALK_SERVER', '127.0.0.1')
    port = 11300
    if server.find(':') > -1:
        server, port = server.split(':', 1)

    port = int(port)
    return greenstalk.Client((server, port))


class BeanstalkError(Exception):
    pass


class BeanstalkClient(object):
    """beanstalk client, automatically connecting to server"""

    def call(self, func, arg='', priority=2**16, delay=0, ttr=60):
        """
        Calls the specified function (in beanstalk terms: put the specified arg
        in tube func)

        priority: an integer number that specifies the priority. Jobs with a
                  smaller priority get executed first
        delay: how many seconds to wait before the job can be reserved
        ttr: how many seconds a worker has to process the job before it gets requeued
        """
        self._beanstalk.use(func)
        self._beanstalk.put(str(arg), priority=priority, delay=delay, ttr=ttr)

    def __init__(self, **kwargs):
        self._beanstalk = connect_beanstalkd()
