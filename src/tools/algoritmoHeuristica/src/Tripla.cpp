/*
 * Par.cpp
 *
 *  Created on: 23/08/2010
 *      Author: riadnassiffe
 */

#include "Tripla.h"

void Tripla::setTripla(Task *t,unsigned short int k,unsigned short int j,float densidaRelativa, int i){

	Tripla::task = t;
	Tripla::k=k;
	Tripla::j=j;
	Tripla::deltaBeneficio=densidaRelativa;
	Tripla::taskNumber=i;
}


float Tripla::getBeneficio()
{
    return task->beneficio[k][j];
}

float Tripla::getDeltaBeneficio() {
	return deltaBeneficio;
}

float Tripla::getEnergia()
{
    return task->energia[k][j];
}

float Tripla::getUtilizacao()
{
    return task->recursoUtilizado[k][j];
}

