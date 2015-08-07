# -*- coding: utf-8 -*-
__author__ = 'alexz'
from BaseStorage import CBaseStorage
from django.core.cache import cache
from core.utils import merge_dict
from datetime import datetime

#constants
TRACKER_KEY = 'Tracker_key'
LISTENER_KEY = 'Listener_key'
#----------------------------


class CRedisStorage(CBaseStorage):
    def __init__(self, *args, **kwargs):
        super(CRedisStorage, self).__init__(*args, **kwargs)

    def start_tracker(self):
        listener_list = cache.get(LISTENER_KEY, [])
        if self._uniq_hash not in listener_list:
            listener_list.append(self._uniq_hash)
            cache.set(LISTENER_KEY, listener_list)

        # create tracker key in list
        tracker_dict = cache.get(TRACKER_KEY, {})
        if self._uniq_hash not in tracker_dict:
            tracker_dict[self._uniq_hash] = []
            cache.set(TRACKER_KEY, tracker_dict)

    def stop_tracker(self):
        listener_list = cache.get(LISTENER_KEY, [])
        if self._uniq_hash in listener_list:
            listener_list.remove(self._uniq_hash)
            cache.set(LISTENER_KEY, listener_list)

    def get_collect_value(self):
        tracker_dict = cache.get(TRACKER_KEY, None)
        tracked_value = {}
        if type(tracker_dict) is dict:
            tracked_value = tracker_dict.get(self._uniq_hash, {})
        return merge_dict(self.get_status_message(), {'tracked_value': tracked_value})

    def delete_tracker(self):
        tracker_dict = cache.get(TRACKER_KEY, {})
        tracker_dict.pop(self._uniq_hash, None)
        cache.set(TRACKER_KEY, tracker_dict)

    def write(self, method, url, body, rule=None):
        listener_list = cache.get(LISTENER_KEY, [])
        if self._uniq_hash not in listener_list:
            return False
        tracker_dict = cache.get(TRACKER_KEY, {})
        product_writer = tracker_dict.get(self._uniq_hash, [])

        product_writer.append(self.__make_serialize_request(method, url, body, rule))
        tracker_dict[self._uniq_hash] = product_writer
        cache.set(TRACKER_KEY, tracker_dict)
        return True

    def __make_serialize_request(self, method, url, body, rule):
        serialize_dict ={
            'method': method,
            'url': url,
            'body': body,
            'strategy': 'INTERCEPTED',
            'rule_name': 'NEW RULE WILL BE CREATED',
            'make_rule': True,
            'time': datetime.now().strftime("%H:%M:%S")
        }

        if rule:
            serialize_dict['rule_name'] = str(rule)
            serialize_dict['strategy'] = rule.strategy
            serialize_dict['make_rule'] = False

        return serialize_dict