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
from nonNegative import NonNegative
from simulador.core.monitor import *
from simulador.core.timer import *
from simulador.core.task import *
import math
import random as random


class Job(object):

        cpuExecutionTime = NonNegative(0)
        devicesExecutionTime = NonNegative(0)
        tardness = NonNegative(0)
        executedTime = NonNegative(0)
        executionTime = NonNegative(0)
        releaseTime = NonNegative(0)

        def __init__(self, task, releaseTime):

                self.devicesExecutionTime = task.devicesExecutionTime
                self.cpuExecutionTime = task.cpuExecutionTime
                self.cpuFrequency = task.frequency
                self.executionTime = self.cpuExecutionTime+self.devicesExecutionTime
                self.executedTime = 0.0
                self.deadline = releaseTime+task.deadline
                self.task = task
                self.deadlineMiss = False
                self.tardness = 0.0
                self.releaseTime = releaseTime
                self.powerConsumed = 0.0
                self.timeHistory = []
                self.powerConsumedHistory = []
                self.status = "Ready"

        def startJob(self):
                self.status = "Running"

        def endJob(self):
                self.status = "Ended"

        def preemptJob(self):
                self.status = "Preempt"

        def execute(self, time):
                if self.executedTime < self.executionTime and self.status == "Running":
                        if self.cpuExecutionTime > 0:
                                self.executedTime += time
                        elif self.devicesExecutionTime > 0:
                                self.executedTime += 1
                        return True
                else:
                        self.endJob()
                        print("a Jobs ends here")
                        return False
