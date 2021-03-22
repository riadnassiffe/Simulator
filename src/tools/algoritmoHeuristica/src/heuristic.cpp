#include <python2.7/Python.h>
#include <iostream>
#include "subgradiente.h"
#include "heuristic.h"
#include "Tripla.h"

/* Docstrings */
PyMODINIT_FUNC initHeuristicSolver2();

static PyMethodDef heuristicSolverMethods[] = {
    {"solver",  solver, METH_VARARGS,"Executes the heuristic."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC initheuristicSolver2()
{ 	

    PyObject *m;
    static void *PyHeuristic_API[PyHeuristic_API_pointers];
    PyObject *c_api_object;

    m = Py_InitModule("heuristicSolver2", heuristicSolverMethods);
    if (m == NULL)
        return;
    PyHeuristic_API[PyHeuristic_System_NUM] = (void *)PyHeuristic_System;

    /* Create a Capsule containing the API pointer array's address */
    c_api_object = PyCapsule_New((void *)PyHeuristic_API, "Heuristic._C_API", NULL);

    if (c_api_object != NULL)
        PyModule_AddObject(m, "_C_API", c_api_object);
}

static PyObject* solver(PyObject *self, PyObject *args) 
 {
	char *filePath;
	double Pmax;
	int ntarefas;
	int modos;
	int frequencias;
	double Fmax;
	
	fprintf(stderr,"starting heuristic algorithmic \n");

	if (! PyArg_ParseTuple( args, "iiiffs", &ntarefas, &modos,&frequencias,&Fmax,&Pmax,&filePath )) 
		return NULL;

	fprintf(stderr,"Path = %s \n",filePath);


	subgradiente* s = new subgradiente();
	
	result r;
	r =  s->calc(0.4,filePath,10.0, 0.2, Pmax,2,5, ntarefas,modos,frequencias,Fmax);

    
	PyObject *list = PyList_New(ntarefas*2+1);

	for (int t = 0; t < (ntarefas); t++) {
		PyObject *op = Py_BuildValue("i", r.C[t].k);
		if (PyList_SetItem(list,t,op) !=0) {
	    		fprintf(stderr,"Error in creating python list object\n");
	    		exit(EXIT_FAILURE);
		}
	}

	for (int t = 0; t < (ntarefas); t++) {
		PyObject *op = Py_BuildValue("i",r.C[t+ntarefas].j);
		if (PyList_SetItem(list,t+ntarefas,op) !=0) {
	    		fprintf(stderr,"Error in creating python list object\n");
	    		exit(EXIT_FAILURE);
		}
	}
	
	PyObject *op = PyFloat_FromDouble(r.cpuTime);
	if (PyList_SetItem(list,ntarefas*2,op) !=0) {
    		fprintf(stderr,"Error in creating python list object\n");
    		exit(EXIT_FAILURE);
	}

	return  list;
}
