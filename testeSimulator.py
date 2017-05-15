# -*- coding: utf-8 -*-
"""
Created on Sat May 24 08:47:15 2014

@author: riad
    """

import components.CPU.continuousSingleCoreCpu as cpuCont
import components.CPU.discretSingleCoreCpu as cpuDisc
import components.scheduler.cbsScheduler as cbs
import simulador.core.loadTasksFromXml as task
from components.reconfigurators.continuosConvexReconfigurator2 import *
from components.reconfigurators.discreteReconfigurator import *
from components.reconfigurators.continuosPWReconfigurator import *
from  simulador.core.system import *


a=(1.50+0.85)/(200.0)
b=1.0/(24.7*200.0)
pleakTable=[0.0, 0.01 , 0.02, .03, 0.04, 0.1, 0.12]
#disc 72
#cpu=cpuCont.ContinuousSingleCoreCpu(1,0.1,.85,0,25.0,a,b,pleakTable,85.0,72.0,65.0)
cpu=cpuDisc.DiscretSingleCoreCpu(1,0.1,.85,0,25.0,a,b,pleakTable,85.0,75.0,65.0)
reconfigurator=continuosConvexReconfigurator1Variable('convexReconfigurator')
#reconfigurator=discreteReconfigurator('discreteReconfigurator')
#reconfigurator=continuosPWReconfigurator('continuosPWReconfigurator')

scheduler=cbs.CBSSchedulerWithReconfigurations('CBS',reconfigurator)

CPU=[]
CPU.append(cpu)
tasks=[]
tasks.append(task.readXmlForConvexModelWithFreq('/home/riad/projects/simulador/simulator/src/tasks1fp.xml'))
tasks.append(task.readXmlForConvexModelWithFreq('/home/riad/projects/simulador/simulator/src/tasks1fm.xml'))


tasks[0][0].state='on'
tasks[0][1].state='on'
tasks[0][2].state='on'
tasks[0][3].state='on'
tasks[0][4].state='off'
tasks[0][5].state='off'
tasks[0][6].state='on'
tasks[0][7].state='off'

simulador=System( CPU , tasks, scheduler, 0, 23,"S1")
simulador.scenario="S1"
simulador.powerAvailable=2.6
scheduler.addSystem(simulador)
simulador.runSystem(20*60*1000)
