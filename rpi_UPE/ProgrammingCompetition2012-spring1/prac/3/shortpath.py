#!/usr/bin/env python 

from __future__ import print_function 
import sys, pdb

class Edge:
	def __init__(self, u, v, w, attr):
		self.u=u
		self.v=v
		self.w=w
		self.a=attr



class Graph:
	def __init__(self):
		self.edges=[]
		self.vertex = set()
		self.dist={}
	
	def add_edge(self, u , v , w, attr ): # graph is buid via adding edges 
		self.edges.append(Edge(u,v,w,attr))
		#self.edges.append(Edge(v,u,w,attr))
		self.vertex.add(u)
		self.vertex.add(v)
	
	def update(self, e):
		if self.dist[e.v] == "inf" and self.dist[e.u] =="inf":
			return 
	
		if self.dist[e.v] == "inf" and self.dist[e.u] !="inf":
			self.dist[e.v] =  self.dist[e.u] + e.w  
			return 
		
		if self.dist[e.v] != "inf" and self.dist[e.u] =="inf":
			self.dist[e.u] = self.dist[e.v] + e.w
			return 
		
		if self.dist[e.v] != "inf" and self.dist[e.u] !="inf":
			if self.dist[e.v] >= self.dist[e.u]:
				self.dist[e.v] = min( self.dist[e.v], self.dist[e.u] + e.w)
				return 
			else:
				self.dist[e.u] = min(self.dist[e.u], self.dist[e.v]+e.w)
				return 
		

	def short_path(self, s, se, alist):
		# all vertex initiate to null 
		for i in self.vertex:
			self.dist[i] = "inf"

		self.dist[s]=0

		for i in range( len(self.vertex)  ):
			for e in self.edges:
				if e.a in alist:
					self.update(e)
			
		if self.dist[se] == "inf":
			return -1
		else:
			return self.dist[se]

fin = open(sys.argv[1], 'r')
nloop = int(fin.readline().strip())

for i in range( nloop ):
	(s, se) = fin.readline().strip().split()
	g= Graph()

	nedges = int( fin.readline().strip() )
	for j in range(nedges):
		(u,v, w, attr ) = fin.readline().strip().split()
		g.add_edge(u,v,int(w),attr)
	
	#pdb.set_trace()
	s1 = g.short_path( s, se, ['stairs', 'hill', 'flat']  )
	s2 = g.short_path( s, se, ['hill', 'flat'])
	s3 = g.short_path( s, se, ['flat'])

	print(s1,s2,s3)

	





