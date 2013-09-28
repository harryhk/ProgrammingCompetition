#!/usr/bin/env python 

from __future__ import print_function 
import sys , pdb

		
class Edge:
	def __init__(self, u, v, w):
		self.u = u 
		self.v = v 
		self.w = w 


class Graph:
	def __init__(self):
		self.edges= []
		self.vertex = set()

	def add_edge(self, u, v, w ):
		self.edges.append( Edge(u,v,w) )
		self.vertex.add(u)
		self.vertex.add(v)
	
	def min_span(self ):
		tree=set()

		self.edges.sort( lambda x, y : cmp( x.w, y.w  )  )
		
		t = self.edges[0]
		tree.add( t.u  )
		tree.add( t.v  )

		tot=t.w

		while len(tree) < len(self.vertex):
			
				
			for i in  self.edges  :
				if (i.u in tree and i.v not in tree) or ( i.v in tree and i.u not in tree ):
					tot= tot+ i.w
					if i.v not in tree:
						tree.add(i.v)
					if i.u not in tree:
						tree.add(i.u)

					break


		return tot 

fin = open(sys.argv[1])

nloop = int( fin.readline().strip() ) 

for i in range(nloop) :
	
	nnloop = int( fin.readline().strip() )
	g = Graph()
	for j in range(nnloop):
		(u, v , w  ) = fin.readline().strip().split()
		g.add_edge( u , v, int(w)  )
	
	print( g.min_span()) 
	
