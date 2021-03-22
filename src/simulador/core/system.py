# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Riad Mattos Nassiffe

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
"""

from simulador.core.timer import *  
from nonNegative import NonNegative
from simulador.core.scheduler import *
from simulador.core.monitor import *
from simulador.core.task import *
from simulador.core.timer import *
from simulador.core.scheduleEvents import *
import components.scheduler.cbsScheduler 
from tools.readXmlModel import *
import numpy
import pickle
import simulador.core.loadTasksFromXml as taskLoader

class System(object):
    
    hambTemperature=NonNegative(0)
  
    def __init__(self, cpus, tasks, scheduler, devices, hambTemperature,name):
        self.cpuList=cpus
        self.tasksSets=tasks
        self.tasks=self.tasksSets[0]
        self.scheduler=scheduler
        self.timer=Timer()
        self.devices=devices
        self.powerAvailable = 5
        self.hambTemperature=hambTemperature
        self.monitor=Monitor("Sys1")
        self.name=name
        self.step=-1
        self.scenarioOld=""
        self.monitor.recordLog("initializing System Class",0,"0")
        self.tempTol=0
        self.reconfiguration=False
        self.statePowerInfo={}
        self.stateExecutionTimeInfo={}
    
    
    def runSystem(self, duration):
        self.monitor.recordLog("starting system execution",0,"0")
        self.scheduler.schedulerStart()         
        self.scheduler.addTasks(self.tasks) 
                    
        for cpu in self.cpuList:
            self.scheduler.addCPU(cpu)
        
        self.monitor.recordLog("System started with "+str(len(self.scheduler.eventList))+"events",0,"0")

        
        tau = self.tasks[0]
        self.scheduler.newEvent(4,tau,0,"S1")
        self.scenario="S1"
        self.scenarioOld="S1"
        self.step=0
        rec=0
        
        
        while self.scheduler.running:
            
            if duration > self.timer.now():
                for tau in self.tasks:
                    if tau.state == "on" and tau.name!='Treconf' :
                        if tau.nextReleaseTime == self.timer.now() and self.reconfiguration==False:
                            self.scheduler.newEvent(1, tau, self.timer.now())
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period               
                    elif tau.name =='Treconf':
                        if self.timer.now()==3*60*1000 and rec == 0:
                            rec=1
                            self.reconfiguration=True
                            #4
                            #powerAvailable=2.0
                            self.scheduler.newEvent(4,tau,self.timer.now()+1*60*1000,"S3")
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period
                            print("asking for config  1"+str(self.timer.now()))
                        elif self.timer.now()== 7*60*1000 and rec==1:
                            rec=2
                            self.reconfiguration=True
                            #3
                            #powerAvailable=2.21
                            self.scheduler.newEvent(4,tau,self.timer.now()+1*60*1000,"S4")
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period
                            print("asking for config  2")
                        elif self.timer.now()== 10*60*1000 and rec==2:
                            rec=3
                            #powerAvailable=2.2
                            self.reconfiguration=True
                            self.scheduler.newEvent(4,tau,self.timer.now()+3*60*1000,"S5")
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period                  
                            print("asking for config  3")
                        elif self.timer.now()== 13*60*1000 and rec == 3:
                            rec=4
                            #powerAvailable=2.21
                            self.reconfiguration=True
                            self.scheduler.newEvent(4,tau,self.timer.now()+1*60*1000,"S3") 
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period
                            print("asking for config  4")
                        elif self.timer.now()== 14*60*1000 and rec==4:
                            rec=5 
                            #powerAvailable=2.0
                            self.reconfiguration=True
                            self.scheduler.newEvent(4,tau,self.timer.now()+3*60*1000,"S5")
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period
                            print("asking for config  5")
                        elif self.timer.now()== 17*60*1000 and rec==5:
                            rec=6
                            #powerAvailable=2.0
                            self.reconfiguration=True
                            self.scheduler.newEvent(4,tau,self.timer.now()+2*60*1000,"S2")
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period
                            print("asking for config 6")
                    else:
                        if tau.nextReleaseTime == self.timer.now():
                            tau.nextReleaseTime=tau.nextReleaseTime+tau.period                                                        
            elif len(self.scheduler.eventList)==0 and len(self.scheduler.serverListReady)==0 and self.scheduler.executingServer == None:
                        self.scheduler.running=False
            self.scheduler.nextStep()   
        
        for i in self.tasks:
            i.taskProfile(self.name)
            
        self.cpuList[0].CPUProfile(self.name)
        self.pickle()        

    def pickle(self):
        f = file(self.name, 'wb')
        pickle.dump(self, f)
        f.close()        
    
    def unpickle(self):
        with file(self.name, 'rb') as f:
            return pickle.load(f)
            