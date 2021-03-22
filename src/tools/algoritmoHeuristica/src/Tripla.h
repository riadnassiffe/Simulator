/*
 * Par.h
 *
 *  Created on: 23/08/2010
 *      Author: riadnassiffe
 */

#ifndef TRIPLA_H_
#define TRIPLA_H_

#include "task.h"

class Tripla {
public:
	unsigned short int k;
	unsigned short int j;
	Task *task;
	float deltaBeneficio;
        
    int taskNumber;
    void setTripla(Task *t,unsigned short int k,unsigned short int j,float densidadeRelatica, int i);
    float getUtilizacao() ;
    float getEnergia() ;
    float getDeltaBeneficio() ;
    float getBeneficio();
    
    Tripla &operator=(int x) {
       deltaBeneficio = x; return *this;
    }


};

#endif /* PAR_H_ */
