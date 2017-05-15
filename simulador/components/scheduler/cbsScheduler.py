# -*- coding: utf-8 -*-



from simulador.core.cpu  import *
from simulador.core.scheduleEvents  import *
from simulador.core.timer     import *
from simulador.core.job import *
from simulador.core.scheduler import *


class CBSScheduleEvent(SchedulerEvent):

    JOB_ARRIVE=1
    JOB_END=2
    SERVER_BUDGET_DEPLETION=3
    RECONFIGURATION_REQUEST=4    
    RECONFIGURATION=5
    
    def __init__(self, eventType, task, releaseTime, eventData=None):    
        if 0 > eventType or eventType > 11:        
           raise ValueError("Invalid enventTypy, it must an interger number equal or grater than 0 and less than 8")                
        self.eventType=eventType 
        self.task=task        
        self.releaseTime=releaseTime
        self.eventData=eventData

    def __lt__(self, other):        
         if self.releaseTime<other.releaseTime:
            return True
            
    def __cmp__(self,other):
        if self.releaseTime<other.releaseTime:
            return True
        else:
            return False

class CBSServer(object):
    
    def __init__(self, task):
        self.task=task
        self.budget=task.wect
        self.currentBudget=task.wect
        self.deadLine=task.deadline
        self.currentDeadLine=task.releaseTime+task.deadline
        self.period=task.period
        self.jobList=[]
        self.executingJob=None
        
    def __lt__(self, other):        
         if self.deadLine<other.deadLine:
            return True
            

