#!/usr/bin/env python 

from __future__ import print_function 
import sys , pdb

def travel(l,time):
	diff = [  y-x for (x, y) in zip( l, l[1:]  )]
	diff.sort()

	jump = len(diff)

	for i in diff:
		time = time -i 
		if time <= 0:
			if time == 0 :
				jump=jump-1
			break
		else:
			jump = jump -1 
	
	return jump 
		




fin = open(sys.argv[1])

nloop = int( fin.readline().strip() ) 

for i in range(nloop) :
	(t, time) = [ int(j) for j in fin.readline().strip().split()   ]
	l=[  int (j) for j in fin.readline().strip().split()  ]
	print( travel(l, time) +1 )
