# -*- coding: utf-8 -*-
__author__ = 'alexz'


class CBaseStorage(object):
    def __init__(self, uniq_hash):
        self._uniq_hash = uniq_hash
        self._status = True
        self._message = ''

    def get_status_message(self):
        return {'status': self._status,
                'message': self._message}

    def start_tracker(self):
        raise NotImplementedError

    def stop_tracker(self):
        raise NotImplementedError

    def get_collect_value(self):
        raise NotImplementedError

    def delete_tracker(self):
        raise NotImplementedError

    def write(self):
        raise NotImplementedError