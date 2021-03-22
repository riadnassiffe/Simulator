#/usr/bin/python2

import cfsqpSolver2
import math

result = cfsqpSolver2.solver(1,200,10,0.98,10,0.2,'./s101.xml')

for i in result:
	item=math.exp(i)
	print(item)
