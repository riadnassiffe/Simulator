# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from simulador.core.task import *
import numpy
import os.path as os

def readXmlForPiceWiseModel(path):
    
    tree = ET.parse(path)
    root = tree.getroot()
    
    x=[]
    fmin=[]
    ci=[]
    cd=[]
    t=[]
    pi=[]
    w1=[]
    w2=[]
 
    for child in root:
        if child.tag=='X':
          for i in child.findall('variable'):
              x.append(float(i.text)) 
        if child.tag=='CI':
          for i in child.findall('variable'):
              ci.append(float(i.text))
        if child.tag=='Cd':
          for i in child.findall('variable'):
              cd.append(float(i.text)) 
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
    i=0
    taskSet=[]
    for confX in x:
        taskSet.append(Task(str(i),cd[i],ci[i],t[i],t[i],pi[i],1,'hard',0,0,0))
    
    return taskSet
    
def readXmlForConvexModelWithFreq(path):
    

    tree = ET.parse(path)
    root = tree.getroot()
    
    x=[]
    ci=[]
    cd=[]
    t=[]
    pi=[]
    w1=[]
    w2=[]
    name=[]

    for child in root:
        if child.tag=='X':
          for i in child.findall('variable'):
              x.append(float(i.text)) 
        if child.tag=='CI':
          for i in child.findall('variable'):
              ci.append(float(i.text))
        if child.tag=='Cd':
          for i in child.findall('variable'):
              cd.append(float(i.text))        
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
        if child.tag=='taskName':
          for i in child.findall('variable'):
              name.append(str(i.text))

    i=0
    taskSet=[]
    for confX in x:
        taskSet.append(Task(name[i],cd[i],ci[i],t[i],t[i],pi[i],confX,'hard',0,0,0))
        i+=1
    
    return taskSet

def readXmlForConvexModelWithFreqBudget(path):
    

    tree = ET.parse(path)
    root = tree.getroot()
    
    x=[]
    ci=[]
    cdMax=[]
    cdMin=[]
    t=[]
    pi=[]
    w1=[]
    w2=[]

    for child in root:
        if child.tag=='X':
          for i in child.findall('variable'):
              x.append(float(i.text)) 
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

    i=0
    taskSet=[]
    for confX in x:
        taskSet.append(Task(str(i),cdMax[i],ci[i],t[i],t[i],pi[i],1,'hard',0,cdMax[i],cdMin[i]))
    
    return taskSet
