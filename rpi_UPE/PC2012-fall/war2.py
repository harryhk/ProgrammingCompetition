#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np


def war(l):

	dec=[ (i, j ) for i , j in enumerate(l)  ]
	dec.sort( key = lambda x: x[1]  )


	troop = np.ones_like(  np.array(l)  )
	N = len(l)
	
	for idx, j  in dec:
		if idx == 0 : 
			p =9999999
			n =l[idx+1]
		elif idx == N-1:
			p = l[idx-1]
			n =9999999
		else:
			p = l[idx-1]
			n = l[idx+1]
		if l[idx] > p : 
			if troop[idx] <= troop[idx-1] : troop[idx] = troop[idx-1] + 1
		if l[idx] > n : 
			if troop[idx] <= troop[idx+1] : troop[idx] = troop[idx+1] + 1
				
	return sum(troop)
		


fin = open(sys.argv[1], 'r')

nloop=int(fin.readline().strip())


for i in range(nloop):

	nn = int( fin.readline().strip()   )
	
	l=[]
	for i in range(nn):
		l.append( int( fin.readline().strip()  ) )

	print(war( l )  )



