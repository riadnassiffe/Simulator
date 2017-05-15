
#ifndef   PROBLEM_H_

struct problemData{
    int numTasks;
    double C0;
    double Pleak;
    double Ps;
    
    double B1;
    double B2;
    
    double b;
    double Fmax;
	
    double Pi[100];
    double Fmin[100];
    double Ci[100];
    double Cd[100];
    double T[100];
    double W[100];
    double W2[100];
};


#define PROBLEM_H_
#endif

	
