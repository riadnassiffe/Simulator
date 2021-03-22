# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:39:18 2014

@author: riad
"""

class Time2(object):
    def __init__(self):
        self.time=0
    
    def increment(self):
        self.time+=1

class Time(object):
    
    def __init__(self):
        """
        There is no Arg: 
        This class represents the time for the system
        """
        self.time_ms=0
        self.time_s=0
        self.time_m=0
        self.time_h=0
        self.time_d=0
        
    def increment(increment):
        self.time_ms+=1
        if self.time_ms==1000:
            self.time_s+=1
            self.time_ms=0
         
        if self.time_s==60:
            self.time_m+=1
            self.time_s=0
         
        if self.time_m==60:
            self.time_h+=1
            self.time_m=0
         
        if self.time_h==24:
            self.time_d+=1
            self.time_h=0
            
    def diff(self,timeB):
        timeB.time_ms=self.time_ms-timeB.time_ms
        timeB.time_s=self.time_s-timeB.time_s
        timeB.time_m=self.time_m-timeB.time_m
        timeB.time_h=self.time_h-timeB.time_h
        timeB.time_d=self.time_d-timeB.time_d

        if timeB.time_ms<0:
            timeB.time_ms+=1000
            timeB.time_s-=1
        
        if timeB.time_s<0:
            timeB.time_s+=60
            timeB.time_m-=1
            
        if timeB.time_m<0:
            timeB.time_m+=60
            timeB.time_h-=1
            
        if timeB.time_h<0:
            timeB.time_h+=24
            timeB.time_d-=1
            
        return timeB
  
    

class Timer(object):
    """
   
    """
    def __init__(self):
        """
        Args:

        Methods:
        """
#        self.system = system
        self.time=Time2()

    def now(self):
        return self.time.time
    

    def start(self):
        """
        Start the timer.
        """
        self.running=True

    def increment(self):
        self.time.increment();

    def stop(self):
        """
        Stop the timer.
        """
        if self.running:
            sself.running = False

#    def equalTo(self,timeB):
#        """
#        Check is the timeB is equal to the time from Timer.
#        """
#        if self.time.time_ms==timeB.time_ms and self.time.time_s==timeB.time_s:
#            if self.time.time_m==timeB.time_m and self.time.time.time_h==timeB.time_h:
#                if self.time.time_d==timeB.time_d:
#                    return True
#        
#        return False
#        
#    def greaterThen(self,timeB):
#        """
#        Check is the timeB is greater then time from Timer.
#        """
#        stringTimeB= str(timeB.time_d)+str(timeB.time_h)+str(timeB.time_m)+str(timeB.time_s)+str(timeB.time_ms)  
#        stringTime=str(self.time.time_d)+str(self.time.time_h)+str(self.time.time_m)+str(self.time.time_s)+str(self.time.time_ms)
#        
#        if float(stringTimeB)<float(stringTime):
#            return True
#            
#        return False        
#        
#    def lessThen(self,timeB):
#        """
#        Check is the timeB is greater then time from Timer.
#        """
#        stringTimeB= str(timeB.time_d)+str(timeB.time_h)+str(timeB.time_m)+str(timeB.time_s)+str(timeB.time_ms)  
#        stringTime=str(self.time.time_d)+str(self.time.time_h)+str(self.time.time_m)+str(self.time.time_s)+str(self.time.time_ms)
#        
#        if float(stringTimeB)>float(stringTime):
#            return True
#            
#        return False   
#        
#    def addMs(ms):
#        while ms>0:
#            self.time.increment()
#            ms-=1