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

import weakref

class Scheduler(object):
    
    
    def __init__(self,name,reconfigurator,schedule_overHead=0,activation_verhead=0, terminate_overhead=0):
        """
        Args:

        - `name`:
        - `schedule_overHead`:
        - `schedule_over_head=0,
        - `verhead_activate`=0,
        - `overhead_terminate`=0,
        - `reconfiguration_overHead`=0
        """     
        self.cpuList = []
        self.jobList = []
        self.name =name
        self.activation_verhead = activation_verhead
        self.terminate_overhead = terminate_overhead
        self.eventList=[]
        self.running=True
        self.reconfigurator=reconfigurator

    def addSystem(self,system):
        self.system=system

    def newEvent(self, eventType, task, time, eventData=None):
        pass

    def schedulerStart(self):
        pass        
        
    def addTask(self,taskList):
        """
        This method is called when the system is ready to run. This method
        should be used in lieu of the __init__ method. This method is
        guaranteed to be called when the simulation starts, after the tasks
        are instantiated
        """
        pass

    def jobArrival(self, job):
        """
        This method is called upon a job activation.

        Args:
            - `job`: The activated `job`.
        """
        pass

    def jobFinish(self):
        """
        This method is called when a job finish (termination or abortion).


        """
        pass
    
    def nextStep(self):
        """
        This method defines the next action of the scheduler
        """
        raise NotImplementedError("Function nexStep to override!")

    def schedule(self):
        """
        The schedule method must be redefined by the simulated scheduler.
        It takes as argument the cpu on which the scheduler runs.
        """
        raise NotImplementedError("Function schedule to override!")


    def addJob(self, job):
        """
        Add a task to the list of tasks handled by this scheduler.

        Args:
            - `task`: The :class:`task` to add.
        """
        self.jobList.append((job.releaseTime, job))


    def addCPU(self, cpu):
        """
        Add a processor to the list of processors handled by this scheduler.

        Args:
            - `processor`: The :class:`processor` to add.
        """
        self.cpuList.append(cpu)
        
    def callReconfigurator(self):
        """
            Function that check if it is necessery to change tasks Configuration.
        """        
