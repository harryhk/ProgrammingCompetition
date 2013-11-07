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


    def addEdge(self,  v1, v2):
        # expect 2 ints 
        self.edges[v1].append(v2)
        self.revEdges[v2].append(v1)


    def solv(self):
        # top sort
        
        if self.nvertex == 1:
            print self.vertex[0]
            return 

        # find source 
        for i in self.vertex:
            if len( self.revEdges[i]  ) == 0:
                vSource = i
                break

        # find sink 
        for i in self.vertex:
            if len( self.edges[i] ) == 0:
                vSink = i
                break

        if _debug:
            print vSource, vSink

        # find right root
        rightRoot = vSource
        while len( self.edges[rightRoot]  ) ==1:
            rightRoot = self.edges[rightRoot][0]

        
        leftRoot = vSink
            

        while len( self.revEdges[leftRoot] ) == 1:
            leftRoot = self.revEdges[leftRoot][0]

        if _debug:
            print leftRoot, rightRoot
        
        tmp=[]
        
        while leftRoot != rightRoot:
            tmp.append( leftRoot )
            leftRoot = self.edges[leftRoot][0]

        tmp.append(rightRoot)


        for i in sorted(tmp):
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
            
