# -*- coding: utf-8 -*-
from weakref import WeakKeyDictionary

class NonNegative(object):
    """
	A descriptor that forbids negative values
	"""
    def __init__(self, default=0):
        self.default = default
        self.data = WeakKeyDictionary()
        
    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("%s is an invalid value for this propertie" % value)
        self.data[instance] = value
