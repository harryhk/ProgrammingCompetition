#!/usr/bin/env python 

from __future__ import print_function
import sys, pdb
import numpy as np

class Graph():
	def __init__(self):
		self.vertex=set()
		self.edges={}
		self.visit={}
		self.stack=[]
	
	
	def add_edge(self, u, v ): # directional u-> v 
		if self.edges.has_key( u ):
			self.edges[u].add(v)
		else:
			self.edges[u] = set([v])
		
		self.vertex.add(u)
		self.vertex.add(v)

	def explore( self, s ):
		self.visit[s] = 1 
		for i in self.edges[s]:
			if self.visit[i] == 0: 
				self.explore( i )
		self.stack.append(s)

	def top_sort(self):
		
		for i in self.vertex:
			self.visit[i] = 0 
			if not self.edges.has_key(i):
				self.edges[i]=set([])

		for i in self.vertex:
			if self.visit[i] == 0 :
				self.explore(i)

		re = ''
		while len( self.stack ) != 0 :
			re = re + self.stack.pop()

		#pdb.set_trace()
		
		return re 
		
if __name__ == "__main__":

	fin = open(sys.argv[1], 'r')
	
	nloop=int(fin.readline().strip())
	
	
	for i in range(nloop):
		
		(nf, t ) = fin.readline().strip().split()
		g= Graph()
		h= []
		for j in range(  int(nf) ):
			l = fin.readline().strip()
			if l in h : continue
			else: h.append(l)
	
			for k1 in range( len(l) -1 ):
				for k2 in range( k1+1 , len(l) ):
					g.add_edge( l[k1], l[k2]  )
		pdb.set_trace()
		print( g.top_sort() )
	
	



