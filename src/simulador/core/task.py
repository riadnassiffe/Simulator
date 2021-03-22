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

from nonNegative import NonNegative
from simulador.core.monitor import Monitor
import math

class Task(object):
    cpuExecutionTime=NonNegative(0)
    devicesExecutionTime=NonNegative(0)
    
    deadline=NonNegative(0)
    period=NonNegative(0)
    
    devicesPower=NonNegative(0)
    
    frequency=NonNegative(0)
    
    deadlineMiss=NonNegative(0)
    tardness=NonNegative(0)
    releaseTime=NonNegative(0)

    
    
    def __init__(self,name,cpuExecutionTime,
                 devicesExecutionTime,deadline,period,
                 devicesPower,frequency,taskType,releaseTime,cpuExecutionTimeMax=0,cpuExecutionTimeMin=0):
        self.name=name      
        self.cpuExecutionTime = math.floor(cpuExecutionTime)
        self.cpuExecutionTimeMax=math.floor(cpuExecutionTimeMax)
        self.cpuExecutionTimeMin=math.floor(cpuExecutionTimeMin)        
        self.devicesExecutionTime=math.floor(devicesExecutionTime)
        self.wect= self.devicesExecutionTime+self.cpuExecutionTime
        self.deadline=math.floor(deadline)
        self.period=math.floor(period)
        self.devicesPower=devicesPower
        self.frequency=frequency
        self.taskType=taskType
        self.tardness=0
        self.missDeadlineResume=0
        self.listTardness=[]
        self.nextReleaseTime=releaseTime
        self.cbs=None
        self.releaseTimeHistory=[]
        self.freqConfigurationHistory=[]
        self.finishedJobs=[]
        self.numJobs=0
        self.executedTime=0
        self.state="on"
             
    
    def endJob(self,job):
        if job.deadlineMiss:
            self.tardness+=job.tardness
            self.listTardness.append(job.tardness);
            self.missDeadlineResume+=1  
        self.finishedJobs.append(job)
        self.executedTime+=job.executedTime
        self.numJobs+=1
        
    def taskProfile(self,systemName):
        f = open(self.name+systemName+".log", 'w')
        f.write("tardness="+str(self.tardness/1000.0)+"\n")
        f.write("numbMissDeadline="+str(self.missDeadlineResume)+"\n") 
        f.write("numJobs="+str(self.numJobs)+"\n")
        f.write("executedTime="+str(self.executedTime/1000.0)+"\n")
        f.write("tardHistory=[\n")
        for item in self.listTardness:
            f.write(str(item/1000.0)+",\n")
        f.write("]\n") 
        f.write("jobsReleaseHistory=[\n")            
        for item in self.finishedJobs:
            f.write(str(item.releaseTime)+",\n")
        f.write("]\n") 
        f.write("jobsConsumedEnergy=[\n")            
        for item in self.finishedJobs:
            f.write(str(item.powerConsumed)+",\n")
        f.write("]\n") 
        f.write("taskConfigurations=[\n")            
        for item in self.freqConfigurationHistory:
            f.write(str(item)+",\n")
        f.write("]\n") 
        f.close() 