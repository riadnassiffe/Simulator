# -*- coding: utf-8 -*-
"""
Created on Thu May 22 07:48:08 2014

@author: riad
"""

class SchedulerEvent(object):
    
    def __init__(self, eventType, task, time, eventData=None):
        raise NotImplementedError("Function __init__ to override!")