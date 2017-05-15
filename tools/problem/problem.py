# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 11:08:37 2014

@author: riad
"""
from  numpy import *

class ProblemWithFreq(object):
        
    def __init__(self,numTasks,cef,vmax,b1,b2,a,b,h,hmax,c1,c2,c3,ftemp,c0):    
        self.numTasks=numTasks       
        self.cef=cef
        self.vmax=vmax
        self.b1=b1
        self.b2=b2
        self.a=a
        self.b=b
        self.h=h
        self.hmax=hmax
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.ftemp=ftemp
        self.x=[]
        self.fmin=[]
        self.ci=[]
        self.cd=[]
        self.t=[]
        self.pi=[]
        self.w1=[]
        self.w2=[]
        self.beta0=[]
        self.beta1=[]
        self.beta2=[]
        self.beta3=[]
        self.beta4=[]
        self.beta5=[]
        self.c0=c0
        
        
    def addTask(self,x,fmin,ci,cd,t,pi,w1,w2):
        self.x.append(x) 
        self.fmin.append(fmin)
        self.ci.append(ci)
        self.cd.append(cd)
        self.t.append(t)
        self.pi.append(pi)
        self.w1.append(w1)
        self.w2.append(w2)
        self.beta0.append(self.cef*(self.vmax**2)*cd/t)
        self.beta1.append((self.c1+self.c2*exp(self.h*self.c3))*ci/t)
        self.beta2.append(pi*ci/t)
        self.beta3.append(self.cef*(self.vmax**2)*cd/t)
        self.beta4.append((self.c1+self.c2*exp(self.h*self.c3))*cd/t)
        self.beta5.append(pi*cd/t)
        
class ProblemWithFreqBudget(object):
        
    def __init__(self,numTasks,b1,b2,a,b,h,hmax,ftemp):    
        self.numTasks=numTasks       
        self.b1=b1
        self.b2=b2
        self.a=a
        self.b=b
        self.h=h
        self.hmax=hmax
        self.ftemp=ftemp
        self.x=[]
        self.fmin=[]
        self.ci=[]
        self.cdMax=[]
        self.cdMin=[]
        self.t=[]
        self.pi=[]
        self.w1=[]
        self.w2=[]
        self.f=[]
        
    def addTask(self,x,f,fmin,ci,cdMin,cdMax,t,pi,w1,w2):
        self.x.append(x)
        self.f.append(f)
        self.fmin.append(fmin)
        self.ci.append(ci)
        self.cdMax.append(cdMax)
        self.cdMin.append(cdMin)
        self.t.append(t)
        self.pi.append(pi)
        self.w1.append(w1)
        self.w2.append(w2)
   
