/*
 * subgradiente.cpp
 *
 *  Created on: 07/07/2010
 *      Author: riadnassiffe
 */

#include "subgradiente.h"

subgradiente::subgradiente() {

}


result subgradiente::calc(float BETA,char* path,float lambda, float mu, double Pmax,double MU, int TMAX,int ntarefas,int modos,int frequencias,int Fmax) {

	for (int i = 0; i < ntarefas; i++) {
		task[i].loadTask(i, modos, frequencias,path);
	}
	fprintf(stderr,"tasks loaded \n");
	fprintf(stderr,"tasks path ==%s \n",path);
	string line;
	string line2;
	string a;
	string b;
	b=path;
	a = b + "kmin.txt";
	ifstream myfile(a.c_str());
	a= b + "jmin.txt";
	ifstream myfile2(a.c_str());
	if (myfile.is_open()) {
		for (int i=0;i<(ntarefas);i++){
			getline(myfile, line);
			getline(myfile2, line2);
			mink[i]=atoi(line.c_str());
			minj[i]=atoi(line2.c_str());
			fprintf(stderr,"j -- %d",minj[i]);		
		}
		myfile.close();
		myfile2.close();
	} else
		cout << "Unable to open config min file";

	fprintf(stderr,"minimal configuration loaded, Fmax==%g \n",Fmax);
	struct timespec startCpuTime, stopCpuTime;
	clock_gettime(CLOCK_THREAD_CPUTIME_ID, &startCpuTime);

	int t;
	t = 0;
	int anteiro = 0;
	float fmax;
	float DeltaLbP;
	float DeltaLbU;
	int kmax;
	int jmax;
	float fFeas;
	float bFeas = 0;
	float v;

	float u, p;

	while (t < TMAX) {
		DeltaLbP = 0;
		DeltaLbU = 0;
		u = 0;
		p = 0;
		FLg = lambda * Pmax* BETA + mu * Umax;

		for (int i = 0; i < ntarefas; i++) {
			kmax = 0;
			jmax = 0;
			fmax = -INFINITY;
			for (int k = 0; k < modos; k++) {
				for (int j = 0+Fmax; j < frequencias; j++) {
					v = task[i].getBeneficio(k,j) - (lambda
							* task[i].getEnergia(k, j) + mu
							* task[i].getRecursoUtilizado(k, j));
					if (v > fmax) {
						fmax = v;
						kmax = k;
						jmax = j;
					}
				}
			}
			FLg = FLg + fmax;

			DeltaLbP = DeltaLbP - task[i].getEnergia(kmax, jmax);
			DeltaLbU = DeltaLbU - task[i].getRecursoUtilizado(kmax, jmax);

			u = u + task[i].getRecursoUtilizado(kmax, jmax);
			p = p + task[i].getEnergia(kmax, jmax);

			auxmink[i] = kmax;
			auxminj[i] = jmax;

		}

		DeltaLbP = DeltaLbP + Pmax * BETA;
		DeltaLbU = DeltaLbU + Umax;

		if (u <= Umax and p <= Pmax * BETA) {

			float tBen = 0;
			for (int tarefa = 0; tarefa < ntarefas; tarefa++) {
				tBen = tBen + task[tarefa].getBeneficio(auxmink[tarefa],auxminj[tarefa]);
			}
			if (tBen > bFeas) {
				fFeas = FLg;
				bFeas = tBen;
				memcpy(mink, auxmink, ntarefas * sizeof(int));
				memcpy(minj, auxminj, ntarefas * sizeof(int));
			}
		}

		lambda = max(lambda - pow(MU,t) * DeltaLbP, 0);
		mu = max(mu - pow(MU,t) * DeltaLbU, 0);

		if (t > TMEAN + 3 and media(t, anteiro) < STOPTOL) {
			break;
		}
		anteiro = FLg;
		t++;
	}

	// x_i^k,j= (k,j) ? 1:0

	int contOmega = 0;
	u = 0;
	for (int i = 0; i < ntarefas; i++) {
		//C={(i,1,1):S_i \in S}
		C[i].setTripla(&task[i],mink[i],minj[i],0,i);
		//u(C) = \sum_{S_i \in S} U_i^{1,1}
		u = u + task[i].getRecursoUtilizado(mink[i], minj[i]);
		//P(C) = \sum_{S_i \in S} P_i^{1,1}
		P = P + task[i].getEnergia(mink[i], minj[i]);
		//f(C) = \sum_{S_i \in S} A_i^{1,1}
		f = f + task[i].getBeneficio(mink[i],minj[i]);
		for (int k = 0; k < modos; k++) {
			for (int j = 0+Fmax; j < frequencias; j++) {
				if (!(k == mink[i] and minj[i] == j)) {
					omegaMenos[contOmega].setTripla(&task[i],k,j,
							densidadeRelativa(task[i].getBeneficio(mink[i],minj[i]),task[i].getBeneficio(k,j),task[i].getRecursoUtilizado(mink[i],minj[i]),task[i].getRecursoUtilizado(k,j),task[i].getEnergia(mink[i],minj[i]),task[i].getEnergia(k,j),mu,lambda),i);
					contOmega++;
				} 
			}
		}
	}
	sort(omegaMenos, omegaMenos + (ntarefas * ((modos * (frequencias-Fmax)) - 1)), regra);

	t=0;
	for (int t = 0; t < (ntarefas * ((modos * (frequencias-Fmax)) - 1)); t++) {
		if((C[omegaMenos[t].taskNumber].getBeneficio() <= omegaMenos[t].getBeneficio())){		
			if (((Pmax * BETA) - (P - C[omegaMenos[t].taskNumber].getEnergia())) >= omegaMenos[t].getEnergia()) {			
			if (((Umax - (u - C[omegaMenos[t].taskNumber].getUtilizacao())) >= omegaMenos[t].getUtilizacao())) {
			 
				u = u - C[omegaMenos[t].taskNumber].getUtilizacao() + omegaMenos[t].getUtilizacao();
				P = P - C[omegaMenos[t].taskNumber].getEnergia() + omegaMenos[t].getEnergia();
				f = f - C[omegaMenos[t].taskNumber].getBeneficio() + omegaMenos[t].getBeneficio();
				C[omegaMenos[t].taskNumber] = omegaMenos[t];
			
			}
			}
		}
	}



	clock_gettime(CLOCK_THREAD_CPUTIME_ID, &stopCpuTime);

	cpuTime = ((float) (stopCpuTime.tv_sec - startCpuTime.tv_sec)
			+ (stopCpuTime.tv_nsec - startCpuTime.tv_nsec)
			/ (float) 1000000000L);
	result r;
	for(int t;t<ntarefas;t++){
		r.C[t]=C[t];
		r.C[t+ntarefas]=C[t+ntarefas];
	}
	r.cpuTime=cpuTime;	
	return r;
}

float subgradiente::media(int atual, float anteiro) {
	return abs((FLg - anteiro) / FLg);
}



subgradiente::~subgradiente() {
	// TODO Auto-generated destructor stub
}
