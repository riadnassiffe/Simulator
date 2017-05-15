/////////////////////////////python stuf
#ifndef Py_HEURISTICMODULE_H
#define Py_HEURISTICMODULE_H
#ifdef __cplusplus
extern "C" {
#endif

/* Header file for spammodule */

/* C API functions */
#define PyHeuristic_System_NUM 0
#define PyHeuristic_System_RETURN int
#define PyHeuristic_System_PROTO (const char *command)

/* Total number of C API pointers */
#define PyHeuristic_API_pointers 1


#ifdef HEURISTIC_MODULE
/* This section is used when compiling spammodule.c */

static PyHeuristic_System_RETURN PyHeuristic_System PyHeuristic_System_PROTO;

#else
/* This section is used in modules that use spammodule's API */

static void **PyHeuristic_API;

#define PyHeuristic_System \
 (*(PyHeuristic_System_RETURN (*)PyHeuristic_System_PROTO) PyHeuristic_API[PyHeuristic_System_NUM])

/* Return -1 on error, 0 on success.
 * PyCapsule_Import will set an exception if there's an error.
 */
static int
import_heusristic(void)
{
    PyHeuristic_API = (void **)PyCapsule_Import("heuristic._C_API", 0);
    return (PyHeuristic_API != NULL) ? 0 : -1;
}

#endif

#ifdef __cplusplus
}
#endif

#endif /* !defined(Py_HEURISTICMODULE_H) */


static PyObject *solver(PyObject *self, PyObject *args);


             




