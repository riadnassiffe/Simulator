from distutils.core import setup, Extension

module1 = Extension('cfsqpSolver2',
                    sources = ['RobotControl.c','cfsqp.c','qld.c'],
                    include_dirs = ['/home/riad/projects/simulador/simulator/src/tools/model2Variable/CFSQP-tese/', '/usr/include/libxml2/'],
                    library_dirs = ['/home/riad/projects/simulador/simulator/src/tools/model2Variable/CFSQP-tese/'],
                    libraries = ['xml2'],
                     )


setup (name = 'cfsqpSolver2',
       version = '1.0',
       description = 'This is a package',
       ext_modules = [module1])
