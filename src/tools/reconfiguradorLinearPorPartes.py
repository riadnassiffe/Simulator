# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:19:02 2015

@author: riad
"""
from readXmlModel import *
from cvxpy import *
import numpy

def solver(self,numberOfTasks,voltagesBreakPoint,path):
        n=len(voltagesBreakPoint)
    
        p=readXmlForPiceWiseModel('../s1/s50'+str(tarefa+1)+'.xml')
    
        pChapeu=numpy.zeros(shape=(numberOfTasks,n))
        uChapeu=numpy.zeros(shape=(numberOfTasks,n))
        objChapeu=numpy.zeros((numberOfTasks,n))
        uL=0.0
        lambdaKi= Variable(numberOfTasks,n)
   
        for i in range(len(voltagesBreakPoint)):
            voltagesBreakPoint[i]= voltagesBreakPoint[i]/1000
    

        potencia=[ 0.052,  0.072,  0.137,  0.197,  0.327,  0.582]    
    
        for i in range(numberOfTasks):
            for k in range(len(voltagesBreakPoint)):
                pChapeu[i][k]=(potencia[k]+p.pi[i]+0.578)*(p.cd[i]/(p.t[i]*voltagesBreakPoint[k])+p.ci[i]/p.t[i])
                uChapeu[i][k]=(((p.cd[i])/(p.t[i]*voltagesBreakPoint[k]))+p.ci[i]/p.t[i])
                objChapeu[i][k]=(p.w1[i]*p.cd[i]/p.t[i] + voltagesBreakPoint[k]*p.ci[i]*p.w2[i]/p.t[i])
        
        obj=0
        e=0
        u=0
        for i in range(numberOfTasks):
            for k in range(len(voltagesBreakPoint)):
                obj=obj + lambdaKi[i,k]*objChapeu[i][k]
                e=e+lambdaKi[i,k]*pChapeu[i][k]
                u=u+lambdaKi[i,k]*uChapeu[i][k]

        
        objective = Minimize(-obj)
            
        constraints=[]
        constraints.append(u<=1)   
        constraints.append(e<=p.b2)
        for i in range(numberOfTasks):
            for k in range(len(voltagesBreakPoint)):      
                constraints.append(lambdaKi[i,k]>=0.0)
                constraints.append(lambdaKi[i,k]<=1.0)
                constraints.append(sum_entries(lambdaKi[i,:])==1.0) 
        
        p.b2=p.b2*.87
        constraints.append(e<=p.b2)
   
        constraints.append(lambdaKi[0,0]*uChapeu[0][0]+lambdaKi[0,1]*uChapeu[0][1]+lambdaKi[0,2]*uChapeu[0][2]+lambdaKi[0,3]*uChapeu[0][3]+lambdaKi[0,4]*uChapeu[0][4]+lambdaKi[0,5]*uChapeu[0][5]+lambdaKi[1,0]*uChapeu[1][0]+lambdaKi[1,1]*uChapeu[1][1]+lambdaKi[1,2]*uChapeu[1][2]+lambdaKi[1,3]*uChapeu[1][3]+lambdaKi[1,4]*uChapeu[1][4]+lambdaKi[1,5]*uChapeu[1][5]+lambdaKi[2,0]*uChapeu[2][0]+lambdaKi[2,1]*uChapeu[2][1]+lambdaKi[2,2]*uChapeu[2][2]+lambdaKi[2,3]*uChapeu[2][3]+lambdaKi[2,4]*uChapeu[2][4]+lambdaKi[2,5]*uChapeu[2][5]+lambdaKi[3,0]*uChapeu[3][0]+lambdaKi[3,1]*uChapeu[3][1]+lambdaKi[3,2]*uChapeu[3][2]+lambdaKi[3,3]*uChapeu[3][3]+lambdaKi[3,4]*uChapeu[3][4]+lambdaKi[3,5]*uChapeu[3][5]+lambdaKi[4,0]*uChapeu[4][0]+lambdaKi[4,1]*uChapeu[4][1]+lambdaKi[4,2]*uChapeu[4][2]+lambdaKi[4,3]*uChapeu[4][3]+lambdaKi[4,4]*uChapeu[4][4]+lambdaKi[4,5]*uChapeu[4][5]+lambdaKi[5,0]*uChapeu[5][0]+lambdaKi[5,1]*uChapeu[5][1]+lambdaKi[5,2]*uChapeu[5][2]+lambdaKi[5,3]*uChapeu[5][3]+lambdaKi[5,4]*uChapeu[5][4]+lambdaKi[5,5]*uChapeu[5][5]+lambdaKi[6,0]*uChapeu[6][0]+lambdaKi[6,1]*uChapeu[6][1]+lambdaKi[6,2]*uChapeu[6][2]+lambdaKi[6,3]*uChapeu[6][3]+lambdaKi[6,4]*uChapeu[6][4]+lambdaKi[6,5]*uChapeu[6][5]+lambdaKi[7,0]*uChapeu[7][0]+lambdaKi[7,1]*uChapeu[7][1]+lambdaKi[7,2]*uChapeu[7][2]+lambdaKi[7,3]*uChapeu[7][3]+lambdaKi[7,4]*uChapeu[7][4]+lambdaKi[7,5]*uChapeu[7][5]+lambdaKi[8,0]*uChapeu[8][0]+lambdaKi[8,1]*uChapeu[8][1]+lambdaKi[8,2]*uChapeu[8][2]+lambdaKi[8,3]*uChapeu[8][3]+lambdaKi[8,4]*uChapeu[8][4]+lambdaKi[8,5]*uChapeu[8][5]+lambdaKi[9,0]*uChapeu[9][0]+lambdaKi[9,1]*uChapeu[9][1]+lambdaKi[9,2]*uChapeu[9][2]+lambdaKi[9,3]*uChapeu[9][3]+lambdaKi[9,4]*uChapeu[9][4]+lambdaKi[9,5]*uChapeu[9][5]+lambdaKi[10,0]*uChapeu[10][0]+lambdaKi[10,1]*uChapeu[10][1]+lambdaKi[10,2]*uChapeu[10][2]+lambdaKi[10,3]*uChapeu[10][3]+lambdaKi[10,4]*uChapeu[10][4]+lambdaKi[10,5]*uChapeu[10][5]+lambdaKi[11,0]*uChapeu[11][0]+lambdaKi[11,1]*uChapeu[11][1]+lambdaKi[11,2]*uChapeu[11][2]+lambdaKi[11,3]*uChapeu[11][3]+lambdaKi[11,4]*uChapeu[11][4]+lambdaKi[11,5]*uChapeu[11][5]+lambdaKi[12,0]*uChapeu[12][0]+lambdaKi[12,1]*uChapeu[12][1]+lambdaKi[12,2]*uChapeu[12][2]+lambdaKi[12,3]*uChapeu[12][3]+lambdaKi[12,4]*uChapeu[12][4]+lambdaKi[12,5]*uChapeu[12][5]+lambdaKi[13,0]*uChapeu[13][0]+lambdaKi[13,1]*uChapeu[13][1]+lambdaKi[13,2]*uChapeu[13][2]+lambdaKi[13,3]*uChapeu[13][3]+lambdaKi[13,4]*uChapeu[13][4]+lambdaKi[13,5]*uChapeu[13][5]+lambdaKi[14,0]*uChapeu[14][0]+lambdaKi[14,1]*uChapeu[14][1]+lambdaKi[14,2]*uChapeu[14][2]+lambdaKi[14,3]*uChapeu[14][3]+lambdaKi[14,4]*uChapeu[14][4]+lambdaKi[14,5]*uChapeu[14][5]+lambdaKi[15,0]*uChapeu[15][0]+lambdaKi[15,1]*uChapeu[15][1]+lambdaKi[15,2]*uChapeu[15][2]+lambdaKi[15,3]*uChapeu[15][3]+lambdaKi[15,4]*uChapeu[15][4]+lambdaKi[15,5]*uChapeu[15][5]+lambdaKi[16,0]*uChapeu[16][0]+lambdaKi[16,1]*uChapeu[16][1]+lambdaKi[16,2]*uChapeu[16][2]+lambdaKi[16,3]*uChapeu[16][3]+lambdaKi[16,4]*uChapeu[16][4]+lambdaKi[16,5]*uChapeu[16][5]+lambdaKi[17,0]*uChapeu[17][0]+lambdaKi[17,1]*uChapeu[17][1]+lambdaKi[17,2]*uChapeu[17][2]+lambdaKi[17,3]*uChapeu[17][3]+lambdaKi[17,4]*uChapeu[17][4]+lambdaKi[17,5]*uChapeu[17][5]+lambdaKi[18,0]*uChapeu[18][0]+lambdaKi[18,1]*uChapeu[18][1]+lambdaKi[18,2]*uChapeu[18][2]+lambdaKi[18,3]*uChapeu[18][3]+lambdaKi[18,4]*uChapeu[18][4]+lambdaKi[18,5]*uChapeu[18][5]+lambdaKi[19,0]*uChapeu[19][0]+lambdaKi[19,1]*uChapeu[19][1]+lambdaKi[19,2]*uChapeu[19][2]+lambdaKi[19,3]*uChapeu[19][3]+lambdaKi[19,4]*uChapeu[19][4]+lambdaKi[19,5]*uChapeu[19][5]+lambdaKi[20,0]*uChapeu[20][0]+lambdaKi[20,1]*uChapeu[20][1]+lambdaKi[20,2]*uChapeu[20][2]+lambdaKi[20,3]*uChapeu[20][3]+lambdaKi[20,4]*uChapeu[20][4]+lambdaKi[20,5]*uChapeu[20][5]+lambdaKi[21,0]*uChapeu[21][0]+lambdaKi[21,1]*uChapeu[21][1]+lambdaKi[21,2]*uChapeu[21][2]+lambdaKi[21,3]*uChapeu[21][3]+lambdaKi[21,4]*uChapeu[21][4]+lambdaKi[21,5]*uChapeu[21][5]+lambdaKi[22,0]*uChapeu[22][0]+lambdaKi[22,1]*uChapeu[22][1]+lambdaKi[22,2]*uChapeu[22][2]+lambdaKi[22,3]*uChapeu[22][3]+lambdaKi[22,4]*uChapeu[22][4]+lambdaKi[22,5]*uChapeu[22][5]+lambdaKi[23,0]*uChapeu[23][0]+lambdaKi[23,1]*uChapeu[23][1]+lambdaKi[23,2]*uChapeu[23][2]+lambdaKi[23,3]*uChapeu[23][3]+lambdaKi[23,4]*uChapeu[23][4]+lambdaKi[23,5]*uChapeu[23][5]+lambdaKi[24,0]*uChapeu[24][0]+lambdaKi[24,1]*uChapeu[24][1]+lambdaKi[24,2]*uChapeu[24][2]+lambdaKi[24,3]*uChapeu[24][3]+lambdaKi[24,4]*uChapeu[24][4]+lambdaKi[24,5]*uChapeu[24][5]+lambdaKi[25,0]*uChapeu[25][0]+lambdaKi[25,1]*uChapeu[25][1]+lambdaKi[25,2]*uChapeu[25][2]+lambdaKi[25,3]*uChapeu[25][3]+lambdaKi[25,4]*uChapeu[25][4]+lambdaKi[25,5]*uChapeu[25][5]+lambdaKi[26,0]*uChapeu[26][0]+lambdaKi[26,1]*uChapeu[26][1]+lambdaKi[26,2]*uChapeu[26][2]+lambdaKi[26,3]*uChapeu[26][3]+lambdaKi[26,4]*uChapeu[26][4]+lambdaKi[26,5]*uChapeu[26][5]+lambdaKi[27,0]*uChapeu[27][0]+lambdaKi[27,1]*uChapeu[27][1]+lambdaKi[27,2]*uChapeu[27][2]+lambdaKi[27,3]*uChapeu[27][3]+lambdaKi[27,4]*uChapeu[27][4]+lambdaKi[27,5]*uChapeu[27][5]+lambdaKi[28,0]*uChapeu[28][0]+lambdaKi[28,1]*uChapeu[28][1]+lambdaKi[28,2]*uChapeu[28][2]+lambdaKi[28,3]*uChapeu[28][3]+lambdaKi[28,4]*uChapeu[28][4]+lambdaKi[28,5]*uChapeu[28][5]+lambdaKi[29,0]*uChapeu[29][0]+lambdaKi[29,1]*uChapeu[29][1]+lambdaKi[29,2]*uChapeu[29][2]+lambdaKi[29,3]*uChapeu[29][3]+lambdaKi[29,4]*uChapeu[29][4]+lambdaKi[29,5]*uChapeu[29][5]+lambdaKi[30,0]*uChapeu[30][0]+lambdaKi[30,1]*uChapeu[30][1]+lambdaKi[30,2]*uChapeu[30][2]+lambdaKi[30,3]*uChapeu[30][3]+lambdaKi[30,4]*uChapeu[30][4]+lambdaKi[30,5]*uChapeu[30][5]+lambdaKi[31,0]*uChapeu[31][0]+lambdaKi[31,1]*uChapeu[31][1]+lambdaKi[31,2]*uChapeu[31][2]+lambdaKi[31,3]*uChapeu[31][3]+lambdaKi[31,4]*uChapeu[31][4]+lambdaKi[31,5]*uChapeu[31][5]+lambdaKi[32,0]*uChapeu[32][0]+lambdaKi[32,1]*uChapeu[32][1]+lambdaKi[32,2]*uChapeu[32][2]+lambdaKi[32,3]*uChapeu[32][3]+lambdaKi[32,4]*uChapeu[32][4]+lambdaKi[32,5]*uChapeu[32][5]+lambdaKi[33,0]*uChapeu[33][0]+lambdaKi[33,1]*uChapeu[33][1]+lambdaKi[33,2]*uChapeu[33][2]+lambdaKi[33,3]*uChapeu[33][3]+lambdaKi[33,4]*uChapeu[33][4]+lambdaKi[33,5]*uChapeu[33][5]+lambdaKi[34,0]*uChapeu[34][0]+lambdaKi[34,1]*uChapeu[34][1]+lambdaKi[34,2]*uChapeu[34][2]+lambdaKi[34,3]*uChapeu[34][3]+lambdaKi[34,4]*uChapeu[34][4]+lambdaKi[34,5]*uChapeu[34][5]+lambdaKi[35,0]*uChapeu[35][0]+lambdaKi[35,1]*uChapeu[35][1]+lambdaKi[35,2]*uChapeu[35][2]+lambdaKi[35,3]*uChapeu[35][3]+lambdaKi[35,4]*uChapeu[35][4]+lambdaKi[35,5]*uChapeu[35][5]+lambdaKi[36,0]*uChapeu[36][0]+lambdaKi[36,1]*uChapeu[36][1]+lambdaKi[36,2]*uChapeu[36][2]+lambdaKi[36,3]*uChapeu[36][3]+lambdaKi[36,4]*uChapeu[36][4]+lambdaKi[36,5]*uChapeu[36][5]+lambdaKi[37,0]*uChapeu[37][0]+lambdaKi[37,1]*uChapeu[37][1]+lambdaKi[37,2]*uChapeu[37][2]+lambdaKi[37,3]*uChapeu[37][3]+lambdaKi[37,4]*uChapeu[37][4]+lambdaKi[37,5]*uChapeu[37][5]+lambdaKi[38,0]*uChapeu[38][0]+lambdaKi[38,1]*uChapeu[38][1]+lambdaKi[38,2]*uChapeu[38][2]+lambdaKi[38,3]*uChapeu[38][3]+lambdaKi[38,4]*uChapeu[38][4]+lambdaKi[38,5]*uChapeu[38][5]+lambdaKi[39,0]*uChapeu[39][0]+lambdaKi[39,1]*uChapeu[39][1]+lambdaKi[39,2]*uChapeu[39][2]+lambdaKi[39,3]*uChapeu[39][3]+lambdaKi[39,4]*uChapeu[39][4]+lambdaKi[39,5]*uChapeu[39][5]+lambdaKi[40,0]*uChapeu[40][0]+lambdaKi[40,1]*uChapeu[40][1]+lambdaKi[40,2]*uChapeu[40][2]+lambdaKi[40,3]*uChapeu[40][3]+lambdaKi[40,4]*uChapeu[40][4]+lambdaKi[40,5]*uChapeu[40][5]+lambdaKi[41,0]*uChapeu[41][0]+lambdaKi[41,1]*uChapeu[41][1]+lambdaKi[41,2]*uChapeu[41][2]+lambdaKi[41,3]*uChapeu[41][3]+lambdaKi[41,4]*uChapeu[41][4]+lambdaKi[41,5]*uChapeu[41][4]+lambdaKi[42,0]*uChapeu[42][0]+lambdaKi[42,1]*uChapeu[42][1]+lambdaKi[42,2]*uChapeu[42][2]+lambdaKi[42,3]*uChapeu[42][3]+lambdaKi[42,4]*uChapeu[42][4]+lambdaKi[42,5]*uChapeu[42][5]+lambdaKi[43,0]*uChapeu[43][0]+lambdaKi[43,1]*uChapeu[43][1]+lambdaKi[43,2]*uChapeu[43][2]+lambdaKi[43,3]*uChapeu[43][3]+lambdaKi[43,4]*uChapeu[43][4]+lambdaKi[43,5]*uChapeu[43][5]+lambdaKi[44,0]*uChapeu[44][0]+lambdaKi[44,1]*uChapeu[44][1]+lambdaKi[44,2]*uChapeu[44][2]+lambdaKi[44,3]*uChapeu[44][3]+lambdaKi[44,4]*uChapeu[44][4]+lambdaKi[44,5]*uChapeu[44][5]+lambdaKi[45,0]*uChapeu[45][0]+lambdaKi[45,1]*uChapeu[45][1]+lambdaKi[45,2]*uChapeu[45][2]+lambdaKi[45,3]*uChapeu[45][3]+lambdaKi[45,4]*uChapeu[45][4]+lambdaKi[45,5]*uChapeu[45][5]+lambdaKi[46,0]*uChapeu[46][0]+lambdaKi[46,1]*uChapeu[46][1]+lambdaKi[46,2]*uChapeu[46][2]+lambdaKi[46,3]*uChapeu[46][3]+lambdaKi[46,4]*uChapeu[46][4]+lambdaKi[46,5]*uChapeu[46][5]+lambdaKi[47,0]*uChapeu[47][0]+lambdaKi[47,1]*uChapeu[47][1]+lambdaKi[47,2]*uChapeu[47][2]+lambdaKi[47,3]*uChapeu[47][3]+lambdaKi[47,4]*uChapeu[47][4]+lambdaKi[47,5]*uChapeu[47][5]+lambdaKi[48,0]*uChapeu[48][0]+lambdaKi[48,1]*uChapeu[48][1]+lambdaKi[48,2]*uChapeu[48][2]+lambdaKi[48,3]*uChapeu[48][3]+lambdaKi[48,4]*uChapeu[48][4]+lambdaKi[48,5]*uChapeu[48][5]+lambdaKi[49,0]*uChapeu[49][0]+lambdaKi[49,1]*uChapeu[49][1]+lambdaKi[49,2]*uChapeu[49][2]+lambdaKi[49,3]*uChapeu[49][3]+lambdaKi[49,4]*uChapeu[49][4]+lambdaKi[49,5]*uChapeu[49][5]<=1.0)
    
    
    
        prob = Problem(objective, constraints)
        #r1= prob.solve(solver=SCS, verbose=True)
        # The optimal objective is returned by prob.solve().

        result = prob.solve(solver=ECOS,verbose=True)
        print "p("+str(tarefa+1)+") ="+ str(prob.value) 
    

        for i in range(50):
            f=0
            for k in range(len(voltagesBreakPoint)):
                f=f+(lambdaKi.value[i,k]*voltagesBreakPoint[k])
                print "f("+str(tarefa+1)+") ="+ str(f)
                
        result={'executionTime':prob.executionTime,}
        return result