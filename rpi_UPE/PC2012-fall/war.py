#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np


def war(l):
	
	d= np.array(l)

	troop = np.zeros_like(d)
	troop[0]=1
	#pdb.set_trace()
	for i in range(1,  len( l )):
		j = i-1
		if d[i] <  d[j]:
			if troop[j] > 1:
				troop[i]=1
			else:
				troop[i]=1
				while (d[j] - d[j+1]) * (troop[j] - troop[j+1]) < 0 :
					troop[j] = troop[j+1]+1
					j = j-1
					
					

		
		
		
		
		elif d[i]== d[j]:
			troop[i] = 1
		else:
			troop[i] = troop[j]+1

	# test 
	for i in range( len(d) -1):
		if (d[i] -d[i+1] )* ( troop[i] - troop[i+1] ) < 0 or troop[i] <=0 or troop[i+1]<=0:
			print(i )
			print("fail")
			break
	np.savetxt("troop.txt", troop, fmt="%5d")
	np.savetxt("d.txt", d, fmt = "%15d")

	#pdb.set_trace()
	return sum(troop)
		


fin = open(sys.argv[1], 'r')

nloop=int(fin.readline().strip())


for i in range(nloop):

	nn = int( fin.readline().strip()   )
	
	l=[]
	for i in range(nn):
		l.append( int( fin.readline().strip()  ) )

	print(war( l )  )



