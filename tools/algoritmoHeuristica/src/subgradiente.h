/*
 * subgradiente.h
 *
 *  Created on: 07/07/2010
 *      Author: riadnassiffe
 */

#ifndef SUBGRADIENTE_H_
#define SUBGRADIENTE_H_
#include "task.h"
#include "defines.h"
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include "Tripla.h"
#include <cmath>
#include <algorithm>
#include <string.h>
#include <python2.7/Python.h>
#include <vector>


#define max(x,y) x>y? x:y;
#define densidadeRelativa(b1,b2,u1,u2,p1,p2,lu,lp)  (b2-b1)/((u2-u1)*lu + (p2-p1)*lp) //((rand()%1000)*1.0)/1000
using namespace std;

class RegraDeOrdenacao {
public:
	bool operator() (Tripla i,Tripla j) {
		return (i.getDeltaBeneficio() >= j.getDeltaBeneficio());
	}
};

struct result { 
  double cpuTime;
  Tripla C[20];
};

class subgradiente {
public:
	Task task[20];
	float lambda;
	float mu ;

	float FLg;
	float cpuTime;

	Tripla C[20];
	Tripla nextTask[20];
	Tripla omegaMenos[(20*3*6)-20];
	float u;
	float P;
	float f;
	
	RegraDeOrdenacao regra;
	unsigned short int mink [20];
	unsigned short int minj [20];
	unsigned short int auxmink [20];
	unsigned short int auxminj [20];


	subgradiente();
	result calc(float BETA,char* path,float lambda, float mu, double Pmax,double MU, int TMAX,int ntarefas,int modos,int frequencias,int Fmax);
	float media (int atual, float anteiro);
	virtual ~subgradiente();
	void loadInitialSet();
};


#endif
