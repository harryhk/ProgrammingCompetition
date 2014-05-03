import sys 
from itertools import combinations
import copy

class Graph:
    
    def __init__(self, n):
        self.node = {}
        self.T = n 
        for i in range(1, n+1):
            self.node[i] = []

    def add_edge(self, i, j ):
        self.node[i].append(j)
        self.node[j].append(i)
    
    def d_node(self, i):
        tmp = self.node[i]
        for j in tmp:
            self.node[j].remove(i)
        self.node.pop(i)

    def isBinary(self, root):
        checkNode = [ root ]
        treeNodeBit = [0 for _ in range(self.T+1) ]  # 1 to T 

        while len( checkNode) != 0 :
            
            n= checkNode.pop(0)
            c = 0
            for i in self.node[n]:
                if treeNodeBit[i] ==0 :
                    checkNode.append(i)
                    treeNodeBit[i] =1 
                    c += 1
            if c == 1 :
                return False
        return True
                
                
                    


f = open( sys.argv[1] ) 

cases = int( f.readline().strip() ) 

for case in range( 1, cases + 1) :
    
    T = int( f.readline().strip()  )
    graph = Graph(T)
    for _ in range(T-1) :
        i,j  = map( int, f.readline().strip().split() ) 
        graph.add_edge( i, j )
    
    flg= False
    for r in graph.node.keys():
        if graph.isBinary(r):
            
            print "Case #%d: %d" % (case, 0)
            flg = True 
            break
    if flg:
        continue

    nodes = range(1, T+1)
    for l in range(1, T ): 
        for dList in combinations(nodes, l ):
            
            tgraph = copy.deepcopy(graph)
            for dd in dList:
                tgraph.d_node(dd)

            for r in tgraph.node.keys():
                if tgraph.isBinary(r):
                    print "Case #%d: %d" % (case, l)
                    flg = True
                    break

            if flg:
                break
        if flg:
            break

            

        
        
        
