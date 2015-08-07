# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2014

@author: alexz
'''
from django.core.serializers.json import Serializer
class JsonSerializer(Serializer):
     
    def end_serialization(self):
        for i, ob in enumerate(self.objects):
            self.objects[i] = ob.get('fields', {})
        return super(JsonSerializer, self).end_serialization()