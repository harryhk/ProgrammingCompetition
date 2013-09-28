#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np


def mycmp(x , y ):
	if x[1] != y[1]:
		return y[1] - x[1]
	else:
		return cmp(x[0],y[0] )


fin = open(sys.argv[1], 'r')

nloop=int(fin.readline().strip())


for i in range(nloop):
	fin.readline()
	s=fin.readline().strip()
	
	d = {}
	for j in range(len(s)-1 ):
		t= s[j:j+2]
		if not d.has_key(t): d[t] = 0
		d[t] +=1
	
	di = d.items()

	#pdb.set_trace()	
	di.sort( cmp=mycmp )
	
	for i, j  in di[:3]:
		print( i, j   )

	print("---")
	