class CBSSchedulerWithReconfigurations(Scheduler):

    def schedulerStart(self):
         self.executingServer=None
         self.serverList=[]
         self.serverListReady=[]
         self.debug=0

    def newEvent(self, eventType, task, time, eventData=None):
        self.eventList.append(CBSScheduleEvent( eventType, task, time,eventData))
        if  len(self.eventList)>1:       
            self.eventList.sort()
        
    def addTasks(self,taskList):
        for tau in taskList:
            self.serverList.append(CBSServer(tau))
            tau.cbs=self.serverList[len(self.serverList)-1]  
            

    def jobArrival(self, event):
        if event.task.cbs.executingJob == None:
           event.task.cbs.executingJob=Job(event.task,self.system.timer.now())           
           event.task.cbs.executingJob.startJob()
           self.serverListReady.append(event.task.cbs)
           self.schedule()
        else:
            event.task.cbs.jobList.append(Job(event.task, event.task.releaseTime))

    def jobFinish(self):
        #verifica se ouve perda de deadline
        if self.system.timer.now() > self.executingServer.executingJob.deadline:      
            self.executingServer.executingJob.deadlineMiss=True
            self.executingServer.executingJob.tardness=self.system.timer.now()-self.executingServer.executingJob.deadline
        
        #adicionar job terminado a lista de jobs finalizados
        self.executingServer.task.endJob(self.executingServer.executingJob)

        #verificar se existe mais algum job para aquela tarefa, se existi coloca em execucão
        if len(self.executingServer.jobList)>0:
            self.executingServer.executingJob= self.executingServer.jobList.pop(0)
            self.executingServer.executingJob.startJob()
        else:
            self.executingServer.executingJob=None
            self.executingServer= None
            

    def cbsRecharge(self):
        if self.executingServer.currentBudget==0:
            self.executingServer.deadLine+=self.executingServer.period
            self.executingServer.currentBudget=self.executingServer.budget
        else:
            self.executingServer.deadLine+=self.executingServer.period
            self.executingServer.currentBudget=self.executingServer.budget
        self.schedule()

    def newConfiguration(self,event):
        cpu=self.cpuList[0]
        tau=self.system.tasks[0]
        path = self.system.scenario
        wect=0                
        if cpu.temperatureMaxThreshold > cpu.temperature:
            freqMax=min(1.0,((cpu.temperatureMaxThreshold+cpu.b*(cpu.temperature-self.system.hambTemperature)-cpu.temperature)/cpu.a)**(1.0/3.0))
            #path=path+"/1/"
        else:
            freqMax=min(1.0,((cpu.b*(cpu.temperature+6-self.system.hambTemperature))/cpu.a)**(1.0/3.0))
            freqMax=freqMax-0.05

        print(cpu.temperature)
        print("Fmax="+str(freqMax))        
        
        if event.eventData!="temperature":                    
            wect=self.reconfigurator.reconfigure(self.system.tasks,self.system.powerAvailable,freqMax,cpu.Pleak,path,self.system.scenario)
            tau.wect=1#math.floor(wect)        
            self.newEvent(1,tau,self.system.timer.now())        
            self.newEvent(5,tau,self.system.timer.now()+tau.period)        
        else:
            path=self.system.scenarioOld#+"/2/"                      
            wect=self.reconfigurator.reconfigure(self.system.tasks,self.system.powerAvailable,freqMax,cpu.Pleak,path,self.system.scenarioOld)
            tau.wect=1#math.floor(wect)        
            self.newEvent(1,tau,self.system.timer.now())
    def reconfigure(self,event):
        """
        This function must be called if the processor is near to its upper or lower temperature trashold.
        """         
        if self.system.step == 0:
            print("setting config 1")
            self.system.step+=1
            self.system.scenario='S3'
            self.system.scenarioOld='S1'
            #S1
            self.tasks=self.system.tasksSets[0]
            self.system.tasks[1].state='on'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='off'
            self.system.tasks[5].state='off'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='off'
            self.system.reconfiguration=False
        elif self.system.step == 1:
            print("setting config 2")
            self.system.step+=1         
            self.system.scenario='S4'
            self.system.scenarioOld='S3'
            #S3
            self.tasks=self.system.tasksSets[0]
            self.system.tasks[1].state='off'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='on'
            self.system.tasks[5].state='off'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='on'
            self.system.reconfiguration=False
        elif self.system.step == 2:
            print("setting config 3")
            self.system.step+=1
            self.system.scenario='S5'
            self.system.scenarioOld='S4'
            #S4
            self.tasks=self.system.tasksSets[1]
            self.system.tasks[1].state='on'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='on'
            self.system.tasks[5].state='on'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='off'
            self.system.reconfiguration=False
        elif self.system.step == 3:
            print("setting config 4")
            self.system.step+=1
            self.system.scenario='S1'
            self.system.scenarioOld='S5'
            #S5
            self.tasks=self.system.tasksSets[1]
            self.system.tasks[1].state='off'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='on'
            self.system.tasks[5].state='on'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='off'
            self.system.reconfiguration=False
        elif self.system.step == 4:
            print("setting config 5")
            self.system.step+=1
            self.system.scenario='S3'
            self.system.scenarioOld='S1'
            #S1
            self.tasks=self.system.tasksSets[0]
            self.system.tasks[1].state='on'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='off'
            self.system.tasks[5].state='off'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='off'
            self.system.reconfiguration=False
        elif self.system.step == 5:
            print("setting config 6")
            self.system.step+=1
            self.system.scenario='S5'
            self.system.scenarioOld='S3'
            #S3         
            self.tasks=self.system.tasksSets[0]
            self.system.tasks[1].state='off'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='on'
            self.system.tasks[5].state='off'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='on'
            self.system.reconfiguration=False
        elif self.system.step == 6:
            print("setting config 7")
            self.system.step+=1
            self.system.scenario='S2'
            self.system.scenarioOld='S5'
            #S5
            self.tasks=self.system.tasksSets[1]
            self.system.tasks[1].state='off'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='on'
            self.system.tasks[5].state='on'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='off'
            self.system.reconfiguration=False
            self.system.hambTemperature=35
            #40 para testes sem economia de energia
        elif self.system.step == 7:
            print("setting config 8")
            self.system.step+=1
            self.system.scenario=None
            self.system.scenarioOld='S2'
            #S2
            self.system.hambTemperature=30
            self.tasks=self.system.tasksSets[0]
            self.system.tasks[1].state='off'
            self.system.tasks[2].state='on'
            self.system.tasks[3].state='on'
            self.system.tasks[4].state='on'
            self.system.tasks[5].state='on'
            self.system.tasks[6].state='on'
            self.system.tasks[7].state='off' 
            self.system.reconfiguration=False
    def executeServer(self):
        #check if there is an CPU assined to the scheduler
        if len(self.cpuList)==0:
            raise ValueError("You need to add a CPU to run a job")
        else:
            #verify if there is a job in execution
            if self.executingServer != None:
                #analise if the job ended, if so assingne a new one for the server
                if self.executingServer.executingJob.executedTime >= self.executingServer.executingJob.executionTime:
                    self.jobFinish()                    
                elif self.executingServer.deadLine < self.system.timer.now():
                    self.cbsRecharge()
                #here the server budget is tested, if there is budget the server execute.                        
                elif self.executingServer.currentBudget > 0:
                    self.cpuList[0].run(self.executingServer.executingJob,self.system)
                    if self.executingServer.executingJob.status=="Ended":
                        self.jobFinish()
                    else:
                        self.executingServer.currentBudget-=1

                elif self.executingServer.currentBudget == 0:
                    self.cbsRecharge()
                else:
                    self.schedule()
            
    
    def schedule(self):

        if self.executingServer!=None:
            self.serverListReady.append(self.executingServer)
            self.executingServer=None  
        
        
        if len(self.serverListReady)==0:
             self.cpuList[0].run(None,self.system)
        else:
             if len(self.serverListReady) > 1:
                 self.serverListReady.sort()
             self.executingServer=self.serverListReady.pop(0)
        
    def checkingSystemStatus(self):
        for cpu in self.cpuList:
            
            if self.system.tempTol == 0:            
                if cpu.temperature >= cpu.temperatureMaxThreshold:
                    self.system.tempTol=400
                    print("event releted with temperature created")                    
                    print(cpu.temperature)
                    self.newEvent(4,self.system.tasks[0],self.system.timer.now,"temperature")                
            elif self.system.tempTol>0:
                self.system.tempTol-=1  

                
    
    def nextStep(self):

      
      self.checkingSystemStatus()
      
      if len(self.eventList)>0:
          event=self.eventList.pop(0)
      else:
          event=CBSScheduleEvent( 3, None, self.system.timer.now())
      
      if event.eventType == event.JOB_ARRIVE:
          self.jobArrival(event)
      elif  event.eventType ==  event.JOB_END:
          self.jobFinish(job)
      elif event.eventType == event.RECONFIGURATION_REQUEST:
          self.newConfiguration(event)
          return
      elif  event.eventType == event.RECONFIGURATION:
          self.reconfigure(event)
      elif  event.eventType == event.SERVER_BUDGET_DEPLETION:
          if self.executingServer==None:
              self.schedule()
          self.executeServer() 
      else: 
          raise ValueError('invaled type of server')
