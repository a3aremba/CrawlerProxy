# -*- coding: utf-8 -*-
__author__ = 'alexz'

def check_status(func):
   def func_wrapper(self_class):
       if self_class._status:
           return func(self_class)
       else:
           return self_class.get_message()
   return func_wrapper