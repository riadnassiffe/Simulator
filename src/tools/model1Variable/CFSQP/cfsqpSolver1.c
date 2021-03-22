/*
 * RobotControl.c
 *
 *  Created on: May 21, 2012
 *      Author: Ríad Mattos Nassiffe
 *     Características dos problema:
 *     Contínuo
 *     Todas restrições e a função objetivo são convexas
 *     somente a frequência X pode ser ajustada
 */
#include <python2.7/Python.h>
#include "cfsqpSolver1.h"

#define DEBUG_1

initcfsqpSolver1(void);
              
/* Docstrings */
static char module_docstring[] =
    "solving an optimization problem";
static char cfsqpSolver_docstring[] =
        "Calculate the min some data given a model.";

static PyMethodDef cfsqpSolverMethods[] = {
    {"solver",  solver, METH_VARARGS,
     "Executes cfspq."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static PyObject *cfsqpSolverError;


initcfsqpSolver1(void)
{ 	
    PyObject *m;
    fprintf(stderr,"loading py mode");
    //m = PyModule_Create(&cfsqpSolvermodule); /*Python3.0*/
    m = Py_InitModule("cfsqpSolver1", cfsqpSolverMethods);
    if (m == NULL)
        return NULL;

    cfsqpSolverError = PyErr_NewException("csfqpSolver.error", NULL, NULL);
    Py_INCREF(cfsqpSolverError);
    PyModule_AddObject(m, "error", cfsqpSolverError);
    return m;
}

static PyObject *solver(PyObject *self, PyObject *args) { 

	int nparam, nf, nineq, neq, mode, iprint, miter, neqn, nineqn, ncsrl, ncsrn,
			nfsr, mesh_pts[1], inform;
	double bigbnd, eps, epsneq, udelta;
	double *x, *f, *g, *lambda;
	static double *bl = NULL;
	static double *bu = NULL;
	double cpuTime;
	void *cd;
	char *filePath;
	float Fmax;
        float power,Pleak; 

   	int numTasks;

	int i = 0;

 	fprintf(stderr,"starting cfsqpSolver \n");

	if (! PyArg_ParseTuple( args, "iiifffs", &iprint, &miter,&numTasks, &Fmax,&power,&Pleak, &filePath )) 
		return NULL;

	p = readFile(filePath);
	p->numTasks = numTasks;
	p->Fmax=Fmax;
   	p->B2=power;
   	p->Pleak=Pleak;
	
	fprintf(stderr,"Umax %f \n",p->B1);	

	fprintf(stderr,"Fmax %f \n",Fmax);

	nparam =numTasks ; /* number of free variables  */
	nf = 1; /* number of objective functions */
	nfsr = 0; /* # sequence related objectives */

	nineqn = 2; /* # of nonlinear inequalities   */
	nineq = 2; /* total number of nonlinear inequalities */

	neqn = 0; /* # of nonlinear equality constraints */
	neq = 0; /* total number of nonlinear equality constraints */

	ncsrl = 0; /* number of sets of linear sequentially related
	 constraints */
	ncsrn = 0; /* number of sets of nonlinear sequentially related
	 constraints */
	mesh_pts[0] = 0; /* pointer to an array of integers of dimension
	 max{1,nfsr + ncsrn + ncsrl } */

	mode = 100;/* mode= CBA.
	 A - probelm to be solved
	 B - algorithm
	 C - line search */

	//iprint = 3; /* 0 - no informatio is displayed
	// 1 - objective and constraint */

	//miter = 500;/* maximum number of iterations */

	bigbnd = 1.e10; /* plays the role of infinity */

	eps = 1e-13; /* epsilon */

	epsneq = eps; /* maximum violation of nonlinear equality
	 constraints */
	udelta = 0.e0; /* perturbation for approximating gradients */

	/* lower bound vector */
	bl = (double *) calloc(nparam, sizeof(double));

	/* upper bound vector */
	bu = (double *) calloc(nparam, sizeof(double));

	/* initial solution */
	x = (double *) calloc(nparam, sizeof(double));

	/* vector for objective functions */
	f = (double *) calloc(nf, sizeof(double));

	/* value of constraints. */
	g = (double *) calloc(nineq + neq, sizeof(double));

	/* lagrange multipliers */
	lambda = (double *) calloc(nineq + neq + nf + nparam, sizeof(double));
	
	for (i = 0; i < nparam; i++) {
		bl[i] = p->Fmin[i];
		bu[i] = p->Fmax;
		x[i]=1.0;
	}
	
    	struct timespec startCpuTime, stopCpuTime;
	clock_gettime(CLOCK_THREAD_CPUTIME_ID, &startCpuTime);

	cfsqp(nparam, nf, nfsr, nineqn, nineq, neqn, neq, ncsrl, ncsrn, mesh_pts,
			mode, iprint, miter, &inform, bigbnd, eps, epsneq, udelta, bl, bu,
			x, f, g, lambda, objFunc, cntrFunc, grobFunc, /* grobFunc | grobfd*/
			grcnFunc, /* grcnFunc | grcnfd*/
			cd);

	clock_gettime(CLOCK_THREAD_CPUTIME_ID, &stopCpuTime);

	cpuTime =
			((float) (stopCpuTime.tv_sec - startCpuTime.tv_sec)
					+ (stopCpuTime.tv_nsec - startCpuTime.tv_nsec)
							/ (float) 1000000000L);


	PyObject *list = PyList_New(numTasks+1);

	for(i=0;i<numTasks;i++){
	PyObject *op = PyFloat_FromDouble((double)x[i]);
		if (PyList_SetItem(list,i,op) !=0) {
		    fprintf(stderr,"Error in creating python list object\n");
		    exit(EXIT_FAILURE);
		}
	}


	PyObject *op = PyFloat_FromDouble((double)cpuTime);
	if (PyList_SetItem(list,i,op) !=0) {
		fprintf(stderr,"Error in creating python list object\n");
		 exit(EXIT_FAILURE);
	}

	free(p);
	free(bl);
	free(bu);
	free(x);
	free(f);
	free(g);
	free(lambda);

	return list;
}

/*  computes the objective function
 -------------------------------------------------------------------------*/
void objFunc(int nparam, int j, double *x, double *fj, void *cd) {
	int i;
	*fj = 0;
	for (i = 0; i < nparam; i++) {
		*fj = *fj + (-p->Cd[i]*p->W2[i]/ p->T[i] - p->Ci[i]*p->W[i]*x[i]/p->T[i]);
	}
	return;
}

/* computes gradient for the objective function
 -------------------------------------------------------------------------*/
void grobFunc(int nparam, int j, double *x, double *gradfj,
		void (*dummy)(int, int, double *, double *, void *), void *cd) {
	int i;
    *gradfj=0;
    for (i = 0; i < nparam; i++) 
	    *gradfj += -p->Ci[i]*p->W[i]/p->T[i];
	return;
}

/* computes constraints
 -------------------------------------------------------------------------*/
void cntrFunc(int nparam, int j, double *x, double *gj, void *cd) {
	int i;
	switch (j) {
	case 1:
		*gj = 0;
		for (i = 0; i < nparam; i++) {
			*gj = *gj + (p->Cd[i]/(x[i] * p->T[i]) + p->Ci[i] / p->T[i]);

		}
		*gj = *gj - p->B1;
		break;
	case 2:
		*gj = 0;
		for (i = 0; i < nparam; i++) {
			*gj = *gj
				+ ((p->C0 * x[i] * x[i] * x[i] + p->Pi[i] +p->Pleak )
				* ((p->Cd[i] / (x[i] * p->T[i])) + (p->Ci[i] / p->T[i])));

		}
		*gj = *gj - p->B2;
		break;
    	default:
		printf("j is different of 1 or 2");
		break;
	}
	return;

}

/* computes gradient for constraints
 -------------------------------------------------------------------------*/
void grcnFunc(int nparam, int j, double *x, double *gradgj,
		void (*dummy)(int, int, double *, double *, void *), void *cd) {

	int i;
	switch (j) {
	case 1:
		for (i = 0; i < nparam; i++) {
			gradgj[i] = -(p->Cd[i]/(x[i]*x[i]*p->T[i]));
		}
		break;
	case 2:
		for (i = 0; i < nparam; i++) {
			gradgj[i] = 3 * p->C0 * pow(x[i], 2) * p->Ci[i] / p->T[i]
				  + 2 * p->C0 * x[i] * p->Cd[i] / p->T[i]
                    		  - p->Cd[i] * p->Pi[i]/ (p->T[i] * pow(x[i], 2));
		}
		break;
   	default:
		printf("j is different of 1 or 2");
		break;
	}
	return;
}

////////////////////////////////////////////////////////////////////////////////////

struct problemData *readFile(const char *fileName) {
	struct problemData *p;
	xmlDocPtr doc;
	xmlNodePtr nodeLevel0;
	xmlNodePtr nodeLevel1;
	xmlNodePtr nodeLevel2;
	xmlChar *name;


	doc = xmlParseFile(fileName);
	nodeLevel0 = doc->children;
	//alocando dados dentro da estrutura para guardar as informações das tarefas
	name=xmlGetProp(nodeLevel0,(const xmlChar *) "tasks");
	int numTasks=atoi(name);

	p = malloc(sizeof(struct problemData));
	p->numTasks=numTasks;


	int i;
	for (nodeLevel1 = nodeLevel0->children; nodeLevel1 != NULL; nodeLevel1 = nodeLevel1->next) {
		if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "B1"))) {
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->B1=xmlXPathCastStringToNumber(name);
				}
			}
		} else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "B2"))) {
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->B2=xmlXPathCastStringToNumber(name);
				}
			}
		} else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Cd"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Cd[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "CI"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Ci[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Fmin"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Fmin[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		} else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "T"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->T[i]=xmlXPathCastStringToNumber(name);

					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Pi"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Pi[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "W1"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->W[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "b"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->b=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "C0"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->C0=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "W2"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->W2[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }										

	}
	return p;

}
