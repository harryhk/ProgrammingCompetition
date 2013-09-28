#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np


fin = open(sys.argv[1], 'r')

nloop=int(fin.readline().strip())


for i in range(nloop):
	fin.readline()
	s=fin.readline().strip()
	
	d = {}
	for j in range(len(s)-1 ):
		k = j+1
		t= s[j]+s[k]
		if d.has_key(t):
			d[t] = d[t]+1
		else:
			d[t]=1
	
	
	
	d_rev={}

	for i in d:
		if d_rev.has_key( d[i] ):
			d_rev[d[i]].append(i)
		else:
			d_rev[d[i] ]=[i]
	
	re=[]
	for i in d_rev:
		re.append( i )
		d_rev[i].sort()
	
	

	re.sort( lambda x,y: -cmp( x, y  )   )

	n=3
	for i in re:
		if len( d_rev[i] ) <= n :
			for j in d_rev[i]:
				print( j, i  )
				n = n-1
		else:
			for j in range(n) :
				print( d_rev[i][j], i  )
			break
				

	print("---")
	
	
	
	#pdb.set_trace()	






