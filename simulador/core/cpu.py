# -*- coding: utf-8 -*-
"""
Created on Tue May 20 14:31:04 2014

@author: riad
"""

from simulador.core.timer import *
from nonNegative import NonNegative

class cpu(object):
    
    def __init__(self):
        self.dvsTotalTime=nonNegative.NonNegative(0)
        self.energy=nonNegative.NonNegative(0)
        self.temperatureMax=nonNegative.NonNegative(0)
        self.temperature=nonNegative.NonNegative(0)
        self.frenquency=nonNegative.NonNegative(0)
        self.frequencyMax=nonNegative.NonNegative(0)
        self.frequencyMin=nonNegative.NonNegative(0)
        self.voltageMax=nonNegative.NonNegative(0)
        self.Cef=nonNegative.NonNegative(0)
        self.Pleak=0.0
    
    def dvs(self):
        pass
    
    def heatModel(self,system):
        pass

    def energyModel(self,system,job):
        pass

    def run(self, job, system):
        raise NotImplementedError("Function schedule to override!")
        
    def throttling(self,j):
        pass
            