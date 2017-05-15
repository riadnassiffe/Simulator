from distutils.core import setup, Extension

module1 = Extension('heuristicSolver2',
                    sources = ['heuristic.cpp','task.cpp','subgradiente.cpp','Tripla.cpp'],
                    include_dirs = ['/home/riad/projects/simulador/simulator/src/tools/algoritmoHeuristica/'],
                    library_dirs = ['/home/riad/projects/simulador/simulator/src/tools/algoritmoHeuristica/'],
                    libraries = [],
                     )


setup (name = 'heuristicSolver2',
       version = '1.0',
       description = 'This is a package',
       ext_modules = [module1])
