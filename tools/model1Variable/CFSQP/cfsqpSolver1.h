	/*
 * RobotControl.h
 *  Created on: May 21, 2012
 *      Author: Ríad Mattos Nassiffe
 *     Problema a implementar:
 *
 *     F(x) = min(1-\sum_{S_i \in \mathcal{S}} \Bigl( \frac{Q^{D}_i}{T_{i}x_i}  +  \sum_{S_i \in \mathcal{S}} \frac{Q^{I}_i}{T_{i}} \Bigl))
 *     s.t.
 *     \sum_{S_i \in \mathcal{S}} \frac{Q^{D}_i}{T_{i}x_i}  \leq 1 -  \sum_{S_i \in \mathcal{S}} \frac{Q^{I}_i}{T_{i}}
 *     \sum_{S_i\in \mathcal{S}}\Bigl( C_{ef} V_{max}^2 x_i^2 F_{max} \frac{Q^{I}_i}{T_{i}} +  C_{ef} V_{max}^2 x_i^3 F_{max}\frac{Q^{D}_i}{T_{i}} + P^{I}_{i} \frac{Q^{I}_i}{T_{i}x_{i}} + P^{I}_{i} \frac{Q^{D}_i}{T_{i}}\Bigl)  \leq  \frac{E^\star}{T_{est}} - P^S
 *
 *     Características dos problema:
 *     Contínuo
 *     Todas restrições e a função objetivo são convexas
 *     somente a frequência X pode ser ajustada
 */



#ifndef cfsqpSolver1
#ifndef PyMODINIT_FUNC  /* declarations for DLL import/export */


#define PyMODINIT_FUNC void

#define PyCfsqp_Solver_NUM 0
#define PyCfsqp_Solver_RETURN int
#define PyCfsqp_SolverPROTO (const char *command)

/* Total number of C API pointers */
#define PyCfsqp_API_pointers 1


#ifdef CFSQP_MODULE
/* This section is used when compiling spammodule.c */

static PyCfsqp_Solver_RETURN PyCfsqp_Solver PyCfsqp_Solver_PROTO;

#else
/* This section is used in modules that use spammodule's API */

static void **PyCfsqp_API;

#define PyCfsqp_Solver  (*(PyCfsqp_Solver_RETURN (*)PyCfsqp_Solver_PROTO) PyCfsqp_API[PyCfsqp_Solver_NUM])

/* Return -1 and set exception on error, 0 on success. */
static int
import_cfsqpSolver1(void)
{
            PyObject *module       = PyImport_ImportModule("cfsqp1");

            if (module != NULL) {
            PyObject *c_api_object = PyObject_GetAttrString(module, "_C_API");
                    if (c_api_object == NULL)
                                        return -1;
                            if (PyCObject_Check(c_api_object))
                                                PySpam_API = (void **)PyCObject_AsVoidPtr(c_api_object);
                                    Py_DECREF(c_api_object);
                                        }
                return 0;
}

#endif



#endif


/////////////////////////

#include <stdlib.h>
#include <string.h>


#include <libxml/xmlreader.h>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <libxml/encoding.h>
#include <libxml/xpath.h>


struct problemData *readFile(const char *fileName);
////////////////////////

/* C includes
------------------------------------------------------------------------*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include "problem.h"

#include <time.h>//real time api to get cpu time
/* CFSQP include
------------------------------------------------------------------------*/

#include "cfsqpusr.h"

/* functions prototype
------------------------------------------------------------------------*/

struct problemData *p;

static PyObject * solver(PyObject *self, PyObject *args);

/*
 *Computes Objective function
 */
void objFunc(int nparam, int j, double *x, double *fj, void *cd);
/*
 *Computes gradient for the objective function
 */
void grobFunc(int nparam, int j, double *x, double *gradfj,
	    void (* dummy)(int,int,double *,double *,void *), void *cd);
/*
 * Computes constraints
 */
void cntrFunc(int nparam, int j, double *x, double *gj, void *cd);
/*
 * Computes gradient for constraints
 */
void grcnFunc(int nparam, int j, double *x, double *gradgj,
	    void (* dummy)(int,int,double *,double *,void *),
	    void *cd);

#endif
