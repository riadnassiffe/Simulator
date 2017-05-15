# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 09:06:47 2014

@author: riad
"""
import xml.etree.ElementTree as ET
from problem import problem
import numpy
import os.path as os


def readXmlForPiceWiseModel(path):
    
    tree = ET.parse(path)
    root = tree.getroot()
    
    x=[]
    fmin=[]
    ci=[]
    cdMax=[]
    ind=0
    t=[]
    pi=[]
    w1=[]
    w2=[]
    cef=0
    c0=0
    vmax=0
    b1=0
    b2=0
    a=0
    b=0
    h=0
    hmax=0
    c1=0
    c2=0
    c3=0
    ftemp=0

    for child in root:
        if child.tag=='X':
          for i in child.findall('variable'):
              x.append(float(i.text)) 
        if child.tag=='Fmin':
          for i in child.findall('variable'):
              fmin.append(float(i.text)) 
        if child.tag=='CI':
          for i in child.findall('variable'):
              ci.append(float(i.text))
        if child.tag=='Cd':
          for i in child.findall('variable'):
              cdMax.append(float(i.text)) 
        if child.tag=='T':
          for i in child.findall('variable'):
              t.append(float(i.text))
        if child.tag=='Pi':
          for i in child.findall('variable'):
              pi.append(float(i.text)) 
        if child.tag=='W1':
          for i in child.findall('variable'):
              w1.append(float(i.text)) 
        if child.tag=='W2':
          for i in child.findall('variable'):
              w2.append(float(i.text))
        if child.tag=='Cef':
            cef=float(child.find('variable').text)
        if child.tag=='C0':
            c0=float(child.find('variable').text)
        if child.tag=='Vmax':
            vmax=float(child.find('variable').text)
        if child.tag=='B1':
            b1=float(child.find('variable').text)
        if child.tag=='B2':
            b2=float(child.find('variable').text)
        if child.tag=='a':
            a=float(child.find('variable').text)
        if child.tag=='b':
            b=float(child.find('variable').text)
        if child.tag=='H':
            h=float(child.find('variable').text)
        if child.tag=='Hmax':
            hmax=float(child.find('variable').text)                 
        if child.tag=='C1':
            c1=float(child.find('variable').text)
        if child.tag=='C2':
            c2=float(child.find('variable').text)
        if child.tag=='C3':
            c3=float(child.find('variable').text)
        if child.tag=='Ftemp':
            ftemp=float(child.find('variable').text)

    p=problem.ProblemWithFreq(len(x),cef,vmax,b1,b2,a,b,h,hmax,c1,c2,c3,ftemp,c0)        

   
    for i in range(len(x)):
        p.addTask(x[i],fmin[i],ci[i],cdMax[i],t[i],pi[i],w1[i],w2[i])
    
    return p
    
def readXmlForConvexModelWithFreq(path):
    

    tree = ET.parse(path)
    root = tree.getroot()
    
    x=[]
    fmin=[]
    ci=[]
    cdMax=[]
    t=[]
    pi=[]
    w1=[]
    w2=[]
    cef=0
    vmax=0
    b1=0
    b2=0
    a=0
    b=0
    h=0
    hmax=0
    c1=0
    c2=0
    c3=0
    ftemp=0

    for child in root:
        if child.tag=='X':
          for i in child.findall('variable'):
              x.append(float(i.text)) 
        if child.tag=='Fmin':
          for i in child.findall('variable'):
              fmin.append(float(i.text)) 
        if child.tag=='CI':
          for i in child.findall('variable'):
              ci.append(float(i.text))
        if child.tag=='CdMax':
          for i in child.findall('variable'):
              cdMax.append(float(i.text))        
        if child.tag=='T':
          for i in child.findall('variable'):
              t.append(float(i.text))
        if child.tag=='Pi':
          for i in child.findall('variable'):
              pi.append(float(i.text)) 
        if child.tag=='W':
          for i in child.findall('variable'):
              w1.append(float(i.text)) 
        if child.tag=='W2':
          for i in child.findall('variable'):
              w2.append(float(i.text))
        if child.tag=='Umax':
            b1=float(child.find('variable').text)
        if child.tag=='Pmax':
            b2=float(child.find('variable').text)
        if child.tag=='a':
            a=float(child.find('variable').text)
        if child.tag=='b':
            b=float(child.find('variable').text)
        if child.tag=='H':
            h=float(child.find('variable').text)
        if child.tag=='Hmax':
            hmax=float(child.find('variable').text)                 
        if child.tag=='Ftemp':
            ftemp=float(child.find('variable').text)

    p=problem.ProblemWithFreq(len(x)/2,cef,vmax,b1,b2,a,b,h,hmax,c1,c2,c3,ftemp)        

    for i in range(len(x)):
        p.addTask(x[i],fmin[i],ci[i],cdMax[i],t[i],pi[i],w1[i],w2[i])
    
    return p

def readXmlForConvexModelWithFreqBudget(path):
    

    tree = ET.parse(path)
    root = tree.getroot()
    
    x=[]
    fmin=[]
    ci=[]
    cdMax=[]
    cdMin=[]
    t=[]
    pi=[]
    w1=[]
    w2=[]
    cef=0
    vmax=0
    b1=0
    b2=0
    a=0
    b=0
    h=0
    hmax=0
    c1=0
    c2=0
    c3=0
    ftemp=0

    for child in root:
        if child.tag=='X':
          for i in child.findall('variable'):
              x.append(float(i.text)) 
        if child.tag=='Fmin':
          for i in child.findall('variable'):
              fmin.append(float(i.text)) 
        if child.tag=='CI':
          for i in child.findall('variable'):
              ci.append(float(i.text))
        if child.tag=='CdMax':
          for i in child.findall('variable'):
              cdMax.append(float(i.text))        
        if child.tag=='CdMin':
          for i in child.findall('variable'):
              cdMin.append(float(i.text))        
        if child.tag=='T':
          for i in child.findall('variable'):
              t.append(float(i.text))
        if child.tag=='Pi':
          for i in child.findall('variable'):
              pi.append(float(i.text)) 
        if child.tag=='W':
          for i in child.findall('variable'):
              w1.append(float(i.text)) 
        if child.tag=='W2':
          for i in child.findall('variable'):
              w2.append(float(i.text))
        if child.tag=='Cef':
            cef=float(child.find('variable').text)
        if child.tag=='Vmax':
            vmax=float(child.find('variable').text)
        if child.tag=='B1':
            b1=float(child.find('variable').text)
        if child.tag=='B2':
            b2=float(child.find('variable').text)
        if child.tag=='a':
            a=float(child.find('variable').text)
        if child.tag=='b':
            b=float(child.find('variable').text)
        if child.tag=='H':
            h=float(child.find('variable').text)
        if child.tag=='Hmax':
            hmax=float(child.find('variable').text)                 
        if child.tag=='C1':
            c1=float(child.find('variable').text)
        if child.tag=='C2':
            c2=float(child.find('variable').text)
        if child.tag=='C3':
            c3=float(child.find('variable').text)
        if child.tag=='Ftemp':
            ftemp=float(child.find('variable').text)

    p=problem.ProblemWithFreqBudget(len(x),b1,b2,a,b,h,hmax,ftemp)        

    for i in range(len(cdMax)):
        p.addTask(x[i+len(cdMax)],x[i],fmin[i],ci[i],cdMin[i],cdMax[i],t[i],pi[i],w1[i],w2[i])
    
    return p
