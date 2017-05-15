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


from simulador.core.job import *
from nonNegative import NonNegative
from simulador.core.cpu import *
from simulador.core.system import *
from simulador.core.task import *

class DiscretSingleCoreCpu(cpu):


    a=NonNegative(0)
    b=NonNegative(0)
    

    def __init__(self,frequencyMax,frequencyMin,Psleep,C0,temperature,a,b,pleakTable,temperatureMAx,temperatureMaxThreshold,temperatureMinThreshold):
        self.totalTime=0
        self.consumedPower=0.0
        self.temperature=temperature
        self.frequencyMax=frequencyMax
        self.frequencyMin=frequencyMin
        self.C0=C0
        self.a=a
        self.b=b
        self.temperatureMax=temperatureMAx
        self.temperatureMaxThreshold=temperatureMaxThreshold
        self.temperatureMinThreshold=temperatureMinThreshold
        self.idle=0
        self.temperatureHistory=[]
        self.frenquency=1
        self.instantPower=[]
        self.PleakTable=pleakTable
        self.Pleak=0.0
        self.Psleep=Psleep
        self.Pfan=0.0
        self.throttlingTime=0.0


    def heatModel(self,HambTemperature):
        self.temperature=self.a*self.frenquency**3-self.b*(self.temperature-HambTemperature)+self.temperature                
        self.temperatureHistory.append(self.temperature)

    def energyModel(self,j):        
        if self.temperature<50:
            self.Pleak=self.PleakTable[0]
        elif 50<=self.temperature<55:
            self.Pleak=self.PleakTable[1]
        elif 55<=self.temperature<60:
            self.Pleak=self.PleakTable[2]
        elif 60<=self.temperature<65:
            self.Pleak=self.PleakTable[3]
        elif 65<=self.temperature<70:
            self.Pleak=self.PleakTable[4]
        elif 70<=self.temperature<75:
            self.Pleak=self.PleakTable[5]
        elif 75<=self.temperature<80:
            self.Pleak=self.PleakTable[6]    
        
        if j!=None:
            if self.frenquency==0.1:
                cpuPower=0.81
            elif self.frenquency<0.2:
                cpuPower=0.83
            elif self.frenquency<0.6:
                cpuPower=0.9
            elif self.frenquency<0.8:
                cpuPower=1.0
            elif self.frenquency<1:
                cpuPower=1.1
            else:
                cpuPower=1.5
                
                
            self.consumedPower=self.consumedPower+(cpuPower+self.Pleak + self.Psleep + self.Pfan)*0.001
            j.powerConsumed=j.powerConsumed+self.consumedPower
            j.powerConsumedHistory.append(cpuPower+self.Pleak + self.Psleep + self.Pfan)
            self.instantPower.append(cpuPower+self.Pleak + self.Psleep + self.Pfan)        
        else:
            self.instantPower.append(self.Pleak + self.Psleep +self.Pfan)                        
            self.consumedPower=self.consumedPower+(self.Pleak + self.Psleep +self.Pfan)*0.001
        
        
    def run(self,job,system):
        """
            Update the CPU status (power consumed and temperature) after the execution on an a unit of time, using the frequency determined
            by the Job.
            Keyword arguments:
            job -- if the Job there is no Job to be executed the CPU will run on IDLE                          
        """
        if job != None:         
            #here I check if there is a Job to be executed
            
            if 0<job.cpuFrequency<=0.1:
                job.cpuFrequency=0.1
            elif 0.1<job.cpuFrequency<=0.2:
                job.cpuFrequency=0.2 
            elif 0.2<job.cpuFrequency<=0.6:
                job.cpuFrequency=0.6
            elif 0.6<job.cpuFrequency<=0.8:
                job.cpuFrequency=0.8
            elif 0.8<job.cpuFrequency<=1.0:
                job.cpuFrequency=1.0
                
            self.throttling(job)
            if(job.execute(self.frenquency)):
                self.energyModel(job)
                job.timeHistory.append(self.totalTime)
            else:
                self.frenquency=self.frequencyMin           
                self.idle+=1
                self.energyModel(None)
        else:  
             #if there is no Job to be executed, the CPU will run on IDLE
             self.frenquency=self.frequencyMin           
             self.idle+=1
             self.energyModel(None)
        self.heatModel(system.hambTemperature)
        system.timer.increment()
        self.totalTime+=1


    def throttling(self,j):
        if self.temperature>=self.temperatureMax:
            self.frenquency=self.frequencyMin
            self.throttlingTime+=1
            print("T")
        else:
            self.frenquency=j.cpuFrequency
        
    def CPUProfile(self,systemName):
        f = open("CPUProfile"+systemName+".log", 'w')
        f.write("Throtling="+str(self.throttlingTime)+"\n")        
        f.write("idleTime="+str(self.idle/1000.0)+"\n")
        f.write("TotalExecutionTime="+str(self.totalTime/1000)+"\n")
        f.write("TotalEnergy="+str((self.consumedPower))+"\n")       
        f.write("tempHistory=[\n")
        oldTemp=0.0        
        for item in self.temperatureHistory:
            if item-oldTemp > 1.00 or item-oldTemp < -1:
                f.write(str(item)+",\n")
                oldTemp=item
        f.write("]\n")   
        f.close() 
