# -*- coding: utf-8 -*-
"""
Created on Sat May 24 08:50:23 2014

@author: riad
"""
        
        
import numpy as np
import random
from simulador.core.task import *

def UUniFast(numberOfTasks, cpuUtilization, deviceUtilization, numberOfTaskSets):
    """
    The UUniFast algorithm was proposed by Bini for generating task
    utilizations on uniprocessor architectures.
    """
    taskSets = []
    while len(taskSets) < numberOfTaskSets:
        # Classic UUniFast algorithm:
        taskSet = []
        sumCpuU = cpuUtilization
        sumDeviceU=  deviceUtilization       
        for i in range(1, numberOfTasks):
            nextSumCpuU = sumCpuU * random.random() ** (1.0 / (numberOfTasks- i))
            nextSumDeviceU = sumDeviceU * random.random() ** (1.0 / (numberOfTasks- i))
            taskSet.append((sumCpuU - nextSumCpuU,sumDeviceU-nextSumDeviceU))
            sumCpuU = nextSumCpuU
            sumDeviceU = nextSumDeviceU
        taskSet.append((sumCpuU,sumDeviceU))
        taskSets.append(taskSet)


    return taskSets
    
def taskSetGenerator(names, utilizationTaskSet, periodSet, devicesPower, cpuUtilizationDiff):   
    
     taskSet=[]          
     for i in range(len(utilizationTaskSet)):
         taskSet.append(Task(names[i],utilizationTaskSet[i][0]*periodSet[i],utilizationTaskSet[i][1]*periodSet[i],periodSet[i],periodSet[i],devicesPower[i],1,'Hard',0,0.05,0.15))
     return taskSet