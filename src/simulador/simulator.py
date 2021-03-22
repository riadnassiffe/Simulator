#!/usr/bin/python3
"""
Copyright (C) 2014 Ríad Mattos Nassiffe

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

# -*- coding: utf-8 -*-
"""
Created on Sat May 24 08:47:15 2014

@author: riad
    """

import components.CPU.continuousSingleCoreCpu as cpu
import components.scheduler.cbsScheduler as cbs
from simulador.core.system import System


a = (0.5498+0.878)/(200)
b = 1.0/(24.7*200)

pleakTable = {"48": .267, "50": .28, "60": .29, "78": .39, "82": .4}

cpu = cpu.ContinuousSingleCoreCpu(
    1.2, 0.1, .878, 0.5498, 25.0, a, b, pleakTable, 74.0, 75.0, 65.0)

scheduler = cbs.CBSSchedulerWithReconfigurations('CBS')


CPU = []
CPU.append(cpu)

simulador = System(CPU, taskSet[0], scheduler, 0, 25, "sh51.xml", "S1")
scheduler.addSystem(simulador)
simulador.runSystem(10*60*1000)
