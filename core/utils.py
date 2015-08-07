# -*- coding: utf-8 -*-
__author__ = 'alexz'

def merge_dict(x, y):
    return dict(x.items() + y.items())

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance
