import sys 



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
    
    
    def maxBT(self, root, used_nodes):
        
        # used_nodes = [] 
        child = 0
        childMap = {}
        for i in self.node[root]:
            if i not  in used_nodes:
                child +=1
                childMap[i] = 0 

        if child == 1 or child == 0:
            return 1 
        
        for i in childMap.keys():
            tmp = used_nodes[:]
            tmp.append(root)
            childMap[i]= self.maxBT(i, tmp )

        childSort = sorted(childMap.viewitems(), key=lambda x:-x[1])
        return childSort[0][1] + childSort[1][1] + 1 

f = open( sys.argv[1] ) 

cases = int( f.readline().strip() ) 

for case in range( 1, cases + 1) :
    
    T = int( f.readline().strip()  )
    graph = Graph(T)
    for _ in range(T-1) :
        i,j  = map( int, f.readline().strip().split() ) 
        graph.add_edge( i, j )
    
    n = T-   sorted( [ graph.maxBT(r, [])  for r in graph.node.keys() ] )[-1]
            
    print "Case #%d: %d" % (case, n)

        
        
