from distutils.core import setup, Extension

module1 = Extension('cfsqpSolver1',
                    sources = ['cfsqpSolver1.c','cfsqp.c','qld.c'],
                    include_dirs = ['/home/riad/projects/simulador/simulator/src/tools/model1Variable/CFSQP/', '/usr/include/libxml2/'],
                    library_dirs = ['/home/riad/projects/simulador/simulator/src/tools/model1Variable/CFSQP/'],
                    libraries = ['xml2'],
                     )


setup (name = 'cfsqpSolver1',
       version = '1.0',
       description = 'This is a package',
       ext_modules = [module1])
