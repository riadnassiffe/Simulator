# -*- coding: utf-8 -*-

from simulador.core.dynamicReconfigurator import *
import cfsqpSolver2
import math

class continuosConvexReconfigurator2Variable(DynamicReconfigurator):

    def reconfigure(self,taskSet,powerAvailable,maxFreq,pleak,path,taskSetName):
        numTasks=0        
        if taskSetName == "S1":    
            numTasks=4
            taskNumbers=[1,2,3,6]
        elif taskSetName == "S2":    
            numTasks=5
            taskNumbers=[2,3,4,5,6]
        elif taskSetName == "S3":    
            numTasks=5
            taskNumbers=[2,3,4,6,7]
        elif taskSetName == "S4":    
            numTasks=6
            taskNumbers=[1,2,3,4,5,6]
        elif taskSetName == "S5":    
            numTasks=5
            taskNumbers=[2,3,4,5,6]


            
        task=taskSet[0]        
        xmlPath='/home/riad/projects/simulador2/simulator/src/scenarioContiF/'+path+'fq.xml'
        
        result = cfsqpSolver2.solver(1,200,numTasks,maxFreq,powerAvailable,pleak,xmlPath)

        print(result)
        k=0        
        for i in taskNumbers:
            taskSet[i].frequency=math.exp(result[k])
            taskSet[i].freqConfigurationHistory.append(math.exp(result[k]))
            taskSet[i].wcet=math.floor(math.exp(result[k+numTasks]))
	    k=k+1
            

        return result[len(result)-1]
            
