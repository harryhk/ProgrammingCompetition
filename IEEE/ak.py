#!/usr/bin/env python 

import sys

_debug = 0 

class Graph(object):
    
    def __init__(self, n):
        # index start from 1 
        self.vertex = range(1,n+1)
        self.nvertex = n

        # { 'V1': [v2, v3, ...etc ] , vertex v1 pointed to    }
        self.edges={}
        for i in self.vertex:
            self.edges[i] = []
        
        # { 'v1': [   ] , vertex pointed to v1}
        self.revEdges ={}
        for i in self.vertex:
            self.revEdges[i] = []

        # set up for dfs
        self.gtime= 0 # global time for DFS 
        self.visited={}
        for i in self.vertex:
            self.visited[i] = 0

        self.exitTime={}
        for i in self.vertex:
            self.exitTime[i] = 0

    def addEdge(self,  v1, v2):
        # expect 2 ints 
        self.edges[v1].append(v2)
        self.revEdges[v2].append(v1)

    def dfs(self):
        
        for i in self.vertex:
            if self.visited[i] == 0:
                self._explore(i)

        if _debug :
            print self.exitTime
            print self.visited

    def _explore(self, vi):
        
        self.gtime += 1
        self.visited[vi] =1
        for i in self.edges[vi]:
            if self.visited[i] == 0 :
                self._explore(i)

        self.exitTime[vi] = self.gtime
        self.gtime +=1


    def solv(self):
        # top sort

        if self.nvertex == 1:
            print self.vertex[0]
            return 

        self.dfs()
        topsort = sorted( self.exitTime.items(), key=lambda x: -x[1] )

        if _debug:
            print topsort

        # find fist v that has >= 2 out edge in topsort order , if or return the last in topsort 
        tmp = [ i[0]  for i in topsort if len(self.edges[i[0]]) >=2  ]
        if tmp :
            endV = tmp[0]
        else:
            endV = topsort[-1][0]

        # find last that has >=2 in edges 
         
        tmp = [ i[0]  for i in topsort if len(self.revEdges[i[0]]) >=2  ]
        if tmp :
            firstV = tmp[-1]
        else:
            firstV = topsort[0][0]

        # print all v between [ firstV , endV ] in top sort 
        tmp = [ i[0] for i in topsort  ]
        fidx = tmp.index(firstV)
        eidx = tmp.index(endV)
        
        if _debug:
            print fidx, eidx

        for i in sorted(tmp[fidx: eidx+1]):
            print i
            

    def p(self):
        print self.__dict__

if __name__ == '__main__':
   
    
    line = sys.stdin.readline()  

    while line:
        
        nline = int( line.strip() ) 
        g = Graph(nline)
        for i in range( nline-1):
            line = sys.stdin.readline()
            tmp = line.strip().split()
            g.addEdge( int(tmp[0]), int(tmp[1]) )
        

        if _debug :
            g.p()

        g.solv()

        #for i in g.solv():
        #    print i

        line = sys.stdin.readline()
            
    

