#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np


fin = open(sys.argv[1], 'r')

nloop=int(fin.readline().strip())


for i_nloop in range(nloop):
	
	fin.readline()
	(sx, sy, ex, ey) = [ int(i) for i in fin.readline().strip().split()	]
	sizex = abs(sx-ex)+1
	sizey = abs(sy-ey ) +1

	grid=  np.ones( [ sizex, sizey ] , dtype = int )
	blockx = np.zeros( [ sizex -1  ,  sizey ] )
	blocky = np.zeros( [ sizex,       sizey -1 ]  )

	nb = int(fin.readline().strip()  )

	gridx = min( sx, ex )
	gridy = min( sy, ey )

	for i_nb in range(nb):
		( ux, uy, vx, vy  ) = [ int(i) for i in fin.readline().strip().split() ]
		ux -= gridx 
		uy -= gridy
		vx -= gridx 
		vy -= gridy 

		if ux * uy * vx * vy < 0 :
			continue 
		else:
			if uy == vy :
				if dirx >=0:
					blockx[ min(ux, vx)  , uy ] = 1 
				else:
					blockx[ max(ux, vx)  , vy ] = 1
			if ux == vx :
				if diry >= 0:
					blocky[ ux, min( uy, vy  ) ]
				else:
					blocky[ ux,  max(uy, vy  )  ]
	
	dirx = 1 
	diry = 1 
	if sx > ex :
		dirx = -1 
	if sy > ey :
		diry = -1 
	
	xran = range(sx, ex+dirx, dirx )

	yran = range(sy, ey+diry, diry  )
	
	for ix in xran:
		for iy in yran:
			
			

		






	
	print(maxsub( l  )   )



