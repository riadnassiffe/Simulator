# -*- coding: utf-8 -*-


from simulador.core.dynamicReconfigurator import *
import heuristicSolver2

class discreteReconfigurator2(DynamicReconfigurator):

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
        
        xmlPath='/home/riad/projects/simulador/simulator/src/scenarioDiscretF/'+path
        
        print(xmlPath)

        if maxFreq ==1.0:
            maxFreq=0
        elif maxFreq >= 0.8:
            maxFreq=1
        elif maxFreq >= 0.6:
            maxFreq=2
        elif maxFreq >= 0.4:
            maxFreq=3
        elif maxFreq >= 0.2:
            maxFreq=4
        else:
            maxFreq=5    
        
        result = heuristicSolver2.solver(numTasks,1,6,maxFreq,powerAvailable,xmlPath)
        
        k=0
        for i in taskNumbers:
                if result[k]==0:
                    taskSet[i].frequency=1.0
                    taskSet[i].freqConfigurationHistory.append(1.0)
                elif result[k]==1:
                    taskSet[i].frequency=0.8
                    taskSet[i].freqConfigurationHistory.append(0.8)
                elif result[k]==2:
                    taskSet[i].frequency=0.6
                    taskSet[i].freqConfigurationHistory.append(0.6)
                elif result[k]==3:
                    ttaskSet[i].frequency=0.4
                    taskSet[i].freqConfigurationHistory.append(0.4)
                elif result[k]==4:
                    taskSet[i].frequency=0.2
                    taskSet[i].freqConfigurationHistory.append(0.2)
                elif result[k]==5:
                    taskSet[i].frequency=0.1
                    taskSet[i].freqConfigurationHistory.append(0.1)
                k+=1
    
            
        return result[len(result)-1]
