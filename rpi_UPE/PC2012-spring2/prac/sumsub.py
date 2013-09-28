#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np

def maxsub(l):
	m = np.zeros_like(l)
	m[0] = l[0]
	for i in range(1, len(l)  ):
		temp = []
		for j in range(i):
			if l[j] > l[i]:
				temp.append(m[j]+ l[i])
		if len(temp) == 0 :
			m[i] = l[i]
		else:
			m[i]=max(temp) 
	
	return max(m)
		

fin = open(sys.argv[1], 'r')

nloop=int(fin.readline().strip())

print(nloop) 

for i in range(nloop):
	fin.readline()
	l= np.array( [ int(j) for j in fin.readline().strip().split()] ) 
	print(maxsub( l  )   )



